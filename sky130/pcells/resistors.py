"""Magic-parity resistor generators for sky130.

Provides poly and diffusion resistor parametric cells that match the geometry
produced by Magic's sky130 device generators, including guard rings, contact
heads, NPC, implant layers, and metal interconnect.

All geometry is centered at the origin to match Magic's output coordinate system.
"""

from __future__ import annotations

from math import floor

import gdsfactory as gf

from sky130.layers import LAYER

# ---------------------------------------------------------------------------
# Shared helpers (same pattern as mosfets.py)
# ---------------------------------------------------------------------------


def _snap(val: float, grid: float = 0.005) -> float:
    """Snap a value to the nearest grid point (default 5 nm)."""
    return round(val / grid) * grid


def _rect(c: gf.Component, layer, x0: float, y0: float, x1: float, y1: float):
    """Add a rectangle defined by two corners ``(x0, y0)`` to ``(x1, y1)``."""
    x0, y0, x1, y1 = _snap(x0), _snap(y0), _snap(x1), _snap(y1)
    c.add_polygon(
        [(x0, y0), (x1, y0), (x1, y1), (x0, y1)],
        layer=layer,
    )


# ---------------------------------------------------------------------------
# Guard-ring builder (inlined to give us full control over licon placement)
# ---------------------------------------------------------------------------

_LICON = 0.17  # licon contact size
_LICON_PITCH = 0.34  # licon pitch (size + spacing)
_GR_RING_W = 0.17  # guard-ring tap width
_PSDM_ENC = 0.125  # psdm enclosure of tap


def _guard_ring_licons_side(
    c: gf.Component,
    bar_x0: float,
    bar_x1: float,
    bar_y0: float,
    bar_y1: float,
) -> None:
    """Place licon contacts along a vertical guard-ring bar, centred at y=0.

    The contacts are placed at 0.34 um pitch, centred within the bar.
    Magic leaves a clearance of at least 0.310 um from each bar end to the
    outermost contact, matching the guard-ring contact placement algorithm.
    """
    bar_h = _snap(bar_y1 - bar_y0)
    cx = _snap((bar_x0 + bar_x1) / 2 - _LICON / 2)

    # Effective available height: bar_h minus clearance at each end
    eff_h = _snap(bar_h - 2 * 0.310)
    n = max(0, 1 + floor((eff_h - _LICON) / _LICON_PITCH))
    if n < 1:
        return

    array_h = _snap((n - 1) * _LICON_PITCH + _LICON)
    y_start = _snap((bar_y0 + bar_y1) / 2 - array_h / 2)

    for i in range(n):
        y = _snap(y_start + i * _LICON_PITCH)
        _rect(c, LAYER.licon1drawing, cx, y, cx + _LICON, y + _LICON)


def _guard_ring_licons_horiz(
    c: gf.Component,
    bar_x0: float,
    bar_x1: float,
    bar_y0: float,
    bar_y1: float,
    fit_width: float,
) -> None:
    """Place licon contacts along a horizontal guard-ring bar.

    ``fit_width`` controls the available width for contacts (typically the
    inner width of the guard ring).  Contacts are centred within the bar.
    """
    cy = _snap(bar_y0)  # bottom edge of the 0.17-high bar

    avail = fit_width
    nc = max(1, 1 + floor((avail - _LICON) / _LICON_PITCH))
    array_w = _snap((nc - 1) * _LICON_PITCH + _LICON)
    x_start = _snap((bar_x0 + bar_x1) / 2 - array_w / 2)

    for i in range(nc):
        x = _snap(x_start + i * _LICON_PITCH)
        _rect(c, LAYER.licon1drawing, x, cy, x + _LICON, cy + _LICON)


