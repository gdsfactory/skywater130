"""Guard ring generators for sky130.

Provides pwell and nwell guard rings used to isolate NMOS and PMOS devices.
"""

import gdsfactory as gf

from sky130.layers import LAYER
from sky130.pcells.contact import contact_array


@gf.cell
def pwell_guard_ring(
    inner_width: float = 2.0,
    inner_height: float = 2.0,
    ring_width: float = 0.34,
    spacing: float = 0.27,
) -> gf.Component:
    """P+ substrate guard ring for NMOS isolation.

    Places a ring of tap (P+ diffusion) around an inner area of size
    inner_width x inner_height.  The ring is built from four rectangular
    segments whose corners overlap so there are no gaps.

    Layers applied:
      - tapdrawing  — ring body (substrate / well tap)
      - psdmdrawing — P+ implant, extends 0.125 um beyond tap on every side
      - li1drawing  — local interconnect covering the tap ring
      - licon1drawing — LiCon contacts along every edge (via contact_array)

    A port named "VSS" is placed on the li1drawing layer at the centre of the
    bottom edge, oriented downward (270 degrees).

    Args:
        inner_width: width of the inner area to be surrounded.
        inner_height: height of the inner area to be surrounded.
        ring_width: width of the tap ring.
        spacing: gap between the inner area and the inner edge of the ring.

    .. plot::
      :include-source:

      import sky130

      c = sky130.pcells.pwell_guard_ring()
      c.plot()
    """
    return _guard_ring(
        inner_width=inner_width,
        inner_height=inner_height,
        ring_width=ring_width,
        spacing=spacing,
        implant_layer=LAYER.psdmdrawing,
        port_name="VSS",
        add_nwell=False,
    )


@gf.cell
def nwell_guard_ring(
    inner_width: float = 2.0,
    inner_height: float = 2.0,
    ring_width: float = 0.34,
    spacing: float = 0.27,
) -> gf.Component:
    """N-well guard ring for PMOS isolation.

    Same structure as pwell_guard_ring but adds an nwelldrawing region under
    the entire ring (extending 0.18 um beyond tap on every side) and uses
    nsdmdrawing (N+ implant) instead of psdmdrawing.

    The supply port is named "VDD" instead of "VSS".

    Args:
        inner_width: width of the inner area to be surrounded.
        inner_height: height of the inner area to be surrounded.
        ring_width: width of the tap ring.
        spacing: gap between the inner area and the inner edge of the ring.

    .. plot::
      :include-source:

      import sky130

      c = sky130.pcells.nwell_guard_ring()
      c.plot()
    """
    return _guard_ring(
        inner_width=inner_width,
        inner_height=inner_height,
        ring_width=ring_width,
        spacing=spacing,
        implant_layer=LAYER.nsdmdrawing,
        port_name="VDD",
        add_nwell=True,
    )


