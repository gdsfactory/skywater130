"""Diode pcell generators for sky130.

Provides N+/P-well and P+/N-well diode parametric cells matching the sky130
Magic VLSI reference geometry, including inline guard ring tap geometry with
licon contacts, mcon, met1, and implant/well layers.
"""

import gdsfactory as gf

from sky130.layers import LAYER
from sky130.pcells.contact import contact_array


# ---------------------------------------------------------------------------
# Geometry constants (um) derived from Magic reference
# ---------------------------------------------------------------------------

_IMPLANT_ENC = 0.125  # NSDM / PSDM enclosure beyond diffusion or tap
_NWELL_ENC = 0.18  # N-well enclosure beyond inner guard ring tap
_RING_SPACING = 0.34  # gap from diff edge (or nwell edge) to guard ring inner edge
_RING_WIDTH = 0.17  # width of each guard ring tap segment
_LICON_SIZE = 0.17  # licon contact size
_LICON_SPACE = 0.17  # licon contact spacing
_LICON_ENC = 0.06  # licon enclosure within diff
_MCON_SIZE = 0.17  # mcon contact size
_MCON_SPACE = 0.19  # mcon contact spacing
_MCON_ENC = 0.14  # mcon enclosure within diff area
_RING_LICON_ENC_BASE = 0.31  # licon enclosure from inner edge of guard ring
# Horizontal segments (with corner overlap) add _RING_WIDTH to this base.
_RING_LICON_ENC_HORIZ = _RING_LICON_ENC_BASE + _RING_WIDTH  # 0.48
_RING_LICON_ENC_VERT = _RING_LICON_ENC_BASE  # 0.31


def _add_box(c: gf.Component, layer, x0: float, y0: float, x1: float, y1: float):
    """Add a rectangle to *c* given (x0, y0) to (x1, y1) corners."""
    c.add_polygon([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], layer=layer)


def _contact_array_eps(
    width: float,
    height: float,
    contact_layer,
    contact_size: float,
    contact_spacing: float,
    enc_x: float,
    enc_y: float,
) -> gf.Component:
    """Contact array with epsilon tolerance to avoid floating-point floor errors."""
    return contact_array(
        width=width,
        height=height,
        contact_layer=contact_layer,
        contact_size=(contact_size, contact_size),
        contact_spacing=(contact_spacing, contact_spacing),
        enclosure=(enc_x, enc_y),
    )


def _guard_ring_contacts(
    c: gf.Component,
    seg_x: float,
    seg_y: float,
    seg_w: float,
    seg_h: float,
):
    """Place licon contacts on one guard ring tap segment.

    Horizontal segments (top/bottom, wider than tall) have corner overlap so
    they use the larger enclosure (_RING_LICON_ENC_HORIZ = 0.48) in the long
    direction and zero in the short direction.

    Vertical segments (left/right, taller than wide) have no corner overlap so
    they use the smaller enclosure (_RING_LICON_ENC_VERT = 0.31) in the long
    direction and zero in the short direction.
    """
    if seg_w >= seg_h:
        # horizontal segment (top / bottom)
        enc_x = _RING_LICON_ENC_HORIZ
        enc_y = 0.0
    else:
        # vertical segment (left / right)
        enc_x = 0.0
        enc_y = _RING_LICON_ENC_VERT

    cont = c.add_ref(
        _contact_array_eps(
            width=seg_w,
            height=seg_h,
            contact_layer=LAYER.licon1drawing,
            contact_size=_LICON_SIZE,
            contact_spacing=_LICON_SPACE,
            enc_x=enc_x,
            enc_y=enc_y,
        )
    )
    cont.move((seg_x, seg_y))


