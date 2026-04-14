"""Magic-parity MOSFET generators for sky130.

Provides nfet_01v8 and pfet_01v8 parametric cells that match the geometry
produced by Magic's sky130 device generators, including multi-finger support,
S/D sharing, guard rings, and deep N-well options.

All geometry is centered at the origin to match Magic's output coordinate system.
"""

import gdsfactory as gf

from sky130.layers import LAYER


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
    diff_surround = 0.06  # Diffusion enclosure of licon contact
    poly_surround = 0.08  # Poly enclosure of licon contact (on poly)
    gate_to_diffcont = 0.145  # Gate edge to diff contact center (edge contacts)
    gate_to_polycont_n = 0.275  # Gate edge to poly contact center (NFET)
    gate_to_polycont_p = 0.32  # Gate edge to poly contact center (PFET)
    diff_extension = 0.29  # Diffusion extension beyond gate (nf=1 edge)
    end_cap = 0.13  # Poly extension beyond diffusion (non-contact side)
    implant_enc = 0.125  # Implant enclosure beyond diffusion
    nwell_enc_x = 0.18  # Nwell enclosure of diff in x (PFET)
    npc_ext = 0.02  # NPC extension beyond poly pad
    met1_surround = 0.03  # Met1 surround of mcon contact
    li1_ext_y = 0.02  # Li1 extension beyond diffusion edge for S/D

    gate_to_polycont = gate_to_polycont_p if is_pmos else gate_to_polycont_n

    # ---- Derived dimensions ----
    W = gate_width
    L = gate_length
    hw = W / 2.0  # half-width (y direction)
    hl = L / 2.0  # half-length (x direction)

    # Poly contact pad dimensions
    pc_pad_size = contact_size + 2 * poly_surround  # 0.33

    # Gate extension on the contact side: poly extends just to the pad base
    gate_ext_contact = gate_to_polycont - (contact_size / 2 + poly_surround)
    # Gate extension on non-contact side (standard end_cap)
    gate_ext_nocont = end_cap

    # ---- Finger pitch and contact positions ----
    # For shared contacts between gates (nf > 1), the gate-to-contact spacing
    # depends on L: when L < contact_size, poly_surround clearance requires
    # wider spacing (0.165 vs 0.145).  A minimum pitch of 0.48 is enforced
    # so intermediate L values (e.g. L=0.18) maintain adequate clearance.
    if L < contact_size:
        shared_gate_to_diffcont = max(
            gate_to_diffcont, contact_size / 2 + poly_surround
        )
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
        finger_pitch = max(L + 2 * shared_gate_to_diffcont, 0.48)
        # Gate centers: symmetric about origin
        gate_centers_x = [
            _snap(-((nf - 1) / 2.0) * finger_pitch + i * finger_pitch)
            for i in range(nf)
        ]
        # S/D contact centers: nf+1 contacts
        sd_centers_x = [
            _snap(-(nf / 2.0) * finger_pitch + i * finger_pitch) for i in range(nf + 1)
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
    # When L >= 2*end_cap (0.26) but < pc_pad_size (0.33), the gate is long
    # enough that the poly body extends symmetrically to gate_ext_contact on
    # both sides, and the pad alternation reverses (even=top, odd=bottom).
    reversed_alternation = L >= 2 * end_cap and L < pc_pad_size and nf > 1
    for gi, gx in enumerate(gate_centers_x):
        if nf == 1 or L >= pc_pad_size or reversed_alternation:
            # Both sides get contacts when:
            # - nf=1 (single finger)
            # - gate is wide enough to serve as its own contact pad (L >= pc_pad_size)
            # - reversed alternation range (L >= 2*end_cap): gate body is symmetric
            #   and both sides have poly contact pads
            contact_sides = ["top", "bottom"]
        else:
            # Standard alternation (L < 2*end_cap): even gates get bottom, odd get top
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
                _rect(
                    c, LAYER.polydrawing, gx - hl, poly_bot_gate, gx + hl, poly_top_gate
                )

                # Top poly contact pad
                pad_half = pc_pad_size / 2.0
                pad_cy_top = hw + gate_to_polycont
                _rect(
                    c,
                    LAYER.polydrawing,
                    gx - pad_half,
                    pad_cy_top - pad_half,
                    gx + pad_half,
                    pad_cy_top + pad_half,
                )
                # Bottom poly contact pad
                pad_cy_bot = -(hw + gate_to_polycont)
                _rect(
                    c,
                    LAYER.polydrawing,
                    gx - pad_half,
                    pad_cy_bot - pad_half,
                    gx + pad_half,
                    pad_cy_bot + pad_half,
                )
            elif reversed_alternation:
                # Multi-finger with intermediate gate width (L >= 2*end_cap):
                # Gate body extends to gate_ext_contact on BOTH sides (symmetric).
                # Pad rectangles on BOTH sides (same as nf=1).
                pad_half = pc_pad_size / 2.0
                poly_ext_y = hw + gate_ext_contact
                _rect(
                    c,
                    LAYER.polydrawing,
                    gx - hl,
                    -poly_ext_y,
                    gx + hl,
                    poly_ext_y,
                )
                # Top poly contact pad
                pad_cy_top = hw + gate_to_polycont
                _rect(
                    c,
                    LAYER.polydrawing,
                    gx - pad_half,
                    pad_cy_top - pad_half,
                    gx + pad_half,
                    pad_cy_top + pad_half,
                )
                # Bottom poly contact pad
                pad_cy_bot = -(hw + gate_to_polycont)
                _rect(
                    c,
                    LAYER.polydrawing,
                    gx - pad_half,
                    pad_cy_bot - pad_half,
                    gx + pad_half,
                    pad_cy_bot + pad_half,
                )
            else:
                # Multi-finger with narrow gate (L < contact_size)
                pad_half = pc_pad_size / 2.0
                if "top" in contact_sides:
                    # Gate extends up to pad base, down to end_cap
                    poly_top_gate = hw + gate_ext_contact
                    poly_bot_gate = -(hw + gate_ext_nocont)
                    _rect(
                        c,
                        LAYER.polydrawing,
                        gx - hl,
                        poly_bot_gate,
                        gx + hl,
                        poly_top_gate,
                    )
                    # Top contact pad
                    pad_cy = hw + gate_to_polycont
                    _rect(
                        c,
                        LAYER.polydrawing,
                        gx - pad_half,
                        pad_cy - pad_half,
                        gx + pad_half,
                        pad_cy + pad_half,
                    )
                else:
                    # Gate extends down to pad base, up to end_cap
                    poly_top_gate = hw + gate_ext_nocont
                    poly_bot_gate = -(hw + gate_ext_contact)
                    _rect(
                        c,
                        LAYER.polydrawing,
                        gx - hl,
                        poly_bot_gate,
                        gx + hl,
                        poly_top_gate,
                    )
                    # Bottom contact pad
                    pad_cy = -(hw + gate_to_polycont)
                    _rect(
                        c,
                        LAYER.polydrawing,
                        gx - pad_half,
                        pad_cy - pad_half,
                        gx + pad_half,
                        pad_cy + pad_half,
                    )

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
            # Licon and mcon use different pitches for wide gates
            licon_poly_pitch = contact_size + contact_size  # 0.34
            mcon_poly_pitch = contact_size + 0.19  # 0.36
            if num_poly_contacts_x == 1:
                _rect(
                    c,
                    LAYER.licon1drawing,
                    gx - licon_half,
                    pad_cy - licon_half,
                    gx + licon_half,
                    pad_cy + licon_half,
                )
                _rect(
                    c,
                    LAYER.mcondrawing,
                    gx - licon_half,
                    pad_cy - licon_half,
                    gx + licon_half,
                    pad_cy + licon_half,
                )
            else:
                # Licon array
                licon_array_w = (
                    num_poly_contacts_x - 1
                ) * licon_poly_pitch + contact_size
                licon_start_x = gx - licon_array_w / 2.0
                for ci in range(num_poly_contacts_x):
                    cx = licon_start_x + ci * licon_poly_pitch
                    _rect(
                        c,
                        LAYER.licon1drawing,
                        cx,
                        pad_cy - licon_half,
                        cx + contact_size,
                        pad_cy + licon_half,
                    )
                # Mcon array (different pitch)
                mcon_array_w = (
                    num_poly_contacts_x - 1
                ) * mcon_poly_pitch + contact_size
                mcon_start_x = gx - mcon_array_w / 2.0
                for ci in range(num_poly_contacts_x):
                    cx = mcon_start_x + ci * mcon_poly_pitch
                    _rect(
                        c,
                        LAYER.mcondrawing,
                        cx,
                        pad_cy - licon_half,
                        cx + contact_size,
                        pad_cy + licon_half,
                    )

            # Li1 over poly contact: covers the larger of pad area or gate width
            li_half_x = max(pc_pad_size / 2.0, hl)
            _rect(
                c,
                LAYER.li1drawing,
                gx - li_half_x,
                pad_cy - licon_half,
                gx + li_half_x,
                pad_cy + licon_half,
            )
            # Met1 over poly contact
            pad_half_x = max(pc_pad_size / 2.0, hl)
            m1_half_x = pad_half_x - npc_ext
            m1_half_y = licon_half + met1_surround
            _rect(
                c,
                LAYER.met1drawing,
                gx - m1_half_x,
                pad_cy - m1_half_y,
                gx + m1_half_x,
                pad_cy + m1_half_y,
            )

            # NPC over poly contact region
            # For reversed alternation: defer NPC to after the loop (spans all gates)
            # For normal cases: per-gate NPC
            if not reversed_alternation:
                if num_poly_contacts_x > 1:
                    licon_array_w = (
                        num_poly_contacts_x - 1
                    ) * licon_poly_pitch + contact_size
                    npc_half_x = licon_array_w / 2.0 + poly_surround + npc_ext
                else:
                    npc_half_x = pc_pad_size / 2.0 + npc_ext
                npc_half_y = pc_pad_size / 2.0 + npc_ext
                _rect(
                    c,
                    LAYER.npcdrawing,
                    gx - npc_half_x,
                    pad_cy - npc_half_y,
                    gx + npc_half_x,
                    pad_cy + npc_half_y,
                )

    # ---- NPC for reversed alternation: span all gates on both top and bottom ----
    if reversed_alternation:
        npc_half_x = pc_pad_size / 2.0 + npc_ext
        npc_half_y = pc_pad_size / 2.0 + npc_ext
        # NPC left edge = leftmost gate center - npc_half_x
        # NPC right edge = rightmost gate center + npc_half_x
        npc_left = gate_centers_x[0] - npc_half_x
        npc_right = gate_centers_x[-1] + npc_half_x
        # Top NPC
        pad_cy_top = hw + gate_to_polycont
        _rect(
            c,
            LAYER.npcdrawing,
            npc_left,
            pad_cy_top - npc_half_y,
            npc_right,
            pad_cy_top + npc_half_y,
        )
        # Bottom NPC
        pad_cy_bot = -(hw + gate_to_polycont)
        _rect(
            c,
            LAYER.npcdrawing,
            npc_left,
            pad_cy_bot - npc_half_y,
            npc_right,
            pad_cy_bot + npc_half_y,
        )

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
            _rect(c, LAYER.licon1drawing, sx - ch, cy - ch, sx + ch, cy + ch)

        # -- Mcon contacts (different pitch and enclosure) --
        avail_h_mcon = W - 2 * mcon_enc_y
        n_mcon = max(1, int((avail_h_mcon - contact_size) / mcon_pitch) + 1)
        arr_h_mcon = (n_mcon - 1) * mcon_pitch + contact_size
        for ci in range(n_mcon):
            cy = -arr_h_mcon / 2.0 + ci * mcon_pitch + ch
            _rect(c, LAYER.mcondrawing, sx - ch, cy - ch, sx + ch, cy + ch)

        # Li1 strip over S/D: same x range as contact, y extends to ±(hw + li1_ext_y)
        li1_y_ext = hw + li1_ext_y
        _rect(c, LAYER.li1drawing, sx - ch, -li1_y_ext, sx + ch, li1_y_ext)

        # Met1 pad over S/D
        m1_half_x = ch + met1_surround
        m1_half_y = hw  # met1 extends to diff edge
        _rect(
            c, LAYER.met1drawing, sx - m1_half_x, -m1_half_y, sx + m1_half_x, m1_half_y
        )

    # ---- 4. Implant layer (NSDM or PSDM) ----
    impl_layer = LAYER.psdmdrawing if is_pmos else LAYER.nsdmdrawing
    _rect(
        c,
        impl_layer,
        -(diff_half_x + implant_enc),
        -(hw + implant_enc),
        diff_half_x + implant_enc,
        hw + implant_enc,
    )

    # ---- 5. N-well (PFET only, skipped when guard ring will provide it) ----
    if is_pmos and not suppress_nwell:
        # Nwell extends 0.18 beyond diff in x, and encompasses poly contact region in y
        nwell_x = diff_half_x + nwell_enc_x
        # In y: extends to poly contact region top/bottom + npc_ext + some clearance
        polycont_pad_top = hw + gate_to_polycont + contact_size / 2 + poly_surround
        nwell_y = polycont_pad_top + 0.015  # empirical from reference: pad_top + 0.015

        if nf > 1 and L < pc_pad_size and not reversed_alternation:
            # Multi-finger with alternating pads: L-shaped nwell.
            # (Only for standard alternation where each gate has a pad on one side.
            #  Reversed alternation has pads on both sides, so uses simple rect.)
            nwell_step_y = _snap(hw + gate_to_polycont - 0.01)
            step_x = _snap(nwell_x - finger_pitch)

            # Determine which y-side ("bottom" = -y, "top" = +y) the even gates use.
            # Even gates are at the outermost positions for odd nf.
            if reversed_alternation:
                even_side = "top"  # even gates get top contacts
            else:
                even_side = "bottom"  # even gates get bottom contacts

            if nf % 2 == 1:
                # Odd nf: both outermost gates are even, so the even-side needs
                # full width; the other side only needs narrow (center) width.
                if even_side == "bottom":
                    # Main rect: full width, from -nwell_y to +nwell_step_y
                    _rect(c, LAYER.nwelldrawing, -nwell_x, -nwell_y, nwell_x, nwell_step_y)
                    # Top bump: narrow, from +nwell_step_y to +nwell_y
                    _rect(c, LAYER.nwelldrawing, -step_x, nwell_step_y, step_x, nwell_y)
                else:
                    # Main rect: full width, from -nwell_step_y to +nwell_y
                    _rect(c, LAYER.nwelldrawing, -nwell_x, -nwell_step_y, nwell_x, nwell_y)
                    # Bottom bump: narrow, from -nwell_y to -nwell_step_y
                    _rect(c, LAYER.nwelldrawing, -step_x, -nwell_y, step_x, -nwell_step_y)
            else:
                # Even nf: outermost gates are 0 (even) and nf-1 (odd).
                # Each side extends in one diagonal direction.
                _rect(c, LAYER.nwelldrawing, -nwell_x, -nwell_step_y, nwell_x, nwell_step_y)
                if even_side == "bottom":
                    _rect(c, LAYER.nwelldrawing, -nwell_x, -nwell_y, step_x, -nwell_step_y)
                    _rect(c, LAYER.nwelldrawing, -step_x, nwell_step_y, nwell_x, nwell_y)
                else:
                    _rect(c, LAYER.nwelldrawing, -step_x, -nwell_y, nwell_x, -nwell_step_y)
                    _rect(c, LAYER.nwelldrawing, -nwell_x, nwell_step_y, step_x, nwell_y)
        else:
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
                c.add_label(text=f"D{gi}", position=(sx, 0.0), layer=LAYER.li1label)
            else:
                c.add_label(text=f"S{gi}", position=(sx, 0.0), layer=LAYER.li1label)
        # Last S/D contact: labeled only for odd nf
        if nf % 2 == 1:
            sx = sd_centers_x[nf]
            c.add_label(text=f"S{nf - 1}", position=(sx, 0.0), layer=LAYER.li1label)

        for gi, gx in enumerate(gate_centers_x):
            if L >= pc_pad_size or reversed_alternation:
                # Wide gate or reversed alternation: contacts on both sides, label on top
                gate_label_y = hw + gate_to_polycont
            elif gi % 2 == 0:
                gate_label_y = -(hw + gate_to_polycont)
            else:
                gate_label_y = hw + gate_to_polycont
            c.add_label(
                text=f"G{gi}",
                position=(gx, gate_label_y),
                layer=LAYER.li1label,
            )

    # ---- Compute outermost gate edge (for variant implant sizing) ----
    outermost_gate_edge_x = abs(gate_centers_x[-1]) + hl

    # ---- Compute nwell extent (for pfet variants) ----
    polycont_pad_top = hw + gate_to_polycont + contact_size / 2 + poly_surround
    nwell_x = diff_half_x + nwell_enc_x
    nwell_y = polycont_pad_top + 0.015  # empirical from reference

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
        "outermost_gate_edge_x": outermost_gate_edge_x,
        "nwell_x": nwell_x,
        "nwell_y": nwell_y,
    }


