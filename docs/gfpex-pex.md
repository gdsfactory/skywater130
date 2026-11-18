# PEX rules for gfpex — SkyWater130

`sky130/pex/rules.py` holds the default parasitic-extraction techfile for
[gfpex](https://github.com/doplaydo/gf-pex): layers and GDS pairs, LVS computed
layers, the process stack (z, thickness, dielectric k), sheet/contact/via
resistances and the Magic-style capacitance tables. The data is carried over
from gf-pex `gfpexconfg/sky130A.py` (KPEX sky130A technology definition and
Magic `sky130A.tech` defaults), with three deliberate departures: the MiM plate
over met4 is named `cap2m` as in `LAYER`, the duplicate li1-over-nwell overlap
is dropped, and the `iox` sidewall dielectric has k = 3.9 (SiO2) instead of the
source's 0.39.

## Usage

gfpex is optional and not a dependency of this package. Install it, then:

```python
from sky130.pex.rules import DEFAULT_PEX_RULES_CONFIG  # a gfpex.gfpex.Techfile
```

## Provenance tags

Section comments in `rules.py` say where the numbers come from:

| Tag | Meaning |
|---|---|
| `FOUNDRY <source>` | value stated by a foundry document |
| `DERIVED <formula>` | computed from foundry values (C = 8.854·k/t aF/µm², Rs = ρ/t, ...) |
| `ASSUMED <source>` | borrowed from an open PDK / tool (here KPEX and Magic) or literature |
| `PALACE-FIT` | fitted with gf-pex `benchmarks/palace_benchmark.py` |

The global `CapacitanceFittingFactors` are already Palace-fitted. A Palace fit
of the per-layer coefficients (fringe, sidewall, side-overlap) is pending.

## Running the tests

```bash
make test-pex   # uv run --no-sync pytest tests/test_pex_sky130.py -v
```

The tests skip when gfpex is not installed. CI runs them through the manual
`Test PEX rules with gfpex` workflow, which needs the `GFPEX_TOKEN` secret.
