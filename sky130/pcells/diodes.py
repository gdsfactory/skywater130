"""Diode pcell generators for sky130.

Provides N+/P-well and P+/N-well diode parametric cells matching the sky130
process device geometries, including diffusion implant layers, licon contacts,
li1 pads, and optional guard rings.
"""

import gdsfactory as gf

from sky130.layers import LAYER
from sky130.pcells.contact import licon_array
from sky130.pcells.guard_ring import nwell_guard_ring, pwell_guard_ring


def _add_rect(c: gf.Component, layer, x: float, y: float, w: float, h: float):
    """Add a rectangle to a component using polygon coordinates."""
    c.add_polygon(
        [(x, y), (x + w, y), (x + w, y + h), (x, y + h)],
        layer=layer,
    )


@gf.cell
def sky130_fd_pr__diode_pw2nd_05v5(
    diode_width: float = 0.42,
    diode_length: float = 0.42,
    guard_ring: bool = True,
) -> gf.Component:
    """Return an N+/P-well diode (cathode is N+ diffusion in P-well substrate).

    Geometry: diffdrawing rectangle with NSDM implant, licon contacts, and
    li1 pad.  An optional P+ substrate guard ring (pwell type) surrounds the
    diode.

    Ports:
      CATHODE — on li1drawing at top of diffusion area.
      ANODE   — on li1drawing at the guard ring bottom (or bottom of cell when
                guard_ring=False).

    Args:
        diode_width: width of the diode diffusion in um.
        diode_length: length (height) of the diode diffusion in um.
        guard_ring: when True, add a pwell guard ring around the diode.

    .. plot::
      :include-source:

      import sky130

      c = sky130.pcells.sky130_fd_pr__diode_pw2nd_05v5()
      c.plot()
    """
    c = gf.Component()

    li_enc = 0.08  # li1 enclosure beyond licon/contact area
    nsdm_enc = 0.125  # NSDM enclosure beyond diffusion

    dw = diode_width
    dl = diode_length

    # --- Diffusion rectangle ---
    _add_rect(c, LAYER.diffdrawing, 0.0, 0.0, dw, dl)

    # --- NSDM implant extends nsdm_enc beyond diffusion ---
    _add_rect(
        c,
        LAYER.nsdmdrawing,
        -nsdm_enc,
        -nsdm_enc,
        dw + 2 * nsdm_enc,
        dl + 2 * nsdm_enc,
    )

    # --- Licon contacts within diffusion ---
    licon_ref = c.add_ref(licon_array(width=dw, height=dl))
    licon_ref.move((0.0, 0.0))

    # --- Li1 pad covering diffusion + small enclosure ---
    li1_x = -li_enc
    li1_y = -li_enc
    li1_w = dw + 2 * li_enc
    li1_h = dl + 2 * li_enc
    _add_rect(c, LAYER.li1drawing, li1_x, li1_y, li1_w, li1_h)

    # --- CATHODE port on li1drawing at top edge of diffusion li1 pad ---
    c.add_port(
        name="CATHODE",
        center=(dw / 2, li1_y + li1_h),
        width=li1_w,
        orientation=90,
        layer=LAYER.li1drawing,
        port_type="electrical",
    )

    # --- Guard ring (pwell type — P+ substrate ring) ---
    if guard_ring:
        ring_spacing = 0.27
        ring_width = 0.34
        c.add_ref(
            pwell_guard_ring(
                inner_width=dw,
                inner_height=dl,
                ring_width=ring_width,
                spacing=ring_spacing,
            )
        )
        # Guard ring origin is at (0,0), matching the diode origin.
        # The VSS port from pwell_guard_ring is at the bottom of the ring.
        # We re-expose it as ANODE.
        ring_outer_bottom = -(ring_spacing + ring_width)
        ring_outer_left = -(ring_spacing + ring_width)
        ring_outer_width = dw + 2 * (ring_spacing + ring_width)

        c.add_port(
            name="ANODE",
            center=(dw / 2 + ring_outer_left + ring_outer_width / 2, ring_outer_bottom),
            width=ring_outer_width,
            orientation=270,
            layer=LAYER.li1drawing,
            port_type="electrical",
        )
    else:
        # Without guard ring, ANODE port at bottom of li1 pad
        c.add_port(
            name="ANODE",
            center=(dw / 2, li1_y),
            width=li1_w,
            orientation=270,
            layer=LAYER.li1drawing,
            port_type="electrical",
        )

    return c