def _draw_ring(
    c: gf.Component,
    inner_half: float,
    ring_width: float,
    tap_layer,
    implant_layer,
    li1_layer,
    with_licon: bool = True,
):
    """Draw one rectangular guard ring centered at origin.

    The ring inner edge is at +/-*inner_half*, ring outer edge at
    +/-(inner_half + ring_width).  Tap, implant, li1, and licon contacts are
    placed on all four segments.

    Returns (outer_half,) for downstream geometry.
    """
    ih = inner_half
    rw = ring_width
    oh = ih + rw  # outer half-extent

    # Four tap / li1 segments (top, bottom full width; left, right full height
    # with corner overlap).
    segs = [
        # (x0, y0, x1, y1)
        (-oh, ih, oh, oh),  # top
        (-oh, -oh, oh, -ih),  # bottom
        (-oh, -ih, -ih, ih),  # left
        (ih, -ih, oh, ih),  # right
    ]

    for x0, y0, x1, y1 in segs:
        _add_box(c, tap_layer, x0, y0, x1, y1)
        _add_box(c, li1_layer, x0, y0, x1, y1)

    # Implant: 4 segments extending _IMPLANT_ENC beyond tap
    ie = _IMPLANT_ENC
    imp_oh = oh + ie
    imp_ih = ih - ie
    imp_segs = [
        (-imp_oh, imp_ih, imp_oh, imp_oh),  # top
        (-imp_oh, -imp_oh, imp_oh, -imp_ih),  # bottom
        (-imp_oh, -imp_ih, -imp_ih, imp_ih),  # left
        (imp_ih, -imp_ih, imp_oh, imp_ih),  # right
    ]
    for x0, y0, x1, y1 in imp_segs:
        _add_box(c, implant_layer, x0, y0, x1, y1)

    # Licon contacts on each segment
    if with_licon:
        for x0, y0, x1, y1 in segs:
            _guard_ring_contacts(c, x0, y0, x1 - x0, y1 - y0)

    return oh


# ---------------------------------------------------------------------------
# pw2nd (N+/P-well) diode
# ---------------------------------------------------------------------------


