"""Parametrized XOR regression tests driven by scripts/magic/sweep_params.json.

For each device/param combination the test:
1. Resolves the cell function from the configured module.
2. Generates the component using only the params that the function accepts.
3. Writes a temporary GDS file and XOR-compares it against a reference GDS in
   tests/ref_gds/<device_name>/<hash>.gds.

Tests skip gracefully when:
- The cell module or function is not yet implemented.
- The reference GDS file has not yet been committed.
"""

from __future__ import annotations

import hashlib
import importlib
import inspect
import json
import pathlib
import tempfile

import gdsfactory as gf
import klayout.db as kdb
import pytest

# ---------------------------------------------------------------------------
# Skip layers: label layers (datatype 5) and boundary markers
# ---------------------------------------------------------------------------

SKIP_LAYERS = {
    (67, 5),   # li1label
    (68, 5),   # met1label
    (69, 5),   # met2label
    (70, 5),   # met3label
    (71, 5),   # met4label
    (72, 5),   # met5label
    (235, 4),  # prBoundary
    (0, 0),    # empty/context
}


def xor_gds_files(
    ref_path: pathlib.Path, run_path: pathlib.Path
) -> dict[tuple[int, int], str]:
    """Layer-by-layer kdb.Region XOR. Returns dict of failing layers.

    Ported from IHP PDK approach — merge regions before XOR,
    no hidden tolerances.
    """
    layout_ref = kdb.Layout()
    layout_ref.read(str(ref_path))
    layout_new = kdb.Layout()
    layout_new.read(str(run_path))

    dbu = layout_ref.dbu
    cell_ref = layout_ref.top_cell()
    cell_new = layout_new.top_cell()

    layers_ref = {}
    for li in layout_ref.layer_indices():
        info = layout_ref.get_info(li)
        key = (info.layer, info.datatype)
        r = kdb.Region(cell_ref.begin_shapes_rec(li))
        if not r.is_empty():
            layers_ref[key] = r

    layers_new = {}
    for li in layout_new.layer_indices():
        info = layout_new.get_info(li)
        key = (info.layer, info.datatype)
        r = kdb.Region(cell_new.begin_shapes_rec(li))
        if not r.is_empty():
            layers_new[key] = r

    all_layers = sorted(set(layers_ref) | set(layers_new))
    failures = {}

    for key in all_layers:
        if key in SKIP_LAYERS:
            continue
        in_ref = key in layers_ref
        in_new = key in layers_new
        if in_ref and not in_new:
            failures[key] = "ONLY IN REF"
            continue
        if in_new and not in_ref:
            failures[key] = "ONLY IN NEW"
            continue

        r_ref = layers_ref[key].merged()
        r_new = layers_new[key].merged()
        xor_area = (r_ref ^ r_new).area() * dbu * dbu
        if xor_area > 1e-6:
            failures[key] = (
                f"XOR={xor_area:.6f} um^2 "
                f"(ref={r_ref.area() * dbu * dbu:.4f}, "
                f"new={r_new.area() * dbu * dbu:.4f})"
            )
    return failures


# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

_REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
_SWEEP_JSON = _REPO_ROOT / "scripts" / "magic" / "sweep_params.json"
_REF_GDS_DIR = pathlib.Path(__file__).resolve().parent / "ref_gds"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _param_hash(params: dict) -> str:
    """Return a 12-character sha256 hex digest of the sorted JSON params."""
    serialised = json.dumps(params, sort_keys=True)
    return hashlib.sha256(serialised.encode()).hexdigest()[:12]


def _human_id(device_name: str, params: dict) -> str:
    """Build a human-readable pytest ID, e.g. nfet_01v8[gate_width=0.42,...]."""
    # Use the last component of the device name (after the last '__') for brevity.
    short_name = device_name.split("__")[-1]
    param_str = ",".join(f"{k}={v}" for k, v in sorted(params.items()))
    return f"{short_name}[{param_str}]"


