"""Magic-parity MOSFET generators for sky130.

Provides nfet_01v8 and pfet_01v8 parametric cells that match the geometry
produced by Magic's sky130 device generators, including multi-finger support,
S/D sharing, guard rings, and deep N-well options.
"""

from math import ceil, floor

import gdsfactory as gf

from sky130.layers import LAYER
from sky130.pcells.contact import contact_array, licon_array
from sky130.pcells.guard_ring import nwell_guard_ring, pwell_guard_ring


def _snap(val: float, grid: float = 0.005) -> float:
    """Snap a value to the nearest grid point (default 5nm)."""
    return round(val / grid) * grid


def _add_rect(c: gf.Component, layer, x: float, y: float, w: float, h: float):
    """Add a rectangle to a component using polygon coordinates."""
    x, y, w, h = _snap(x), _snap(y), _snap(w), _snap(h)
    c.add_polygon(
        [(x, y), (x + w, y), (x + w, y + h), (x, y + h)],
        layer=layer,
    )


def _mosfet_core(
    c: gf.Component,
    gate_width: float,
    gate_length: float,
    sd_width: float,
    nf: int,
    end_cap: float,
    is_pmos: bool,
) -> dict:
    """Build the core MOSFET geometry (shared between NMOS and PMOS).

    Returns a dict of key coordinates for port placement and enclosure calculations.
    """
    # ---- Design rule constants ----
    implant_enc = 0.125  # implant enclosure beyond diffusion
    nwell_enc = 0.18  # nwell enclosure (PMOS only)
    npc_spacing = 0.09  # NPC spacing from diffusion edge
    contact_enc_poly = 0.06  # licon enclosure within poly
    contact_size = 0.17
    li_enc = 0.08  # li1 enclosure beyond licon region

    # ---- Derived dimensions ----
    diff_w = nf * gate_length + (nf + 1) * sd_width  # total diffusion width (x)
    diff_h = gate_width  # total diffusion height (y)
    pitch = gate_length + sd_width  # gate-to-gate pitch

    # ---- 1. Diffusion rectangle ----
    _add_rect(c, LAYER.diffdrawing, 0, 0, diff_w, diff_h)

    # ---- 2. Poly gates ----
    poly_h = gate_width + 2 * end_cap
    poly_y = -end_cap
    for i in range(nf):
        gate_x = sd_width + i * pitch
        _add_rect(c, LAYER.polydrawing, gate_x, poly_y, gate_length, poly_h)

    # ---- 3. S/D contacts (licon) in diffusion ----
    # Each S/D region: sd_width x gate_width, with licon contacts inside
    for i in range(nf + 1):
        sd_x = i * pitch
        licon_ref = c.add_ref(licon_array(width=sd_width, height=gate_width))
        licon_ref.move((sd_x, 0))

    # ---- 4. Local interconnect (li1) strips over S/D regions ----
    for i in range(nf + 1):
        sd_x = i * pitch
        _add_rect(c, LAYER.li1drawing, sd_x, -li_enc / 2, sd_width, gate_width + li_enc)

    # ---- 5. Gate contacts: poly pads above diffusion ----
    # Poly contact pad: extends above the diffusion on the poly extension area
    # Pad width = max(gate_length, 2*contact_enc_poly + contact_size)
    pc_pad_w = max(gate_length, 2 * contact_enc_poly + contact_size)
    pc_pad_h = 2 * contact_enc_poly + contact_size
    pc_pad_x_offset = (gate_length - pc_pad_w) / 2  # center pad on gate

    for i in range(nf):
        gate_x = sd_width + i * pitch
        pad_x = gate_x + pc_pad_x_offset

        # Upper poly contact pad
        pad_y_upper = gate_width + end_cap
        _add_rect(c, LAYER.polydrawing, pad_x, pad_y_upper, pc_pad_w, pc_pad_h)

        # Lower poly contact pad
        pad_y_lower = -end_cap - pc_pad_h
        _add_rect(c, LAYER.polydrawing, pad_x, pad_y_lower, pc_pad_w, pc_pad_h)

        # Licon on poly contact pads
        licon_upper = c.add_ref(
            contact_array(
                width=pc_pad_w,
                height=pc_pad_h,
                contact_layer=LAYER.licon1drawing,
                contact_size=(contact_size, contact_size),
                contact_spacing=(contact_size, contact_size),
                enclosure=(contact_enc_poly, contact_enc_poly),
            )
        )
        licon_upper.move((pad_x, pad_y_upper))

        licon_lower = c.add_ref(
            contact_array(
                width=pc_pad_w,
                height=pc_pad_h,
                contact_layer=LAYER.licon1drawing,
                contact_size=(contact_size, contact_size),
                contact_spacing=(contact_size, contact_size),
                enclosure=(contact_enc_poly, contact_enc_poly),
            )
        )
        licon_lower.move((pad_x, pad_y_lower))

        # Li1 strips on gate contact pads
        _add_rect(
            c,
            LAYER.li1drawing,
            pad_x - li_enc / 2,
            pad_y_upper,
            pc_pad_w + li_enc,
            pc_pad_h,
        )
        _add_rect(
            c,
            LAYER.li1drawing,
            pad_x - li_enc / 2,
            pad_y_lower,
            pc_pad_w + li_enc,
            pc_pad_h,
        )

        # NPC (nitride poly cut) rectangles over poly contact regions
        npc_en = end_cap - npc_spacing
        npc_w = pc_pad_w + npc_en
        npc_h = pc_pad_h + npc_en
        npc_x = pad_x - npc_en / 2

        # Upper NPC
        npc_y_upper = gate_width + npc_spacing + npc_en / 2
        _add_rect(c, LAYER.npcdrawing, npc_x, npc_y_upper, npc_w, npc_h)

        # Lower NPC
        npc_y_lower = -end_cap - pc_pad_h - npc_en / 2
        _add_rect(c, LAYER.npcdrawing, npc_x, npc_y_lower, npc_w, npc_h)

    # ---- 6. Implant layers ----
    if is_pmos:
        # PMOS: psdm over diffusion, nsdm over body tap (handled in guard ring)
        diff_implant_layer = LAYER.psdmdrawing
    else:
        # NMOS: nsdm over diffusion, psdm over body tap (handled in guard ring)
        diff_implant_layer = LAYER.nsdmdrawing

    _add_rect(
        c,
        diff_implant_layer,
        -implant_enc,
        -implant_enc,
        diff_w + 2 * implant_enc,
        diff_h + 2 * implant_enc,
    )

    # ---- 7. N-well (PMOS only) ----
    if is_pmos:
        _add_rect(
            c,
            LAYER.nwelldrawing,
            -nwell_enc,
            -nwell_enc,
            diff_w + 2 * nwell_enc,
            diff_h + 2 * nwell_enc,
        )

    # ---- Return coordinate info for ports and guard ring ----
    return {
        "diff_w": diff_w,
        "diff_h": diff_h,
        "pitch": pitch,
        "pc_pad_h": pc_pad_h,
        "end_cap": end_cap,
        "npc_spacing": npc_spacing,
        "implant_enc": implant_enc,
        "nwell_enc": nwell_enc,
    }


