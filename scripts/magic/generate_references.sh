#!/usr/bin/env bash
# Generate reference GDS from Magic for XOR validation.
# Requires: magic + open_pdks installed ($PDK_ROOT set)
#
# Usage:
#   ./generate_references.sh                          # all devices
#   ./generate_references.sh sky130_fd_pr__nfet_01v8  # single device
#
# Reads sweep_params.json for parameter combinations.
# Outputs to ../../tests/ref_gds/{device_name}/{param_hash}.gds

set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REF_DIR="$SCRIPT_DIR/../../tests/ref_gds"
PARAMS_FILE="$SCRIPT_DIR/sweep_params.json"

if ! command -v magic &>/dev/null; then
    echo "Error: magic not found. Install Magic VLSI and set PATH." >&2
    exit 1
fi

if [ -z "${PDK_ROOT:-}" ]; then
    echo "Error: PDK_ROOT not set. Install open_pdks first." >&2
    exit 1
fi

echo "Reference generation requires Magic + open_pdks."
echo "See README.md for installation instructions."
echo "Param file: $PARAMS_FILE"
echo "Output dir: $REF_DIR"
echo ""

FILTER="${1:-}"

python3 - "$PARAMS_FILE" "$REF_DIR" "$FILTER" <<'PYEOF'
import json, sys, hashlib, pathlib, subprocess, os

params_file, ref_dir, device_filter = sys.argv[1], sys.argv[2], sys.argv[3]

with open(params_file) as f:
    config = json.load(f)

param_maps = config["param_maps"]

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

        magic_params = " ".join(
            f"{pmap.get(k, k)} {v}" for k, v in sorted(params.items())
        )

        short_name = device_name.replace("sky130_fd_pr__", "")
        magic_proc = f"sky130::{short_name}_draw"

        print(f"  Generating {device_name} {params} -> {out_path.name}")

        tcl_script = f"""
load {{}}
box 0 0 0 0
{magic_proc} {magic_params}
select top cell
expand
gds write {out_path}
quit
"""
        result = subprocess.run(
            ["magic", "-dnull", "-noconsole", "-T", "sky130A"],
            input=tcl_script, capture_output=True, text=True,
            env={**os.environ, "PDK_ROOT": os.environ["PDK_ROOT"]}
        )
        if result.returncode != 0:
            print(f"    FAILED: {result.stderr[:200]}", file=sys.stderr)
        else:
            print(f"    OK: {out_path}")
PYEOF
