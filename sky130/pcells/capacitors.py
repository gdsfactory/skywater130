"""MIM capacitor pcells for sky130.

Provides:
    sky130_fd_pr__cap_mim_m3_1 — MIM capacitor between M3 (bottom) and M4 (top)
    sky130_fd_pr__cap_mim_m3_2 — MIM capacitor between M4 (bottom) and M5 (top)

Geometry matches Magic VLSI output exactly: the cap is asymmetric with the MIM
dielectric plate on the left side and a bottom-plate via pickup strip on the
right.  The bottom metal layer extends across the full cell width, with
the upper metal split into two rectangles (top plate landing + bottom plate
connection).
"""

from __future__ import annotations

from math import floor

import gdsfactory as gf

from sky130.layers import LAYER


# ---------------------------------------------------------------------------
# Helpers (same pattern as mosfets.py)
# ---------------------------------------------------------------------------


def _snap(val: float, grid: float = 0.005) -> float:
    """Snap a value to the nearest grid point (default 5 nm)."""
    return round(val / grid) * grid


def _rect(c: gf.Component, layer, x0: float, y0: float, x1: float, y1: float):
    """Add a rectangle from (x0, y0) to (x1, y1), snapped to grid."""
    x0, y0, x1, y1 = _snap(x0), _snap(y0), _snap(x1), _snap(y1)
    c.add_polygon([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], layer=layer)


def _via_array(
    c: gf.Component,
    layer,
    region_x0: float,
    region_y0: float,
    region_x1: float,
    region_y1: float,
    via_size: float,
    via_pitch: float,
    enc_x: float,
    enc_y: float,
) -> None:
    """Place a centered grid of square vias within a rectangular region.

    Parameters
    ----------
    region_x0, region_y0, region_x1, region_y1 : float
        Bounding box of the region within which vias are placed.
    via_size : float
        Side length of each square via.
    via_pitch : float
        Centre-to-centre pitch (= via_size + spacing).
    enc_x, enc_y : float
        Minimum enclosure on each side used to compute the available area
        for the array.  The actual array is then centered in the full region.
    """
    w = _snap(region_x1 - region_x0)
    h = _snap(region_y1 - region_y0)

    avail_w = _snap(w - 2 * enc_x)
    avail_h = _snap(h - 2 * enc_y)

    if avail_w < via_size - 1e-9 or avail_h < via_size - 1e-9:
        return

    nc = 1 + floor((avail_w - via_size) / via_pitch + 1e-9)
    nr = 1 + floor((avail_h - via_size) / via_pitch + 1e-9)
    nc = max(nc, 1)
    nr = max(nr, 1)

    array_w = nc * via_size + (nc - 1) * (via_pitch - via_size)
    array_h = nr * via_size + (nr - 1) * (via_pitch - via_size)

    # Center the array within the full region
    ox = region_x0 + (w - array_w) / 2
    oy = region_y0 + (h - array_h) / 2

    for col in range(nc):
        for row in range(nr):
            vx = ox + col * via_pitch
            vy = oy + row * via_pitch
            _rect(c, layer, vx, vy, vx + via_size, vy + via_size)


# ---------------------------------------------------------------------------
# cap_mim_m3_1 — MIM between M3 (bottom plate) and M4 (top plate)
# ---------------------------------------------------------------------------

# Design-rule constants for M3/M4 MIM (from Magic reference geometry)
_M31_MET3_ENC_CAPM = 0.200      # met3 enclosure of capm on left/top/bottom
_M31_MET3_RIGHT_EXT = 1.960     # met3 extends this far to the right of capm
_M31_MET4_TOP_INSET = 0.195     # met4 top-plate inset from capm on all sides
_M31_MET4_BOT_WIDTH = 0.480     # met4 bottom-plate pickup strip width (X)
_M31_MET4_BOT_INSET_R = 0.020  # met4 bot inset from met3 right edge
_M31_MET4_BOT_INSET_Y = 0.060  # met4 bot inset from met3 top/bottom
_M31_VIA3_SIZE = 0.200
_M31_VIA3_PITCH = 0.400
_M31_VIA3_ENC_TOP = 0.300       # via3 enclosure within capm for top plate
_M31_VIA3_ENC_BOT_X = 0.140    # via3 enclosure within met4_bot (X)
_M31_VIA3_ENC_BOT_Y = 0.140    # via3 enclosure within met4_bot (Y)


