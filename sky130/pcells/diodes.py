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
_MCON_ENC = 0.06  # mcon enclosure within diff area
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
    inner_half_x: float,
    inner_half_y: float,
    ring_width: float,
    tap_layer,
    implant_layer,
    li1_layer,
    with_licon: bool = True,
):
    """Draw one rectangular guard ring centered at origin.

    The ring inner edge is at +/-*inner_half_x* in X and +/-*inner_half_y*
    in Y.  Ring outer edge is inner + *ring_width*.  Tap, implant, li1, and
    licon contacts are placed on all four segments.

    Returns (outer_half_x, outer_half_y) for downstream geometry.
    """
    ihx = inner_half_x
    ihy = inner_half_y
    rw = ring_width
    ohx = ihx + rw  # outer half-extent in X
    ohy = ihy + rw  # outer half-extent in Y

    # Four tap / li1 segments (top, bottom full width; left, right inner height).
    segs = [
        # (x0, y0, x1, y1)
        (-ohx, ihy, ohx, ohy),   # top
        (-ohx, -ohy, ohx, -ihy),  # bottom
        (-ohx, -ihy, -ihx, ihy),  # left
        (ihx, -ihy, ohx, ihy),   # right
    ]

    for x0, y0, x1, y1 in segs:
        _add_box(c, tap_layer, x0, y0, x1, y1)
        _add_box(c, li1_layer, x0, y0, x1, y1)

    # Implant: 4 segments extending _IMPLANT_ENC beyond tap
    ie = _IMPLANT_ENC
    imp_ohx = ohx + ie
    imp_ohy = ohy + ie
    imp_ihx = ihx - ie
    imp_ihy = ihy - ie
    imp_segs = [
        (-imp_ohx, imp_ihy, imp_ohx, imp_ohy),   # top
        (-imp_ohx, -imp_ohy, imp_ohx, -imp_ihy),  # bottom
        (-imp_ohx, -imp_ihy, -imp_ihx, imp_ihy),  # left
        (imp_ihx, -imp_ihy, imp_ohx, imp_ihy),   # right
    ]
    for x0, y0, x1, y1 in imp_segs:
        _add_box(c, implant_layer, x0, y0, x1, y1)

    # Licon contacts on each segment
    if with_licon:
        for x0, y0, x1, y1 in segs:
            _guard_ring_contacts(c, x0, y0, x1 - x0, y1 - y0)

    return ohx, ohy


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
    # When W >= L the wider dimension is X; when W < L the wider is Y.
    if diode_width >= diode_length:
        li1_hx = hw + 0.02
        li1_hy = hl - 0.06
    else:
        li1_hx = hw - 0.06
        li1_hy = hl + 0.02
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
    if diode_width >= diode_length:
        met1_hx = hw
        met1_hy = hl - 0.03
    else:
        met1_hx = hw - 0.03
        met1_hy = hl
    _add_box(c, LAYER.met1drawing, -met1_hx, -met1_hy, met1_hx, met1_hy)

    # --- P+ guard ring (pwell / substrate ring) ---
    ring_ih_x = hw + _RING_SPACING
    ring_ih_y = hl + _RING_SPACING
    ring_oh_x, ring_oh_y = _draw_ring(
        c, ring_ih_x, ring_ih_y, _RING_WIDTH,
        tap_layer=LAYER.tapdrawing,
        implant_layer=LAYER.psdmdrawing,
        li1_layer=LAYER.li1drawing,
    )

    # --- Boundary marker (235,4) ---
    bnd_x = ring_ih_x + ring_oh_x
    bnd_y = ring_ih_y + ring_oh_y
    _add_box(c, LAYER.prBoundaryboundary, -bnd_x, -bnd_y, bnd_x, bnd_y)

    # --- Labels ---
    c.add_label("D1", position=(0.0, 0.0), layer=LAYER.li1label)
    d2_y = -(ring_ih_y + ring_oh_y) / 2
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
        width=2 * ring_oh_x,
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
    if diode_width >= diode_length:
        li1_hx = hw + 0.02
        li1_hy = hl - 0.06
    else:
        li1_hx = hw - 0.06
        li1_hy = hl + 0.02
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
    if diode_width >= diode_length:
        met1_hx = hw
        met1_hy = hl - 0.03
    else:
        met1_hx = hw - 0.03
        met1_hy = hl
    _add_box(c, LAYER.met1drawing, -met1_hx, -met1_hy, met1_hx, met1_hy)

    # --- Inner guard ring: N+ tap ring inside N-well ---
    inner_ih_x = hw + _RING_SPACING
    inner_ih_y = hl + _RING_SPACING
    inner_oh_x, inner_oh_y = _draw_ring(
        c, inner_ih_x, inner_ih_y, _RING_WIDTH,
        tap_layer=LAYER.tapdrawing,
        implant_layer=LAYER.nsdmdrawing,
        li1_layer=LAYER.li1drawing,
    )

    # --- N-well: covers diff + inner ring + 0.18 extension ---
    nwell_hx = inner_oh_x + _NWELL_ENC
    nwell_hy = inner_oh_y + _NWELL_ENC
    _add_box(c, LAYER.nwelldrawing, -nwell_hx, -nwell_hy, nwell_hx, nwell_hy)

    # --- Outer guard ring: P+ tap ring in substrate ---
    outer_ih_x = nwell_hx + _RING_SPACING
    outer_ih_y = nwell_hy + _RING_SPACING
    _draw_ring(
        c, outer_ih_x, outer_ih_y, _RING_WIDTH,
        tap_layer=LAYER.tapdrawing,
        implant_layer=LAYER.psdmdrawing,
        li1_layer=LAYER.li1drawing,
    )

    outer_oh_x = outer_ih_x + _RING_WIDTH
    outer_oh_y = outer_ih_y + _RING_WIDTH

    # --- Boundary marker (235,4) — based on inner ring geometry ---
    bnd_x = inner_ih_x + inner_oh_x
    bnd_y = inner_ih_y + inner_oh_y
    _add_box(c, LAYER.prBoundaryboundary, -bnd_x, -bnd_y, bnd_x, bnd_y)

    # --- Labels ---
    c.add_label("D1", position=(0.0, 0.0), layer=LAYER.li1label)
    d2_y = -(inner_ih_y + inner_oh_y) / 2
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
        width=2 * inner_oh_x,
        orientation=270,
        layer=LAYER.li1drawing,
        port_type="electrical",
    )

    return c


if __name__ == "__main__":
    c = sky130_fd_pr__diode_pw2nd_05v5()
    c.show()
