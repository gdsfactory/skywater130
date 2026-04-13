"""Magic-parity MOSFET generators for sky130.

Provides nfet_01v8 and pfet_01v8 parametric cells that match the geometry
produced by Magic's sky130 device generators, including multi-finger support,
S/D sharing, guard rings, and deep N-well options.

All geometry is centered at the origin to match Magic's output coordinate system.
"""

import gdsfactory as gf

from sky130.layers import LAYER
from sky130.pcells.guard_ring import nwell_guard_ring, pwell_guard_ring


def _snap(val: float, grid: float = 0.005) -> float:
    """Snap a value to the nearest grid point (default 5nm)."""
    return round(val / grid) * grid


def _rect(c: gf.Component, layer, x0: float, y0: float, x1: float, y1: float):
    """Add a rectangle defined by two corners (x0,y0) to (x1,y1)."""
    x0, y0, x1, y1 = _snap(x0), _snap(y0), _snap(x1), _snap(y1)
    c.add_polygon(
        [(x0, y0), (x1, y0), (x1, y1), (x0, y1)],
        layer=layer,
    )


def _mosfet_core(
    c: gf.Component,
    gate_width: float,
    gate_length: float,
    nf: int,
    is_pmos: bool,
    suppress_nwell: bool = False,
) -> dict:
    """Build the core MOSFET geometry matching Magic's mos_device output.

    All geometry is centered at origin (0, 0).

    Returns a dict of key coordinates for port placement and enclosure calculations.
    """
    # ---- Magic design-rule constants ----
    contact_size = 0.17
    diff_surround = 0.06       # Diffusion enclosure of licon contact
    poly_surround = 0.08       # Poly enclosure of licon contact (on poly)
    gate_to_diffcont = 0.145   # Gate edge to diff contact center (edge contacts)
    gate_to_polycont_n = 0.275  # Gate edge to poly contact center (NFET)
    gate_to_polycont_p = 0.32   # Gate edge to poly contact center (PFET)
    diff_extension = 0.29      # Diffusion extension beyond gate (nf=1 edge)
    end_cap = 0.13             # Poly extension beyond diffusion (non-contact side)
    implant_enc = 0.125        # Implant enclosure beyond diffusion
    nwell_enc_x = 0.18         # Nwell enclosure of diff in x (PFET)
    npc_ext = 0.02             # NPC extension beyond poly pad
    met1_surround = 0.03       # Met1 surround of mcon contact
    li1_ext_y = 0.02           # Li1 extension beyond diffusion edge for S/D

    gate_to_polycont = gate_to_polycont_p if is_pmos else gate_to_polycont_n

    # ---- Derived dimensions ----
    W = gate_width
    L = gate_length
    hw = W / 2.0    # half-width (y direction)
    hl = L / 2.0    # half-length (x direction)

    # Poly contact pad dimensions
    pc_pad_size = contact_size + 2 * poly_surround  # 0.33

    # Gate extension on the contact side: poly extends just to the pad base
    gate_ext_contact = gate_to_polycont - (contact_size / 2 + poly_surround)
    # Gate extension on non-contact side (standard end_cap)
    gate_ext_nocont = end_cap

    # ---- Finger pitch and contact positions ----
    # For shared contacts between gates (nf > 1), the gate-to-contact spacing
    # depends on L:  when L < pc_pad_size (gate narrower than contact pad),
    # the poly_surround constraint (0.08) applies.  When L >= pc_pad_size,
    # the standard gate_to_diffcont (0.145) is used.
    if L < pc_pad_size:
        shared_gate_to_diffcont = max(gate_to_diffcont,
                                      contact_size / 2 + poly_surround)
    else:
        shared_gate_to_diffcont = gate_to_diffcont

    if nf == 1:
        # Single finger: contacts on both sides at gate_to_diffcont from gate edge
        finger_pitch = 0.0  # not applicable
        # S/D contact centers
        sd_centers_x = [-(hl + gate_to_diffcont), hl + gate_to_diffcont]
        gate_centers_x = [0.0]
        # Diffusion half-width in x
        diff_half_x = hl + diff_extension
    else:
        # Multi-finger: regular grid with shared contacts
        finger_pitch = L + 2 * shared_gate_to_diffcont
        # Gate centers: symmetric about origin
        gate_centers_x = [
            _snap(-((nf - 1) / 2.0) * finger_pitch + i * finger_pitch)
            for i in range(nf)
        ]
        # S/D contact centers: nf+1 contacts
        sd_centers_x = [
            _snap(-(nf / 2.0) * finger_pitch + i * finger_pitch)
            for i in range(nf + 1)
        ]
        # Diffusion extends diff_surround + contact_size/2 beyond outermost contact
        diff_half_x = abs(sd_centers_x[-1]) + contact_size / 2 + diff_surround

    # ---- 1. Diffusion rectangle ----
    _rect(c, LAYER.diffdrawing, -diff_half_x, -hw, diff_half_x, hw)

    # ---- 2. Poly gates and contact pads ----
    # For nf=1: both top and bottom get contacts
    # For nf>1: gates alternate — even-indexed on bottom, odd-indexed on top
    #           (gate 0 has contact bottom, gate 1 has contact top, etc.)

    # Determine which side each gate gets a poly contact
    # "top" means positive y, "bottom" means negative y
    for gi, gx in enumerate(gate_centers_x):
        if nf == 1:
            # Both sides get contacts
            contact_sides = ["top", "bottom"]
        else:
            # Alternate: even gates get bottom contact, odd gates get top
            if gi % 2 == 0:
                contact_sides = ["bottom"]
            else:
                contact_sides = ["top"]

        # Poly gate rectangle
        if L >= pc_pad_size:
            # Gate is wide enough to serve as its own contact pad.
            # Poly extends symmetrically to full pad range on BOTH sides,
            # regardless of which side has the contact.
            poly_ext = hw + gate_to_polycont + contact_size / 2 + poly_surround
            _rect(c, LAYER.polydrawing, gx - hl, -poly_ext, gx + hl, poly_ext)
        else:
            # Gate is narrower than contact pad — need separate pad rectangles
            if nf == 1:
                # Gate rect connects top and bottom pads
                poly_top_gate = hw + gate_ext_contact
                poly_bot_gate = -(hw + gate_ext_contact)
                _rect(c, LAYER.polydrawing, gx - hl, poly_bot_gate, gx + hl, poly_top_gate)

                # Top poly contact pad
                pad_half = pc_pad_size / 2.0
                pad_cy_top = hw + gate_to_polycont
                _rect(c, LAYER.polydrawing,
                      gx - pad_half, pad_cy_top - pad_half,
                      gx + pad_half, pad_cy_top + pad_half)
                # Bottom poly contact pad
                pad_cy_bot = -(hw + gate_to_polycont)
                _rect(c, LAYER.polydrawing,
                      gx - pad_half, pad_cy_bot - pad_half,
                      gx + pad_half, pad_cy_bot + pad_half)
            else:
                # Multi-finger with narrow gate
                pad_half = pc_pad_size / 2.0
                if "top" in contact_sides:
                    # Gate extends up to pad base, down to end_cap
                    poly_top_gate = hw + gate_ext_contact
                    poly_bot_gate = -(hw + gate_ext_nocont)
                    _rect(c, LAYER.polydrawing, gx - hl, poly_bot_gate, gx + hl, poly_top_gate)
                    # Top contact pad
                    pad_cy = hw + gate_to_polycont
                    _rect(c, LAYER.polydrawing,
                          gx - pad_half, pad_cy - pad_half,
                          gx + pad_half, pad_cy + pad_half)
                else:
                    # Gate extends down to pad base, up to end_cap
                    poly_top_gate = hw + gate_ext_nocont
                    poly_bot_gate = -(hw + gate_ext_contact)
                    _rect(c, LAYER.polydrawing, gx - hl, poly_bot_gate, gx + hl, poly_top_gate)
                    # Bottom contact pad
                    pad_cy = -(hw + gate_to_polycont)
                    _rect(c, LAYER.polydrawing,
                          gx - pad_half, pad_cy - pad_half,
                          gx + pad_half, pad_cy + pad_half)

        # ---- Licon contacts on poly pads ----
        # For wide gates (L > contact pad size), use a horizontal contact array
        cpl = gate_length - 2 * poly_surround  # poly contact width (coverage area)
        if cpl < contact_size:
            cpl = contact_size  # minimum one contact

        for side in contact_sides:
            if side == "top":
                pad_cy = hw + gate_to_polycont
            else:
                pad_cy = -(hw + gate_to_polycont)

            licon_half = contact_size / 2.0

            # Determine contact array dimensions for poly contacts
            # For narrow gates: single contact at gate center
            # For wide gates: array of contacts spanning gate width
            num_poly_contacts_x = 1
            if cpl > contact_size:
                from math import floor
                num_poly_contacts_x = 1 + floor(
                    (cpl - contact_size) / (contact_size + contact_size)
                )
            num_poly_contacts_x = max(1, num_poly_contacts_x)

            # Place contact array horizontally
            if num_poly_contacts_x == 1:
                _rect(c, LAYER.licon1drawing,
                      gx - licon_half, pad_cy - licon_half,
                      gx + licon_half, pad_cy + licon_half)
                _rect(c, LAYER.mcondrawing,
                      gx - licon_half, pad_cy - licon_half,
                      gx + licon_half, pad_cy + licon_half)
            else:
                pitch = contact_size + contact_size  # 0.34 for licon
                array_w = (num_poly_contacts_x - 1) * pitch + contact_size
                start_x = gx - array_w / 2.0
                for ci in range(num_poly_contacts_x):
                    cx = start_x + ci * pitch
                    _rect(c, LAYER.licon1drawing,
                          cx, pad_cy - licon_half,
                          cx + contact_size, pad_cy + licon_half)
                    _rect(c, LAYER.mcondrawing,
                          cx, pad_cy - licon_half,
                          cx + contact_size, pad_cy + licon_half)

            # Li1 over poly contact: covers the larger of pad area or gate width
            li_half_x = max(pc_pad_size / 2.0, hl)
            _rect(c, LAYER.li1drawing,
                  gx - li_half_x, pad_cy - licon_half,
                  gx + li_half_x, pad_cy + licon_half)
            # Met1 over poly contact
            pad_half_x = max(pc_pad_size / 2.0, hl)
            m1_half_x = pad_half_x - npc_ext
            m1_half_y = licon_half + met1_surround
            _rect(c, LAYER.met1drawing,
                  gx - m1_half_x, pad_cy - m1_half_y,
                  gx + m1_half_x, pad_cy + m1_half_y)

            # NPC over poly contact region (stays at pad size, not gate width)
            npc_half_x = pc_pad_size / 2.0 + npc_ext
            npc_half_y = pc_pad_size / 2.0 + npc_ext
            _rect(c, LAYER.npcdrawing,
                  gx - npc_half_x, pad_cy - npc_half_y,
                  gx + npc_half_x, pad_cy + npc_half_y)

    # ---- 3. S/D contacts (licon, li1, mcon, met1) ----
    # Licon: size=0.17, spacing=0.17, enclosure=0.06
    licon_spacing = 0.17
    licon_pitch = contact_size + licon_spacing  # 0.34
    # Mcon: size=0.17, spacing=0.19, enclosure=(0.03x, 0.06y)
    mcon_spacing = 0.19
    mcon_pitch = contact_size + mcon_spacing  # 0.36
    mcon_enc_y = 0.06

    for si, sx in enumerate(sd_centers_x):
        ch = contact_size / 2.0

        # -- Licon contacts --
        avail_h_licon = W - 2 * diff_surround
        n_licon = max(1, int((avail_h_licon - contact_size) / licon_pitch) + 1)
        arr_h_licon = (n_licon - 1) * licon_pitch + contact_size
        for ci in range(n_licon):
            cy = -arr_h_licon / 2.0 + ci * licon_pitch + ch
            _rect(c, LAYER.licon1drawing,
                  sx - ch, cy - ch, sx + ch, cy + ch)

        # -- Mcon contacts (different pitch and enclosure) --
        avail_h_mcon = W - 2 * mcon_enc_y
        n_mcon = max(1, int((avail_h_mcon - contact_size) / mcon_pitch) + 1)
        arr_h_mcon = (n_mcon - 1) * mcon_pitch + contact_size
        for ci in range(n_mcon):
            cy = -arr_h_mcon / 2.0 + ci * mcon_pitch + ch
            _rect(c, LAYER.mcondrawing,
                  sx - ch, cy - ch, sx + ch, cy + ch)

        # Li1 strip over S/D: same x range as contact, y extends to ±(hw + li1_ext_y)
        li1_y_ext = hw + li1_ext_y
        _rect(c, LAYER.li1drawing,
              sx - ch, -li1_y_ext,
              sx + ch, li1_y_ext)

        # Met1 pad over S/D
        m1_half_x = ch + met1_surround
        m1_half_y = hw  # met1 extends to diff edge
        _rect(c, LAYER.met1drawing,
              sx - m1_half_x, -m1_half_y,
              sx + m1_half_x, m1_half_y)

    # ---- 4. Implant layer (NSDM or PSDM) ----
    impl_layer = LAYER.psdmdrawing if is_pmos else LAYER.nsdmdrawing
    _rect(c, impl_layer,
          -(diff_half_x + implant_enc), -(hw + implant_enc),
          diff_half_x + implant_enc, hw + implant_enc)

    # ---- 5. N-well (PFET only, skipped when guard ring will provide it) ----
    if is_pmos and not suppress_nwell:
        # Nwell extends 0.18 beyond diff in x, and encompasses poly contact region in y
        nwell_x = diff_half_x + nwell_enc_x
        # In y: extends to poly contact region top/bottom + npc_ext + some clearance
        polycont_pad_top = hw + gate_to_polycont + contact_size / 2 + poly_surround
        nwell_y = polycont_pad_top + 0.015  # empirical from reference: pad_top + 0.015
        _rect(c, LAYER.nwelldrawing, -nwell_x, -nwell_y, nwell_x, nwell_y)

    # ---- 6. Labels ----
    # For nf=1: D (drain) on left/negative-x, S (source) on right/positive-x
    # For nf>1: D0, S1, D2, S3, ... alternating, with G labels at poly contact centers
    if nf == 1:
        # Drain on left (negative x), Source on right (positive x)
        c.add_label(
            text="D",
            position=(sd_centers_x[0], 0.0),
            layer=LAYER.li1label,
        )
        c.add_label(
            text="S",
            position=(sd_centers_x[1], 0.0),
            layer=LAYER.li1label,
        )
        # Gate label at poly contact center (top)
        c.add_label(
            text="G",
            position=(0.0, hw + gate_to_polycont),
            layer=LAYER.li1label,
        )
    else:
        # For nf>1: each gate i gets a label Gi.
        # Each gate's LEFT S/D contact gets Di (even i) or Si (odd i).
        # For odd nf: the last gate's RIGHT S/D also gets S(nf-1).
        # For even nf: the last S/D is unlabeled (same drain net as D0).
        for gi in range(nf):
            sx = sd_centers_x[gi]
            if gi % 2 == 0:
                c.add_label(text=f"D{gi}", position=(sx, 0.0),
                            layer=LAYER.li1label)
            else:
                c.add_label(text=f"S{gi}", position=(sx, 0.0),
                            layer=LAYER.li1label)
        # Last S/D contact: labeled only for odd nf
        if nf % 2 == 1:
            sx = sd_centers_x[nf]
            c.add_label(text=f"S{nf - 1}", position=(sx, 0.0),
                        layer=LAYER.li1label)

        for gi, gx in enumerate(gate_centers_x):
            if gi % 2 == 0:
                gate_label_y = -(hw + gate_to_polycont)
            else:
                gate_label_y = hw + gate_to_polycont
            c.add_label(
                text=f"G{gi}",
                position=(gx, gate_label_y),
                layer=LAYER.li1label,
            )

    # ---- Return coordinate info ----
    return {
        "diff_half_x": diff_half_x,
        "hw": hw,
        "gate_to_polycont": gate_to_polycont,
        "pc_pad_size": pc_pad_size,
        "sd_centers_x": sd_centers_x,
        "gate_centers_x": gate_centers_x,
        "finger_pitch": finger_pitch,
        "implant_enc": implant_enc,
        "nwell_enc_x": nwell_enc_x,
        "npc_ext": npc_ext,
    }


