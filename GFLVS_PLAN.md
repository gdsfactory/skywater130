# GFLVS LVS Config Plan — SkyWater130

## PDK Info
- Package: `sky130`
- Classification: electronic (CMOS 130nm, open-source)
- Technology: SkyWater 130nm open-source CMOS process
- Layers file: `sky130/layers.py` (LayerMap class: `LayerMapSky130`)
- Dev branch: dev/gflvs-config

## Namespace Note
DO NOT create a `gflvs/` directory inside the package — it would shadow the
installed `gflvs` library. Use `sky130/lvs/` instead.

## Files to Create
- `sky130/lvs/__init__.py`   — re-exports (3 lines)
- `sky130/lvs/lvs.py`        — GDS_TABLE, LAYER_CONNECTIVITY, flag switches,
                               DEVICE_TEMPLATES, DEFAULT_LVS_CONFIG, run_lvs_sky130()
- `tests/gflvs/test_lvs_sky130.py` — integration test; pytest.importorskip("gflvs")
- `docs/gflvs-lvs.md`        — installation, config flags, usage example
- `Makefile`: add `test-lvs` recipe → `uv run pytest tests/gflvs/ -v`

## Layer Extraction
Read `sky130/layers.py` statically (do NOT import the PDK).
Extract `(layer, datatype)` pairs from `LayerMapSky130`.
Key layers: li1 (67/0), mcon (67/44), met1 (68/0), via (68/44), met2 (69/0),
via2 (69/44), met3 (70/0), via3 (70/44), met4 (71/0), via4 (71/44), met5 (72/0),
nwell (64/0), pwell (122/0), poly (66/0), licon1 (66/44).

## Connectivity
- li1-mcon-met1 (li1 → mcon → met1)
- met1-via-met2
- met2-via2-met3
- met3-via3-met4
- met4-via4-met5
- poly-licon1-li1 (gate poly → licon1 → li1)
- nwell-nsdm (nwell definition)
- pwell-pwbm (pwell/deep nwell)

## Flag Switches
```python
INCLUDE_NFET       = True  # sky130_fd_pr__nfet_01v8, nfet_01v8_lvt, nfet_01v8_hvt, nfet_g5v0d10v5, nfet_05v0, nfet_03v3_nvt, nfet_20v0
INCLUDE_PFET       = True  # sky130_fd_pr__pfet_01v8, pfet_01v8_lvt, pfet_01v8_hvt, pfet_g5v0d10v5, pfet_05v0, pfet_20v0
INCLUDE_BJT        = True  # npn_05v5_W1p00L1p00, pnp_05v5_W3p40L3p40
INCLUDE_CAPACITORS = True  # cap_mim_m3_1, cap_mim_m4_2
INCLUDE_DIODES     = True  # diode_pw2nd_05v5, diode_nd2ps_05v5
INCLUDE_ESD        = True  # esd_nfet_g5v0d10v5
INCLUDE_RESISTORS  = True  # res_generic_nd, res_generic_pd, res_generic_l1
INCLUDE_VIA_CELLS  = True  # via_generator, vias
```

Group templates by family; assemble DEVICE_TEMPLATES conditionally:
```python
NFET_TEMPLATES: list[DeviceTemplate] = [NFET_01V8_TEMPLATE, ...]
PFET_TEMPLATES: list[DeviceTemplate] = [PFET_01V8_TEMPLATE, ...]
DEVICE_TEMPLATES: list[DeviceTemplate] = [
    *(NFET_TEMPLATES if INCLUDE_NFET else []),
    *(PFET_TEMPLATES if INCLUDE_PFET else []),
    *(BJT_TEMPLATES if INCLUDE_BJT else []),
    *(CAPACITOR_TEMPLATES if INCLUDE_CAPACITORS else []),
    *(DIODE_TEMPLATES if INCLUDE_DIODES else []),
    *([ESD_TEMPLATE] if INCLUDE_ESD else []),
    *(RESISTOR_TEMPLATES if INCLUDE_RESISTORS else []),
    *(VIA_TEMPLATES if INCLUDE_VIA_CELLS else []),
]
```

## Device Templates
For each PCell in `sky130/pcells/`:
- `mosfets.py`: nfet/pfet variants — terminal layers from gate, drain, source pin layers
- `bjts.py`: npn/pnp — terminal from base, collector, emitter pins
- `capacitors.py`: cap_mim_m3_1, cap_mim_m4_2 — terminal from met3/met4 pin layers
- `diodes.py`: anode/cathode from li1/pwell pin layers
- `esd.py`: esd_nfet — gate/drain/source from li1 pin layers
- `resistors.py`: res_generic — terminal from li1 pin layers
All templates: CONFIDENCE: MEDIUM (requires layer inspection to verify pin datatype)

## Test Circuit (Inverter)
File: `tests/gflvs/test_lvs_sky130.py`
```python
pytest.importorskip("gflvs")
# pfet (M1, sky130_fd_pr__pfet_01v8, w=1.0µm, l=0.15µm, nf=1)
# nfet (M2, sky130_fd_pr__nfet_01v8, w=0.5µm, l=0.15µm, nf=1)
# met1 net connecting M1 drain to M2 drain (net "out")
# run_lvs_sky130(lib, circuit) — smoke assertion (no raise)
```

## CI Workflow
File: `.github/workflows/test_lvs.yml`
Trigger: `workflow_dispatch` only (skipped by default in CI).
```yaml
name: Test LVS (gflvs)
on:
  workflow_dispatch:
jobs:
  test-lvs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v5
      - run: uv sync --all-extras
      - run: uv pip install gflvs
      - run: make test-lvs
```

## Makefile Recipe
```makefile
test-lvs:
	uv run pytest tests/gflvs/ -v
```

## Verification Checklist
- [ ] `python -c "from sky130.lvs import DEFAULT_LVS_CONFIG"` succeeds
- [ ] Setting `INCLUDE_NFET = False` removes NFET templates from `DEVICE_TEMPLATES`
- [ ] Test skips cleanly when gflvs not installed (`pytest.importorskip`)
- [ ] `ruff check sky130/lvs/` passes
- [ ] All CONFIDENCE: LOW templates have # TODO comment with alternatives
