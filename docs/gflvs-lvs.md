# LVS with gflvs — SkyWater130

## Installation

```bash
uv pip install gflvs
```

## Usage

```python
from sky130.lvs import DEFAULT_LVS_CONFIG, run_lvs_sky130

result = run_lvs_sky130(lib_or_component, circuit)
```

## Configuration flags

| Flag | Default | Devices |
|---|---|---|
| `INCLUDE_NFET` | `True` | sky130_fd_pr__nfet_01v8, nfet_01v8_lvt |
| `INCLUDE_PFET` | `True` | sky130_fd_pr__pfet_01v8, pfet_01v8_hvt |
| `INCLUDE_BJT` | `True` | npn_05v5_W1p00L1p00 |
| `INCLUDE_CAPACITORS` | `True` | cap_mim_m3_1 |
| `INCLUDE_DIODES` | `True` | diode_pw2nd_05v5, diode_nd2ps_05v5 |
| `INCLUDE_ESD` | `True` | (stub — TODO) |
| `INCLUDE_RESISTORS` | `True` | res_generic_nd |
| `INCLUDE_VIA_CELLS` | `True` | via_generator, via_stack |

## Running LVS tests

```bash
make test-lvs
```
