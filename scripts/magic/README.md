# Magic Reference GDS Generation

Generates reference GDS layouts from Magic VLSI's device generators for XOR
validation against our gdsfactory pcells.

## Pinned Versions

The committed `tests/ref_gds/` files were generated from **exactly** these commits:

| Tool | Commit | Repository |
|------|--------|------------|
| Magic | `67c6ed939514e537773f9f01cc2ecca5c3400c44` | [RTimothyEdwards/magic](https://github.com/RTimothyEdwards/magic) |
| open_pdks | `fc20c144baf309002e0b335585a3aaef06b56f00` | [RTimothyEdwards/open_pdks](https://github.com/RTimothyEdwards/open_pdks) |

**Do not bump these without regenerating all reference GDS and fixing any XOR
failures.** Upstream geometry changes will break the XOR tests silently if refs
are not regenerated.

## Usage

```bash
# Build the Docker image (first time takes ~15 min)
docker build -t sky130-magic-ref scripts/magic/

# Generate all 211 reference GDS files
docker run --rm -e PDK_ROOT=/usr/local/share/pdk \
  -v $(pwd)/tests/ref_gds:/output sky130-magic-ref

# Generate for a single device
docker run --rm -e PDK_ROOT=/usr/local/share/pdk \
  -v $(pwd)/tests/ref_gds:/output sky130-magic-ref sky130_fd_pr__nfet_01v8
```

## How It Works

1. `sweep_params.json` defines device names and parameter combinations (211 total)
2. `generate_references.sh` iterates each combo, calls the device's `_defaults`
   proc to get Magic's default parameters, merges in the sweep overrides, then
   calls the `_draw` proc to generate geometry
3. Magic exports the cell to GDS via `gds write`
4. Output goes to `tests/ref_gds/{device_name}/{param_hash}.gds`

The param hash is `sha256(json.dumps(params, sort_keys=True))[:12]` — deterministic
from the parameter dict.

## Updating Upstream

If you need to track a newer Magic or open_pdks:

1. Update `MAGIC_COMMIT` and/or `OPEN_PDKS_COMMIT` in `Dockerfile`
2. Rebuild the Docker image
3. Delete existing refs: `rm -rf tests/ref_gds/sky130_fd_pr__*`
4. Regenerate: `docker run --rm -e PDK_ROOT=/usr/local/share/pdk -v $(pwd)/tests/ref_gds:/output sky130-magic-ref`
5. Run `uv run pytest tests/test_xor.py` — fix any XOR failures
6. Commit the new refs + geometry fixes together