def _pwell_guard_ring(
    c: gf.Component,
    inner_w: float,
    inner_h: float,
    licon_fit_w: float | None = None,
) -> None:
    """Draw a p-well guard ring centred at the origin.

    ``inner_w`` and ``inner_h`` specify the full inner opening dimensions.
    ``licon_fit_w`` controls how many licons fit on the horizontal bars.
    The ring uses non-overlapping segments (sides fit between top/bottom bars).
    """
    rw = _GR_RING_W
    hw = inner_w / 2
    hh = inner_h / 2

    # Outer bounds
    ox = _snap(hw + rw)
    oy = _snap(hh + rw)

    # Tap segments (65, 44) ------------------------------------------------
    # Top & bottom bars span full outer width
    _rect(c, LAYER.tapdrawing, -ox, hh, ox, oy)  # top
    _rect(c, LAYER.tapdrawing, -ox, -oy, ox, -hh)  # bottom
    # Left & right bars span inner height only (no corner overlap)
    _rect(c, LAYER.tapdrawing, -ox, -hh, -hw, hh)  # left
    _rect(c, LAYER.tapdrawing, hw, -hh, ox, hh)  # right

    # Li1 (67, 20) — same footprint as tap --------------------------------
    _rect(c, LAYER.li1drawing, -ox, hh, ox, oy)
    _rect(c, LAYER.li1drawing, -ox, -oy, ox, -hh)
    _rect(c, LAYER.li1drawing, -ox, -hh, -hw, hh)
    _rect(c, LAYER.li1drawing, hw, -hh, ox, hh)

    # PSDM (94, 20) — 4-piece ring extending 0.125 beyond tap -------------
    pe = _PSDM_ENC
    _rect(c, LAYER.psdmdrawing, -ox - pe, hh - pe, ox + pe, oy + pe)  # top
    _rect(c, LAYER.psdmdrawing, -ox - pe, -oy - pe, ox + pe, -hh + pe)  # bottom
    _rect(c, LAYER.psdmdrawing, -ox - pe, -hh + pe, -hw + pe, hh - pe)  # left
    _rect(c, LAYER.psdmdrawing, hw - pe, -hh + pe, ox + pe, hh - pe)  # right

    # Licon contacts on guard ring -----------------------------------------
    fw = licon_fit_w if licon_fit_w is not None else inner_w
    # Horizontal bars — fit contacts based on device width
    _guard_ring_licons_horiz(c, -ox, ox, hh, oy, fit_width=fw)
    _guard_ring_licons_horiz(c, -ox, ox, -oy, -hh, fit_width=fw)

    # Vertical bars
    _guard_ring_licons_side(c, -ox, -hw, -hh, hh)
    _guard_ring_licons_side(c, hw, ox, -hh, hh)


def _pwell_guard_ring_solid_psdm(
    c: gf.Component,
    inner_w: float,
    inner_h: float,
    licon_fit_w: float | None = None,
) -> None:
    """Draw a p-well guard ring with a SOLID psdm rectangle (for high-R poly)."""
    rw = _GR_RING_W
    hw = inner_w / 2
    hh = inner_h / 2

    ox = _snap(hw + rw)
    oy = _snap(hh + rw)

    # Tap
    _rect(c, LAYER.tapdrawing, -ox, hh, ox, oy)
    _rect(c, LAYER.tapdrawing, -ox, -oy, ox, -hh)
    _rect(c, LAYER.tapdrawing, -ox, -hh, -hw, hh)
    _rect(c, LAYER.tapdrawing, hw, -hh, ox, hh)

    # Li1
    _rect(c, LAYER.li1drawing, -ox, hh, ox, oy)
    _rect(c, LAYER.li1drawing, -ox, -oy, ox, -hh)
    _rect(c, LAYER.li1drawing, -ox, -hh, -hw, hh)
    _rect(c, LAYER.li1drawing, hw, -hh, ox, hh)

    # PSDM — single solid rectangle
    pe = _PSDM_ENC
    _rect(c, LAYER.psdmdrawing, -ox - pe, -oy - pe, ox + pe, oy + pe)

    # Licon contacts
    fw = licon_fit_w if licon_fit_w is not None else inner_w
    _guard_ring_licons_horiz(c, -ox, ox, hh, oy, fit_width=fw)
    _guard_ring_licons_horiz(c, -ox, ox, -oy, -hh, fit_width=fw)
    _guard_ring_licons_side(c, -ox, -hw, -hh, hh)
    _guard_ring_licons_side(c, hw, ox, -hh, hh)


# ---------------------------------------------------------------------------
# Contact arrays (mcon)
# ---------------------------------------------------------------------------


