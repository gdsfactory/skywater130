"""Resistor pcell generators for sky130.

Provides poly and diffusion resistor parametric cells matching the sky130
process device geometries, including poly body, contact heads, implant layers,
and NPC (nitride poly cut) for poly resistors.
"""

import gdsfactory as gf

from sky130.layers import LAYER
from sky130.pcells.contact import licon_array


def _add_rect(c: gf.Component, layer, x: float, y: float, w: float, h: float):
    """Add a rectangle to a component using polygon coordinates."""
    c.add_polygon(
        [(x, y), (x + w, y), (x + w, y + h), (x, y + h)],
        layer=layer,
    )


@gf.cell
def sky130_fd_pr__res_generic_po(
    res_width: float = 0.33,
    res_length: float = 2.0,
    nf: int = 1,
) -> gf.Component:
    """Return a standard poly resistor (~48 ohm/sq).

    Geometry: poly body rectangle with licon contacts on li1 pads at each end,
    RPM layer over body, NPC over contact regions, PSDM over body.

    Args:
        res_width: width of the resistor body in um.
        res_length: length of the resistor body in um.
        nf: number of fingers (for future multi-finger support).

    .. plot::
      :include-source:

      import sky130

      c = sky130.pcells.sky130_fd_pr__res_generic_po()
      c.plot()
    """
    c = gf.Component()

    # Contact region dimensions (head/tail)
    li_enc = 0.08          # li1 enclosure beyond licon
    licon_enc = 0.06       # licon enclosure within poly
    contact_size = 0.17
    contact_h = contact_size + 2 * licon_enc  # minimum contact area height
    head_h = max(contact_h, 0.29)             # li1 pad height

    # Total poly height: body + two contact heads
    poly_total_h = res_length + 2 * head_h

    # X positions (centered)
    poly_x = 0.0
    poly_y = -head_h

    # --- Poly body (full extent including head/tail regions) ---
    _add_rect(c, LAYER.polydrawing, poly_x, poly_y, res_width, poly_total_h)

    # --- RPM (resistor poly mask) over body only ---
    rpm_enc_x = 0.2
    rpm_enc_y = 0.2
    rpm_x = poly_x - rpm_enc_x
    rpm_y = 0.0 - rpm_enc_y
    rpm_w = res_width + 2 * rpm_enc_x
    rpm_h = res_length + 2 * rpm_enc_y
    _add_rect(c, LAYER.rpmdrawing, rpm_x, rpm_y, rpm_w, rpm_h)

    # --- NPC (nitride poly cut) over poly contact regions ---
    npc_enc = 0.095
    # Bottom contact region
    _add_rect(
        c,
        LAYER.npcdrawing,
        poly_x - npc_enc,
        poly_y - npc_enc,
        res_width + 2 * npc_enc,
        head_h + npc_enc * 2,
    )
    # Top contact region
    _add_rect(
        c,
        LAYER.npcdrawing,
        poly_x - npc_enc,
        res_length - npc_enc,
        res_width + 2 * npc_enc,
        head_h + npc_enc * 2,
    )

    # --- PSDM implant over the entire poly region ---
    psdm_enc = 0.125
    _add_rect(
        c,
        LAYER.psdmdrawing,
        rpm_x - psdm_enc,
        rpm_y - psdm_enc,
        rpm_w + 2 * psdm_enc,
        rpm_h + 2 * psdm_enc,
    )

    # --- Licon contacts in head/tail regions ---
    # Bottom head
    bot_licon = c.add_ref(licon_array(width=res_width, height=head_h))
    bot_licon.move((poly_x, poly_y))

    # Top head
    top_licon = c.add_ref(licon_array(width=res_width, height=head_h))
    top_licon.move((poly_x, res_length))

    # --- Li1 pads over contact regions ---
    li1_w = res_width + 2 * li_enc
    li1_h = head_h + 2 * li_enc

    # Bottom li1 pad
    _add_rect(
        c,
        LAYER.li1drawing,
        poly_x - li_enc,
        poly_y - li_enc,
        li1_w,
        li1_h,
    )
    # Top li1 pad
    _add_rect(
        c,
        LAYER.li1drawing,
        poly_x - li_enc,
        res_length - li_enc,
        li1_w,
        li1_h,
    )

    # --- Ports ---
    c.add_port(
        name="PLUS",
        center=(poly_x + res_width / 2, poly_y - li_enc),
        width=res_width,
        orientation=270,
        layer=LAYER.li1drawing,
    )
    c.add_port(
        name="MINUS",
        center=(poly_x + res_width / 2, res_length + head_h + li_enc),
        width=res_width,
        orientation=90,
        layer=LAYER.li1drawing,
    )
    c.add_port(
        name="BODY",
        center=(poly_x + res_width / 2, res_length / 2),
        width=res_length,
        orientation=0,
        layer=LAYER.psdmdrawing,
    )

    return c


