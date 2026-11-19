"""gflvs LVS rules for the sky130 PDK.

Usage::

    import gflvs
    from sky130.lvs import DEFAULT_LVS_CONFIG

    gflvs.lvs(netlist, lib, DEFAULT_LVS_CONFIG, topcell=component.name)

An empty topcell picks gdsfactory's `$$$CONTEXT_INFO$$$` cell (doplaydo/gflvs#137), so pass it.

Flip the flags below and call `build_lvs_config()` for a variant config.

Targets the gflvs `dev` API (`gflvs.gflvs_refactor`: `LvsConfig`, `NetlistTracerConfig`,
`ElectricalDeviceExtractionConfig`) with protos from `gflvs.gflvs_schema`.

gflvs extracts devices from each cell's own polygons only (depth 0), so device PCells must be
flat: the BJT PCells call `c.flatten()` for this reason.
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Callable, Iterable, Sequence

import gdstk
from gflvs import ElectricalDeviceExtractionConfig, LvsConfig, NetlistTracerConfig
from gflvs.gflvs_schema import (
    DeviceParameterTemplate,
    DeviceTemplate,
    DeviceTerminalTemplate,
    DeviceTerminalType,
    LayerGds,
    LayerOffsetOperation,
    LayerOperation,
    LayerRef,
    LvsRunMode,
)

from sky130.layers import LAYER

# ── Flags ───────────────────────────────────────────────────────────
ENABLE_ELECTRICAL_TRACING = (
    True  # trace metal/via nets; False → tracer galvanic layers empty
)
ENABLE_DEVICE_EXTRACTION = True  # use DEVICE_TEMPLATES; False → connectivity-only LVS
ENABLE_MOSFET_TEMPLATES = True  # nfet/pfet flavours and the ESD nfet
ENABLE_RESISTOR_TEMPLATES = True  # poly and diffusion resistors
ENABLE_CAPACITOR_TEMPLATES = True  # MIM caps
ENABLE_DIODE_TEMPLATES = True  # pw2nd / pd2nw diodes
ENABLE_BJT_TEMPLATES = True  # vertical npn / pnp
ENABLE_PARAMETER_CHECK = True  # False → every template blackboxed (topology only)
HIERARCHICAL_RUN = False  # True → LVS_RUN_MODE_HIERARCHICAL, else FLAT
VERBOSE = False  # True → LvsConfig.verbose=1
PARAMETER_RELATIVE_TOLERANCE = 1e-3  # relative tolerance for parameter comparison

# ── Helpers ─────────────────────────────────────────────────────────
# ponytail: duplicated per PDK repo; move to gflvs when it ships helpers
LayerKey = tuple[int, int]
PIN = DeviceTerminalType.DEVICE_TERMINAL_TYPE_PIN
Region = LayerRef | LayerOperation


def L(layer: tuple[int, int]) -> LayerRef:
    """Return a LayerRef for a PDK layer."""
    return LayerRef(layer=LayerGds(layer=int(layer[0]), datatype=int(layer[1])))


def op(x: Region) -> LayerOperation:
    """Wrap a LayerRef as a LayerOperation."""
    return x if isinstance(x, LayerOperation) else LayerOperation(layer_ref_left=x)


def grow(x: Region, d: float) -> LayerOperation:
    """Grow a region isotropically by d um (the evaluator reads offset_x only)."""
    return LayerOperation(
        layer_op_left=op(x), offset_op=LayerOffsetOperation(offset_x=d, offset_y=d)
    )


def pin(name: str, x: Region) -> DeviceTerminalTemplate:
    """Return a PIN terminal template."""
    return DeviceTerminalTemplate(
        terminal_name=name, terminal_type=PIN, layer_composed_op=op(x)
    )


def par(name: str, x: Region, extractor: str | None = None) -> DeviceParameterTemplate:
    """Return a parameter template; extractor is "length" | "width" | "count" or None (custom)."""
    p = DeviceParameterTemplate(name=name, layer_composed_op=op(x))
    if extractor:
        p.properties["extractor"] = extractor
    return p


def tpl(
    name: str,
    terms: Sequence[DeviceTerminalTemplate],
    params: Sequence[DeviceParameterTemplate] = (),
) -> DeviceTemplate:
    """Return a device template whose class name is its device name."""
    return DeviceTemplate(
        device_name=name,
        device_class_name=name,
        device_terminal_template=list(terms),
        device_parameter_template=list(params),
    )


def bbox_x(polygons: list[gdstk.Polygon]) -> float:
    """Return the bounding-box width of the polygons, nan if none."""
    xs = [x for p in polygons for x, _ in p.points]
    return float(max(xs) - min(xs)) if xs else float("nan")


def bbox_y(polygons: list[gdstk.Polygon]) -> float:
    """Return the bounding-box height of the polygons, nan if none."""
    ys = [y for p in polygons for _, y in p.points]
    return float(max(ys) - min(ys)) if ys else float("nan")


def _leaf_layers(operation: LayerOperation) -> set[LayerKey]:
    """Return every layer an operation reads."""
    layers: set[LayerKey] = set()
    for side in ("left", "right"):
        field = operation.WhichOneof(f"layer_{side}")
        if field == f"layer_ref_{side}":
            ref = getattr(operation, field).layer
            layers.add((ref.layer, ref.datatype))
        elif field:
            layers |= _leaf_layers(getattr(operation, field))
    return layers


def _template_layers(templates: Iterable[DeviceTemplate]) -> frozenset[LayerKey]:
    """Return every layer the templates read, implants and markers included."""
    return frozenset(
        layer
        for t in templates
        for x in (*t.device_terminal_template, *t.device_parameter_template)
        for layer in _leaf_layers(x.layer_composed_op)
    )


def connectivity(
    chains: Iterable[tuple[tuple[int, int], tuple[int, int], tuple[int, int]]],
) -> dict[LayerKey, list[LayerKey]]:
    """Turn [(a, via, b)] chains into symmetric NetlistTracerConfig.layer_connectivity."""
    c: defaultdict[LayerKey, list[LayerKey]] = defaultdict(list)
    for chain in chains:
        a, v, b = ((int(x[0]), int(x[1])) for x in chain)
        for x, y in ((a, v), (v, a), (v, b), (b, v)):
            if y not in c[x]:
                c[x].append(y)
    return dict(c)


# ── Layers ──────────────────────────────────────────────────────────
NWELL, DIFF, TAP, POLY = (
    L(LAYER.nwelldrawing),
    L(LAYER.diffdrawing),
    L(LAYER.tapdrawing),
    L(LAYER.polydrawing),
)
DIFFRES, POLYRES = L(LAYER.diffres), L(LAYER.polyres)
LICON1, LI1, MET1 = L(LAYER.licon1drawing), L(LAYER.li1drawing), L(LAYER.met1drawing)
MET3, MET4, MET5 = L(LAYER.met3drawing), L(LAYER.met4drawing), L(LAYER.met5drawing)
CAPM, CAP2M = L(LAYER.capm), L(LAYER.cap2m)
NSDM, PSDM, LVTN = L(LAYER.nsdmdrawing), L(LAYER.psdmdrawing), L(LAYER.lvtndrawing)
HVTP, HVI, RPM = L(LAYER.hvtpdrawing), L(LAYER.hvidrawing), L(LAYER.rpmdrawing)
AREAID_ESD, AREAID_DIODE, AREAID_NATIVE = (
    L(LAYER.areaidesd),
    L(LAYER.areaiddiode),
    L(LAYER.areaidlvNative),
)
NPN, PNP = L(LAYER.npndrawing), L(LAYER.pnpdrawing)

MARKER_LAYERS: frozenset[LayerKey] = frozenset(
    (layer[0], layer[1])
    for layer in (
        LAYER.areaidesd,
        LAYER.areaiddiode,
        LAYER.areaidlvNative,
        LAYER.npndrawing,
        LAYER.pnpdrawing,
        LAYER.polyres,
        LAYER.diffres,
        LAYER.capm,
        LAYER.cap2m,
    )
)  # the PCells draw no pin layers (port labels are text only)

# ponytail: tuned on PCell geometry; re-measure if PCell rules change
# S/D diffusion and guard ring lie within this of the channel (max seen 1.155)
MOS_REACH = 1.2
# own poly contact from its channel (max seen 0.24); in hd nand2 the other gate's is 0.52 away
GATE_REACH = 0.35
# grows S/D licons into one piece per strap (licon gap <= 0.19; other-net li1 >= 0.17 away)
LICON_MERGE = 0.12
RES_REACH = 2.5  # farthest met1 head point from the resistor body (max seen 2.13)
RES_LINK = 0.1  # met1 heads start up to 0.025 from the body: the grown "l" region bridges that gap
CAP_REACH = 3.5  # farthest bottom-plate metal from the dielectric (max seen 3.09, m3_2)
DIODE_REACH = (
    0.8  # guard-ring tap distance from the diode diffusion (seen 0.51 PCell, 0.34 deck)
)

LAYER_CONNECTIVITY: dict[LayerKey, list[LayerKey]] = connectivity(
    [
        # poly-licon1 not traced: poly is the gate and resistor body, tracing it shorts resistor heads
        (LAYER.licon1, LAYER.li1, LAYER.mcon),
        # added mcon-met1: the PDK chain stops at mcon, cutting li1 off from met1
        (LAYER.li1, LAYER.mcon, LAYER.met1),
        (LAYER.met1, LAYER.via, LAYER.met2),
        (LAYER.met2, LAYER.via2, LAYER.met3),
        # TODO(https://github.com/gdsfactory/skywater130/issues/296): via3 inside capm (via4 inside cap2m) shorts the MIM plates here;
        # TODO(gflvs): needs layer-op connectivity (via3 - capm) to express the deck's rule (doplaydo/gflvs#136)
        (LAYER.met3, LAYER.via3, LAYER.met4),
        (LAYER.met4, LAYER.via4, LAYER.met5),
        # well/implant pairs (nwell-dnwell/nsdm, pwell/hvtp-pwbm, hvi/ldntm/hvntm-poly) dropped:
        # not conductors, and hvi-poly would merge every gate under HVI
    ]
)

# ── Templates ───────────────────────────────────────────────────────
# Leaf PCells are not traced inside, and gflvs binds a terminal only to parent nets on its leftmost
# layer, so every terminal starts with the li1/met1/met3-5 its route lands on (rule 2).
# Terminal names are the PCell logical pin names (port names where a PCell registers no pins).


def mos(
    name: str,
    implant: LayerRef,
    body_implant: LayerRef,
    require: Sequence[LayerRef] = (),
    exclude: Sequence[LayerRef] = (),
) -> DeviceTemplate:
    """MOSFET: gate = poly & diff & implant, S/D and body tap bound to the gate by MOS_REACH."""
    gate = POLY & DIFF & implant
    for layer in require:
        gate = gate & layer
    for layer in exclude:
        gate = gate - layer
    near_gate = grow(gate, MOS_REACH)
    return tpl(
        name,
        [
            # nets ordered by x: leftmost is the drain (the DRAIN port), matching the D0/S1/D2... labels.
            # Only li1 on S/D contacts counts (li1 crossing uncontacted diffusion is not a terminal),
            # and the implant keeps the other-type diffusion of dense cells out.
            pin(
                "DRAIN/SOURCE",
                LI1 & grow(((DIFF & implant & near_gate) - POLY) & LICON1, LICON_MERGE),
            ),
            # li1 on this gate's own poly contacts: not an S/D strap over a poly edge, not a
            # neighbouring gate's contact
            pin("GATE", LI1 & POLY & LICON1 & grow(gate, GATE_REACH)),
            # TODO(gflvs): no shared body net: taps can't be traced through well/substrate, so each
            # tap ring is its own net and a MOS without a local tap has no b (std cells)
            pin("BODY", LI1 & TAP & body_implant & near_gate),
        ],
        # l per finger on the gate; w on this transistor's same-implant diffusion and nf on the poly
        # (one finger+pad polygon per finger), which also tie the li1 S/D and gate contacts into one
        # device when there is no guard ring.
        # ponytail: w is the diffusion height, wrong if fingers of different W share a diffusion
        # within MOS_REACH; switch to the gate once gflvs can group devices without it
        [
            par("l", gate),
            par("w", DIFF & implant & near_gate),
            par("nf", POLY & near_gate, "count"),
        ],
    )


def res(
    name: str,
    conductor: LayerRef,
    marker: LayerRef,
    require: Sequence[LayerRef] = (),
    exclude: Sequence[LayerRef] = (),
) -> DeviceTemplate:
    """Resistor: body = conductor & marker, terminals are the met1 heads within RES_REACH."""
    body = conductor & marker
    for layer in require:
        body = body & layer
    for layer in exclude:
        body = body - layer
    return tpl(
        name,
        # lower head first: MINUS sits at -y, PLUS at +y in every resistor pcell
        [pin("MINUS/PLUS", MET1 & grow(body, RES_REACH))],
        [par("l", conductor & grow(body, RES_LINK)), par("w", body)],
    )


def cap(
    name: str, dielectric: LayerRef, bottom: LayerRef, top: LayerRef
) -> DeviceTemplate:
    """MIM cap: TOP = top plate over the dielectric, BOTTOM = bottom plate near it."""
    return tpl(
        name,
        [
            pin("TOP", top & dielectric),
            pin("BOTTOM", bottom & grow(dielectric, CAP_REACH)),
        ],
        [par("w", dielectric), par("l", dielectric)],
    )


def diode(
    name: str,
    implant: LayerRef,
    ring_implant: LayerRef,
    terminal: str,
    ring_terminal: str,
) -> DeviceTemplate:
    """Diode: junction = diff & areaiddiode & implant, ring tap bound by DIODE_REACH.

    w/l read the junction grown by DIODE_REACH (the extractors subtract it): that region overlaps
    the ring-tap li1 pieces, so an open ring (separate li1 sides, as in the deck) stays one device.
    """
    junction = DIFF & AREAID_DIODE & implant
    return tpl(
        name,
        [
            pin(terminal, MET1 & junction),
            pin(ring_terminal, LI1 & TAP & ring_implant & grow(junction, DIODE_REACH)),
        ],
        [par("w", grow(junction, DIODE_REACH)), par("l", grow(junction, DIODE_REACH))],
    )


# TODO(https://github.com/gdsfactory/skywater130/issues/296): MOS/ESD BODY port sits on the gate poly-contact pad, not the guard ring
# TODO(https://github.com/gdsfactory/skywater130/issues/296): for even nf the SOURCE port sits on a drain diffusion
MOSFET_TEMPLATES = [
    mos(
        "sky130_fd_pr__nfet_01v8", NSDM, PSDM, exclude=(LVTN, HVI, AREAID_ESD)
    ),  # CONFIDENCE: HIGH
    mos(
        "sky130_fd_pr__nfet_01v8_lvt",
        NSDM,
        PSDM,
        require=(LVTN,),
        exclude=(HVI, AREAID_ESD),
    ),  # CONFIDENCE: HIGH
    # TODO(https://github.com/gdsfactory/skywater130/issues/296): nfet_20v0 draws the same layers as g5v0d10v5, so it extracts as g5v0d10v5
    mos(
        "sky130_fd_pr__nfet_g5v0d10v5", NSDM, PSDM, require=(HVI,), exclude=(LVTN,)
    ),  # CONFIDENCE: MEDIUM
    mos(
        "sky130_fd_pr__nfet_03v3_nvt", NSDM, PSDM, require=(HVI, LVTN, AREAID_NATIVE)
    ),  # CONFIDENCE: HIGH
    mos(
        "sky130_fd_pr__nfet_05v0_nvt",
        NSDM,
        PSDM,
        require=(HVI, LVTN),
        exclude=(AREAID_NATIVE,),
    ),  # CONFIDENCE: MEDIUM
    mos(
        "sky130_fd_pr__esd_nfet_01v8", NSDM, PSDM, require=(AREAID_ESD,), exclude=(HVI,)
    ),  # CONFIDENCE: HIGH
    mos(
        "sky130_fd_pr__pfet_01v8", PSDM, NSDM, exclude=(LVTN, HVTP, HVI)
    ),  # CONFIDENCE: HIGH
    mos(
        "sky130_fd_pr__pfet_01v8_lvt", PSDM, NSDM, require=(LVTN,), exclude=(HVI,)
    ),  # CONFIDENCE: HIGH
    mos(
        "sky130_fd_pr__pfet_01v8_hvt", PSDM, NSDM, require=(HVTP,), exclude=(HVI,)
    ),  # CONFIDENCE: HIGH
    # TODO(https://github.com/gdsfactory/skywater130/issues/296): pfet_20v0 draws the same layers as g5v0d10v5, so it extracts as g5v0d10v5
    mos(
        "sky130_fd_pr__pfet_g5v0d10v5", PSDM, NSDM, require=(HVI,)
    ),  # CONFIDENCE: MEDIUM
]
RESISTOR_TEMPLATES = [
    res(
        "sky130_fd_pr__res_generic_po", POLY, POLYRES, exclude=(RPM,)
    ),  # CONFIDENCE: HIGH
    res(
        "sky130_fd_pr__res_high_po_0p35", POLY, POLYRES, require=(RPM,)
    ),  # CONFIDENCE: HIGH
    res("sky130_fd_pr__res_generic_nd", DIFF, DIFFRES),  # CONFIDENCE: HIGH
]
# TODO(https://github.com/gdsfactory/skywater130/issues/296): via3 inside capm (via4 inside cap2m) shorts the plates in the tracer
CAPACITOR_TEMPLATES = [
    cap("sky130_fd_pr__cap_mim_m3_1", CAPM, MET3, MET4),  # CONFIDENCE: MEDIUM
    cap("sky130_fd_pr__cap_mim_m3_2", CAP2M, MET4, MET5),  # CONFIDENCE: MEDIUM
]
DIODE_TEMPLATES = [
    diode(
        "sky130_fd_pr__diode_pw2nd_05v5", NSDM, PSDM, "CATHODE", "ANODE"
    ),  # CONFIDENCE: MEDIUM
    diode(
        "sky130_fd_pr__diode_pd2nw_05v5", PSDM, NSDM, "ANODE", "CATHODE"
    ),  # CONFIDENCE: MEDIUM
]
# TODO: LOW — real BJT models are fixed-size (…_W1p00L1p00); w/l only check the emitter box
BJT_TEMPLATES = [
    # CONFIDENCE: LOW
    # TODO(https://github.com/gdsfactory/skywater130/issues/296): npn collector li1 is merged with the base ring and has no tap, so the
    # PCell's npn extracts no COLLECTOR
    tpl(
        "sky130_fd_pr__npn_05v5",
        [
            pin("EMITTER", LI1 & DIFF & NSDM & NPN),
            pin("BASE", LI1 & TAP & PSDM & NPN),
            # the n+ collector tap ring in the nwell
            pin("COLLECTOR", LI1 & TAP & NSDM & NPN),
        ],
        [par("w", DIFF & NSDM & NPN), par("l", DIFF & NSDM & NPN)],
    ),
    # CONFIDENCE: LOW
    tpl(
        "sky130_fd_pr__pnp_05v5",
        [
            pin("EMITTER", LI1 & DIFF & PSDM & PNP),
            pin("BASE", LI1 & TAP & NSDM & PNP),
            pin("COLLECTOR", LI1 & TAP & PSDM & PNP),
        ],
        [par("w", DIFF & PSDM & PNP), par("l", DIFF & PSDM & PNP)],
    ),
]
DEVICE_TEMPLATES: list[DeviceTemplate] = [
    *MOSFET_TEMPLATES,
    *RESISTOR_TEMPLATES,
    *CAPACITOR_TEMPLATES,
    *DIODE_TEMPLATES,
    *BJT_TEMPLATES,
]

# sky130 draws no recognition layer on plain MOSFETs: the gate implant/Vt set identifies them and
# the S/D/body terminals are bound to that gate by MOS_REACH. (nfet_01v8 and nfet_05v0_nvt only
# subtract a marker, which is not a gate, so they are listed too.)
NO_MARKER_TEMPLATES: frozenset[str] = frozenset(
    {
        "sky130_fd_pr__nfet_01v8",
        "sky130_fd_pr__nfet_01v8_lvt",
        "sky130_fd_pr__nfet_g5v0d10v5",
        "sky130_fd_pr__nfet_05v0_nvt",
        "sky130_fd_pr__pfet_01v8",
        "sky130_fd_pr__pfet_01v8_lvt",
        "sky130_fd_pr__pfet_01v8_hvt",
        "sky130_fd_pr__pfet_g5v0d10v5",
    }
)


def finger_x(polygons: list[gdstk.Polygon]) -> float:
    """Return the gate length: the width of one gate finger (fingers run along y in every MOS pcell)."""
    return bbox_x(polygons[:1])


def res_length(polygons: list[gdstk.Polygon]) -> float:
    """Return the resistor length from its body grown by RES_LINK along y."""
    return bbox_y(polygons) - 2 * RES_LINK


def diode_w(polygons: list[gdstk.Polygon]) -> float:
    """Return the junction width from the junction grown by DIODE_REACH."""
    return bbox_x(polygons) - 2 * DIODE_REACH


def diode_l(polygons: list[gdstk.Polygon]) -> float:
    """Return the junction length from the junction grown by DIODE_REACH."""
    return bbox_y(polygons) - 2 * DIODE_REACH


# rule 3: every w/l reads its own parameter region, never the gap between paired terminals
PARAMETER_EXTRACTORS: dict[tuple[str, str], Callable[[list[gdstk.Polygon]], float]] = {
    **{
        (t.device_name, n): f
        for t in MOSFET_TEMPLATES
        for n, f in (("l", finger_x), ("w", bbox_y))
    },
    **{
        (t.device_name, n): f
        for t in RESISTOR_TEMPLATES
        for n, f in (("l", res_length), ("w", bbox_x))
    },
    **{
        (t.device_name, n): f
        for t in DIODE_TEMPLATES
        for n, f in (("w", diode_w), ("l", diode_l))
    },
    **{
        (t.device_name, n): f
        for t in (*CAPACITOR_TEMPLATES, *BJT_TEMPLATES)
        for n, f in (("w", bbox_x), ("l", bbox_y))
    },
}

# TODO(https://github.com/gdsfactory/skywater130/issues/296): via_m1_m2 is not exported from sky130.pcells ("via" covers it anyway)
PASSTHROUGH_DEVICE_CLASS_NAMES: tuple[str, ...] = ("via", "contact_array")


# ── Config ──────────────────────────────────────────────────────────
def _blackbox(template: DeviceTemplate) -> DeviceTemplate:
    copy = DeviceTemplate()
    copy.CopyFrom(template)
    copy.properties["blackbox"] = "true"
    return copy


def build_lvs_config() -> LvsConfig:
    """Build an LvsConfig from the module flags, read at call time."""
    groups = [
        (ENABLE_MOSFET_TEMPLATES, MOSFET_TEMPLATES),
        (ENABLE_RESISTOR_TEMPLATES, RESISTOR_TEMPLATES),
        (ENABLE_CAPACITOR_TEMPLATES, CAPACITOR_TEMPLATES),
        (ENABLE_DIODE_TEMPLATES, DIODE_TEMPLATES),
        (ENABLE_BJT_TEMPLATES, BJT_TEMPLATES),
    ]
    templates = (
        [t for on, group in groups if on for t in group]
        if ENABLE_DEVICE_EXTRACTION
        else []
    )
    if not ENABLE_PARAMETER_CHECK:
        templates = [_blackbox(t) for t in templates]
    return LvsConfig(
        device_templates=templates,
        netlist_tracer_config=NetlistTracerConfig(
            layer_connectivity=LAYER_CONNECTIVITY,
            # routing metals and contacts only: diff/poly/tap stay out or they short S/D and resistor heads
            galvanic_drawing_layers=frozenset(LAYER_CONNECTIVITY)
            if ENABLE_ELECTRICAL_TRACING
            else frozenset(),
            passthrough_device_class_names=PASSTHROUGH_DEVICE_CLASS_NAMES,
        ),
        electrical_device_extraction_config=ElectricalDeviceExtractionConfig(
            galvanic_drawing_layers=_template_layers(templates),
            parameter_extractors=PARAMETER_EXTRACTORS,
        ),
        parameter_relative_tolerance=PARAMETER_RELATIVE_TOLERANCE,
        run_mode=LvsRunMode.LVS_RUN_MODE_HIERARCHICAL
        if HIERARCHICAL_RUN
        else LvsRunMode.LVS_RUN_MODE_FLAT,
        verbose=1 if VERBOSE else 0,
    )


DEFAULT_LVS_CONFIG = build_lvs_config()