@gf.cell
def sky130_fd_pr__cap_mim_m3_1(
    cap_width: float = 2.0,
    cap_length: float = 2.0,
) -> gf.Component:
    """MIM capacitor between Metal 3 (bottom plate) and Metal 4 (top plate).

    The layout is asymmetric: the capm (MIM dielectric) layer sits on the
    left side of the cell with met4 landing on top, while a bottom-plate
    pickup strip (met4 over via3 down to met3) occupies the right side.

    All geometry is centered at the origin to match Magic's output.

    Args:
        cap_width: X-dimension of the MIM dielectric (capm) in um.
        cap_length: Y-dimension of the MIM dielectric (capm) in um.

    .. plot::
      :include-source:

      import sky130

      c = sky130.pcells.sky130_fd_pr__cap_mim_m3_1()
      c.plot()
    """
    c = gf.Component()
    W = cap_width
    L = cap_length

    # ---- met3 (bottom plate) — centered at origin ----
    met3_sx = _M31_MET3_ENC_CAPM + W + _M31_MET3_RIGHT_EXT
    met3_sy = L + 2 * _M31_MET3_ENC_CAPM

    met3_l = -met3_sx / 2
    met3_r = met3_sx / 2
    met3_b = -met3_sy / 2
    met3_t = met3_sy / 2

    _rect(c, LAYER.met3drawing, met3_l, met3_b, met3_r, met3_t)

    # ---- capm (MIM dielectric) ----
    capm_l = met3_l + _M31_MET3_ENC_CAPM
    capm_r = capm_l + W
    capm_b = -L / 2
    capm_t = L / 2

    _rect(c, LAYER.capm, capm_l, capm_b, capm_r, capm_t)

    # ---- prBoundary (235,4) — covers capm + enclosure area only ----
    _rect(
        c,
        LAYER.prBoundaryboundary,
        met3_l,
        met3_b,
        capm_r + _M31_MET3_ENC_CAPM,
        met3_t,
    )

    # ---- met4 top plate (over capm) ----
    inset = _M31_MET4_TOP_INSET
    met4t_l = capm_l + inset
    met4t_r = capm_r - inset
    met4t_b = capm_b + inset
    met4t_t = capm_t - inset

    _rect(c, LAYER.met4drawing, met4t_l, met4t_b, met4t_r, met4t_t)

    # ---- met4 bottom-plate pickup strip (right side) ----
    met4b_r = met3_r - _M31_MET4_BOT_INSET_R
    met4b_l = met4b_r - _M31_MET4_BOT_WIDTH
    met4b_b = met3_b + _M31_MET4_BOT_INSET_Y
    met4b_t = met3_t - _M31_MET4_BOT_INSET_Y

    _rect(c, LAYER.met4drawing, met4b_l, met4b_b, met4b_r, met4b_t)

    # ---- via3 array — top plate (within capm region) ----
    _via_array(
        c,
        LAYER.via3drawing,
        capm_l,
        capm_b,
        capm_r,
        capm_t,
        _M31_VIA3_SIZE,
        _M31_VIA3_PITCH,
        _M31_VIA3_ENC_TOP,
        _M31_VIA3_ENC_TOP,
    )

    # ---- via3 array — bottom plate pickup (within met4_bot) ----
    _via_array(
        c,
        LAYER.via3drawing,
        met4b_l,
        met4b_b,
        met4b_r,
        met4b_t,
        _M31_VIA3_SIZE,
        _M31_VIA3_PITCH,
        _M31_VIA3_ENC_BOT_X,
        _M31_VIA3_ENC_BOT_Y,
    )

    # ---- Labels on met4label (71,5) ----
    c1_x = _snap((capm_l + capm_r) / 2)
    c2_x = _snap((met4b_l + met4b_r) / 2)
    c.add_label(text="C1", position=(c1_x, 0.0), layer=LAYER.met4label)
    c.add_label(text="C2", position=(c2_x, 0.0), layer=LAYER.met4label)

    # ---- Ports ----
    c.add_port(
        name="BOTTOM",
        center=(0.0, 0.0),
        width=min(met3_sx, met3_sy),
        orientation=90,
        layer=LAYER.met3drawing,
    )
    c.add_port(
        name="TOP",
        center=(c1_x, 0.0),
        width=min(met4t_r - met4t_l, met4t_t - met4t_b),
        orientation=90,
        layer=LAYER.met4drawing,
    )

    return c


# ---------------------------------------------------------------------------
# cap_mim_m3_2 — MIM between M4 (bottom plate) and M5 (top plate)
# ---------------------------------------------------------------------------

# Design-rule constants for M4/M5 MIM
_M32_MET4_ENC_CAP2M = 0.400     # met4 enclosure of cap2m on left/top/bottom
_M32_MET4_RIGHT_EXT = 3.090     # met4 extends this far to the right of cap2m
_M32_MET5_TOP_INSET = 0.080     # met5 top-plate inset from cap2m on all sides
_M32_MET5_BOT_WIDTH = 1.600     # met5 bottom-plate pickup strip width (X)
_M32_MET5_BOT_EXT_R = 0.110     # met5 bot extends beyond met4 right edge
_M32_MET5_BOT_EXT_Y = 0.005     # met5 bot extends beyond met4 top/bottom
_M32_VIA4_SIZE = 0.800
_M32_VIA4_PITCH = 1.600
_M32_VIA4_ENC_TOP_X = 0.000     # via4 within cap2m: use full area (centered)
_M32_VIA4_ENC_TOP_Y = 0.000
_M32_VIA4_ENC_BOT_X = 0.400     # via4 within met5_bot: 0.400 enclosure
_M32_VIA4_ENC_BOT_Y = 0.400


