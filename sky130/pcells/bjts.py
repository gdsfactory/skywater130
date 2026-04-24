"""Bipolar Junction Transistor (BJT) pcells for sky130.

Provides NPN and PNP vertical BJT generators.
"""

import gdsfactory as gf

from sky130.layers import LAYER
from sky130.pcells.contact import licon_array


@gf.cell
def sky130_fd_pr__npn_05v5(
    emitter_width: float = 1.0,
    emitter_length: float = 1.0,
    base_ring_width: float = 0.4,
    np_spacing: float = 0.27,
    sdm_enclosure: float = 0.125,
    nwell_enclosure: float = 0.18,
    li_enclosure: float = 0.08,
) -> gf.Component:
    """Vertical NPN BJT for sky130 05V5 devices.

    Structure (inside-out):
      - Emitter: N+ diffusion (diffdrawing + nsdmdrawing) rectangle
      - Base: P-type annular tap ring (tapdrawing + psdmdrawing) around emitter
      - Collector: N-well (nwelldrawing) underneath the whole device
      - Licon contacts on emitter and base, Li1 pads

    Ports:
      EMITTER, BASE, COLLECTOR on li1drawing layer.

    Args:
        emitter_width: Width of the emitter diffusion rectangle in um.
        emitter_length: Length of the emitter diffusion rectangle in um.
        base_ring_width: Width of the P-type base ring in um.
        np_spacing: Spacing between emitter edge and inner edge of base ring in um.
        sdm_enclosure: Enclosure of SDM layers over diffusion in um.
        nwell_enclosure: Enclosure of nwell/collector beyond outer base ring in um.
        li_enclosure: Enclosure of li1 over licon contacts in um.

    .. plot::
      :include-source:

      import sky130

      c = sky130.pcells.sky130_fd_pr__npn_05v5()
      c.plot()
    """
    c = gf.Component()

    ew = emitter_width
    el = emitter_length
    brw = base_ring_width
    sp = np_spacing
    sdm_enc = sdm_enclosure
    nw_enc = nwell_enclosure
    li_enc = li_enclosure

    # ------------------------------------------------------------------ #
    # Emitter region: diff + nsdm
    # ------------------------------------------------------------------ #
    c.add_ref(gf.components.rectangle(size=(ew, el), layer=LAYER.diffdrawing))
    # N+ implant with enclosure
    c.add_ref(
        gf.components.rectangle(
            size=(ew + 2 * sdm_enc, el + 2 * sdm_enc),
            layer=LAYER.nsdmdrawing,
        )
    ).move((-sdm_enc, -sdm_enc))

    # Licon contacts on emitter
    c.add_ref(licon_array(width=ew, height=el))

    # Li1 pad over emitter
    e_li_w = ew
    e_li_h = el
    e_li = c.add_ref(
        gf.components.rectangle(size=(e_li_w, e_li_h), layer=LAYER.li1drawing)
    )
    # EMITTER port centred on li1 pad
    c.add_port(
        name="EMITTER",
        center=(e_li.xmin + e_li_w / 2, e_li.ymin + e_li_h / 2),
        width=min(e_li_w, e_li_h),
        orientation=90,
        layer=LAYER.li1drawing,
    )

    # ------------------------------------------------------------------ #
    # Base region: annular P-tap ring (tapdrawing + psdmdrawing)
    # The inner edge of the base ring is at distance sp from the emitter edge.
    # ------------------------------------------------------------------ #
    # Outer dimensions of the base ring:
    b_outer_w = ew + 2 * sp + 2 * brw
    b_outer_h = el + 2 * sp + 2 * brw

    # Corners of inner hole (cutout)
    b_inner_x0 = -(sp)
    b_inner_y0 = -(sp)
    b_inner_w = ew + 2 * sp
    b_inner_h = el + 2 * sp

    # The tap ring starts at offset -(sp + brw) from emitter origin
    b_origin_x = -(sp + brw)
    b_origin_y = -(sp + brw)

    # Build annular tap ring via boolean subtraction
    tap_outer = gf.components.rectangle(
        size=(b_outer_w, b_outer_h), layer=LAYER.tapdrawing
    )
    tap_inner = gf.components.rectangle(
        size=(b_inner_w, b_inner_h), layer=LAYER.tapdrawing
    )

    tap_outer_ref = gf.Component()
    tap_outer_ref.add_ref(tap_outer)
    tap_inner_placed = tap_outer_ref.add_ref(tap_inner)
    tap_inner_placed.move(
        (
            sp + brw - (sp + brw - b_inner_x0 + b_origin_x),
            sp + brw - (sp + brw - b_inner_y0 + b_origin_y),
        )
    )
    # Simpler: outer at (b_origin_x, b_origin_y), inner at (b_inner_x0, b_inner_y0)
    # Use gdsfactory boolean directly
    tap_outer_comp = gf.components.rectangle(
        size=(b_outer_w, b_outer_h), layer=LAYER.tapdrawing
    )
    tap_inner_comp = gf.components.rectangle(
        size=(b_inner_w, b_inner_h), layer=LAYER.tapdrawing
    )

    # Position them: outer at b_origin, inner at b_inner_x0/y0
    # Both are placed at origin=0 in their own frames.
    # We'll use add_ref with absolute offsets.
    base_ring_comp = gf.Component()
    outer_r = base_ring_comp.add_ref(tap_outer_comp)
    inner_r = base_ring_comp.add_ref(tap_inner_comp)
    # outer starts at (0,0) in base_ring_comp -> corresponds to b_origin in c
    # inner starts at (brw + sp - sp, brw + sp - sp) = (brw, brw) in base_ring_comp
    # Wait: inner edge at sp from emitter, outer at sp+brw from emitter, so inner is at offset brw within outer
    inner_r.move((brw, brw))

    base_ring = gf.boolean(
        A=outer_r, B=inner_r, operation="not", layer=LAYER.tapdrawing
    )
    base_ring_ref = c.add_ref(base_ring)
    base_ring_ref.move((b_origin_x, b_origin_y))

    # psdm ring (P+ implant for base contacts)
    psdm_outer_w = b_outer_w + 2 * sdm_enc
    psdm_outer_h = b_outer_h + 2 * sdm_enc
    psdm_inner_w = b_inner_w - 2 * sdm_enc
    psdm_inner_h = b_inner_h - 2 * sdm_enc

    psdm_outer_comp = gf.components.rectangle(
        size=(psdm_outer_w, psdm_outer_h), layer=LAYER.psdmdrawing
    )
    psdm_inner_comp = gf.components.rectangle(
        size=(psdm_inner_w, psdm_inner_h), layer=LAYER.psdmdrawing
    )

    psdm_ring_comp = gf.Component()
    po_r = psdm_ring_comp.add_ref(psdm_outer_comp)
    pi_r = psdm_ring_comp.add_ref(psdm_inner_comp)
    pi_r.move((brw + sdm_enc, brw + sdm_enc))

    psdm_ring = gf.boolean(A=po_r, B=pi_r, operation="not", layer=LAYER.psdmdrawing)
    psdm_ring_ref = c.add_ref(psdm_ring)
    psdm_ring_ref.move((b_origin_x - sdm_enc, b_origin_y - sdm_enc))

    # ------------------------------------------------------------------ #
    # Base contacts: licon arrays on left, right, top, bottom sides
    # ------------------------------------------------------------------ #
    # Side sizes: left/right sides are brw wide, inner_h tall
    # top/bottom sides are b_outer_w wide, brw tall
    # We use the ring corners (b_origin_x, b_origin_y) as reference

    # Left side licons
    left_licon = c.add_ref(licon_array(width=brw, height=b_inner_h))
    left_licon.move((b_origin_x, b_origin_y + brw))

    # Right side licons
    right_licon = c.add_ref(licon_array(width=brw, height=b_inner_h))
    right_licon.move((b_origin_x + brw + b_inner_w, b_origin_y + brw))

    # Bottom side licons
    bot_licon = c.add_ref(licon_array(width=b_outer_w, height=brw))
    bot_licon.move((b_origin_x, b_origin_y))

    # Top side licons
    top_licon = c.add_ref(licon_array(width=b_outer_w, height=brw))
    top_licon.move((b_origin_x, b_origin_y + brw + b_inner_h))

    # ------------------------------------------------------------------ #
    # Base Li1 ring (annular)
    # ------------------------------------------------------------------ #
    li_outer_w = b_outer_w + 2 * li_enc
    li_outer_h = b_outer_h + 2 * li_enc
    li_inner_w = b_inner_w - 2 * li_enc
    li_inner_h = b_inner_h - 2 * li_enc

    li_outer_c = gf.components.rectangle(
        size=(li_outer_w, li_outer_h), layer=LAYER.li1drawing
    )
    li_inner_c = gf.components.rectangle(
        size=(li_inner_w, li_inner_h), layer=LAYER.li1drawing
    )

    li_ring_parent = gf.Component()
    lo_r = li_ring_parent.add_ref(li_outer_c)
    li_r = li_ring_parent.add_ref(li_inner_c)
    li_r.move((brw + li_enc, brw + li_enc))

    li_base_ring = gf.boolean(A=lo_r, B=li_r, operation="not", layer=LAYER.li1drawing)
    li_base_ref = c.add_ref(li_base_ring)
    li_base_ref.move((b_origin_x - li_enc, b_origin_y - li_enc))

    # BASE port on left side of li1 ring
    c.add_port(
        name="BASE",
        center=(b_origin_x - li_enc + brw / 2, b_origin_y + brw + b_inner_h / 2),
        width=min(brw, b_inner_h),
        orientation=180,
        layer=LAYER.li1drawing,
    )

    # ------------------------------------------------------------------ #
    # Collector: N-well underneath entire device
    # ------------------------------------------------------------------ #
    nw_x0 = b_origin_x - nw_enc
    nw_y0 = b_origin_y - nw_enc
    nw_w = b_outer_w + 2 * nw_enc
    nw_h = b_outer_h + 2 * nw_enc

    c.add_ref(
        gf.components.rectangle(size=(nw_w, nw_h), layer=LAYER.nwelldrawing)
    ).move((nw_x0, nw_y0))

    # Collector tap: thin n+ tap ring at the outer nwell edge (collector contact)
    # Use a simple Li1 rectangle placed below the base ring for the collector port
    coll_li_w = nw_w
    coll_li_h = nw_enc * 0.8  # thin strip
    # Place below device
    coll_li = c.add_ref(
        gf.components.rectangle(
            size=(coll_li_w, max(coll_li_h, 0.17)), layer=LAYER.li1drawing
        )
    )
    coll_li.move((nw_x0, nw_y0))

    c.add_port(
        name="COLLECTOR",
        center=(nw_x0 + coll_li_w / 2, nw_y0 + max(coll_li_h, 0.17) / 2),
        width=coll_li_w,
        orientation=270,
        layer=LAYER.li1drawing,
    )

    # ------------------------------------------------------------------ #
    # NPN identifier layer
    # ------------------------------------------------------------------ #
    c.add_ref(
        gf.components.rectangle(
            size=(b_outer_w + 2 * nw_enc, b_outer_h + 2 * nw_enc),
            layer=LAYER.npndrawing,
        )
    ).move((nw_x0, nw_y0))

    return c