@gf.cell
def sky130_fd_pr__nfet_01v8(
    gate_width: float = 0.42,
    gate_length: float = 0.15,
    sd_width: float = 0.28,
    nf: int = 1,
    guard_ring: bool = True,
    dnwell: bool = False,
    end_cap: float = 0.13,
    mult: int = 1,
) -> gf.Component:
    """1.8V N-channel MOSFET (sky130_fd_pr__nfet_01v8).

    Generates a multi-finger NMOS transistor with Magic-parity geometry,
    including source/drain contacts, gate contacts, implants, optional
    guard ring, and optional deep N-well.

    Args:
        gate_width: transistor width (um), i.e. the diffusion extent in y.
        gate_length: gate poly length (um) in the direction of current flow.
        sd_width: source/drain contact region width (um).
        nf: number of gate fingers.
        guard_ring: if True, add a pwell (P+ substrate) guard ring.
        dnwell: if True, add a deep N-well under the device.
        end_cap: poly extension beyond diffusion edge (um).
        mult: multiplier (currently generates one device; reserved for future use).
    """
    c = gf.Component()

    info = _mosfet_core(
        c,
        gate_width=gate_width,
        gate_length=gate_length,
        sd_width=sd_width,
        nf=nf,
        end_cap=end_cap,
        is_pmos=False,
    )

    diff_w = info["diff_w"]
    diff_h = info["diff_h"]
    pitch = info["pitch"]

    # ---- Guard ring ----
    if guard_ring:
        ring_spacing = 0.27
        ring_width = 0.34
        # Total device extent including poly contact pads
        pc_pad_h = info["pc_pad_h"]
        device_top = diff_h + end_cap + pc_pad_h
        device_bottom = -(end_cap + pc_pad_h)
        device_height = device_top - device_bottom
        device_width = diff_w

        gr = c.add_ref(
            pwell_guard_ring(
                inner_width=device_width,
                inner_height=device_height,
                ring_width=ring_width,
                spacing=ring_spacing,
            )
        )
        gr.move((0, device_bottom))

    # ---- Deep N-well ----
    if dnwell:
        dnwell_enc = 0.40
        bb = c.bbox()
        _add_rect(
            c,
            LAYER.dnwelldrawing,
            float(bb.left) - dnwell_enc,
            float(bb.bottom) - dnwell_enc,
            float(bb.width()) + 2 * dnwell_enc,
            float(bb.height()) + 2 * dnwell_enc,
        )

    # ---- Ports ----
    # GATE: center of first poly gate, on polydrawing
    gate0_x = sd_width + gate_length / 2
    gate0_y = diff_h / 2
    c.add_port(
        name="GATE",
        center=(gate0_x, gate0_y),
        width=gate_width,
        orientation=0,
        layer=LAYER.polydrawing,
        port_type="electrical",
    )

    # SOURCE: even-indexed S/D regions (0, 2, 4, ...) — first one at index 0
    src_x = sd_width / 2
    src_y = diff_h / 2
    c.add_port(
        name="SOURCE",
        center=(src_x, src_y),
        width=gate_width,
        orientation=180,
        layer=LAYER.li1drawing,
        port_type="electrical",
    )

    # DRAIN: odd-indexed S/D regions (1, 3, 5, ...) — first one at index 1
    drain_x = pitch + sd_width / 2
    drain_y = diff_h / 2
    c.add_port(
        name="DRAIN",
        center=(drain_x, drain_y),
        width=gate_width,
        orientation=0,
        layer=LAYER.li1drawing,
        port_type="electrical",
    )

    # BODY: below the device on li1drawing
    body_x = diff_w / 2
    body_y = -(end_cap + info["pc_pad_h"])
    c.add_port(
        name="BODY",
        center=(body_x, body_y),
        width=diff_w,
        orientation=270,
        layer=LAYER.li1drawing,
        port_type="electrical",
    )

    return c


