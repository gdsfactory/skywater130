import gdsfactory as gf

from .via_generator import *
from .layers_def import *


def draw_cap_var(
    layout,
    type="sky130_fd_pr__cap_var_lvt",
    l: float = 0.18,
    w: float = 1,
    tap_con_col: int = 1,
    gr: int = 1,
    grw: float = 0.17,
    nf: int = 1,
):

    """
    Retern varactor

    Args:
        layout : layout object
        l : float of gate length
        w : float of gate width
        tap_con_col : int of tap contacts columns
        gr : boolaen of having guard ring
        grw : float of guard ring width
        nf : integer of number of fingers


    """

    c = gf.Component("sky_cap_var_dev")

    c_inst = gf.Component("dev inst")

    # used dimensions and layers

    end_cap = 0.15
    con_size = (0.17, 0.17)
    con_enc = (0.05, 0.08)
    con_spacing = (0.17, 0.17)
    con_t_enc = (0.06, 0.12)
    gate_con_spacing = 0.195
    tap_nsdm_enc = 0.125
    nwell_enclosing = 0.18
    tap_spacing = 0.27
    hv_enc = 0.18
    nwell_spacing = 1.27

    # draw the channel tap and poly and thier contacts

    tap_con = (
        (tap_con_col * con_size[0])
        + ((tap_con_col - 1) * con_size[0])
        + 3 * con_t_enc[0]
    )
    tap_w = gate_con_spacing + tap_con

    tap = c_inst.add_ref(
        gf.components.rectangle(size=(l + 2 * tap_w, w), layer=tap_layer)
    )

    # adding nsdm
    nsdm = c_inst.add_ref(
        gf.components.rectangle(
            size=(
                tap.xmax - tap.xmin + 2 * tap_nsdm_enc,
                tap.ymax - tap.ymin + 2 * tap_nsdm_enc,
            ),
            layer=nsdm_layer,
        )
    )
    nsdm.move((tap.xmin - tap_nsdm_enc, tap.ymin - tap_nsdm_enc))

    tap_con = via_stack(
        x_range=(0, tap_w - gate_con_spacing),
        y_range=(0.06, w - 0.06),
        base_layer=tap_layer,
        metal_level=1,
    )
    c_inst.add_array(
        component=tap_con, columns=2, rows=1, spacing=(tap_w + l + gate_con_spacing, 0)
    )

    poly = c_inst.add_ref(
        gf.components.rectangle(size=(l, w + 2 * end_cap), layer=poly_layer)
    )
    poly.move((tap_w, -end_cap))

    if l < (con_size[0] + 2 * con_enc[0]):
        pc_x = con_size[0] + 2 * con_enc[0]
    else:
        pc_x = l

    pc_y = con_size[1] + 2 * con_enc[1]

    c_pc = gf.Component("poly con")

    rect_pc = c_pc.add_ref(gf.components.rectangle(size=(pc_x, pc_y), layer=poly_layer))

    poly_con = via_stack(
        x_range=(rect_pc.xmin, rect_pc.xmax),
        y_range=(rect_pc.ymin, rect_pc.ymax),
        base_layer=poly_layer,
        metal_level=1,
        li_enc_dir="H",
    )
    c_pc.add_ref(poly_con)

    pc = c_inst.add_array(
        component=c_pc, rows=2, columns=1, spacing=(0, pc_y + w + 2 * end_cap)
    )
    pc.move((tap_w - ((pc_x - l) / 2), -pc_y - end_cap))

    # adding nwell
    nwell = c_inst.add_ref(
        gf.components.rectangle(
            size=(tap.xmax - tap.xmin + 2 * nwell_enclosing, pc.ymax - pc.ymin),
            layer=nwell_layer,
        )
    )
    nwell.move((tap.xmin - nwell_enclosing, pc.ymin))

    # c.add_ref(c_inst)
    c.add_array(
        component=c_inst,
        columns=1,
        rows=nf,
        spacing=(0, (c_inst.ymax - c_inst.ymin) + nwell_spacing),
    )

    if gr == 1:
        c_temp = gf.Component("gr form")
        g_r_in = c_temp.add_ref(
            gf.components.rectangle(
                size=(
                    (c_inst.xmax - c_inst.xmin) + 2 * tap_spacing,
                    nf * (c_inst.ymax - c_inst.ymin)
                    + (nf - 1) * nwell_spacing
                    + 2 * tap_spacing,
                ),
                layer=tap_layer,
            )
        )
        g_r_in.move((c_inst.xmin - tap_spacing, c_inst.ymin - tap_spacing))
        g_r_out = c_temp.add_ref(
            gf.components.rectangle(
                size=(
                    g_r_in.xmax - g_r_in.xmin + 2 * grw,
                    g_r_in.ymax - g_r_in.ymin + 2 * grw,
                ),
                layer=tap_layer,
            )
        )
        g_r_out.move((g_r_in.xmin - grw, g_r_in.ymin - grw))
        g_r = c.add_ref(
            gf.geometry.boolean(A=g_r_out, B=g_r_in, operation="A-B", layer=tap_layer)
        )

        g_r_li = c.add_ref(
            gf.geometry.boolean(A=g_r_out, B=g_r_in, operation="A-B", layer=li_layer)
        )

        g_psdm_in = c_temp.add_ref(
            gf.components.rectangle(
                size=(
                    g_r_in.xmax - g_r_in.xmin - 2 * tap_nsdm_enc,
                    g_r_in.ymax - g_r_in.ymin - 2 * tap_nsdm_enc,
                ),
                layer=psdm_layer,
            )
        )
        g_psdm_in.move((g_r_in.xmin + tap_nsdm_enc, g_r_in.ymin + tap_nsdm_enc))
        g_psdm_out = c_temp.add_ref(
            gf.components.rectangle(
                size=(
                    g_r_out.xmax - g_r_out.xmin + 2 * tap_nsdm_enc,
                    g_r_out.ymax - g_r_out.ymin + 2 * tap_nsdm_enc,
                ),
                layer=psdm_layer,
            )
        )
        g_psdm_out.move((g_r_out.xmin - tap_nsdm_enc, g_r_out.ymin - tap_nsdm_enc))

        g_psdm = c.add_ref(
            gf.geometry.boolean(
                A=g_psdm_out, B=g_psdm_in, operation="A-B", layer=psdm_layer
            )
        )

        if grw < con_size[0] + 2 * con_t_enc[0]:
            g_con_range = (g_r_in.ymin, g_r_in.ymax)
        else:
            g_con_range = (g_r_out.ymin, g_r_out.ymax)

        g_licon_u = c.add_ref(
            via_generator(
                x_range=(g_r_in.xmin + 0.17, g_r_in.xmax - 0.17),
                y_range=(g_r_in.ymax, g_r_out.ymax),
                via_enclosure=con_t_enc,
                via_layer=licon_layer,
                via_size=con_size,
                via_spacing=con_spacing,
            )
        )

        g_licon_d = c.add_ref(
            via_generator(
                x_range=(g_r_in.xmin + 0.17, g_r_in.xmax - 0.17),
                y_range=(g_r_out.ymin, g_r_in.ymin),
                via_enclosure=con_t_enc,
                via_layer=licon_layer,
                via_size=con_size,
                via_spacing=con_spacing,
            )
        )

        g_licon_l = c.add_ref(
            via_generator(
                x_range=(g_r_out.xmin, g_r_in.xmin),
                y_range=g_con_range,
                via_enclosure=con_t_enc,
                via_layer=licon_layer,
                via_size=con_size,
                via_spacing=con_spacing,
            )
        )

        g_licon_r = c.add_ref(
            via_generator(
                x_range=(g_r_in.xmax, g_r_out.xmax),
                y_range=g_con_range,
                via_enclosure=con_t_enc,
                via_layer=licon_layer,
                via_size=con_size,
                via_spacing=con_spacing,
            )
        )

    if type == "sky130_fd_pr__cap_var_hvt":
        hvtp = c_inst.add_ref(
            gf.components.rectangle(
                size=(l + 2 * hv_enc, w + 2 * hv_enc), layer=hvtp_layer
            )
        )
        hvtp.move((poly.xmin - hv_enc, tap.ymin - hv_enc))

    c.write_gds("cap_var_temp.gds")
    layout.read("cap_var_temp.gds")
    cell_name = "sky_cap_var_dev"

    return layout.cell(cell_name)