@gf.cell
def sky130_fd_pr__pnp_05v5(
    emitter_width: float = 0.68,
    emitter_length: float = 0.68,
    base_ring_width: float = 0.4,
    np_spacing: float = 0.27,
    sdm_enclosure: float = 0.125,
    nwell_enclosure: float = 0.18,
    li_enclosure: float = 0.08,
) -> gf.Component:
    """Vertical PNP BJT for sky130 05V5 devices.

    Structure (inside-out):
      - Emitter: P+ diffusion (diffdrawing + psdmdrawing) rectangle
      - Base: N-well (nwelldrawing) surrounding emitter, with N+ tap contacts
              (tapdrawing + nsdmdrawing ring) for base access
      - Collector: P-substrate (accessed via outer P+ guard ring, tapdrawing + psdmdrawing)
      - Licon contacts on emitter and base/collector rings, Li1 pads

    Ports:
      EMITTER, BASE, COLLECTOR on li1drawing layer.

    Args:
        emitter_width: Width of the emitter diffusion rectangle in um.
        emitter_length: Length of the emitter diffusion rectangle in um.
        base_ring_width: Width of the N+ base contact ring in um.
        np_spacing: Spacing between emitter edge and base ring in um.
        sdm_enclosure: Enclosure of SDM layers over diffusion in um.
        nwell_enclosure: Enclosure of nwell beyond the base contact ring in um.
        li_enclosure: Enclosure of li1 over licon contacts in um.

    .. plot::
      :include-source:

      import sky130

      c = sky130.pcells.sky130_fd_pr__pnp_05v5()
      c.plot()
    """
    c = gf.Component()

    ew = emitter_width
    el = emitter_length
    brw = base_ring_width
    sp = np_spacing
    sdm_enc = sdm_enclosure
    nw_enc = nwell_enclosure
    li_enc = li_enclosure

    # ------------------------------------------------------------------ #
    # Emitter: P+ diffusion (diffdrawing + psdmdrawing)
    # ------------------------------------------------------------------ #
    c.add_ref(gf.components.rectangle(size=(ew, el), layer=LAYER.diffdrawing))
    c.add_ref(
        gf.components.rectangle(
            size=(ew + 2 * sdm_enc, el + 2 * sdm_enc),
            layer=LAYER.psdmdrawing,
        )
    ).move((-sdm_enc, -sdm_enc))

    # Licon contacts on emitter
    c.add_ref(licon_array(width=ew, height=el))

    # Li1 pad over emitter
    c.add_ref(gf.components.rectangle(size=(ew, el), layer=LAYER.li1drawing))
    c.add_port(
        name="EMITTER",
        center=(ew / 2, el / 2),
        width=min(ew, el),
        orientation=90,
        layer=LAYER.li1drawing,
    )

    # ------------------------------------------------------------------ #
    # Base: N+ tap ring (tapdrawing + nsdmdrawing) — accesses N-well base
    # ------------------------------------------------------------------ #
    b_outer_w = ew + 2 * sp + 2 * brw
    b_outer_h = el + 2 * sp + 2 * brw
    b_inner_w = ew + 2 * sp
    b_inner_h = el + 2 * sp

    b_origin_x = -(sp + brw)
    b_origin_y = -(sp + brw)

    # Tap ring (N+)
    tap_o = gf.components.rectangle(size=(b_outer_w, b_outer_h), layer=LAYER.tapdrawing)
    tap_i = gf.components.rectangle(size=(b_inner_w, b_inner_h), layer=LAYER.tapdrawing)

    tap_parent = gf.Component()
    to_r = tap_parent.add_ref(tap_o)
    ti_r = tap_parent.add_ref(tap_i)
    ti_r.move((brw, brw))
    base_tap_ring = gf.boolean(A=to_r, B=ti_r, operation="not", layer=LAYER.tapdrawing)
    c.add_ref(base_tap_ring).move((b_origin_x, b_origin_y))

    # nsdm ring (N+ implant for base tap)
    nsdm_o = gf.components.rectangle(
        size=(b_outer_w + 2 * sdm_enc, b_outer_h + 2 * sdm_enc), layer=LAYER.nsdmdrawing
    )
    nsdm_i = gf.components.rectangle(
        size=(b_inner_w - 2 * sdm_enc, b_inner_h - 2 * sdm_enc), layer=LAYER.nsdmdrawing
    )
    nsdm_parent = gf.Component()
    no_r = nsdm_parent.add_ref(nsdm_o)
    ni_r = nsdm_parent.add_ref(nsdm_i)
    ni_r.move((brw + sdm_enc, brw + sdm_enc))
    base_nsdm_ring = gf.boolean(
        A=no_r, B=ni_r, operation="not", layer=LAYER.nsdmdrawing
    )
    c.add_ref(base_nsdm_ring).move((b_origin_x - sdm_enc, b_origin_y - sdm_enc))

    # Base licons (4 sides)
    c.add_ref(licon_array(width=brw, height=b_inner_h)).move(
        (b_origin_x, b_origin_y + brw)
    )
    c.add_ref(licon_array(width=brw, height=b_inner_h)).move(
        (b_origin_x + brw + b_inner_w, b_origin_y + brw)
    )
    c.add_ref(licon_array(width=b_outer_w, height=brw)).move((b_origin_x, b_origin_y))
    c.add_ref(licon_array(width=b_outer_w, height=brw)).move(
        (b_origin_x, b_origin_y + brw + b_inner_h)
    )

    # Base Li1 ring
    li_o = gf.components.rectangle(
        size=(b_outer_w + 2 * li_enc, b_outer_h + 2 * li_enc), layer=LAYER.li1drawing
    )
    li_i = gf.components.rectangle(
        size=(b_inner_w - 2 * li_enc, b_inner_h - 2 * li_enc), layer=LAYER.li1drawing
    )
    li_parent = gf.Component()
    lop = li_parent.add_ref(li_o)
    lip = li_parent.add_ref(li_i)
    lip.move((brw + li_enc, brw + li_enc))
    base_li_ring = gf.boolean(A=lop, B=lip, operation="not", layer=LAYER.li1drawing)
    c.add_ref(base_li_ring).move((b_origin_x - li_enc, b_origin_y - li_enc))

    # BASE port
    c.add_port(
        name="BASE",
        center=(b_origin_x - li_enc + brw / 2, b_origin_y + brw + b_inner_h / 2),
        width=min(brw, b_inner_h),
        orientation=180,
        layer=LAYER.li1drawing,
    )

    # ------------------------------------------------------------------ #
    # N-well (base region body)
    # ------------------------------------------------------------------ #
    nw_x0 = b_origin_x - nw_enc
    nw_y0 = b_origin_y - nw_enc
    nw_w = b_outer_w + 2 * nw_enc
    nw_h = b_outer_h + 2 * nw_enc

    c.add_ref(
        gf.components.rectangle(size=(nw_w, nw_h), layer=LAYER.nwelldrawing)
    ).move((nw_x0, nw_y0))

    # ------------------------------------------------------------------ #
    # Collector: outer P+ guard ring (pwell contact = P-substrate)
    # The collector ring surrounds the nwell.
    # ------------------------------------------------------------------ #
    c_sp = np_spacing  # spacing between nwell edge and collector ring inner edge
    c_rw = base_ring_width  # collector ring width

    c_outer_w = nw_w + 2 * c_sp + 2 * c_rw
    c_outer_h = nw_h + 2 * c_sp + 2 * c_rw
    c_inner_w = nw_w + 2 * c_sp
    c_inner_h = nw_h + 2 * c_sp

    c_origin_x = nw_x0 - c_sp - c_rw
    c_origin_y = nw_y0 - c_sp - c_rw

    # Tap (P-well tap for collector)
    ctap_o = gf.components.rectangle(
        size=(c_outer_w, c_outer_h), layer=LAYER.tapdrawing
    )
    ctap_i = gf.components.rectangle(
        size=(c_inner_w, c_inner_h), layer=LAYER.tapdrawing
    )
    ctap_parent = gf.Component()
    cto_r = ctap_parent.add_ref(ctap_o)
    cti_r = ctap_parent.add_ref(ctap_i)
    cti_r.move((c_rw, c_rw))
    coll_tap_ring = gf.boolean(
        A=cto_r, B=cti_r, operation="not", layer=LAYER.tapdrawing
    )
    c.add_ref(coll_tap_ring).move((c_origin_x, c_origin_y))

    # psdm ring for collector
    cpsdm_o = gf.components.rectangle(
        size=(c_outer_w + 2 * sdm_enc, c_outer_h + 2 * sdm_enc), layer=LAYER.psdmdrawing
    )
    cpsdm_i = gf.components.rectangle(
        size=(c_inner_w - 2 * sdm_enc, c_inner_h - 2 * sdm_enc), layer=LAYER.psdmdrawing
    )
    cpsdm_parent = gf.Component()
    cpso_r = cpsdm_parent.add_ref(cpsdm_o)
    cpsi_r = cpsdm_parent.add_ref(cpsdm_i)
    cpsi_r.move((c_rw + sdm_enc, c_rw + sdm_enc))
    coll_psdm_ring = gf.boolean(
        A=cpso_r, B=cpsi_r, operation="not", layer=LAYER.psdmdrawing
    )
    c.add_ref(coll_psdm_ring).move((c_origin_x - sdm_enc, c_origin_y - sdm_enc))

    # Collector licons
    c.add_ref(licon_array(width=c_rw, height=c_inner_h)).move(
        (c_origin_x, c_origin_y + c_rw)
    )
    c.add_ref(licon_array(width=c_rw, height=c_inner_h)).move(
        (c_origin_x + c_rw + c_inner_w, c_origin_y + c_rw)
    )
    c.add_ref(licon_array(width=c_outer_w, height=c_rw)).move((c_origin_x, c_origin_y))
    c.add_ref(licon_array(width=c_outer_w, height=c_rw)).move(
        (c_origin_x, c_origin_y + c_rw + c_inner_h)
    )

    # Collector Li1 ring
    cli_o = gf.components.rectangle(
        size=(c_outer_w + 2 * li_enc, c_outer_h + 2 * li_enc), layer=LAYER.li1drawing
    )
    cli_i = gf.components.rectangle(
        size=(c_inner_w - 2 * li_enc, c_inner_h - 2 * li_enc), layer=LAYER.li1drawing
    )
    cli_parent = gf.Component()
    clop = cli_parent.add_ref(cli_o)
    clip = cli_parent.add_ref(cli_i)
    clip.move((c_rw + li_enc, c_rw + li_enc))
    coll_li_ring = gf.boolean(A=clop, B=clip, operation="not", layer=LAYER.li1drawing)
    c.add_ref(coll_li_ring).move((c_origin_x - li_enc, c_origin_y - li_enc))

    # COLLECTOR port
    c.add_port(
        name="COLLECTOR",
        center=(c_origin_x - li_enc + c_rw / 2, c_origin_y + c_rw + c_inner_h / 2),
        width=min(c_rw, c_inner_h),
        orientation=180,
        layer=LAYER.li1drawing,
    )

    # PNP identifier layer
    c.add_ref(
        gf.components.rectangle(
            size=(c_outer_w + 2 * nw_enc, c_outer_h + 2 * nw_enc),
            layer=LAYER.pnpdrawing,
        )
    ).move((c_origin_x - nw_enc, c_origin_y - nw_enc))

    return c


if __name__ == "__main__":
    c = sky130_fd_pr__npn_05v5()
    c.show()