@gf.cell
def sky130_fd_pr__pfet_01v8(
    gate_width: float = 0.42,
    gate_length: float = 0.15,
    sd_width: float = 0.28,
    nf: int = 1,
    guard_ring: bool = True,
    dnwell: bool = False,
    end_cap: float = 0.13,
    mult: int = 1,
) -> gf.Component:
    """1.8V P-channel MOSFET (sky130_fd_pr__pfet_01v8).

    Generates a multi-finger PMOS transistor with Magic-parity geometry,
    including source/drain contacts, gate contacts, N-well, implants,
    optional nwell guard ring, and optional deep N-well.

    Args:
        gate_width: transistor width (um), i.e. the diffusion extent in y.
        gate_length: gate poly length (um) in the direction of current flow.
        sd_width: source/drain contact region width (um).
        nf: number of gate fingers.
        guard_ring: if True, add an nwell (N+ tap) guard ring.
        dnwell: if True, add a deep N-well under the device.
        end_cap: poly extension beyond diffusion edge (um).
        mult: multiplier (currently generates one device; reserved for future use).
    """
    c = gf.Component()

    info = _mosfet_core(
        c,
        gate_width=gate_width,
        gate_length=gate_length,
        sd_width=sd_width,
        nf=nf,
        end_cap=end_cap,
        is_pmos=True,
    )

    diff_w = info["diff_w"]
    diff_h = info["diff_h"]
    pitch = info["pitch"]

    # ---- Guard ring ----
    if guard_ring:
        ring_spacing = 0.27
        ring_width = 0.34
        pc_pad_h = info["pc_pad_h"]
        device_top = diff_h + end_cap + pc_pad_h
        device_bottom = -(end_cap + pc_pad_h)
        device_height = device_top - device_bottom
        device_width = diff_w

        gr = c.add_ref(
            nwell_guard_ring(
                inner_width=device_width,
                inner_height=device_height,
                ring_width=ring_width,
                spacing=ring_spacing,
            )
        )
        gr.move((0, device_bottom))

    # ---- Deep N-well ----
    if dnwell:
        dnwell_enc = 0.40
        bb = c.bbox()
        _add_rect(
            c,
            LAYER.dnwelldrawing,
            float(bb.left) - dnwell_enc,
            float(bb.bottom) - dnwell_enc,
            float(bb.width()) + 2 * dnwell_enc,
            float(bb.height()) + 2 * dnwell_enc,
        )

    # ---- Ports ----
    # GATE: center of first poly gate, on polydrawing
    gate0_x = sd_width + gate_length / 2
    gate0_y = diff_h / 2
    c.add_port(
        name="GATE",
        center=(gate0_x, gate0_y),
        width=gate_width,
        orientation=0,
        layer=LAYER.polydrawing,
        port_type="electrical",
    )

    # SOURCE: even-indexed S/D regions (0, 2, 4, ...) — first one at index 0
    src_x = sd_width / 2
    src_y = diff_h / 2
    c.add_port(
        name="SOURCE",
        center=(src_x, src_y),
        width=gate_width,
        orientation=180,
        layer=LAYER.li1drawing,
        port_type="electrical",
    )

    # DRAIN: odd-indexed S/D regions (1, 3, 5, ...) — first one at index 1
    drain_x = pitch + sd_width / 2
    drain_y = diff_h / 2
    c.add_port(
        name="DRAIN",
        center=(drain_x, drain_y),
        width=gate_width,
        orientation=0,
        layer=LAYER.li1drawing,
        port_type="electrical",
    )

    # BODY: below the device on li1drawing
    body_x = diff_w / 2
    body_y = -(end_cap + info["pc_pad_h"])
    c.add_port(
        name="BODY",
        center=(body_x, body_y),
        width=diff_w,
        orientation=270,
        layer=LAYER.li1drawing,
        port_type="electrical",
    )

    return c