@gf.cell
def sky130_fd_pr__cap_mim_m3_2(
    cap_width: float = 2.0,
    cap_length: float = 2.0,
) -> gf.Component:
    """MIM capacitor between Metal 4 (bottom plate) and Metal 5 (top plate).

    Same asymmetric layout as cap_mim_m3_1 but one metal layer up: cap2m
    dielectric on the left, bottom-plate pickup on the right.

    All geometry is centered at the origin to match Magic's output.

    Args:
        cap_width: X-dimension of the MIM dielectric (cap2m) in um.
        cap_length: Y-dimension of the MIM dielectric (cap2m) in um.

    .. plot::
      :include-source:

      import sky130

      c = sky130.pcells.sky130_fd_pr__cap_mim_m3_2()
      c.plot()
    """
    c = gf.Component()
    W = cap_width
    L = cap_length

    # ---- met4 (bottom plate) — centered at origin ----
    met4_sx = _M32_MET4_ENC_CAP2M + W + _M32_MET4_RIGHT_EXT
    met4_sy = L + 2 * _M32_MET4_ENC_CAP2M

    met4_l = -met4_sx / 2
    met4_r = met4_sx / 2
    met4_b = -met4_sy / 2
    met4_t = met4_sy / 2

    _rect(c, LAYER.met4drawing, met4_l, met4_b, met4_r, met4_t)

    # ---- cap2m (MIM dielectric) ----
    cap2m_l = met4_l + _M32_MET4_ENC_CAP2M
    cap2m_r = cap2m_l + W
    cap2m_b = -L / 2
    cap2m_t = L / 2

    _rect(c, LAYER.cap2m, cap2m_l, cap2m_b, cap2m_r, cap2m_t)

    # ---- prBoundary (235,4) — covers cap2m + enclosure area only ----
    _rect(
        c,
        LAYER.prBoundaryboundary,
        met4_l,
        met4_b,
        cap2m_r + _M32_MET4_ENC_CAP2M,
        met4_t,
    )

    # ---- met5 top plate (over cap2m) ----
    inset = _M32_MET5_TOP_INSET
    met5t_l = cap2m_l + inset
    met5t_r = cap2m_r - inset
    met5t_b = cap2m_b + inset
    met5t_t = cap2m_t - inset

    _rect(c, LAYER.met5drawing, met5t_l, met5t_b, met5t_r, met5t_t)

    # ---- met5 bottom-plate pickup strip (right side) ----
    met5b_r = met4_r + _M32_MET5_BOT_EXT_R
    met5b_l = met5b_r - _M32_MET5_BOT_WIDTH
    met5b_b = met4_b - _M32_MET5_BOT_EXT_Y
    met5b_t = met4_t + _M32_MET5_BOT_EXT_Y

    _rect(c, LAYER.met5drawing, met5b_l, met5b_b, met5b_r, met5b_t)

    # ---- via4 array — top plate (within cap2m region) ----
    _via_array(
        c,
        LAYER.via4drawing,
        cap2m_l,
        cap2m_b,
        cap2m_r,
        cap2m_t,
        _M32_VIA4_SIZE,
        _M32_VIA4_PITCH,
        _M32_VIA4_ENC_TOP_X,
        _M32_VIA4_ENC_TOP_Y,
    )

    # ---- via4 array — bottom plate pickup (within met5_bot) ----
    _via_array(
        c,
        LAYER.via4drawing,
        met5b_l,
        met5b_b,
        met5b_r,
        met5b_t,
        _M32_VIA4_SIZE,
        _M32_VIA4_PITCH,
        _M32_VIA4_ENC_BOT_X,
        _M32_VIA4_ENC_BOT_Y,
    )

    # ---- Labels on met5label (72,5) ----
    c1_x = _snap((cap2m_l + cap2m_r) / 2)
    c2_x = _snap((met5b_l + met5b_r) / 2)
    c.add_label(text="C1", position=(c1_x, 0.0), layer=LAYER.met5label)
    c.add_label(text="C2", position=(c2_x, 0.0), layer=LAYER.met5label)

    # ---- Ports ----
    c.add_port(
        name="BOTTOM",
        center=(0.0, 0.0),
        width=min(met4_sx, met4_sy),
        orientation=90,
        layer=LAYER.met4drawing,
    )
    c.add_port(
        name="TOP",
        center=(c1_x, 0.0),
        width=min(met5t_r - met5t_l, met5t_t - met5t_b),
        orientation=90,
        layer=LAYER.met5drawing,
    )

    return c


if __name__ == "__main__":
    c1 = sky130_fd_pr__cap_mim_m3_1()
    c1.show()
    c2 = sky130_fd_pr__cap_mim_m3_2()
    c2.show()