def _mcon_array(
    c: gf.Component,
    x0: float,
    y0: float,
    x1: float,
    y1: float,
) -> None:
    """Place mcon contacts (0.17 x 0.17) in met1 area (x0,y0)-(x1,y1).

    Uses enclosure (0.030, 0.065) matching Magic's mcon placement in resistors.
    Contacts are centred in x and aligned to y0 + enc_y in y.
    """
    size = 0.17
    pitch_x = 0.36  # 0.17 + 0.19
    pitch_y = 0.36
    enc_x = 0.030
    enc_y = 0.065

    avail_w = _snap(x1 - x0 - 2 * enc_x)
    avail_h = _snap(y1 - y0 - 2 * enc_y)

    if avail_w < size or avail_h < size:
        return

    nc = max(1, 1 + floor((avail_w - size) / pitch_x))
    nr = max(1, 1 + floor((avail_h - size) / pitch_y))

    array_w = _snap((nc - 1) * pitch_x + size)

    ox = _snap((x0 + x1) / 2 - array_w / 2)
    oy = _snap(y0 + enc_y)

    for r in range(nr):
        for col in range(nc):
            x = _snap(ox + col * pitch_x)
            y = _snap(oy + r * pitch_y)
            _rect(c, LAYER.mcondrawing, x, y, x + size, y + size)


def _nd_mcon_array(
    c: gf.Component,
    x0: float,
    y0: float,
    x1: float,
    y1: float,
) -> None:
    """Place mcon contacts for ND resistor head/tail (different enc from poly)."""
    size = 0.17
    pitch_x = 0.36
    pitch_y = 0.36
    enc_x = 0.060
    enc_y = 0.060

    avail_w = _snap(x1 - x0 - 2 * enc_x)
    avail_h = _snap(y1 - y0 - 2 * enc_y)

    if avail_w < size or avail_h < size:
        return

    nc = max(1, 1 + floor((avail_w - size) / pitch_x))
    nr = max(1, 1 + floor((avail_h - size) / pitch_y))

    array_w = _snap((nc - 1) * pitch_x + size)
    array_h = _snap((nr - 1) * pitch_y + size)

    ox = _snap((x0 + x1) / 2 - array_w / 2)
    oy = _snap((y0 + y1) / 2 - array_h / 2)

    for r in range(nr):
        for col in range(nc):
            x = _snap(ox + col * pitch_x)
            y = _snap(oy + r * pitch_y)
            _rect(c, LAYER.mcondrawing, x, y, x + size, y + size)


# ---------------------------------------------------------------------------
# Head/tail poly licon contacts for generic poly resistor
# ---------------------------------------------------------------------------


def _poly_head_licons(
    c: gf.Component,
    W: float,
    licon_y0: float,
    licon_y1: float,
) -> None:
    """Place licon contacts on the poly head/tail contact region.

    Magic uses enclosure = 0.12 (poly surround of 0.08 + extra) for poly
    head contacts, giving fewer contacts than the guard ring bars.
    """
    size = 0.17
    pitch = 0.34
    enc = 0.08  # poly surround of licon contact

    avail = _snap(W - 2 * enc)
    nc = max(1, 1 + floor((avail - size) / pitch)) if avail >= size else 0
    if nc < 1:
        return

    array_w = _snap((nc - 1) * pitch + size)
    x_start = _snap(-array_w / 2)

    # Place contacts — 1 row, nc columns
    y = _snap((licon_y0 + licon_y1) / 2 - size / 2)
    for i in range(nc):
        x = _snap(x_start + i * pitch)
        _rect(c, LAYER.licon1drawing, x, y, x + size, y + size)


def _diff_head_licons(
    c: gf.Component,
    W: float,
    licon_y0: float,
    licon_y1: float,
) -> None:
    """Place licon contacts on the diffusion head/tail contact region."""
    size = 0.17
    pitch = 0.34
    enc = 0.06

    avail = _snap(W - 2 * enc)
    nc = max(1, 1 + floor((avail - size) / pitch)) if avail >= size else 0
    if nc < 1:
        return

    array_w = _snap((nc - 1) * pitch + size)
    x_start = _snap(-array_w / 2)

    y = _snap((licon_y0 + licon_y1) / 2 - size / 2)
    for i in range(nc):
        x = _snap(x_start + i * pitch)
        _rect(c, LAYER.licon1drawing, x, y, x + size, y + size)


# ===========================================================================
# res_generic_po — standard poly resistor (~48 ohm/sq)
# ===========================================================================