@gf.cell
def sky130_fd_pr__res_high_po(
    res_width: float = 0.35,
    res_length: float = 2.0,
    nf: int = 1,
) -> gf.Component:
    """Return a high-resistance poly resistor (~320-2000 ohm/sq).

    Same structure as res_generic_po but with an additional URPM
    (ultra-high-resistance poly mask) layer over the resistor body.

    Args:
        res_width: width of the resistor body in um.
        res_length: length of the resistor body in um.
        nf: number of fingers (for future multi-finger support).

    .. plot::
      :include-source:

      import sky130

      c = sky130.pcells.sky130_fd_pr__res_high_po()
      c.plot()
    """
    c = gf.Component()

    # Contact region dimensions (head/tail)
    li_enc = 0.08
    licon_enc = 0.06
    contact_size = 0.17
    contact_h = contact_size + 2 * licon_enc
    head_h = max(contact_h, 0.29)

    poly_total_h = res_length + 2 * head_h
    poly_x = 0.0
    poly_y = -head_h

    # --- Poly body ---
    _add_rect(c, LAYER.polydrawing, poly_x, poly_y, res_width, poly_total_h)

    # --- RPM over body ---
    rpm_enc_x = 0.2
    rpm_enc_y = 0.2
    rpm_x = poly_x - rpm_enc_x
    rpm_y = 0.0 - rpm_enc_y
    rpm_w = res_width + 2 * rpm_enc_x
    rpm_h = res_length + 2 * rpm_enc_y
    _add_rect(c, LAYER.rpmdrawing, rpm_x, rpm_y, rpm_w, rpm_h)

    # --- URPM over body (additional high-R mask) ---
    urpm_min_w = 1.27
    urpm_enc_x = 0.2
    urpm_enc_y = 0.2
    urpm_w = max(res_width + 2 * urpm_enc_x, urpm_min_w + 2 * urpm_enc_x)
    urpm_h = res_length + 2 * urpm_enc_y
    urpm_x = poly_x + res_width / 2 - urpm_w / 2
    urpm_y = 0.0 - urpm_enc_y
    _add_rect(c, LAYER.urpm, urpm_x, urpm_y, urpm_w, urpm_h)

    # --- NPC over contact regions ---
    npc_enc = 0.095
    _add_rect(
        c,
        LAYER.npcdrawing,
        poly_x - npc_enc,
        poly_y - npc_enc,
        res_width + 2 * npc_enc,
        head_h + npc_enc * 2,
    )
    _add_rect(
        c,
        LAYER.npcdrawing,
        poly_x - npc_enc,
        res_length - npc_enc,
        res_width + 2 * npc_enc,
        head_h + npc_enc * 2,
    )

    # --- PSDM implant ---
    psdm_enc = 0.125
    _add_rect(
        c,
        LAYER.psdmdrawing,
        rpm_x - psdm_enc,
        rpm_y - psdm_enc,
        rpm_w + 2 * psdm_enc,
        rpm_h + 2 * psdm_enc,
    )

    # --- Licon contacts ---
    bot_licon = c.add_ref(licon_array(width=res_width, height=head_h))
    bot_licon.move((poly_x, poly_y))

    top_licon = c.add_ref(licon_array(width=res_width, height=head_h))
    top_licon.move((poly_x, res_length))

    # --- Li1 pads ---
    li1_w = res_width + 2 * li_enc
    li1_h = head_h + 2 * li_enc

    _add_rect(c, LAYER.li1drawing, poly_x - li_enc, poly_y - li_enc, li1_w, li1_h)
    _add_rect(c, LAYER.li1drawing, poly_x - li_enc, res_length - li_enc, li1_w, li1_h)

    # --- Ports ---
    c.add_port(
        name="PLUS",
        center=(poly_x + res_width / 2, poly_y - li_enc),
        width=res_width,
        orientation=270,
        layer=LAYER.li1drawing,
    )
    c.add_port(
        name="MINUS",
        center=(poly_x + res_width / 2, res_length + head_h + li_enc),
        width=res_width,
        orientation=90,
        layer=LAYER.li1drawing,
    )
    c.add_port(
        name="BODY",
        center=(poly_x + res_width / 2, res_length / 2),
        width=res_length,
        orientation=0,
        layer=LAYER.psdmdrawing,
    )

    return c