@gf.cell
def sky130_fd_pr__diode_pd2nw_05v5(
    diode_width: float = 0.42,
    diode_length: float = 0.42,
    guard_ring: bool = True,
) -> gf.Component:
    """Return a P+/N-well diode (anode is P+ diffusion in N-well).

    Geometry: diffdrawing rectangle with PSDM implant inside nwelldrawing,
    licon contacts, and li1 pad.  An optional N-well guard ring surrounds
    the diode.

    Ports:
      ANODE   — on li1drawing at top of diffusion area.
      CATHODE — on li1drawing at the guard ring bottom (or bottom of cell when
                guard_ring=False).

    Args:
        diode_width: width of the diode diffusion in um.
        diode_length: length (height) of the diode diffusion in um.
        guard_ring: when True, add an nwell guard ring around the diode.

    .. plot::
      :include-source:

      import sky130

      c = sky130.pcells.sky130_fd_pr__diode_pd2nw_05v5()
      c.plot()
    """
    c = gf.Component()

    li_enc = 0.08  # li1 enclosure beyond licon/contact area
    psdm_enc = 0.125  # PSDM enclosure beyond diffusion
    nwell_enc = 0.18  # N-well enclosure beyond diffusion

    dw = diode_width
    dl = diode_length

    # --- N-well enclosing the diffusion ---
    _add_rect(
        c,
        LAYER.nwelldrawing,
        -nwell_enc,
        -nwell_enc,
        dw + 2 * nwell_enc,
        dl + 2 * nwell_enc,
    )

    # --- Diffusion rectangle ---
    _add_rect(c, LAYER.diffdrawing, 0.0, 0.0, dw, dl)

    # --- PSDM implant extends psdm_enc beyond diffusion ---
    _add_rect(
        c,
        LAYER.psdmdrawing,
        -psdm_enc,
        -psdm_enc,
        dw + 2 * psdm_enc,
        dl + 2 * psdm_enc,
    )

    # --- Licon contacts within diffusion ---
    licon_ref = c.add_ref(licon_array(width=dw, height=dl))
    licon_ref.move((0.0, 0.0))

    # --- Li1 pad covering diffusion + small enclosure ---
    li1_x = -li_enc
    li1_y = -li_enc
    li1_w = dw + 2 * li_enc
    li1_h = dl + 2 * li_enc
    _add_rect(c, LAYER.li1drawing, li1_x, li1_y, li1_w, li1_h)

    # --- ANODE port on li1drawing at top edge of diffusion li1 pad ---
    c.add_port(
        name="ANODE",
        center=(dw / 2, li1_y + li1_h),
        width=li1_w,
        orientation=90,
        layer=LAYER.li1drawing,
        port_type="electrical",
    )

    # --- Guard ring (nwell type — N+ tap ring in N-well) ---
    if guard_ring:
        ring_spacing = 0.27
        ring_width = 0.34
        c.add_ref(
            nwell_guard_ring(
                inner_width=dw,
                inner_height=dl,
                ring_width=ring_width,
                spacing=ring_spacing,
            )
        )
        # Guard ring origin is at (0,0), matching the diode origin.
        # The VDD port from nwell_guard_ring is at the bottom of the ring.
        # We re-expose it as CATHODE.
        ring_outer_bottom = -(ring_spacing + ring_width)
        ring_outer_left = -(ring_spacing + ring_width)
        ring_outer_width = dw + 2 * (ring_spacing + ring_width)

        c.add_port(
            name="CATHODE",
            center=(dw / 2 + ring_outer_left + ring_outer_width / 2, ring_outer_bottom),
            width=ring_outer_width,
            orientation=270,
            layer=LAYER.li1drawing,
            port_type="electrical",
        )
    else:
        # Without guard ring, CATHODE port at bottom of li1 pad
        c.add_port(
            name="CATHODE",
            center=(dw / 2, li1_y),
            width=li1_w,
            orientation=270,
            layer=LAYER.li1drawing,
            port_type="electrical",
        )

    return c


if __name__ == "__main__":
    c = sky130_fd_pr__diode_pw2nd_05v5()
    c.show()
