# Magic Reference GDS Generation

This directory contains tooling for generating reference GDS layouts from
Magic VLSI's device generators (open_pdks) for XOR validation.

## Prerequisites

- [Magic VLSI](https://github.com/RTimothyEdwards/magic) installed
- [open_pdks](https://github.com/RTimothyEdwards/open_pdks) built with `--enable-sky130-pdk`
- `PDK_ROOT` environment variable pointing to installed PDK

## Tcl Source

The canonical device generators live in `sky130/magic/sky130.tcl` in
[open_pdks](https://github.com/RTimothyEdwards/open_pdks). Refer to that
repository for the authoritative Tcl procedures.

## Usage

```bash
export PDK_ROOT=/usr/local/share/pdk
./generate_references.sh                          # all devices
./generate_references.sh sky130_fd_pr__nfet_01v8  # single device
```

Output goes to `../../tests/ref_gds/{device}/{hash}.gds`.

## sweep_params.json

Single source of truth for parameter combinations tested. Both this script
and `tests/test_xor.py` read from it. Each device entry contains:

- `cell_module`: Python module path for the gdsfactory cell
- `sweep`: list of parameter dicts to test

The `param_maps` section translates Python parameter names to Magic parameter names.