def draw_mim_cap(
    layout,
    type="sky130_fd_pr__model__cap_mim",
    l: float = 2,
    w: float = 2,
):

    """
    Retern mim cap

    Args:
        layout : layout object
        l : float of capm length
        w : float of capm width


    """

    c = gf.Component("sky_mim_cap_dev")

    # used dimensions and layers

    bottom_layer = m3_layer
    upper_layer = m4_layer
    lbl = m4_lbl
    via_layer = via3_layer
    via_size = (0.2, 0.2)
    via_enc = (0.09, 0.065)
    via_spacing = (0.2, 0.2)
    cap_layer = capm_layer
    cap_enc = 0.195
    m_dn_enc = 0.2
    m_up_spacing = 1.355
    m_up_w = 0.48

    if type == "sky130_fd_pr__model__cap_mim_m4":
        bottom_layer = m4_layer
        upper_layer = m5_layer
        lbl = m5_lbl
        via_layer = via4_layer
        via_size = (0.8, 0.8)
        via_enc = (0.31, 0.31)
        via_spacing = (0.8, 0.8)
        cap_layer = cap2m_layer
        cap_enc = 0.08
        m_dn_enc = 0.4
        m_up_spacing = 1.68
        m_up_w = 1.6

    side_enc = (0.02, 0.06)

    # drawing cap identifier and bottom , upper layers
    cap = c.add_ref(gf.components.rectangle(size=(w, l), layer=cap_layer))

    m_up1 = c.add_ref(
        gf.components.rectangle(
            size=(cap.xmax - cap.xmin - 2 * cap_enc, cap.ymax - cap.ymin - 2 * cap_enc),
            layer=upper_layer,
        )
    )
    m_up1.move((cap.xmin + cap_enc, cap.ymin + cap_enc))

    m_dn = c.add_ref(
        gf.components.rectangle(
            size=(
                m_dn_enc
                + cap_enc
                + m_up1.xmax
                - m_up1.xmin
                + m_up_spacing
                + m_up_w
                + side_enc[0],
                cap.ymax - cap.ymin + 2 * m_dn_enc,
            ),
            layer=bottom_layer,
        )
    )
    m_dn.move((cap.xmin - m_dn_enc, cap.ymin - m_dn_enc))

    m_up2 = c.add_ref(
        gf.components.rectangle(
            size=(m_up_w, m_dn.ymax - m_dn.ymin - 2 * side_enc[1]), layer=upper_layer
        )
    )
    m_up2.move((m_up1.xmax + m_up_spacing, m_dn.ymin + side_enc[1]))

    # generating vias

    via_1 = via_generator(
        x_range=(m_up1.xmin, m_up1.xmax),
        y_range=(m_up1.ymin, m_up1.ymax),
        via_enclosure=via_enc,
        via_layer=via_layer,
        via_size=via_size,
        via_spacing=via_spacing,
    )
    c.add_ref(via_1)

    via_2 = via_generator(
        x_range=(m_up2.xmin, m_up2.xmax),
        y_range=(m_up2.ymin, m_up2.ymax),
        via_enclosure=via_enc,
        via_layer=via_layer,
        via_size=via_size,
        via_spacing=via_spacing,
    )
    c.add_ref(via_2)

    c.write_gds("mim_cap_temp.gds")
    layout.read("mim_cap_temp.gds")
    cell_name = "sky_mim_cap_dev"

    return layout.cell(cell_name)