@gf.cell
def sky130_fd_pr__diode_pw2nd_05v5(
    diode_width: float = 0.45,
    diode_length: float = 0.45,
) -> gf.Component:
    """Return an N+/P-well diode (cathode = N+ diffusion in P-well substrate).

    Geometry centered at origin, matching Magic VLSI reference layout:
    - diff + NSDM implant (cathode)
    - P+ tap guard ring with PSDM implant (anode / substrate)
    - licon on diff and guard ring, mcon + met1 on diff
    - areaid_diode marker

    Ports:
      CATHODE -- on met1drawing over diffusion.
      ANODE   -- on li1drawing at guard ring bottom.

    Args:
        diode_width: width of the diode diffusion in um.
        diode_length: length (height) of the diode diffusion in um.

    .. plot::
      :include-source:

      import sky130

      c = sky130.pcells.sky130_fd_pr__diode_pw2nd_05v5()
      c.plot()
    """
    c = gf.Component()

    hw = diode_width / 2  # half-width
    hl = diode_length / 2  # half-length

    # --- Diffusion ---
    _add_box(c, LAYER.diffdrawing, -hw, -hl, hw, hl)

    # --- areaid_diode ---
    _add_box(c, LAYER.areaiddiode, -hw, -hl, hw, hl)

    # --- NSDM implant over diff ---
    _add_box(c, LAYER.nsdmdrawing, -hw - _IMPLANT_ENC, -hl - _IMPLANT_ENC,
             hw + _IMPLANT_ENC, hl + _IMPLANT_ENC)

    # --- Licon contacts on diff ---
    licon_ref = c.add_ref(
        _contact_array_eps(
            width=diode_width, height=diode_length,
            contact_layer=LAYER.licon1drawing,
            contact_size=_LICON_SIZE, contact_spacing=_LICON_SPACE,
            enc_x=_LICON_ENC, enc_y=_LICON_ENC,
        )
    )
    licon_ref.move((-hw, -hl))

    # --- Li1 pad on diff ---
    li1_hx = hw + 0.02
    li1_hy = hl - 0.06
    _add_box(c, LAYER.li1drawing, -li1_hx, -li1_hy, li1_hx, li1_hy)

    # --- Mcon contacts on diff ---
    mcon_ref = c.add_ref(
        _contact_array_eps(
            width=diode_width, height=diode_length,
            contact_layer=LAYER.mcondrawing,
            contact_size=_MCON_SIZE, contact_spacing=_MCON_SPACE,
            enc_x=_MCON_ENC, enc_y=_MCON_ENC,
        )
    )
    mcon_ref.move((-hw, -hl))

    # --- Met1 pad on diff ---
    met1_hx = hw
    met1_hy = hl - 0.03
    _add_box(c, LAYER.met1drawing, -met1_hx, -met1_hy, met1_hx, met1_hy)

    # --- P+ guard ring (pwell / substrate ring) ---
    ring_inner_half = hw + _RING_SPACING  # == hl + _RING_SPACING when square
    # Use max(hw, hl) + spacing as inner half to handle non-square (conservative)
    ring_inner_half_x = hw + _RING_SPACING
    ring_inner_half_y = hl + _RING_SPACING
    # For square diodes (all reference cases), these are equal.
    ring_ih = max(ring_inner_half_x, ring_inner_half_y)
    _draw_ring(
        c, ring_ih, _RING_WIDTH,
        tap_layer=LAYER.tapdrawing,
        implant_layer=LAYER.psdmdrawing,
        li1_layer=LAYER.li1drawing,
    )

    ring_oh = ring_ih + _RING_WIDTH

    # --- Boundary marker (235,4) ---
    bnd = ring_ih + ring_oh
    _add_box(c, LAYER.prBoundaryboundary, -bnd, -bnd, bnd, bnd)

    # --- Labels ---
    c.add_label("D1", position=(0.0, 0.0), layer=LAYER.li1label)
    d2_y = -(ring_ih + ring_oh) / 2
    c.add_label("D2", position=(0.0, d2_y), layer=LAYER.li1label)

    # --- Ports ---
    c.add_port(
        name="CATHODE",
        center=(0.0, 0.0),
        width=diode_width,
        orientation=90,
        layer=LAYER.met1drawing,
        port_type="electrical",
    )
    c.add_port(
        name="ANODE",
        center=(0.0, d2_y),
        width=2 * ring_oh,
        orientation=270,
        layer=LAYER.li1drawing,
        port_type="electrical",
    )

    return c


# ---------------------------------------------------------------------------
# pd2nw (P+/N-well) diode
# ---------------------------------------------------------------------------