@gf.cell
def sky130_fd_pr__res_generic_nd(
    res_width: float = 0.42,
    res_length: float = 2.0,
) -> gf.Component:
    """Return an N+ diffusion resistor.

    Geometry: diffusion rectangle with NSDM implant and licon contacts at
    each end.  No poly involved.

    Args:
        res_width: width of the resistor body in um.
        res_length: length of the resistor body in um.

    .. plot::
      :include-source:

      import sky130

      c = sky130.pcells.sky130_fd_pr__res_generic_nd()
      c.plot()
    """
    c = gf.Component()

    # Contact region dimensions
    li_enc = 0.08
    licon_enc = 0.06
    contact_size = 0.17
    contact_h = contact_size + 2 * licon_enc
    head_h = max(contact_h, 0.29)

    diff_x = 0.0
    diff_y = -head_h
    diff_total_h = res_length + 2 * head_h

    # --- Diffusion rectangle (body + head/tail) ---
    _add_rect(c, LAYER.diffdrawing, diff_x, diff_y, res_width, diff_total_h)

    # --- NSDM implant over full diffusion area ---
    nsdm_enc = 0.125
    _add_rect(
        c,
        LAYER.nsdmdrawing,
        diff_x - nsdm_enc,
        diff_y - nsdm_enc,
        res_width + 2 * nsdm_enc,
        diff_total_h + 2 * nsdm_enc,
    )

    # --- Licon contacts in head/tail regions ---
    bot_licon = c.add_ref(licon_array(width=res_width, height=head_h))
    bot_licon.move((diff_x, diff_y))

    top_licon = c.add_ref(licon_array(width=res_width, height=head_h))
    top_licon.move((diff_x, res_length))

    # --- Li1 pads ---
    li1_w = res_width + 2 * li_enc
    li1_h = head_h + 2 * li_enc

    _add_rect(c, LAYER.li1drawing, diff_x - li_enc, diff_y - li_enc, li1_w, li1_h)
    _add_rect(c, LAYER.li1drawing, diff_x - li_enc, res_length - li_enc, li1_w, li1_h)

    # --- Ports ---
    c.add_port(
        name="PLUS",
        center=(diff_x + res_width / 2, diff_y - li_enc),
        width=res_width,
        orientation=270,
        layer=LAYER.li1drawing,
    )
    c.add_port(
        name="MINUS",
        center=(diff_x + res_width / 2, res_length + head_h + li_enc),
        width=res_width,
        orientation=90,
        layer=LAYER.li1drawing,
    )
    c.add_port(
        name="BODY",
        center=(diff_x + res_width / 2, res_length / 2),
        width=res_length,
        orientation=0,
        layer=LAYER.nsdmdrawing,
    )

    return c


if __name__ == "__main__":
    c = sky130_fd_pr__res_generic_po()
    c.show()