def _add_guard_ring(
    c: gf.Component,
    info: dict,
    is_pmos: bool,
    is_hvi: bool = False,
    is_nvt: bool = False,
) -> dict:
    """Add a guard ring around the device matching Magic's exact geometry.

    For standard devices: ring_width=0.17, spacing from nsdm/npc.
    For HVI devices: ring_width=0.29, larger spacing, different nwell enclosure.

    Returns a dict with guard ring extents for HVI layer placement.
    """

    hw = info["hw"]
    diff_half_x = info["diff_half_x"]
    gate_to_polycont = info["gate_to_polycont"]
    pc_pad_size = info["pc_pad_size"]
    npc_ext = info["npc_ext"]

    # Guard ring constants — differ for HVI devices
    contact_size = 0.17
    contact_pitch = 0.34  # contact_size + contact_spacing
    impl_enc = 0.125

    if is_hvi:
        ring_width = 0.29
        # HVI devices use larger spacing from device boundary
        implant_x = diff_half_x + info["implant_enc"]
        if is_nvt:
            inner_spacing_x = 0.255
        else:
            # nfet_g5v0d10v5 uses 0.265, pfet_g5v0d10v5 uses 0.255
            inner_spacing_x = 0.265 if not is_pmos else 0.255
        inner_spacing_y = 0.36
    else:
        ring_width = 0.17
        inner_spacing_x = 0.215
        inner_spacing_y = 0.24

    # Device extents for spacing calculations
    nsdm_x = diff_half_x + info["implant_enc"]
    npc_y = hw + gate_to_polycont + pc_pad_size / 2.0 + npc_ext

    # Guard ring inner/outer edges
    gr_inner_x = _snap(nsdm_x + inner_spacing_x)
    gr_inner_y = _snap(npc_y + inner_spacing_y)
    gr_outer_x = gr_inner_x + ring_width
    gr_outer_y = gr_inner_y + ring_width

    # ---- Tap segments ----
    # Top and bottom span full width; left and right span inner_y range only
    # (corners formed by overlap of horizontal and vertical segments)
    _rect(c, LAYER.tapdrawing, -gr_outer_x, gr_inner_y, gr_outer_x, gr_outer_y)  # top
    _rect(
        c, LAYER.tapdrawing, -gr_outer_x, -gr_outer_y, gr_outer_x, -gr_inner_y
    )  # bottom
    _rect(
        c, LAYER.tapdrawing, -gr_outer_x, -gr_inner_y, -gr_inner_x, gr_inner_y
    )  # left
    _rect(c, LAYER.tapdrawing, gr_inner_x, -gr_inner_y, gr_outer_x, gr_inner_y)  # right

    # ---- Li1 on guard ring ----
    # For HVI devices, Li1 is 0.17 wide (standard) centered in the wider 0.29 tap.
    # For standard devices, Li1 matches the tap footprint.
    if is_hvi:
        li1_width = 0.17
        li1_margin = (ring_width - li1_width) / 2.0
        li1_inner_x = gr_inner_x + li1_margin
        li1_outer_x = gr_outer_x - li1_margin
        li1_inner_y = gr_inner_y + li1_margin
        li1_outer_y = gr_outer_y - li1_margin
    else:
        li1_inner_x = gr_inner_x
        li1_outer_x = gr_outer_x
        li1_inner_y = gr_inner_y
        li1_outer_y = gr_outer_y
    _rect(c, LAYER.li1drawing, -li1_outer_x, li1_inner_y, li1_outer_x, li1_outer_y)
    _rect(c, LAYER.li1drawing, -li1_outer_x, -li1_outer_y, li1_outer_x, -li1_inner_y)
    _rect(c, LAYER.li1drawing, -li1_outer_x, -li1_inner_y, -li1_inner_x, li1_inner_y)
    _rect(c, LAYER.li1drawing, li1_inner_x, -li1_inner_y, li1_outer_x, li1_inner_y)

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

    # For HVI devices, licon contacts use the li1 inner edge for available region,
    # not the tap inner edge (since li1 is narrower than tap in HVI).
    if is_hvi:
        contact_region_inner_x = li1_inner_x
        contact_region_inner_y = li1_inner_y
    else:
        contact_region_inner_x = gr_inner_x
        contact_region_inner_y = gr_inner_y

    # Horizontal segment contacts (top/bottom)
    non_corner_x = 2 * contact_region_inner_x
    # Contact count uses enclosure in the non-corner region.
    # Use integer nanometer arithmetic for exact boundary handling.
    horiz_enc = 0.325 if is_hvi else 0.31
    _ncx_nm = round(non_corner_x * 1000)
    _henc_nm = round(horiz_enc * 1000)
    _cs_nm = round(contact_size * 1000)
    _cp_nm = round(contact_pitch * 1000)
    n_horiz = max(1, 1 + (_ncx_nm - 2 * _henc_nm - _cs_nm) // _cp_nm)
    arr_w = (n_horiz - 1) * contact_pitch + contact_size
    ch = contact_size / 2.0
    for sign_y in [1, -1]:
        cy = sign_y * gr_cy
        for i in range(n_horiz):
            cx = -arr_w / 2.0 + i * contact_pitch + ch
            _rect(c, LAYER.licon1drawing, cx - ch, cy - ch, cx + ch, cy + ch)

    # Vertical segment contacts (left/right)
    non_corner_y = 2 * contact_region_inner_y
    # Contact count — also in integer nanometers.
    # Subtract 1 before division for strict less-than at exact boundaries
    # (e.g. PFET W=5.0 where the available height is exactly N*pitch).
    vert_enc = 0.29 if is_hvi else 0.30
    _ncy_nm = round(non_corner_y * 1000)
    _venc_nm = round(vert_enc * 1000)
    _vert_avail_nm = _ncy_nm - 2 * _venc_nm - _cs_nm
    n_vert = max(1, 1 + (_vert_avail_nm - 1) // _cp_nm)
    arr_h = (n_vert - 1) * contact_pitch + contact_size
    for sign_x in [-1, 1]:
        cx = sign_x * gr_cx
        for i in range(n_vert):
            cy = -arr_h / 2.0 + i * contact_pitch + ch
            _rect(c, LAYER.licon1drawing, cx - ch, cy - ch, cx + ch, cy + ch)

    # ---- N-well for PFET guard ring ----
    if is_pmos:
        # HVI PFET uses larger nwell enclosure (0.33 vs 0.18)
        nw_ext = 0.33 if is_hvi else 0.18
        _rect(
            c,
            LAYER.nwelldrawing,
            -(gr_outer_x + nw_ext),
            -(gr_outer_y + nw_ext),
            gr_outer_x + nw_ext,
            gr_outer_y + nw_ext,
        )

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

    return {
        "gr_outer_x": gr_outer_x,
        "gr_outer_y": gr_outer_y,
        "gr_inner_x": gr_inner_x,
        "gr_inner_y": gr_inner_y,
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

    _add_ports(c, info, gate_width)
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

    info = _mosfet_core(
        c, gate_width, gate_length, nf, is_pmos=True, suppress_nwell=guard_ring
    )

    if guard_ring:
        _add_guard_ring(c, info, is_pmos=True)

    _add_ports(c, info, gate_width)
    return c


def _add_ports(
    c: gf.Component,
    info: dict,
    gate_width: float,
) -> None:
    """Add standard MOSFET ports to a component."""
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


def _add_lvtn_or_hvtp(c, info, layer):
    """Add LVTN (125/44) or HVTP (78/44) implant layer.

    Sizing: outermost_gate_edge + 0.18 in x, hw + 0.18 in y.
    """
    enc = 0.18
    ge = info["outermost_gate_edge_x"]
    hw = info["hw"]
    _rect(c, layer, -(ge + enc), -(hw + enc), ge + enc, hw + enc)


def _add_hvntm(c, info):
    """Add HVNTM (125/20) layer.

    Sizing: diff_half_x + 0.185 in x, hw + 0.185 in y.
    """
    enc = 0.185
    dhx = info["diff_half_x"]
    hw = info["hw"]
    _rect(c, LAYER.hvntmdrawing, -(dhx + enc), -(hw + enc), dhx + enc, hw + enc)


def _add_hvi_nfet(c, info, guard_ring, gr_info=None):
    """Add HVI (75/20) layer for NFET devices.

    Without guard ring: diff_half_x + 0.185 in x, hw + 0.185 in y (nf>1)
                        or hw + 0.21 in y (nf=1).
    With guard ring: gr_outer + 0.185 in both x and y.
    """
    hvi_enc = 0.185
    if guard_ring and gr_info is not None:
        hvi_x = gr_info["gr_outer_x"] + hvi_enc
        hvi_y = gr_info["gr_outer_y"] + hvi_enc
    else:
        dhx = info["diff_half_x"]
        hw = info["hw"]
        hvi_x = dhx + hvi_enc
        # Magic uses minimum HVI y-extent of 0.42 (matching nf=1 W=0.42 case),
        # or hw + hvi_enc for larger W where hw already exceeds the minimum.
        hvi_y = max(hw + hvi_enc, 0.42)
    _rect(c, LAYER.hvidrawing, -hvi_x, -hvi_y, hvi_x, hvi_y)


def _add_hvi_pfet(c, info, guard_ring, gr_info=None):
    """Add HVI (75/20) layer for PFET devices.

    With guard ring: same as nwell extent (gr_outer + nw_ext).
    Without guard ring: three rectangles covering nwell + extra horizontal band.
    """
    if guard_ring and gr_info is not None:
        # HVI = nwell extent = gr_outer + 0.33
        nw_ext = 0.33
        hvi_x = gr_info["gr_outer_x"] + nw_ext
        hvi_y = gr_info["gr_outer_y"] + nw_ext
        _rect(c, LAYER.hvidrawing, -hvi_x, -hvi_y, hvi_x, hvi_y)
    else:
        # Three rectangles forming a cross/plus shape around nwell
        nwell_x = info["nwell_x"]
        nwell_y = info["nwell_y"]
        hw = info["hw"]
        hvi_enc = 0.185
        center_y = max(hw + hvi_enc, 0.42)
        if center_y > 0.42:
            # Large W: minimal protrusion beyond nwell
            center_x = nwell_x + (hvi_enc - 0.18)  # nwell_x + 0.005
        else:
            # Small W: wider horizontal band for HVI clearance
            center_x = nwell_x + 0.425
        # Center horizontal band
        _rect(c, LAYER.hvidrawing, -center_x, -center_y, center_x, center_y)
        # Top fill to nwell boundary
        _rect(c, LAYER.hvidrawing, -nwell_x, center_y, nwell_x, nwell_y)
        # Bottom fill to nwell boundary
        _rect(c, LAYER.hvidrawing, -nwell_x, -nwell_y, nwell_x, -center_y)


def _add_areaid_native(c, info):
    """Add areaidlvNative (81/60) marker for native NMOS devices.

    For nf=1: single rect covering gate_edge + 0.10 in x, hw + 0.10 in y.
    For nf>1: separate per-gate rects, each gate_center ± (hl + 0.10) in x.
    """
    enc = 0.10
    hw = info["hw"]
    gate_centers = info["gate_centers_x"]
    # hl is the half gate length (outermost_gate_edge minus last gate center)
    if len(gate_centers) == 1:
        hl = info["outermost_gate_edge_x"]
    else:
        hl = info["outermost_gate_edge_x"] - abs(gate_centers[-1])

    for gx in gate_centers:
        _rect(
            c, LAYER.areaidlvNative, gx - hl - enc, -(hw + enc), gx + hl + enc, hw + enc
        )


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
    c = gf.Component()
    info = _mosfet_core(c, gate_width, gate_length, nf, is_pmos=False)

    # LVTN implant: gate_edge + 0.18 enclosure
    _add_lvtn_or_hvtp(c, info, LAYER.lvtndrawing)

    if guard_ring:
        _add_guard_ring(c, info, is_pmos=False)

    _add_ports(c, info, gate_width)
    return c


# ---------------------------------------------------------------------------
# Variant: Low-Vt PMOS 1.8V
# ---------------------------------------------------------------------------


@gf.cell
def sky130_fd_pr__pfet_01v8_lvt(
    gate_width: float = 0.42,
    gate_length: float = 0.35,
    sd_width: float = 0.28,
    nf: int = 1,
    guard_ring: bool = True,
    dnwell: bool = False,
    end_cap: float = 0.13,
    mult: int = 1,
) -> gf.Component:
    """Low-Vt 1.8V PMOS (sky130_fd_pr__pfet_01v8_lvt)."""
    c = gf.Component()
    info = _mosfet_core(
        c, gate_width, gate_length, nf, is_pmos=True, suppress_nwell=guard_ring
    )

    # LVTN implant: gate_edge + 0.18 enclosure
    _add_lvtn_or_hvtp(c, info, LAYER.lvtndrawing)

    if guard_ring:
        _add_guard_ring(c, info, is_pmos=True)

    _add_ports(c, info, gate_width)
    return c


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
    c = gf.Component()
    info = _mosfet_core(
        c, gate_width, gate_length, nf, is_pmos=True, suppress_nwell=guard_ring
    )

    # HVTP implant: gate_edge + 0.18 enclosure
    _add_lvtn_or_hvtp(c, info, LAYER.hvtpdrawing)

    if guard_ring:
        _add_guard_ring(c, info, is_pmos=True)

    _add_ports(c, info, gate_width)
    return c


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
    c = gf.Component()
    info = _mosfet_core(c, gate_width, gate_length, nf, is_pmos=False)

    # HVNTM layer
    _add_hvntm(c, info)

    gr_info = None
    if guard_ring:
        gr_info = _add_guard_ring(c, info, is_pmos=False, is_hvi=True)

    # HVI layer (sizing depends on guard ring)
    _add_hvi_nfet(c, info, guard_ring, gr_info)

    _add_ports(c, info, gate_width)
    return c


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
    c = gf.Component()
    info = _mosfet_core(
        c, gate_width, gate_length, nf, is_pmos=True, suppress_nwell=guard_ring
    )

    gr_info = None
    if guard_ring:
        gr_info = _add_guard_ring(c, info, is_pmos=True, is_hvi=True)

    # HVI layer (sizing depends on guard ring and nwell)
    _add_hvi_pfet(c, info, guard_ring, gr_info)

    _add_ports(c, info, gate_width)
    return c


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
    c = gf.Component()
    info = _mosfet_core(c, gate_width, gate_length, nf, is_pmos=False)

    _add_hvntm(c, info)

    gr_info = None
    if guard_ring:
        gr_info = _add_guard_ring(c, info, is_pmos=False, is_hvi=True)

    _add_hvi_nfet(c, info, guard_ring, gr_info)

    _add_ports(c, info, gate_width)
    return c


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
    c = gf.Component()
    info = _mosfet_core(
        c, gate_width, gate_length, nf, is_pmos=True, suppress_nwell=guard_ring
    )

    gr_info = None
    if guard_ring:
        gr_info = _add_guard_ring(c, info, is_pmos=True, is_hvi=True)

    _add_hvi_pfet(c, info, guard_ring, gr_info)

    _add_ports(c, info, gate_width)
    return c


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
    c = gf.Component()
    info = _mosfet_core(c, gate_width, gate_length, nf, is_pmos=False)

    # areaidlvNative marker
    _add_areaid_native(c, info)
    # LVTN implant
    _add_lvtn_or_hvtp(c, info, LAYER.lvtndrawing)
    # HVNTM layer
    _add_hvntm(c, info)

    gr_info = None
    if guard_ring:
        gr_info = _add_guard_ring(c, info, is_pmos=False, is_hvi=True, is_nvt=True)

    # HVI layer
    _add_hvi_nfet(c, info, guard_ring, gr_info)

    _add_ports(c, info, gate_width)
    return c


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
    c = gf.Component()
    info = _mosfet_core(c, gate_width, gate_length, nf, is_pmos=False)

    # LVTN implant
    _add_lvtn_or_hvtp(c, info, LAYER.lvtndrawing)
    # HVNTM layer
    _add_hvntm(c, info)

    gr_info = None
    if guard_ring:
        gr_info = _add_guard_ring(c, info, is_pmos=False, is_hvi=True, is_nvt=True)

    # HVI layer
    _add_hvi_nfet(c, info, guard_ring, gr_info)

    _add_ports(c, info, gate_width)
    return c


if __name__ == "__main__":
    c = sky130_fd_pr__nfet_01v8()
    c.show()