def _add_ports(
    c: gf.Component,
    info: dict,
    gate_width: float,
    gate_length: float,
    sd_width: float,
    end_cap: float,
) -> None:
    """Add GATE, SOURCE, DRAIN, BODY ports to a MOSFET component."""
    diff_w = info["diff_w"]
    diff_h = info["diff_h"]
    pitch = info["pitch"]

    gate0_x = sd_width + gate_length / 2
    gate0_y = diff_h / 2
    c.add_port(
        name="GATE",
        center=(gate0_x, gate0_y),
        width=gate_width,
        orientation=0,
        layer=LAYER.polydrawing,
        port_type="electrical",
    )

    src_x = sd_width / 2
    src_y = diff_h / 2
    c.add_port(
        name="SOURCE",
        center=(src_x, src_y),
        width=gate_width,
        orientation=180,
        layer=LAYER.li1drawing,
        port_type="electrical",
    )

    drain_x = pitch + sd_width / 2
    drain_y = diff_h / 2
    c.add_port(
        name="DRAIN",
        center=(drain_x, drain_y),
        width=gate_width,
        orientation=0,
        layer=LAYER.li1drawing,
        port_type="electrical",
    )

    body_x = diff_w / 2
    body_y = -(end_cap + info["pc_pad_h"])
    c.add_port(
        name="BODY",
        center=(body_x, body_y),
        width=diff_w,
        orientation=270,
        layer=LAYER.li1drawing,
        port_type="electrical",
    )


