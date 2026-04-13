#!/usr/bin/env bash
# Generate reference GDS from Magic for XOR validation.
# Requires: magic + open_pdks installed ($PDK_ROOT set)
#
# Usage:
#   ./generate_references.sh                          # all devices
#   ./generate_references.sh sky130_fd_pr__nfet_01v8  # single device
#
# Reads sweep_params.json for parameter combinations.
# Outputs to $REF_DIR/{device_name}/{param_hash}.gds
#
# Can also run via Docker:
#   docker build -t sky130-magic-ref scripts/magic/
#   docker run -v $(pwd)/tests/ref_gds:/output sky130-magic-ref

set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REF_DIR="${REF_DIR:-$SCRIPT_DIR/../../tests/ref_gds}"
PARAMS_FILE="$SCRIPT_DIR/sweep_params.json"

if ! command -v magic &>/dev/null; then
    echo "Error: magic not found. Install Magic VLSI and set PATH." >&2
    exit 1
fi

if [ -z "${PDK_ROOT:-}" ]; then
    echo "Error: PDK_ROOT not set. Install open_pdks first." >&2
    exit 1
fi

echo "Magic reference GDS generator"
echo "PDK_ROOT: $PDK_ROOT"
echo "Param file: $PARAMS_FILE"
echo "Output dir: $REF_DIR"
echo ""

FILTER="${1:-}"

python3 - "$PARAMS_FILE" "$REF_DIR" "$FILTER" <<'PYEOF'
import json, sys, hashlib, pathlib, subprocess, os, tempfile

params_file, ref_dir, device_filter = sys.argv[1], sys.argv[2], sys.argv[3]

with open(params_file) as f:
    config = json.load(f)

param_maps = config["param_maps"]
successes = 0
failures = 0

for device_name, device_cfg in config["devices"].items():
    if device_filter and device_filter != device_name:
        continue

    out_dir = pathlib.Path(ref_dir) / device_name
    out_dir.mkdir(parents=True, exist_ok=True)

    pmap = param_maps.get(device_name, {})

    for params in device_cfg["sweep"]:
        param_str = json.dumps(params, sort_keys=True)
        param_hash = hashlib.sha256(param_str.encode()).hexdigest()[:12]
        out_path = out_dir / f"{param_hash}.gds"

        # Build Tcl dict by merging defaults with overrides
        # The draw proc expects: sky130::sky130_fd_pr__nfet_01v8_draw $params_dict
        # where params_dict is a Tcl dict with keys like w, l, nf, guard, etc.
        tcl_overrides = []
        for py_name, value in sorted(params.items()):
            magic_name = pmap.get(py_name, py_name)
            # Convert Python bools to Tcl values
            if isinstance(value, bool):
                tcl_val = "1" if value else "0"
            else:
                tcl_val = str(value)
            tcl_overrides.append(f"{magic_name} {tcl_val}")
        override_str = " ".join(tcl_overrides)

        print(f"  [{device_name}] {params} -> {out_path.name}")

        # Write Tcl script to temp file (avoids heredoc/stdin issues)
        tcl_script = f"""
# Get device defaults and merge overrides
set defaults [sky130::{device_name}_defaults]
set overrides [dict create {override_str}]
set params [dict merge $defaults $overrides]

# Draw the device
sky130::{device_name}_draw $params

# Export current cell to GDS
select top cell
expand
gds write {out_path}
puts "OK: {out_path}"
quit -noprompt
"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.tcl', delete=False) as f:
            f.write(tcl_script)
            tcl_path = f.name

        pdk_root = os.environ["PDK_ROOT"]
        tech_file = f"{pdk_root}/sky130A/libs.tech/magic/sky130A.tech"
        magicrc = f"{pdk_root}/sky130A/libs.tech/magic/sky130A.magicrc"

        # Use magicrc which sets up the full sky130 environment
        try:
            result = subprocess.run(
                ["magic", "-dnull", "-noconsole", "-rcfile", magicrc, tcl_path],
                capture_output=True, text=True, timeout=120,
                env={**os.environ, "PDK_ROOT": pdk_root}
            )
            if out_path.exists() and out_path.stat().st_size > 0:
                print(f"    OK ({out_path.stat().st_size} bytes)")
                successes += 1
            else:
                print(f"    FAILED: GDS not created", file=sys.stderr)
                if result.stderr:
                    print(f"    stderr: {result.stderr[:300]}", file=sys.stderr)
                if result.stdout:
                    print(f"    stdout: {result.stdout[:300]}", file=sys.stderr)
                failures += 1
        except subprocess.TimeoutExpired:
            print(f"    TIMEOUT", file=sys.stderr)
            failures += 1
        finally:
            os.unlink(tcl_path)

print(f"\nDone: {successes} succeeded, {failures} failed")
PYEOF