@gf.cell
def sky130_fd_pr__res_generic_po(
    res_width: float = 0.33,
    res_length: float = 1.65,
) -> gf.Component:
    """Return a standard poly resistor matching Magic VLSI geometry.

    Geometry: poly body centred at origin with head/tail poly contacts,
    NPC over contact ends, RPM (polyres) over resistor body, pwell guard ring.

    Args:
        res_width: width of the resistor body (W) in um.
        res_length: length of the resistor body (L) in um.

    .. plot::
      :include-source:

      import sky130

      c = sky130.pcells.sky130_fd_pr__res_generic_po()
      c.plot()
    """
    c = gf.Component()
    W = res_width
    L = res_length
    hw = _snap(W / 2)

    # ---- Key derived dimensions ----
    contact_region = 2.150  # poly extension beyond RPM for contacts
    poly_half = _snap(L / 2 + contact_region)

    gr_gap = 0.480  # gap between poly edge and guard ring inner edge
    gr_inner_x = _snap(hw + gr_gap)
    gr_inner_y = _snap(poly_half + gr_gap)
    inner_w = _snap(2 * gr_inner_x)
    inner_h = _snap(2 * gr_inner_y)

    # ---- Poly body (66, 20) — full length including contact heads ----
    _rect(c, LAYER.polydrawing, -hw, -poly_half, hw, poly_half)

    # ---- RPM / polyres (66, 13) — over resistor body only ----
    _rect(c, LAYER.polyres, -hw, -L / 2, hw, L / 2)

    # ---- NPC (95, 20) — over poly contact ends ----
    # NPC half-width = outermost licon edge + 0.100
    # (For head licons with enc=0.08: outer edge = (nc-1)*pitch/2 + 0.17/2)
    enc_licon = 0.08
    avail_licon = _snap(W - 2 * enc_licon)
    nc_licon = (
        max(1, 1 + floor((avail_licon - 0.17) / 0.34)) if avail_licon >= 0.17 else 1
    )
    licon_array_hw = _snap(((nc_licon - 1) * 0.34 + 0.17) / 2)
    npc_hw = _snap(licon_array_hw + 0.100)
    npc_h = 0.370  # NPC height
    npc_top = _snap(poly_half + 0.020)
    npc_bot = _snap(npc_top - npc_h)
    _rect(c, LAYER.npcdrawing, -npc_hw, npc_bot, npc_hw, npc_top)  # top
    _rect(c, LAYER.npcdrawing, -npc_hw, -npc_top, npc_hw, -npc_bot)  # bottom

    # ---- Guard ring ----
    # Horizontal bar licons use fit_width = W + 0.240
    _pwell_guard_ring(c, inner_w, inner_h, licon_fit_w=_snap(W + 0.240))

    # ---- Head/tail poly licon contacts (66, 44) ----
    licon_cap_bot = _snap(poly_half - 0.250)
    licon_cap_top = _snap(licon_cap_bot + _LICON)
    _poly_head_licons(c, W, licon_cap_bot, licon_cap_top)  # top head
    _poly_head_licons(c, W, -licon_cap_top, -licon_cap_bot)  # bottom head

    # ---- Li1 head/tail (67, 20) ----
    # Cap (full poly width) over licon
    _rect(c, LAYER.li1drawing, -hw, licon_cap_bot, hw, licon_cap_top)  # top cap
    _rect(c, LAYER.li1drawing, -hw, -licon_cap_top, hw, -licon_cap_bot)  # bottom cap

    # Vertical strip connecting cap to met1 area
    li_strip_hw = _snap(hw - 0.080)
    li_strip_bot = _snap(L / 2 + 0.085)
    li_strip_top = licon_cap_bot
    _rect(
        c, LAYER.li1drawing, -li_strip_hw, li_strip_bot, li_strip_hw, li_strip_top
    )  # top
    _rect(
        c, LAYER.li1drawing, -li_strip_hw, -li_strip_top, li_strip_hw, -li_strip_bot
    )  # bottom

    # ---- Met1 (68, 20) ----
    m1_hw = _snap(hw - 0.050)
    m1_inner = _snap(L / 2 + 0.025)
    m1_outer = _snap(poly_half - 0.020)
    _rect(c, LAYER.met1drawing, -m1_hw, m1_inner, m1_hw, m1_outer)  # top
    _rect(c, LAYER.met1drawing, -m1_hw, -m1_outer, m1_hw, -m1_inner)  # bottom

    # ---- Mcon contacts (67, 44) ----
    _mcon_array(c, -m1_hw, m1_inner, m1_hw, m1_outer)  # top
    _mcon_array(c, -m1_hw, -m1_outer, m1_hw, -m1_inner)  # bottom

    # ---- Boundary marker (235, 4) ----
    bnd_x = _snap(gr_inner_x + _GR_RING_W - 0.085)
    bnd_y = _snap(gr_inner_y + _GR_RING_W - 0.085)
    _rect(c, LAYER.prBoundaryboundary, -bnd_x, -bnd_y, bnd_x, bnd_y)

    # ---- Labels (match Magic output on li1label) ----
    mcon_cy = _snap((m1_inner + m1_outer) / 2)
    gr_bottom = _snap(-(gr_inner_y + _GR_RING_W))
    c.add_label(text="R1", position=(0, mcon_cy), layer=LAYER.li1label)
    c.add_label(text="R2", position=(0, -mcon_cy), layer=LAYER.li1label)
    c.add_label(text="B", position=(0, gr_bottom), layer=LAYER.li1label)

    # ---- Ports ----
    c.add_port(
        name="PLUS",
        center=(0, m1_outer),
        width=W,
        orientation=90,
        layer=LAYER.met1drawing,
    )
    c.add_port(
        name="MINUS",
        center=(0, -m1_outer),
        width=W,
        orientation=270,
        layer=LAYER.met1drawing,
    )

    return c