def _add_guard_ring(
    c: gf.Component,
    info: dict,
    end_cap: float,
    is_pmos: bool,
) -> None:
    """Add a guard ring (pwell for NMOS, nwell for PMOS) to the component."""
    ring_spacing = 0.27
    ring_width = 0.34
    diff_h = info["diff_h"]
    diff_w = info["diff_w"]
    pc_pad_h = info["pc_pad_h"]
    device_top = diff_h + end_cap + pc_pad_h
    device_bottom = -(end_cap + pc_pad_h)
    device_height = device_top - device_bottom

    if is_pmos:
        gr = c.add_ref(
            nwell_guard_ring(
                inner_width=diff_w,
                inner_height=device_height,
                ring_width=ring_width,
                spacing=ring_spacing,
            )
        )
    else:
        gr = c.add_ref(
            pwell_guard_ring(
                inner_width=diff_w,
                inner_height=device_height,
                ring_width=ring_width,
                spacing=ring_spacing,
            )
        )
    gr.move((0, device_bottom))


def _add_dnwell(c: gf.Component) -> None:
    """Add deep N-well rectangle enclosing the entire component bounding box."""
    dnwell_enc = 0.40
    bb = c.bbox()
    _add_rect(
        c,
        LAYER.dnwelldrawing,
        float(bb.left) - dnwell_enc,
        float(bb.bottom) - dnwell_enc,
        float(bb.width()) + 2 * dnwell_enc,
        float(bb.height()) + 2 * dnwell_enc,
    )


def _mosfet_variant(
    gate_width: float,
    gate_length: float,
    sd_width: float,
    nf: int,
    guard_ring: bool,
    dnwell: bool,
    end_cap: float,
    is_pmos: bool,
    extra_layers: list,
) -> gf.Component:
    """Build a MOSFET variant component with optional extra implant/well layers."""
    c = gf.Component()
    info = _mosfet_core(c, gate_width, gate_length, sd_width, nf, end_cap, is_pmos=is_pmos)

    # Extra implant/process layers covering diffusion + implant_enc margin
    for layer in extra_layers:
        enc = info["implant_enc"]
        _add_rect(
            c,
            layer,
            -enc,
            -enc,
            info["diff_w"] + 2 * enc,
            info["diff_h"] + 2 * enc,
        )

    if guard_ring:
        _add_guard_ring(c, info, end_cap, is_pmos=is_pmos)

    if dnwell:
        _add_dnwell(c)

    _add_ports(c, info, gate_width, gate_length, sd_width, end_cap)
    return c


# ---------------------------------------------------------------------------
# Variant: Low-Vt NMOS 1.8V
# ---------------------------------------------------------------------------