def _guard_ring(
    inner_width: float,
    inner_height: float,
    ring_width: float,
    spacing: float,
    implant_layer,
    port_name: str,
    add_nwell: bool,
) -> gf.Component:
    """Shared implementation for pwell and nwell guard rings.

    The inner area spans (0, 0) → (inner_width, inner_height).

    Ring coordinates (all four segments use full-corner overlap):
      - outer extent: -(spacing + ring_width)  to  inner_width  + (spacing + ring_width)
      - inner extent: -spacing                 to  inner_width  + spacing

    The four rectangular tap segments are:
      bottom:  x_outer_left  → x_outer_right,  y from -(s+rw) → -s
      top:     x_outer_left  → x_outer_right,  y from  ih+s   → ih+s+rw
      left:    x from -(s+rw) → -s,            y from -(s+rw) → ih+(s+rw)
      right:   x from  iw+s  → iw+s+rw,        y from -(s+rw) → ih+(s+rw)

    Implant (PSDM / NSDM) extends 0.125 um beyond tap.
    N-well (nwell variant only) extends 0.18 um beyond tap.
    """
    c = gf.Component()

    s = spacing
    rw = ring_width
    iw = inner_width
    ih = inner_height

    implant_ext = 0.125
    nwell_ext = 0.18

    # Ring outer and inner bounds
    x0 = -(s + rw)   # outer left
    x1 = iw + s + rw  # outer right
    y0 = -(s + rw)   # outer bottom
    y1 = ih + s + rw  # outer top

    # Four tap segments -------------------------------------------------------
    # bottom and top segments span full outer width (corner overlap)
    seg_bottom_x = x0
    seg_bottom_y = -(s + rw)
    seg_bottom_w = x1 - x0
    seg_bottom_h = rw

    seg_top_x = x0
    seg_top_y = ih + s
    seg_top_w = x1 - x0
    seg_top_h = rw

    # left and right segments span full outer height (corner overlap)
    seg_left_x = -(s + rw)
    seg_left_y = -(s + rw)
    seg_left_w = rw
    seg_left_h = ih + 2 * (s + rw)

    seg_right_x = iw + s
    seg_right_y = -(s + rw)
    seg_right_w = rw
    seg_right_h = ih + 2 * (s + rw)

    def add_rect(layer, x, y, w, h):
        rect = gf.components.rectangle(size=(w, h), layer=layer)
        ref = c.add_ref(rect)
        ref.move((x, y))
        return ref

    # --- tap (tapdrawing) ---
    add_rect(LAYER.tapdrawing, seg_bottom_x, seg_bottom_y, seg_bottom_w, seg_bottom_h)
    add_rect(LAYER.tapdrawing, seg_top_x, seg_top_y, seg_top_w, seg_top_h)
    add_rect(LAYER.tapdrawing, seg_left_x, seg_left_y, seg_left_w, seg_left_h)
    add_rect(LAYER.tapdrawing, seg_right_x, seg_right_y, seg_right_w, seg_right_h)

    # --- implant (psdmdrawing or nsdmdrawing) extends 0.125 beyond tap ---
    imp_ext = implant_ext
    add_rect(
        implant_layer,
        x0 - imp_ext,
        y0 - imp_ext,
        (x1 - x0) + 2 * imp_ext,
        (y1 - y0) + 2 * imp_ext,
    )

    # --- li1drawing (local interconnect) — same footprint as implant-less outer ring ---
    # Li1 covers the ring body (tap footprint), also using full-extent rectangles
    add_rect(LAYER.li1drawing, seg_bottom_x, seg_bottom_y, seg_bottom_w, seg_bottom_h)
    add_rect(LAYER.li1drawing, seg_top_x, seg_top_y, seg_top_w, seg_top_h)
    add_rect(LAYER.li1drawing, seg_left_x, seg_left_y, seg_left_w, seg_left_h)
    add_rect(LAYER.li1drawing, seg_right_x, seg_right_y, seg_right_w, seg_right_h)

    # --- nwelldrawing (nwell variant only) extends 0.18 beyond tap ---
    if add_nwell:
        nw_ext = nwell_ext
        add_rect(
            LAYER.nwelldrawing,
            x0 - nw_ext,
            y0 - nw_ext,
            (x1 - x0) + 2 * nw_ext,
            (y1 - y0) + 2 * nw_ext,
        )

    # --- licon1drawing contacts along each edge via contact_array ---
    # Bottom edge
    bot_cont = c.add_ref(
        contact_array(
            width=seg_bottom_w,
            height=seg_bottom_h,
            contact_layer=LAYER.licon1drawing,
        )
    )
    bot_cont.move((seg_bottom_x, seg_bottom_y))

    # Top edge
    top_cont = c.add_ref(
        contact_array(
            width=seg_top_w,
            height=seg_top_h,
            contact_layer=LAYER.licon1drawing,
        )
    )
    top_cont.move((seg_top_x, seg_top_y))

    # Left edge
    left_cont = c.add_ref(
        contact_array(
            width=seg_left_w,
            height=seg_left_h,
            contact_layer=LAYER.licon1drawing,
        )
    )
    left_cont.move((seg_left_x, seg_left_y))

    # Right edge
    right_cont = c.add_ref(
        contact_array(
            width=seg_right_w,
            height=seg_right_h,
            contact_layer=LAYER.licon1drawing,
        )
    )
    right_cont.move((seg_right_x, seg_right_y))

    # --- Port on li1drawing at bottom edge centre, pointing down (270 deg) ---
    bottom_centre_x = seg_bottom_x + seg_bottom_w / 2
    bottom_edge_y = seg_bottom_y  # bottom of the bottom tap segment

    c.add_port(
        name=port_name,
        center=(bottom_centre_x, bottom_edge_y),
        width=seg_bottom_w,
        orientation=270,
        layer=LAYER.li1drawing,
        port_type="electrical",
    )

    return c


if __name__ == "__main__":
    c = pwell_guard_ring()
    c.show()