# ===========================================================================
# res_high_po_0p35 — high-resistance poly resistor
# ===========================================================================


@gf.cell
def sky130_fd_pr__res_high_po_0p35(
    res_width: float = 0.35,
    res_length: float = 0.50,
) -> gf.Component:
    """Return a high-resistance poly resistor matching Magic VLSI geometry.

    Different from generic_po: uses rpmdrawing (86,20), single NPC covering
    entire poly, solid PSDM, continuous licon contact strips, and different
    contact region dimensions.

    Args:
        res_width: width of the resistor body (W) in um.
        res_length: length of the resistor body (L) in um.

    .. plot::
      :include-source:

      import sky130

      c = sky130.pcells.sky130_fd_pr__res_high_po_0p35()
      c.plot()
    """
    c = gf.Component()
    W = res_width
    L = res_length
    hw = _snap(W / 2)

    # ---- Key derived dimensions ----
    contact_region = 2.080
    poly_half = _snap(L / 2 + contact_region)

    gr_gap = 0.480
    gr_inner_x = _snap(hw + gr_gap)
    gr_inner_y = _snap(poly_half + gr_gap)
    inner_w = _snap(2 * gr_inner_x)
    inner_h = _snap(2 * gr_inner_y)

    # ---- Poly body (66, 20) ----
    _rect(c, LAYER.polydrawing, -hw, -poly_half, hw, poly_half)

    # ---- RPM (86, 20) — extends 0.200 beyond poly ----
    rpm_enc = 0.200
    _rect(
        c,
        LAYER.rpmdrawing,
        -hw - rpm_enc,
        -poly_half - rpm_enc,
        hw + rpm_enc,
        poly_half + rpm_enc,
    )

    # ---- polyres (66, 13) — just the resistor body ----
    _rect(c, LAYER.polyres, -hw, -L / 2, hw, L / 2)

    # ---- NPC (95, 20) — single rectangle covering entire poly + 0.095 ----
    npc_enc = 0.095
    _rect(
        c,
        LAYER.npcdrawing,
        -hw - npc_enc,
        -poly_half - npc_enc,
        hw + npc_enc,
        poly_half + npc_enc,
    )

    # ---- Guard ring with solid PSDM ----
    _pwell_guard_ring_solid_psdm(c, inner_w, inner_h, licon_fit_w=_snap(W + 0.240))

    # ---- Continuous licon strips (66, 44) on poly head/tail ----
    # Strip width = W - 2*0.080 = W - 0.160
    licon_strip_hw = _snap(hw - 0.080)
    licon_strip_len = 2.000  # fixed length
    licon_strip_bot = _snap(L / 2)
    licon_strip_top = _snap(licon_strip_bot + licon_strip_len)

    # Top head
    _rect(
        c,
        LAYER.licon1drawing,
        -licon_strip_hw,
        licon_strip_bot,
        licon_strip_hw,
        licon_strip_top,
    )
    # Bottom head
    _rect(
        c,
        LAYER.licon1drawing,
        -licon_strip_hw,
        -licon_strip_top,
        licon_strip_hw,
        -licon_strip_bot,
    )

    # ---- Li1 head/tail (67, 20) — full poly width ----
    li_bot = _snap(L / 2 - 0.080)
    li_top = poly_half
    _rect(c, LAYER.li1drawing, -hw, li_bot, hw, li_top)  # top
    _rect(c, LAYER.li1drawing, -hw, -li_top, hw, -li_bot)  # bottom

    # ---- Met1 (68, 20) ----
    m1_hw = _snap(hw - 0.050)
    m1_inner = _snap(L / 2 - 0.055)
    m1_outer = _snap(poly_half - 0.030)
    _rect(c, LAYER.met1drawing, -m1_hw, m1_inner, m1_hw, m1_outer)  # top
    _rect(c, LAYER.met1drawing, -m1_hw, -m1_outer, m1_hw, -m1_inner)  # bottom

    # ---- Mcon contacts (67, 44) ----
    _mcon_array(c, -m1_hw, m1_inner, m1_hw, m1_outer)  # top
    _mcon_array(c, -m1_hw, -m1_outer, m1_hw, -m1_inner)  # bottom

    # ---- Boundary marker (235, 4) ----
    bnd_x = _snap(gr_inner_x + _GR_RING_W - 0.085)
    bnd_y = _snap(gr_inner_y + _GR_RING_W - 0.085)
    _rect(c, LAYER.prBoundaryboundary, -bnd_x, -bnd_y, bnd_x, bnd_y)

    # ---- Labels ----
    mcon_cy = _snap((m1_inner + m1_outer) / 2)
    gr_bottom = _snap(-(gr_inner_y + _GR_RING_W))
    c.add_label(text="R1", position=(0, mcon_cy), layer=LAYER.li1label)
    c.add_label(text="R2", position=(0, -mcon_cy), layer=LAYER.li1label)
    c.add_label(text="B", position=(0, gr_bottom), layer=LAYER.li1label)

    # ---- Ports ----
    c.add_port(
        name="PLUS",
        center=(0, m1_outer),
        width=W,
        orientation=90,
        layer=LAYER.met1drawing,
    )
    c.add_port(
        name="MINUS",
        center=(0, -m1_outer),
        width=W,
        orientation=270,
        layer=LAYER.met1drawing,
    )

    return c