@gf.cell
def sky130_fd_pr__nfet_01v8_lvt(
    gate_width: float = 0.42,
    gate_length: float = 0.15,
    sd_width: float = 0.28,
    nf: int = 1,
    guard_ring: bool = True,
    dnwell: bool = False,
    end_cap: float = 0.13,
    mult: int = 1,
) -> gf.Component:
    """Low-Vt 1.8V NMOS (sky130_fd_pr__nfet_01v8_lvt)."""
    return _mosfet_variant(
        gate_width=gate_width,
        gate_length=gate_length,
        sd_width=sd_width,
        nf=nf,
        guard_ring=guard_ring,
        dnwell=dnwell,
        end_cap=end_cap,
        is_pmos=False,
        extra_layers=[LAYER.lvtndrawing],
    )


# ---------------------------------------------------------------------------
# Variant: Low-Vt PMOS 1.8V
# ---------------------------------------------------------------------------


@gf.cell
def sky130_fd_pr__pfet_01v8_lvt(
    gate_width: float = 0.42,
    gate_length: float = 0.15,
    sd_width: float = 0.28,
    nf: int = 1,
    guard_ring: bool = True,
    dnwell: bool = False,
    end_cap: float = 0.13,
    mult: int = 1,
) -> gf.Component:
    """Low-Vt 1.8V PMOS (sky130_fd_pr__pfet_01v8_lvt)."""
    return _mosfet_variant(
        gate_width=gate_width,
        gate_length=gate_length,
        sd_width=sd_width,
        nf=nf,
        guard_ring=guard_ring,
        dnwell=dnwell,
        end_cap=end_cap,
        is_pmos=True,
        extra_layers=[LAYER.lvtndrawing],
    )


# ---------------------------------------------------------------------------
# Variant: High-Vt PMOS 1.8V
# ---------------------------------------------------------------------------


@gf.cell
def sky130_fd_pr__pfet_01v8_hvt(
    gate_width: float = 0.42,
    gate_length: float = 0.15,
    sd_width: float = 0.28,
    nf: int = 1,
    guard_ring: bool = True,
    dnwell: bool = False,
    end_cap: float = 0.13,
    mult: int = 1,
) -> gf.Component:
    """High-Vt 1.8V PMOS (sky130_fd_pr__pfet_01v8_hvt)."""
    return _mosfet_variant(
        gate_width=gate_width,
        gate_length=gate_length,
        sd_width=sd_width,
        nf=nf,
        guard_ring=guard_ring,
        dnwell=dnwell,
        end_cap=end_cap,
        is_pmos=True,
        extra_layers=[LAYER.hvtpdrawing],
    )


# ---------------------------------------------------------------------------
# Variant: Thick-oxide NMOS 5V/10V
# ---------------------------------------------------------------------------


@gf.cell
def sky130_fd_pr__nfet_g5v0d10v5(
    gate_width: float = 0.42,
    gate_length: float = 0.50,
    sd_width: float = 0.28,
    nf: int = 1,
    guard_ring: bool = True,
    dnwell: bool = False,
    end_cap: float = 0.13,
    mult: int = 1,
) -> gf.Component:
    """Thick-oxide 5V/10V NMOS (sky130_fd_pr__nfet_g5v0d10v5)."""
    return _mosfet_variant(
        gate_width=gate_width,
        gate_length=gate_length,
        sd_width=sd_width,
        nf=nf,
        guard_ring=guard_ring,
        dnwell=dnwell,
        end_cap=end_cap,
        is_pmos=False,
        extra_layers=[LAYER.hvidrawing],
    )


# ---------------------------------------------------------------------------
# Variant: Thick-oxide PMOS 5V/10V
# ---------------------------------------------------------------------------


@gf.cell
def sky130_fd_pr__pfet_g5v0d10v5(
    gate_width: float = 0.42,
    gate_length: float = 0.50,
    sd_width: float = 0.28,
    nf: int = 1,
    guard_ring: bool = True,
    dnwell: bool = False,
    end_cap: float = 0.13,
    mult: int = 1,
) -> gf.Component:
    """Thick-oxide 5V/10V PMOS (sky130_fd_pr__pfet_g5v0d10v5)."""
    return _mosfet_variant(
        gate_width=gate_width,
        gate_length=gate_length,
        sd_width=sd_width,
        nf=nf,
        guard_ring=guard_ring,
        dnwell=dnwell,
        end_cap=end_cap,
        is_pmos=True,
        extra_layers=[LAYER.hvidrawing],
    )