def _add_guard_ring(
    c: gf.Component,
    info: dict,
    is_pmos: bool,
) -> None:
    """Add a guard ring around the device matching Magic's exact geometry.

    Ring is 0.17um wide tap with 0.125um implant enclosure.
    Guard ring inner edge is positioned at:
      x: (diff_half_x + implant_enc) + 0.215  from origin
      y: NPC_edge + 0.24  from origin
    """
    from math import floor as _floor

    hw = info["hw"]
    diff_half_x = info["diff_half_x"]
    gate_to_polycont = info["gate_to_polycont"]
    pc_pad_size = info["pc_pad_size"]
    npc_ext = info["npc_ext"]

    # Guard ring constants
    ring_width = 0.17
    impl_enc = 0.125
    contact_size = 0.17
    contact_pitch = 0.34  # contact_size + contact_spacing

    # Device extents for spacing calculations
    nsdm_x = diff_half_x + info["implant_enc"]
    npc_y = hw + gate_to_polycont + pc_pad_size / 2.0 + npc_ext

    # Guard ring inner/outer edges (empirically matched to Magic)
    gr_inner_x = _snap(nsdm_x + 0.215)
    gr_inner_y = _snap(npc_y + 0.24)
    gr_outer_x = gr_inner_x + ring_width
    gr_outer_y = gr_inner_y + ring_width

    # ---- Tap segments ----
    # Top and bottom span full width; left and right span inner_y range only
    # (corners formed by overlap of horizontal and vertical segments)
    _rect(c, LAYER.tapdrawing, -gr_outer_x, gr_inner_y, gr_outer_x, gr_outer_y)    # top
    _rect(c, LAYER.tapdrawing, -gr_outer_x, -gr_outer_y, gr_outer_x, -gr_inner_y)  # bottom
    _rect(c, LAYER.tapdrawing, -gr_outer_x, -gr_inner_y, -gr_inner_x, gr_inner_y)  # left
    _rect(c, LAYER.tapdrawing, gr_inner_x, -gr_inner_y, gr_outer_x, gr_inner_y)    # right

    # ---- Li1 on guard ring (same footprint as tap) ----
    _rect(c, LAYER.li1drawing, -gr_outer_x, gr_inner_y, gr_outer_x, gr_outer_y)
    _rect(c, LAYER.li1drawing, -gr_outer_x, -gr_outer_y, gr_outer_x, -gr_inner_y)
    _rect(c, LAYER.li1drawing, -gr_outer_x, -gr_inner_y, -gr_inner_x, gr_inner_y)
    _rect(c, LAYER.li1drawing, gr_inner_x, -gr_inner_y, gr_outer_x, gr_inner_y)

    # ---- Implant on guard ring ----
    # PSDM for NFET body tap (P+ substrate), NSDM for PFET body tap (N+ well)
    # Implant is 4 separate rectangles matching tap corners (with overlap)
    gr_impl_layer = LAYER.nsdmdrawing if is_pmos else LAYER.psdmdrawing
    imp_x0 = -(gr_outer_x + impl_enc)
    imp_x1 = gr_outer_x + impl_enc
    imp_y0 = -(gr_outer_y + impl_enc)
    imp_y1 = gr_outer_y + impl_enc
    imp_inner_x0 = -(gr_inner_x - impl_enc)
    imp_inner_x1 = gr_inner_x - impl_enc
    imp_inner_y0 = -(gr_inner_y - impl_enc)
    imp_inner_y1 = gr_inner_y - impl_enc
    # Top horizontal
    _rect(c, gr_impl_layer, imp_x0, imp_inner_y1, imp_x1, imp_y1)
    # Bottom horizontal
    _rect(c, gr_impl_layer, imp_x0, imp_y0, imp_x1, imp_inner_y0)
    # Left vertical
    _rect(c, gr_impl_layer, imp_x0, imp_inner_y0, imp_inner_x0, imp_inner_y1)
    # Right vertical
    _rect(c, gr_impl_layer, imp_inner_x1, imp_inner_y0, imp_x1, imp_inner_y1)

    # ---- Licon contacts on guard ring ----
    # Ring center positions
    gr_cx = (gr_inner_x + gr_outer_x) / 2.0  # x center of left/right segments
    gr_cy = (gr_inner_y + gr_outer_y) / 2.0  # y center of top/bottom segments

    # Horizontal segment contacts (top/bottom)
    # Non-corner x region: -gr_inner_x to +gr_inner_x
    non_corner_x = 2 * gr_inner_x
    # Contact count uses enclosure = contact_pitch in the non-corner region
    n_horiz = max(1, 1 + _floor((non_corner_x - 2 * contact_pitch - contact_size) / contact_pitch))
    arr_w = (n_horiz - 1) * contact_pitch + contact_size
    ch = contact_size / 2.0
    for sign_y in [1, -1]:
        cy = sign_y * gr_cy
        for i in range(n_horiz):
            cx = -arr_w / 2.0 + i * contact_pitch + ch
            _rect(c, LAYER.licon1drawing,
                  cx - ch, cy - ch, cx + ch, cy + ch)

    # Vertical segment contacts (left/right)
    # Non-corner y region: -gr_inner_y to +gr_inner_y
    non_corner_y = 2 * gr_inner_y
    # Contact count uses enclosure = 0.27 in the non-corner region
    vert_enc = 0.27
    n_vert = max(1, 1 + _floor((non_corner_y - 2 * vert_enc - contact_size) / contact_pitch))
    arr_h = (n_vert - 1) * contact_pitch + contact_size
    for sign_x in [-1, 1]:
        cx = sign_x * gr_cx
        for i in range(n_vert):
            cy = -arr_h / 2.0 + i * contact_pitch + ch
            _rect(c, LAYER.licon1drawing,
                  cx - ch, cy - ch, cx + ch, cy + ch)

    # ---- N-well for PFET guard ring ----
    if is_pmos:
        nw_ext = 0.18
        _rect(c, LAYER.nwelldrawing,
              -(gr_outer_x + nw_ext), -(gr_outer_y + nw_ext),
              gr_outer_x + nw_ext, gr_outer_y + nw_ext)

    # ---- PR boundary at ring center ----
    pr_x = (gr_inner_x + gr_outer_x) / 2.0
    pr_y = (gr_inner_y + gr_outer_y) / 2.0
    _rect(c, LAYER.prBoundaryboundary, -pr_x, -pr_y, pr_x, pr_y)

    # ---- Body label at bottom of PR boundary ----
    c.add_label(
        text="B",
        position=(0.0, -pr_y),
        layer=LAYER.li1label,
    )


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
        sd_width: source/drain contact region width (um) — reserved, not used directly.
        nf: number of gate fingers.
        guard_ring: if True, add a pwell (P+ substrate) guard ring.
        dnwell: if True, add a deep N-well under the device.
        end_cap: poly extension beyond diffusion edge (um) — reserved, not used directly.
        mult: multiplier (currently generates one device; reserved for future use).
    """
    c = gf.Component()

    info = _mosfet_core(c, gate_width, gate_length, nf, is_pmos=False)

    if guard_ring:
        _add_guard_ring(c, info, is_pmos=False)

    # Note: dnwell parameter accepted for API compatibility but not generated
    # (Magic's reference GDS does not include a dnwell layer for standard MOSFETs)

    # ---- Ports ----
    sd = info["sd_centers_x"]
    hw = info["hw"]
    gpc = info["gate_to_polycont"]

    c.add_port(
        name="GATE",
        center=(info["gate_centers_x"][0], 0.0),
        width=gate_width,
        orientation=0,
        layer=LAYER.polydrawing,
        port_type="electrical",
    )
    # Source = rightmost S/D for nf=1
    c.add_port(
        name="SOURCE",
        center=(sd[-1], 0.0),
        width=gate_width,
        orientation=0,
        layer=LAYER.li1drawing,
        port_type="electrical",
    )
    # Drain = leftmost S/D for nf=1
    c.add_port(
        name="DRAIN",
        center=(sd[0], 0.0),
        width=gate_width,
        orientation=180,
        layer=LAYER.li1drawing,
        port_type="electrical",
    )
    c.add_port(
        name="BODY",
        center=(0.0, -(hw + gpc)),
        width=gate_width,
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
        sd_width: source/drain contact region width (um) — reserved, not used directly.
        nf: number of gate fingers.
        guard_ring: if True, add an nwell (N+ tap) guard ring.
        dnwell: if True, add a deep N-well under the device.
        end_cap: poly extension beyond diffusion edge (um) — reserved, not used directly.
        mult: multiplier (currently generates one device; reserved for future use).
    """
    c = gf.Component()

    info = _mosfet_core(c, gate_width, gate_length, nf, is_pmos=True,
                        suppress_nwell=guard_ring)

    if guard_ring:
        _add_guard_ring(c, info, is_pmos=True)

    # Note: dnwell parameter accepted for API compatibility but not generated

    # ---- Ports ----
    sd = info["sd_centers_x"]
    hw = info["hw"]
    gpc = info["gate_to_polycont"]

    c.add_port(
        name="GATE",
        center=(info["gate_centers_x"][0], 0.0),
        width=gate_width,
        orientation=0,
        layer=LAYER.polydrawing,
        port_type="electrical",
    )
    c.add_port(
        name="SOURCE",
        center=(sd[-1], 0.0),
        width=gate_width,
        orientation=0,
        layer=LAYER.li1drawing,
        port_type="electrical",
    )
    c.add_port(
        name="DRAIN",
        center=(sd[0], 0.0),
        width=gate_width,
        orientation=180,
        layer=LAYER.li1drawing,
        port_type="electrical",
    )
    c.add_port(
        name="BODY",
        center=(0.0, -(hw + gpc)),
        width=gate_width,
        orientation=270,
        layer=LAYER.li1drawing,
        port_type="electrical",
    )

    return c


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
    info = _mosfet_core(c, gate_width, gate_length, nf, is_pmos=is_pmos,
                        suppress_nwell=(is_pmos and guard_ring))

    # Extra implant/process layers covering diffusion + implant_enc margin
    enc = info["implant_enc"]
    dhx = info["diff_half_x"]
    hw = info["hw"]
    for layer in extra_layers:
        _rect(c, layer, -(dhx + enc), -(hw + enc), dhx + enc, hw + enc)

    if guard_ring:
        _add_guard_ring(c, info, is_pmos=is_pmos)

    # Note: dnwell parameter accepted for API compatibility but not generated

    # Ports
    sd = info["sd_centers_x"]
    gpc = info["gate_to_polycont"]
    c.add_port(
        name="GATE",
        center=(info["gate_centers_x"][0], 0.0),
        width=gate_width,
        orientation=0,
        layer=LAYER.polydrawing,
        port_type="electrical",
    )
    c.add_port(
        name="SOURCE",
        center=(sd[-1], 0.0),
        width=gate_width,
        orientation=0,
        layer=LAYER.li1drawing,
        port_type="electrical",
    )
    c.add_port(
        name="DRAIN",
        center=(sd[0], 0.0),
        width=gate_width,
        orientation=180,
        layer=LAYER.li1drawing,
        port_type="electrical",
    )
    c.add_port(
        name="BODY",
        center=(0.0, -(hw + gpc)),
        width=gate_width,
        orientation=270,
        layer=LAYER.li1drawing,
        port_type="electrical",
    )
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