@gf.cell
def sky130_fd_pr__diode_pd2nw_05v5(
    diode_width: float = 0.45,
    diode_length: float = 0.45,
) -> gf.Component:
    """Return a P+/N-well diode (anode = P+ diffusion in N-well).

    Geometry centered at origin, matching Magic VLSI reference layout:
    - diff + PSDM implant (anode) inside N-well
    - Inner N+ tap guard ring with NSDM implant (cathode / N-well contact)
    - N-well covering diff + inner ring + 0.18 um extension
    - Outer P+ tap guard ring with PSDM implant (substrate ring)
    - licon on diff and both guard rings, mcon + met1 on diff
    - areaid_diode marker

    Ports:
      ANODE   -- on met1drawing over diffusion.
      CATHODE -- on li1drawing at inner guard ring bottom.

    Args:
        diode_width: width of the diode diffusion in um.
        diode_length: length (height) of the diode diffusion in um.

    .. plot::
      :include-source:

      import sky130

      c = sky130.pcells.sky130_fd_pr__diode_pd2nw_05v5()
      c.plot()
    """
    c = gf.Component()

    hw = diode_width / 2
    hl = diode_length / 2

    # --- Diffusion ---
    _add_box(c, LAYER.diffdrawing, -hw, -hl, hw, hl)

    # --- areaid_diode ---
    _add_box(c, LAYER.areaiddiode, -hw, -hl, hw, hl)

    # --- PSDM implant over diff (P+ diffusion) ---
    _add_box(c, LAYER.psdmdrawing, -hw - _IMPLANT_ENC, -hl - _IMPLANT_ENC,
             hw + _IMPLANT_ENC, hl + _IMPLANT_ENC)

    # --- Licon contacts on diff ---
    licon_ref = c.add_ref(
        _contact_array_eps(
            width=diode_width, height=diode_length,
            contact_layer=LAYER.licon1drawing,
            contact_size=_LICON_SIZE, contact_spacing=_LICON_SPACE,
            enc_x=_LICON_ENC, enc_y=_LICON_ENC,
        )
    )
    licon_ref.move((-hw, -hl))

    # --- Li1 pad on diff ---
    li1_hx = hw + 0.02
    li1_hy = hl - 0.06
    _add_box(c, LAYER.li1drawing, -li1_hx, -li1_hy, li1_hx, li1_hy)

    # --- Mcon contacts on diff ---
    mcon_ref = c.add_ref(
        _contact_array_eps(
            width=diode_width, height=diode_length,
            contact_layer=LAYER.mcondrawing,
            contact_size=_MCON_SIZE, contact_spacing=_MCON_SPACE,
            enc_x=_MCON_ENC, enc_y=_MCON_ENC,
        )
    )
    mcon_ref.move((-hw, -hl))

    # --- Met1 pad on diff ---
    met1_hx = hw
    met1_hy = hl - 0.03
    _add_box(c, LAYER.met1drawing, -met1_hx, -met1_hy, met1_hx, met1_hy)

    # --- Inner guard ring: N+ tap ring inside N-well ---
    inner_ring_ih = max(hw, hl) + _RING_SPACING
    inner_ring_oh = _draw_ring(
        c, inner_ring_ih, _RING_WIDTH,
        tap_layer=LAYER.tapdrawing,
        implant_layer=LAYER.nsdmdrawing,
        li1_layer=LAYER.li1drawing,
    )

    # --- N-well: covers diff + inner ring + 0.18 extension ---
    nwell_half = inner_ring_oh + _NWELL_ENC
    _add_box(c, LAYER.nwelldrawing, -nwell_half, -nwell_half, nwell_half, nwell_half)

    # --- Outer guard ring: P+ tap ring in substrate ---
    outer_ring_ih = nwell_half + _RING_SPACING
    _draw_ring(
        c, outer_ring_ih, _RING_WIDTH,
        tap_layer=LAYER.tapdrawing,
        implant_layer=LAYER.psdmdrawing,
        li1_layer=LAYER.li1drawing,
    )

    outer_ring_oh = outer_ring_ih + _RING_WIDTH

    # --- Boundary marker (235,4) — based on inner ring geometry ---
    bnd = inner_ring_ih + inner_ring_oh
    _add_box(c, LAYER.prBoundaryboundary, -bnd, -bnd, bnd, bnd)

    # --- Labels ---
    c.add_label("D1", position=(0.0, 0.0), layer=LAYER.li1label)
    d2_y = -(inner_ring_ih + inner_ring_oh) / 2
    c.add_label("D2", position=(0.0, d2_y), layer=LAYER.li1label)

    # --- Ports ---
    c.add_port(
        name="ANODE",
        center=(0.0, 0.0),
        width=diode_width,
        orientation=90,
        layer=LAYER.met1drawing,
        port_type="electrical",
    )
    c.add_port(
        name="CATHODE",
        center=(0.0, d2_y),
        width=2 * inner_ring_oh,
        orientation=270,
        layer=LAYER.li1drawing,
        port_type="electrical",
    )

    return c


if __name__ == "__main__":
    c = sky130_fd_pr__diode_pw2nd_05v5()
    c.show()