# Keep backward compatibility alias
sky130_fd_pr__res_high_po = sky130_fd_pr__res_high_po_0p35


# ===========================================================================
# res_generic_nd — N+ diffusion resistor
# ===========================================================================


@gf.cell
def sky130_fd_pr__res_generic_nd(
    res_width: float = 0.42,
    res_length: float = 2.10,
) -> gf.Component:
    """Return an N+ diffusion resistor matching Magic VLSI geometry.

    Geometry: diffusion body centred at origin with licon contacts at
    head/tail, NSDM implant, diffres marker, and pwell guard ring.

    Args:
        res_width: width of the resistor body (W) in um.
        res_length: length of the resistor body (L) in um.

    .. plot::
      :include-source:

      import sky130

      c = sky130.pcells.sky130_fd_pr__res_generic_nd()
      c.plot()
    """
    c = gf.Component()
    W = res_width
    L = res_length
    hw = _snap(W / 2)

    # ---- Key derived dimensions ----
    contact_region = 0.515
    diff_half = _snap(L / 2 + contact_region)

    gr_gap = 0.440
    gr_inner_x = _snap(hw + gr_gap)
    gr_inner_y = _snap(diff_half + gr_gap)
    inner_w = _snap(2 * gr_inner_x)
    inner_h = _snap(2 * gr_inner_y)

    # ---- Diffusion body (65, 20) ----
    _rect(c, LAYER.diffdrawing, -hw, -diff_half, hw, diff_half)

    # ---- diffres (65, 13) — resistor marker ----
    _rect(c, LAYER.diffres, -hw, -L / 2, hw, L / 2)

    # ---- NSDM (93, 44) — N+ implant extending 0.125 beyond diff ----
    nsdm_enc = 0.125
    _rect(
        c,
        LAYER.nsdmdrawing,
        -hw - nsdm_enc,
        -diff_half - nsdm_enc,
        hw + nsdm_enc,
        diff_half + nsdm_enc,
    )

    # ---- Guard ring ----
    _pwell_guard_ring(c, inner_w, inner_h, licon_fit_w=_snap(W + 0.240))

    # ---- Head/tail licon contacts on diff (66, 44) ----
    licon_enc_diff = 0.060
    licon_top = _snap(diff_half - licon_enc_diff)
    licon_bot = _snap(licon_top - _LICON)
    _diff_head_licons(c, W, licon_bot, licon_top)  # top head
    _diff_head_licons(c, W, -licon_top, -licon_bot)  # bottom head

    # ---- Li1 head/tail (67, 20) ----
    # Cap over licon area
    li_cap_hw = _snap(hw + 0.020)
    _rect(c, LAYER.li1drawing, -li_cap_hw, licon_bot, li_cap_hw, licon_top)  # top cap
    _rect(
        c, LAYER.li1drawing, -li_cap_hw, -licon_top, li_cap_hw, -licon_bot
    )  # bottom cap

    # Short connecting strip below the cap
    li_strip_hw = _snap(hw - 0.060)
    li_strip_h = 0.200
    li_strip_top = licon_bot
    li_strip_bot = _snap(li_strip_top - li_strip_h)
    _rect(
        c, LAYER.li1drawing, -li_strip_hw, li_strip_bot, li_strip_hw, li_strip_top
    )  # top
    _rect(
        c, LAYER.li1drawing, -li_strip_hw, -li_strip_top, li_strip_hw, -li_strip_bot
    )  # bottom

    # ---- Met1 (68, 20) ----
    # Met1 dimensions scale with diffusion size:
    # hw = W/2 - 0.030 for narrow, W/2 for wide (when W >= ~0.7)
    # outer = diff_half for narrow, diff_half - 0.030 for wide
    # inner = outer - met1_height
    # met1 height for W=0.42: 0.490, for W=1.0: 0.430
    m1_hw = _snap(hw - 0.030)
    m1_outer = _snap(diff_half)
    m1_inner = _snap(L / 2 + 0.025)

    # Adjust for wide devices: met1 expands to full diffusion width
    # and outer retracts by 0.030
    if W >= 0.70:
        m1_hw = hw
        m1_outer = _snap(diff_half - 0.030)
        m1_inner = _snap(m1_outer - 0.430)

    _rect(c, LAYER.met1drawing, -m1_hw, m1_inner, m1_hw, m1_outer)
    _rect(c, LAYER.met1drawing, -m1_hw, -m1_outer, m1_hw, -m1_inner)

    # ---- Mcon contacts (67, 44) ----
    _nd_mcon_array(c, -m1_hw, m1_inner, m1_hw, m1_outer)
    _nd_mcon_array(c, -m1_hw, -m1_outer, m1_hw, -m1_inner)

    # ---- Boundary marker (235, 4) ----
    bnd_x = _snap(gr_inner_x + _GR_RING_W - 0.085)
    bnd_y = _snap(gr_inner_y + _GR_RING_W - 0.085)
    _rect(c, LAYER.prBoundaryboundary, -bnd_x, -bnd_y, bnd_x, bnd_y)

    # ---- Labels ----
    mcon_cy = _snap((m1_inner + m1_outer) / 2)
    gr_bottom = _snap(-(gr_inner_y + _GR_RING_W))
    c.add_label(text="R1", position=(0, mcon_cy), layer=LAYER.li1label)
    c.add_label(text="R2", position=(0, -mcon_cy), layer=LAYER.li1label)
    c.add_label(text="B", position=(0, gr_bottom), layer=LAYER.li1label)

    # ---- Ports ----
    c.add_port(
        name="PLUS",
        center=(0, m1_outer),
        width=W,
        orientation=90,
        layer=LAYER.met1drawing,
    )
    c.add_port(
        name="MINUS",
        center=(0, -m1_outer),
        width=W,
        orientation=270,
        layer=LAYER.met1drawing,
    )

    return c


if __name__ == "__main__":
    c = sky130_fd_pr__res_generic_po()
    c.show()
