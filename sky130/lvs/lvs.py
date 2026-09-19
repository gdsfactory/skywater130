"""LVS configuration for the SkyWater 130nm open-source CMOS PDK.

CONFIDENCE annotations:
  HIGH   — layer stack unambiguous, matches proven patterns
  MEDIUM — layer stack inferred from connectivity; single plausible interpretation
  LOW    — multiple interpretations possible; manual verification required

CRITICAL notes:
  1. Sky130 uses a local interconnect (li1) between poly/diff and met1.
     Contacts: licon1 (poly/diff → li1), mcon (li1 → met1).
  2. Diffusion pin layer (65/16) exists; gate poly pin layer (66/16) also exists.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from gflvs.electrical_device import (
    default_device_parameter_extract_count,
    default_device_parameter_extract_height,
    default_device_parameter_extract_width,
)
from gflvs.gflvs_schema import (
    DeviceParameterTemplate,
    DeviceTemplate,
    LayerBooleanOperation,
    LayerComposedOperation,
    LayerGds,
    LayerRef,
    LvsRunConfig,
    LvsRunMode,
)
from gflvs.gflvs_schema.lvs_config import ConnectivityKeyValuePair
from gflvs.helpers import build_terminal_from_overlapping_layers, lr
from gflvs.lvs import LvsResult, run_lvs

if TYPE_CHECKING:
    from gdsfactory import Component
    from gdstk import Library
    from gflvs.gflvs_schema.circuit import Circuit
    from gflvs.gflvs_schema.layout_to_netlist import Device
    from gflvs.gflvs_schema.layout_to_netlist import Port as SchemaPort
    from gflvs.tech import GdsTable

# ── GDS Layer Table ───────────────────────────────────────────────────────────
# All (layer, datatype) values read from sky130/layers.py LayerMapSky130.

GDS_TABLE: dict[str, LayerGds] = {
    # ── Active / diffusion ────────────────────────────────────────────
    "Diffdrawing": LayerGds(layer=65, datatype=20),
    "Difflabel": LayerGds(layer=65, datatype=6),
    "Diffpin": LayerGds(layer=65, datatype=16),
    # ── Gate poly ─────────────────────────────────────────────────────
    "Polydrawing": LayerGds(layer=66, datatype=20),
    "Polylabel": LayerGds(layer=66, datatype=5),
    "Polypin": LayerGds(layer=66, datatype=16),
    # ── Local interconnect contact (poly/diff → li1) ──────────────────
    "Licon1drawing": LayerGds(layer=66, datatype=44),
    "Licon1pin": LayerGds(layer=66, datatype=58),
    # ── Local interconnect metal ──────────────────────────────────────
    "Li1drawing": LayerGds(layer=67, datatype=20),
    "Li1label": LayerGds(layer=67, datatype=5),
    "Li1pin": LayerGds(layer=67, datatype=16),
    # ── Metal contact (li1 → met1) ────────────────────────────────────
    "Mcondrawing": LayerGds(layer=67, datatype=44),
    "Mconpin": LayerGds(layer=67, datatype=48),
    # ── Metal 1 ───────────────────────────────────────────────────────
    "Met1drawing": LayerGds(layer=68, datatype=20),
    "Met1label": LayerGds(layer=68, datatype=5),
    "Met1pin": LayerGds(layer=68, datatype=16),
    # ── Via 1 / Metal 2 ───────────────────────────────────────────────
    "Viadrawing": LayerGds(layer=68, datatype=44),
    "Met2drawing": LayerGds(layer=69, datatype=20),
    "Met2label": LayerGds(layer=69, datatype=5),
    "Met2pin": LayerGds(layer=69, datatype=16),
    # ── Via 2 / Metal 3 ───────────────────────────────────────────────
    "Via2drawing": LayerGds(layer=69, datatype=44),
    "Met3drawing": LayerGds(layer=70, datatype=20),
    "Met3label": LayerGds(layer=70, datatype=5),
    "Met3pin": LayerGds(layer=70, datatype=16),
    # ── Via 3 / Metal 4 ───────────────────────────────────────────────
    "Via3drawing": LayerGds(layer=70, datatype=44),
    "Met4drawing": LayerGds(layer=71, datatype=20),
    "Met4label": LayerGds(layer=71, datatype=5),
    "Met4pin": LayerGds(layer=71, datatype=16),
    # ── Via 4 / Metal 5 ───────────────────────────────────────────────
    "Via4drawing": LayerGds(layer=71, datatype=44),
    "Met5drawing": LayerGds(layer=72, datatype=20),
    "Met5label": LayerGds(layer=72, datatype=5),
    "Met5pin": LayerGds(layer=72, datatype=16),
    # ── Well / implant ────────────────────────────────────────────────
    "Nwelldrawing": LayerGds(layer=64, datatype=20),
    "Nwelllabel": LayerGds(layer=64, datatype=5),
    "Nwellpin": LayerGds(layer=64, datatype=16),
    "Pwelldrawing": LayerGds(layer=64, datatype=44),
    "Nsdmdrawing": LayerGds(layer=93, datatype=44),
    "Psdmdrawing": LayerGds(layer=94, datatype=20),
    "Dnwelldrawing": LayerGds(layer=64, datatype=18),
}

# ── Layer Lists ───────────────────────────────────────────────────────────────

DRAWING_LAYERS: list[str] = [
    "Li1drawing",
    "Met1drawing",
    "Met2drawing",
    "Met3drawing",
    "Met4drawing",
    "Met5drawing",
]

VIA_DRAWING_LAYERS: list[str] = [
    "Licon1drawing",
    "Mcondrawing",
    "Viadrawing",
    "Via2drawing",
    "Via3drawing",
    "Via4drawing",
]

PIN_LOGIC_LAYERS: list[str] = [
    "Li1pin",
    "Met1pin",
    "Met2pin",
    "Met3pin",
    "Met4pin",
    "Met5pin",
]

LABEL_LOGIC_LAYERS: list[str] = [
    "Li1label",
    "Met1label",
    "Met2label",
    "Met3label",
    "Met4label",
    "Met5label",
]

# ── Layer Connectivity ────────────────────────────────────────────────────────

LAYER_CONNECTIVITY: dict[str, list[str]] = {
    # pin → drawing
    "Li1pin": ["Li1drawing"],
    "Li1label": ["Li1drawing"],
    "Met1pin": ["Met1drawing"],
    "Met1label": ["Met1drawing"],
    "Met2pin": ["Met2drawing"],
    "Met2label": ["Met2drawing"],
    "Met3pin": ["Met3drawing"],
    "Met3label": ["Met3drawing"],
    "Met4pin": ["Met4drawing"],
    "Met4label": ["Met4drawing"],
    "Met5pin": ["Met5drawing"],
    "Met5label": ["Met5drawing"],
    # substrate → local contact
    "Diffdrawing": ["Licon1drawing"],
    "Polydrawing": ["Licon1drawing"],
    # licon1 → li1
    "Licon1drawing": ["Li1drawing"],
    # mcon → met1
    "Mcondrawing": ["Met1drawing"],
    # li1 → mcon
    "Li1drawing": ["Mcondrawing"],
    # metal stack
    "Met1drawing": ["Viadrawing"],
    "Viadrawing": ["Met2drawing"],
    "Met2drawing": ["Via2drawing"],
    "Via2drawing": ["Met3drawing"],
    "Met3drawing": ["Via3drawing"],
    "Via3drawing": ["Met4drawing"],
    "Met4drawing": ["Via4drawing"],
    "Via4drawing": ["Met5drawing"],
    # well connections
    "Nwelldrawing": ["Nsdmdrawing"],
    "Pwelldrawing": ["Psdmdrawing"],
    "Dnwelldrawing": ["Nwelldrawing"],
}

# ── Device Family Switches ────────────────────────────────────────────────────

INCLUDE_NFET = True
INCLUDE_PFET = True
INCLUDE_BJT = True
INCLUDE_CAPACITORS = True
INCLUDE_DIODES = True
INCLUDE_ESD = True
INCLUDE_RESISTORS = True
INCLUDE_VIA_CELLS = True

# ── Shared Layer Operations ───────────────────────────────────────────────────

# Gate overlap: diff AND poly — used for MOSFET parameter extraction
_gate_overlap_op = LayerComposedOperation(
    layer_a_ref=LayerRef(canonical_layer_name="Diffdrawing", layer_gds=GDS_TABLE["Diffdrawing"]),
    layer_b_ref=LayerRef(canonical_layer_name="Polydrawing", layer_gds=GDS_TABLE["Polydrawing"]),
    bool_op=LayerBooleanOperation.AND,
)

# ── Device Templates ──────────────────────────────────────────────────────────

# CONFIDENCE: MEDIUM — S/D via licon1→li1; gate poly terminal
NFET_01V8_TEMPLATE = DeviceTemplate(
    device_name="sky130_fd_pr__nfet_01v8",
    device_class_name="nfet_01v8",
    device_terminal_template=[
        build_terminal_from_overlapping_layers(0, "SD_terminals", ["Diffdrawing", "Licon1drawing", "Li1drawing"], GDS_TABLE),
        build_terminal_from_overlapping_layers(1, "Gate_terminals", ["Polydrawing"], GDS_TABLE),
    ],
    device_parameter_template=[
        DeviceParameterTemplate(uid=0, name="w", layer_composed_op=[_gate_overlap_op], extract=default_device_parameter_extract_height),
        DeviceParameterTemplate(uid=1, name="l", layer_composed_op=[_gate_overlap_op], extract=default_device_parameter_extract_width),
        DeviceParameterTemplate(uid=2, name="nf", layer_composed_op=[_gate_overlap_op], extract=default_device_parameter_extract_count),
    ],
)

# CONFIDENCE: MEDIUM
NFET_01V8_LVT_TEMPLATE = DeviceTemplate(
    device_name="sky130_fd_pr__nfet_01v8_lvt",
    device_class_name="nfet_01v8_lvt",
    device_terminal_template=[
        build_terminal_from_overlapping_layers(0, "SD_terminals", ["Diffdrawing", "Licon1drawing", "Li1drawing"], GDS_TABLE),
        build_terminal_from_overlapping_layers(1, "Gate_terminals", ["Polydrawing"], GDS_TABLE),
    ],
    device_parameter_template=[
        DeviceParameterTemplate(uid=0, name="w", layer_composed_op=[_gate_overlap_op], extract=default_device_parameter_extract_height),
        DeviceParameterTemplate(uid=1, name="l", layer_composed_op=[_gate_overlap_op], extract=default_device_parameter_extract_width),
        DeviceParameterTemplate(uid=2, name="nf", layer_composed_op=[_gate_overlap_op], extract=default_device_parameter_extract_count),
    ],
)

# CONFIDENCE: MEDIUM
PFET_01V8_TEMPLATE = DeviceTemplate(
    device_name="sky130_fd_pr__pfet_01v8",
    device_class_name="pfet_01v8",
    device_terminal_template=[
        build_terminal_from_overlapping_layers(0, "SD_terminals", ["Diffdrawing", "Licon1drawing", "Li1drawing"], GDS_TABLE),
        build_terminal_from_overlapping_layers(1, "Gate_terminals", ["Polydrawing"], GDS_TABLE),
    ],
    device_parameter_template=[
        DeviceParameterTemplate(uid=0, name="w", layer_composed_op=[_gate_overlap_op], extract=default_device_parameter_extract_height),
        DeviceParameterTemplate(uid=1, name="l", layer_composed_op=[_gate_overlap_op], extract=default_device_parameter_extract_width),
        DeviceParameterTemplate(uid=2, name="nf", layer_composed_op=[_gate_overlap_op], extract=default_device_parameter_extract_count),
    ],
)

# CONFIDENCE: MEDIUM
PFET_01V8_HVT_TEMPLATE = DeviceTemplate(
    device_name="sky130_fd_pr__pfet_01v8_hvt",
    device_class_name="pfet_01v8_hvt",
    device_terminal_template=[
        build_terminal_from_overlapping_layers(0, "SD_terminals", ["Diffdrawing", "Licon1drawing", "Li1drawing"], GDS_TABLE),
        build_terminal_from_overlapping_layers(1, "Gate_terminals", ["Polydrawing"], GDS_TABLE),
    ],
    device_parameter_template=[
        DeviceParameterTemplate(uid=0, name="w", layer_composed_op=[_gate_overlap_op], extract=default_device_parameter_extract_height),
        DeviceParameterTemplate(uid=1, name="l", layer_composed_op=[_gate_overlap_op], extract=default_device_parameter_extract_width),
        DeviceParameterTemplate(uid=2, name="nf", layer_composed_op=[_gate_overlap_op], extract=default_device_parameter_extract_count),
    ],
)

# CONFIDENCE: MEDIUM — NPN BJT: collector=nwell, base=diff, emitter=diff
# TODO: Verify terminal layer stack for NPN in sky130
NPN_05V5_TEMPLATE = DeviceTemplate(
    device_name="sky130_fd_pr__npn_05v5_W1p00L1p00",
    device_class_name="npn_05v5",
    device_terminal_template=[
        build_terminal_from_overlapping_layers(0, "Emitter_terminal", ["Diffdrawing", "Licon1drawing", "Li1drawing"], GDS_TABLE),
        build_terminal_from_overlapping_layers(1, "Base_terminal", ["Diffdrawing", "Licon1drawing", "Li1drawing"], GDS_TABLE),
        build_terminal_from_overlapping_layers(2, "Collector_terminal", ["Nwelldrawing"], GDS_TABLE),
    ],
)

# CONFIDENCE: LOW — MIM cap: top plate on met3, bottom on met2
# TODO: Verify exact MIM cap layer stack for sky130
CAP_MIM_M3_1_TEMPLATE = DeviceTemplate(
    device_name="sky130_fd_pr__cap_mim_m3_1",
    device_class_name="cap_mim_m3_1",
    device_terminal_template=[
        build_terminal_from_overlapping_layers(0, "Top_terminal", ["Met3drawing"], GDS_TABLE),
        build_terminal_from_overlapping_layers(1, "Bottom_terminal", ["Met2drawing"], GDS_TABLE),
    ],
)

# CONFIDENCE: MEDIUM
DIODE_PW2ND_05V5_TEMPLATE = DeviceTemplate(
    device_name="sky130_fd_pr__diode_pw2nd_05v5",
    device_class_name="diode_pw2nd_05v5",
    device_terminal_template=[
        build_terminal_from_overlapping_layers(0, "Anode_terminal", ["Diffdrawing", "Licon1drawing", "Li1drawing"], GDS_TABLE),
        build_terminal_from_overlapping_layers(1, "Cathode_terminal", ["Nwelldrawing"], GDS_TABLE),
    ],
)

# CONFIDENCE: MEDIUM
DIODE_ND2PS_05V5_TEMPLATE = DeviceTemplate(
    device_name="sky130_fd_pr__diode_nd2ps_05v5",
    device_class_name="diode_nd2ps_05v5",
    device_terminal_template=[
        build_terminal_from_overlapping_layers(0, "Anode_terminal", ["Diffdrawing", "Licon1drawing", "Li1drawing"], GDS_TABLE),
        build_terminal_from_overlapping_layers(1, "Cathode_terminal", ["Diffdrawing", "Licon1drawing", "Li1drawing"], GDS_TABLE),
    ],
)

# CONFIDENCE: MEDIUM
# TODO: res_generic layers need confirmation from pcells/resistors.py
RES_GENERIC_ND_TEMPLATE = DeviceTemplate(
    device_name="sky130_fd_pr__res_generic_nd",
    device_class_name="res_generic_nd",
    device_terminal_template=[
        build_terminal_from_overlapping_layers(0, "R0_terminal", ["Diffdrawing", "Licon1drawing", "Li1drawing"], GDS_TABLE),
        build_terminal_from_overlapping_layers(1, "R1_terminal", ["Diffdrawing", "Licon1drawing", "Li1drawing"], GDS_TABLE),
    ],
)

# CONFIDENCE: HIGH
VIA_GENERATOR_TEMPLATE = DeviceTemplate(device_name="via_generator", device_class_name="via")
VIA_STACK_TEMPLATE = DeviceTemplate(device_name="via_stack", device_class_name="via")

# ── Template Groups ───────────────────────────────────────────────────────────

NFET_TEMPLATES: list[DeviceTemplate] = [NFET_01V8_TEMPLATE, NFET_01V8_LVT_TEMPLATE]
PFET_TEMPLATES: list[DeviceTemplate] = [PFET_01V8_TEMPLATE, PFET_01V8_HVT_TEMPLATE]
BJT_TEMPLATES: list[DeviceTemplate] = [NPN_05V5_TEMPLATE]
CAPACITOR_TEMPLATES: list[DeviceTemplate] = [CAP_MIM_M3_1_TEMPLATE]
DIODE_TEMPLATES: list[DeviceTemplate] = [DIODE_PW2ND_05V5_TEMPLATE, DIODE_ND2PS_05V5_TEMPLATE]
ESD_TEMPLATES: list[DeviceTemplate] = []  # TODO: add ESD template after confirming layer stack
RESISTOR_TEMPLATES: list[DeviceTemplate] = [RES_GENERIC_ND_TEMPLATE]
VIA_TEMPLATES: list[DeviceTemplate] = [VIA_GENERATOR_TEMPLATE, VIA_STACK_TEMPLATE]

DEVICE_TEMPLATES: list[DeviceTemplate] = [
    *(NFET_TEMPLATES if INCLUDE_NFET else []),
    *(PFET_TEMPLATES if INCLUDE_PFET else []),
    *(BJT_TEMPLATES if INCLUDE_BJT else []),
    *(CAPACITOR_TEMPLATES if INCLUDE_CAPACITORS else []),
    *(DIODE_TEMPLATES if INCLUDE_DIODES else []),
    *(ESD_TEMPLATES if INCLUDE_ESD else []),
    *(RESISTOR_TEMPLATES if INCLUDE_RESISTORS else []),
    *(VIA_TEMPLATES if INCLUDE_VIA_CELLS else []),
]

# ── Connectivity Pairs ────────────────────────────────────────────────────────

_CONNECTIVITY_PAIRS: list[ConnectivityKeyValuePair] = [
    ConnectivityKeyValuePair(source_layer=lr(src, GDS_TABLE), to=lr(dst, GDS_TABLE))
    for src, dsts in LAYER_CONNECTIVITY.items()
    for dst in dsts
    if src in GDS_TABLE and dst in GDS_TABLE
]

# ── Default LVS Config ────────────────────────────────────────────────────────

DEFAULT_LVS_CONFIG = LvsRunConfig(
    run_mode=LvsRunMode.HIERARCHICAL,
    drawing_layers=DRAWING_LAYERS,
    via_drawing_layers=VIA_DRAWING_LAYERS,
    pin_logic_layers=PIN_LOGIC_LAYERS,
    label_logic_layers=LABEL_LOGIC_LAYERS,
    layer_connectivity=_CONNECTIVITY_PAIRS,
    device_templates=DEVICE_TEMPLATES,
    dbu=1e3,
    precision=1e-3,
)

# ── Convenience Runner ────────────────────────────────────────────────────────


def run_lvs_sky130(
    lib: Library | Component,
    circuit: Circuit,
    *,
    config: LvsRunConfig | None = None,
    devices: list[Device] | None = None,
    components: list[Component] | None = None,
    device_ports: dict[str, dict[str, SchemaPort]] | None = None,
    tech_gds_table: GdsTable | None = None,
    original_file: str = "",
) -> LvsResult:
    """Run LVS for the SkyWater 130nm PDK with default configuration."""
    return run_lvs(
        lib,
        circuit,
        config or DEFAULT_LVS_CONFIG,
        devices=devices,
        components=components,
        device_ports=device_ports,
        tech_gds_table=tech_gds_table or GDS_TABLE,
        original_file=original_file,
    )