def _load_sweep_cases() -> list[tuple[str, dict, str]]:
    """Return a list of (device_name, params, cell_module) tuples."""
    if not _SWEEP_JSON.exists():
        return []

    data = json.loads(_SWEEP_JSON.read_text())
    cases: list[tuple[str, dict, str]] = []
    for device_name, device_cfg in data.get("devices", {}).items():
        cell_module = device_cfg.get("cell_module", "")
        for params in device_cfg.get("sweep", []):
            cases.append((device_name, params, cell_module))
    return cases


# ---------------------------------------------------------------------------
# Parametrize
# ---------------------------------------------------------------------------

_sweep_cases = _load_sweep_cases()

# Build IDs from (device_name, params) so they are human-readable.
_ids = [_human_id(dev, params) for dev, params, _ in _sweep_cases]


@pytest.mark.parametrize("device_name,params,cell_module", _sweep_cases, ids=_ids)
def test_xor(device_name: str, params: dict, cell_module: str) -> None:
    """XOR-compare a generated component against its committed reference GDS."""

    # ------------------------------------------------------------------
    # 1. Resolve the cell function
    # ------------------------------------------------------------------
    # First try the configured module, looking for a function whose name
    # matches the device name or the final segment of it.
    cell_fn = None
    short_name = device_name.split("__")[-1]  # e.g. "nfet_01v8"

    try:
        mod = importlib.import_module(cell_module)
        # Try exact device name first, then the short name.
        for candidate in (device_name, short_name):
            fn = getattr(mod, candidate, None)
            if callable(fn):
                cell_fn = fn
                break
    except ModuleNotFoundError:
        pass

    # Fallback: search sky130.cells (the full PDK registry).
    if cell_fn is None:
        try:
            import sky130

            for candidate in (device_name, short_name):
                fn = sky130.cells.get(candidate)
                if fn is not None and callable(fn):
                    cell_fn = fn
                    break
        except Exception:  # pragma: no cover
            pass

    if cell_fn is None:
        pytest.skip(f"Cell {device_name} not yet implemented")

    # ------------------------------------------------------------------
    # 2. Filter params to only those the function accepts
    # ------------------------------------------------------------------
    try:
        sig = inspect.signature(cell_fn)
        accepted = {
            k
            for k, p in sig.parameters.items()
            if p.kind
            not in (
                inspect.Parameter.VAR_POSITIONAL,
                inspect.Parameter.VAR_KEYWORD,
            )
        }
    except (ValueError, TypeError):
        accepted = set(params.keys())

    filtered_params = {k: v for k, v in params.items() if k in accepted}

    # ------------------------------------------------------------------
    # 3. Check for reference GDS
    # ------------------------------------------------------------------
    param_hash = _param_hash(params)
    ref_gds = _REF_GDS_DIR / device_name / f"{param_hash}.gds"

    if not ref_gds.exists():
        pytest.skip(f"Reference GDS not found: {ref_gds}")

    # ------------------------------------------------------------------
    # 4. Generate component and write to a temporary GDS
    # ------------------------------------------------------------------
    component = cell_fn(**filtered_params)

    with tempfile.NamedTemporaryFile(suffix=".gds", delete=False) as tmp:
        run_gds = pathlib.Path(tmp.name)

    component.write_gds(str(run_gds))

    # ------------------------------------------------------------------
    # 5. XOR comparison (kdb.Region based — no hidden tolerances)
    # ------------------------------------------------------------------
    try:
        failures = xor_gds_files(ref_gds, run_gds)
        if failures:
            lines = [f"  ({l},{d}): {msg}" for (l, d), msg in sorted(failures.items())]
            raise AssertionError(
                f"XOR differences for {device_name} with {params}:\n"
                + "\n".join(lines)
            )
    finally:
        run_gds.unlink(missing_ok=True)
