"""Smoke tests for sky130.lvs.rules (skipped unless gflvs is installed)."""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path
from typing import Any

import pytest

gflvs = pytest.importorskip("gflvs")

import gdstk  # noqa: E402  (ships with gflvs)
from gflvs.gflvs_refactor import ElectricalDeviceExtractionPolicy  # noqa: E402
from gflvs.gflvs_schema import LvsRunMode  # noqa: E402
from result import Err, Ok  # noqa: E402

from sky130 import PDK, pcells  # noqa: E402
from sky130.layers import LAYER  # noqa: E402
from sky130.lvs import rules  # noqa: E402

GROUP_FLAGS = {
    "ENABLE_MOSFET_TEMPLATES": rules.MOSFET_TEMPLATES,
    "ENABLE_RESISTOR_TEMPLATES": rules.RESISTOR_TEMPLATES,
    "ENABLE_CAPACITOR_TEMPLATES": rules.CAPACITOR_TEMPLATES,
    "ENABLE_DIODE_TEMPLATES": rules.DIODE_TEMPLATES,
    "ENABLE_BJT_TEMPLATES": rules.BJT_TEMPLATES,
}


def _names(templates: list[Any]) -> list[str]:
    return [t.device_name for t in templates]


def test_default_config_builds() -> None:
    assert isinstance(rules.DEFAULT_LVS_CONFIG, gflvs.LvsConfig)


def test_connectivity_symmetric() -> None:
    assert all(
        a in rules.LAYER_CONNECTIVITY[b]
        for a, bs in rules.LAYER_CONNECTIVITY.items()
        for b in bs
    )


def test_template_layers_in_pdk() -> None:
    pdk_layers = {(layer.layer, layer.datatype) for layer in LAYER}
    used = rules._template_layers(rules.DEVICE_TEMPLATES) | set(
        rules.LAYER_CONNECTIVITY
    )
    assert used <= pdk_layers


def test_terminals_use_markers() -> None:
    missing = [
        (t.device_name, term.terminal_name)
        for t in rules.DEVICE_TEMPLATES
        if t.device_name not in rules.NO_MARKER_TEMPLATES
        for term in t.device_terminal_template
        if not rules._leaf_layers(term.layer_composed_op) & rules.MARKER_LAYERS
    ]
    assert not missing


def test_flags_toggle(monkeypatch: pytest.MonkeyPatch) -> None:
    with monkeypatch.context() as m:
        m.setattr(rules, "ENABLE_ELECTRICAL_TRACING", False)
        assert (
            not rules.build_lvs_config().netlist_tracer_config.galvanic_drawing_layers
        )

    with monkeypatch.context() as m:
        m.setattr(rules, "ENABLE_DEVICE_EXTRACTION", False)
        assert rules.build_lvs_config().device_templates == []

    with monkeypatch.context() as m:
        m.setattr(rules, "ENABLE_PARAMETER_CHECK", False)
        templates = rules.build_lvs_config().device_templates
        assert templates
        assert all(t.properties["blackbox"] == "true" for t in templates)
        assert all("blackbox" not in t.properties for t in rules.DEVICE_TEMPLATES)

    full = _names(rules.build_lvs_config().device_templates)
    for flag, group in GROUP_FLAGS.items():
        with monkeypatch.context() as m:
            m.setattr(rules, flag, False)
            kept = _names(rules.build_lvs_config().device_templates)
            assert kept == [n for n in full if n not in _names(group)], flag

    with monkeypatch.context() as m:
        m.setattr(rules, "HIERARCHICAL_RUN", True)
        assert rules.build_lvs_config().run_mode == LvsRunMode.LVS_RUN_MODE_HIERARCHICAL


# values from the swarm verification table (templates-sky130.md §3)
PCELL_ROWS = [
    (
        "nfet_01v8",
        dict(nf=3, gate_width=1, gate_length=0.5),
        4,
        dict(w=1.0, l=0.5, nf=3),
    ),
    ("nfet_01v8_lvt", dict(nf=5, gate_width=2), 4, dict(w=2.0, l=0.15, nf=5)),
    ("nfet_03v3_nvt", dict(nf=2), 4, dict(w=0.42, l=0.5, nf=2)),
    ("nfet_05v0_nvt", dict(nf=3), 4, dict(w=0.42, l=0.9, nf=3)),
    ("nfet_g5v0d10v5", dict(nf=2), 4, dict(w=0.42, l=0.5, nf=2)),
    ("esd_nfet_01v8", dict(nf=2, gate_width=5), 4, dict(w=5.0, l=0.15, nf=2)),
    (
        "pfet_01v8",
        dict(nf=2, gate_width=2, gate_length=0.25),
        4,
        dict(w=2.0, l=0.25, nf=2),
    ),
    ("pfet_01v8_lvt", dict(nf=3), 4, dict(w=0.42, l=0.35, nf=3)),
    (
        "pfet_01v8_hvt",
        dict(nf=2, gate_width=3, gate_length=1),
        4,
        dict(w=3.0, l=1.0, nf=2),
    ),
    ("pfet_g5v0d10v5", {}, 4, dict(w=0.42, l=0.5, nf=1)),
    ("res_generic_po", dict(res_width=1, res_length=5), 2, dict(w=1.0, l=5.0)),
    ("res_high_po_0p35", dict(res_length=2), 2, dict(w=0.35, l=2.0)),
    ("res_generic_nd", dict(res_width=0.5, res_length=4), 2, dict(w=0.5, l=4.0)),
    ("cap_mim_m3_1", dict(cap_width=5, cap_length=3), 2, dict(w=5.0, l=3.0)),
    ("cap_mim_m3_2", dict(cap_width=4, cap_length=6), 2, dict(w=4.0, l=6.0)),
    ("diode_pw2nd_05v5", dict(diode_width=1, diode_length=2), 2, dict(w=1.0, l=2.0)),
    ("diode_pd2nw_05v5", dict(diode_width=2, diode_length=1), 2, dict(w=2.0, l=1.0)),
    ("npn_05v5", dict(emitter_width=2, emitter_length=2), 3, dict(w=2.0, l=2.0)),
    ("pnp_05v5", dict(emitter_width=3.4, emitter_length=3.4), 3, dict(w=3.4, l=3.4)),
]


@pytest.mark.parametrize("pcell, kwargs, n_terminals, params", PCELL_ROWS)
def test_pcell_extracts(
    pcell: str,
    kwargs: dict[str, float],
    n_terminals: int,
    params: dict[str, float],
    tmp_path: Path,
) -> None:
    device = f"sky130_fd_pr__{pcell}"
    PDK.activate()
    factory: Callable[..., Any] = getattr(pcells, device)
    component = factory(**kwargs)
    gds = component.write_gds(tmp_path / f"{pcell}.gds")
    # top_level() returns kfactory's $$$CONTEXT_INFO$$$ cell, so look the pcell up by name
    (top,) = [c for c in gdstk.read_gds(str(gds)).cells if c.name == component.name]

    results = ElectricalDeviceExtractionPolicy().execute(
        top,
        rules.DEVICE_TEMPLATES,
        rules.DEFAULT_LVS_CONFIG.electrical_device_extraction_config,
    )

    assert not [r for r in results if isinstance(r, Err)]
    devices = [r.ok_value for r in results if isinstance(r, Ok)]
    assert [d.class_name for d in devices] == [device]
    (extracted,) = devices
    assert len(extracted.terminals) == n_terminals
    values = {p.name: p.value for p in extracted.parameters}
    assert values == pytest.approx(params, rel=1e-3)