# ---------------------------------------------------------------------------
# Variant: 20V LDNMOS
# ---------------------------------------------------------------------------


@gf.cell
def sky130_fd_pr__nfet_20v0(
    gate_width: float = 0.42,
    gate_length: float = 2.0,
    sd_width: float = 0.50,
    nf: int = 1,
    guard_ring: bool = True,
    dnwell: bool = False,
    end_cap: float = 0.13,
    mult: int = 1,
) -> gf.Component:
    """20V LDNMOS (sky130_fd_pr__nfet_20v0) — simplified."""
    return _mosfet_variant(
        gate_width=gate_width,
        gate_length=gate_length,
        sd_width=sd_width,
        nf=nf,
        guard_ring=guard_ring,
        dnwell=dnwell,
        end_cap=end_cap,
        is_pmos=False,
        extra_layers=[LAYER.hvidrawing],
    )


# ---------------------------------------------------------------------------
# Variant: 20V LDPMOS
# ---------------------------------------------------------------------------


@gf.cell
def sky130_fd_pr__pfet_20v0(
    gate_width: float = 0.42,
    gate_length: float = 2.0,
    sd_width: float = 0.50,
    nf: int = 1,
    guard_ring: bool = True,
    dnwell: bool = False,
    end_cap: float = 0.13,
    mult: int = 1,
) -> gf.Component:
    """20V LDPMOS (sky130_fd_pr__pfet_20v0) — simplified."""
    return _mosfet_variant(
        gate_width=gate_width,
        gate_length=gate_length,
        sd_width=sd_width,
        nf=nf,
        guard_ring=guard_ring,
        dnwell=dnwell,
        end_cap=end_cap,
        is_pmos=True,
        extra_layers=[LAYER.hvidrawing],
    )


# ---------------------------------------------------------------------------
# Variant: Native NMOS 3.3V
# ---------------------------------------------------------------------------


@gf.cell
def sky130_fd_pr__nfet_03v3_nvt(
    gate_width: float = 0.42,
    gate_length: float = 0.50,
    sd_width: float = 0.28,
    nf: int = 1,
    guard_ring: bool = True,
    dnwell: bool = False,
    end_cap: float = 0.13,
    mult: int = 1,
) -> gf.Component:
    """Native NMOS 3.3V (sky130_fd_pr__nfet_03v3_nvt)."""
    return _mosfet_variant(
        gate_width=gate_width,
        gate_length=gate_length,
        sd_width=sd_width,
        nf=nf,
        guard_ring=guard_ring,
        dnwell=dnwell,
        end_cap=end_cap,
        is_pmos=False,
        extra_layers=[LAYER.lvtndrawing],
    )


# ---------------------------------------------------------------------------
# Variant: Native NMOS 5V
# ---------------------------------------------------------------------------


@gf.cell
def sky130_fd_pr__nfet_05v0_nvt(
    gate_width: float = 0.42,
    gate_length: float = 0.90,
    sd_width: float = 0.28,
    nf: int = 1,
    guard_ring: bool = True,
    dnwell: bool = False,
    end_cap: float = 0.13,
    mult: int = 1,
) -> gf.Component:
    """Native NMOS 5V (sky130_fd_pr__nfet_05v0_nvt)."""
    return _mosfet_variant(
        gate_width=gate_width,
        gate_length=gate_length,
        sd_width=sd_width,
        nf=nf,
        guard_ring=guard_ring,
        dnwell=dnwell,
        end_cap=end_cap,
        is_pmos=False,
        extra_layers=[LAYER.lvtndrawing, LAYER.hvidrawing],
    )


if __name__ == "__main__":
    c = sky130_fd_pr__nfet_01v8()
    c.show()
