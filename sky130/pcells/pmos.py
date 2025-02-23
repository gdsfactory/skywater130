from math import floor

import gdsfactory as gf
from gdsfactory.typings import Float2, LayerSpec


@gf.cell
def pmos(
    diffusion_layer: LayerSpec = (65, 20),
    poly_layer: LayerSpec = (66, 20),
    gate_width: float = 0.42,
    gate_length: float = 0.15,
    sd_width: float = 0.3,
    end_cap: float = 0.13,
    contact_size: Float2 = (0.17, 0.17),
    contact_spacing: Float2 = (0.17, 0.17),
    contact_layer: LayerSpec = (66, 44),
    contact_enclosure: Float2 = (0.06, 0.06),
    diff_spacing: float = 0.27,
    diff_enclosure: Float2 = (0.18, 0.18),
    diffn_layer: LayerSpec = (65, 44),
    nwell_layer: LayerSpec = (64, 20),
    dnwell_enclosure: Float2 = (0.4, 0.4),
    dnwell_layer: LayerSpec = (64, 18),
    nf: int = 1,
    sdm_enclosure: Float2 = (0.125, 0.125),
    nsdm_layer: LayerSpec = (93, 44),
    sdm_spacing: float = 0.13,
    psdm_layer: LayerSpec = (94, 20),
    li_width: float = 0.17,
    li_layer: LayerSpec = (67, 20),
    li_enclosure: float = 0.08,
    mcon_layer: LayerSpec = (67, 44),
    mcon_enclosure: Float2 = (0.03, 0.06),
    m1_layer: LayerSpec = (68, 20),
    npc_layer: LayerSpec = (95, 20),
    npc_spacing: float = 0.09,
) -> gf.Component:
    """Return PMOS.

    Args:
        diffusion_layer: spec.
        poly_layer: spec.
        gate_width: for poly.
        gate_length: for poly.
        sd_width: source drain length.
        end_cap : end cap length.
        contact_size : contact dimension (length and width)
        contact_layer : for contacts
        contact_enclosure : for contacts within diffusion or poly
        diff_spacing : for two adjacent diffusions
        diff_enclosure : for diffusion within well
        diffn_layer : for bulk tie
        dnwell layer : for deep nwell


    .. code::
                    _______
                    | poly |
           _________|      |_________  _
          | sd_width|      | sd_width| |
          |<------->|      |<------->| |gate_width
          |_________|      |_________| |
                    |  Lg  |
                    |<---->|
                    |______|


    .. plot::
      :include-source:

      import sky130

      c = sky130.pcells.pmos()
      c.plot()
    """

    c = gf.Component()

    # generating poly and p+ diffusion
    w_p = end_cap + gate_width + end_cap  # poly total width
    rect_p = gf.components.rectangle(size=(gate_length, w_p), layer=poly_layer)

    # adding fingers
    # poly = c.add_ref(rect_p)
    poly = c.add_ref(rect_p, columns=nf, column_pitch=sd_width + gate_length)

    l_d = (nf + 1) * (sd_width + gate_length) - gate_length  # n diffution total length
    rect_d = gf.components.rectangle(size=(l_d, gate_width), layer=diffusion_layer)
    diff_p = c.add_ref(rect_d)

    poly.dmovex(sd_width)
    poly.dmovey(-end_cap)

    # generating p+ implant
    rect_pm = gf.components.rectangle(
        size=(l_d + 2 * sdm_enclosure[0], gate_width + 2 * sdm_enclosure[1]),
        layer=psdm_layer,
    )
    psdm = c.add_ref(rect_pm)
    psdm.dmovex(-sdm_enclosure[0])
    psdm.dmovey(-sdm_enclosure[1])

    # generating contacts and local interconnect and mcon and m1 of p+ diffusion
    rect_c = gf.components.rectangle(size=contact_size, layer=contact_layer)
    rect_mc = gf.components.rectangle(size=contact_size, layer=mcon_layer)

    nr = floor(gate_width / (2 * contact_size[1]))
    nc = floor(sd_width / (2 * contact_size[0]))

    con_sp = list(contact_spacing)
    con_sp[0] = con_sp[1] = contact_spacing[0] + contact_size[0]

    min_gate_wid = 0.42

    cont_arr1 = c.add_ref(
        rect_c, rows=nr, columns=nc, column_pitch=con_sp[0], row_pitch=con_sp[1]
    )
    cont_arr2 = c.add_ref(
        rect_c, rows=nr, columns=nc, column_pitch=con_sp[0], row_pitch=con_sp[1]
    )

    cont_arr1.dmovey((min_gate_wid - contact_size[1]) / 2)
    cont_arr2.dmovey((min_gate_wid - contact_size[1]) / 2)

    mcont_arr1 = c.add_ref(
        rect_mc, rows=nr, columns=nc, column_pitch=con_sp[0], row_pitch=con_sp[1]
    )
    mcont_arr2 = c.add_ref(
        rect_mc, rows=nr, columns=nc, column_pitch=con_sp[0], row_pitch=con_sp[1]
    )

    mcont_arr1.dmovey((min_gate_wid - contact_size[1]) / 2)
    mcont_arr2.dmovey((min_gate_wid - contact_size[1]) / 2)

    rect_lid = gf.components.rectangle(
        size=(li_width, gate_width + li_enclosure), layer=li_layer
    )
    li1 = c.add_ref(
        rect_lid, rows=1, columns=nc, column_pitch=con_sp[0], row_pitch=con_sp[1]
    )
    li2 = c.add_ref(
        rect_lid, rows=1, columns=nc, column_pitch=con_sp[0], row_pitch=con_sp[1]
    )

    rect_m1d = gf.components.rectangle(
        size=(contact_size[0] + 2 * mcon_enclosure[0], gate_width), layer=m1_layer
    )
    m1d1 = c.add_ref(
        rect_m1d, rows=1, columns=nc, column_pitch=con_sp[0], row_pitch=con_sp[1]
    )
    m1d2 = c.add_ref(
        rect_m1d, rows=1, columns=nc, column_pitch=con_sp[0], row_pitch=con_sp[1]
    )

    if nc > 1:
        cont_arr1.dmovex((sd_width - (cont_arr1.dxmax - cont_arr1.dxmin)) / 2)
        cont_arr2.dmovex(
            (nf * (sd_width + gate_length))
            + ((sd_width - (cont_arr2.dxmax - cont_arr2.dxmin)) / 2)
        )
        mcont_arr1.dmovex((sd_width - (cont_arr1.dxmax - cont_arr1.dxmin)) / 2)
        mcont_arr2.dmovex(
            (nf * (sd_width + gate_length))
            + ((sd_width - (cont_arr2.dxmax - cont_arr2.dxmin)) / 2)
        )
        li1.dmovex((sd_width - (cont_arr1.dxmax - cont_arr1.dxmin)) / 2)
        li2.dmovex(
            (nf * (sd_width + gate_length))
            + ((sd_width - (cont_arr2.dxmax - cont_arr2.dxmin)) / 2)
        )
        m1d1.dmovex(
            (sd_width - (cont_arr1.dxmax - cont_arr1.dxmin)) / 2 - mcon_enclosure[0]
        )
        m1d2.dmovex(
            (nf * (sd_width + gate_length))
            + ((sd_width - (cont_arr2.dxmax - cont_arr2.dxmin)) / 2)
            - mcon_enclosure[0]
        )
    else:
        cont_arr1.dmovex((sd_width - contact_size[0]) / 2)
        cont_arr2.dmovex(
            (nf * (sd_width + gate_length)) + ((sd_width - contact_size[0]) / 2)
        )
        mcont_arr1.dmovex((sd_width - contact_size[0]) / 2)
        mcont_arr2.dmovex(
            (nf * (sd_width + gate_length)) + ((sd_width - contact_size[0]) / 2)
        )
        li1.dmovex((sd_width - contact_size[0]) / 2)
        li2.dmovex((nf * (sd_width + gate_length)) + ((sd_width - contact_size[0]) / 2))
        m1d1.dmovex((sd_width - contact_size[0]) / 2 - mcon_enclosure[0])
        m1d2.dmovex(
            (nf * (sd_width + gate_length))
            + ((sd_width - contact_size[0]) / 2)
            - mcon_enclosure[0]
        )

    li1.dmovey(-li_enclosure / 2)
    li2.dmovey(-li_enclosure / 2)

    # generating contacts and local interconnects  and mcon and m1 of poly

    if gate_length <= contact_size[0]:
        pc_x = contact_enclosure[0] + contact_size[0] + contact_enclosure[0]
        cont_p = c.add_ref(
            rect_c, rows=1, columns=nf, column_pitch=sd_width + gate_length
        )
        cont_p.dmovex(sd_width - ((pc_x - gate_length) / 2) + contact_enclosure[0])
        cont_p.dmovey(gate_width + end_cap + contact_enclosure[1])
        cont_p2 = c.add_ref(
            rect_c, rows=1, columns=nf, column_pitch=sd_width + gate_length
        )
        cont_p2.dmovex(sd_width - ((pc_x - gate_length) / 2) + contact_enclosure[0])
        cont_p2.dmovey(-end_cap - contact_enclosure[1] - contact_size[1])

        mcont_p = c.add_ref(
            rect_mc, rows=1, columns=nf, column_pitch=sd_width + gate_length
        )
        mcont_p.dmovex(sd_width - ((pc_x - gate_length) / 2) + contact_enclosure[0])
        mcont_p.dmovey(gate_width + end_cap + contact_enclosure[1])
        mcont_p2 = c.add_ref(
            rect_mc, rows=1, columns=nf, column_pitch=sd_width + gate_length
        )
        mcont_p2.dmovex(sd_width - ((pc_x - gate_length) / 2) + contact_enclosure[0])
        mcont_p2.dmovey(-end_cap - contact_enclosure[1] - contact_size[1])

    else:
        pc_x = gate_length
        nc_p = floor(pc_x / (2 * contact_size[0]))
        for i in range(nf):
            cont_arr3 = c.add_ref(
                rect_c,
                rows=1,
                columns=nc_p,
                column_pitch=con_sp[0],
                row_pitch=con_sp[1],
            )
            cont_arr3.dmovex(
                sd_width
                + ((gate_length - (cont_arr3.dxmax - cont_arr3.dxmin)) / 2)
                + (i * (gate_length + sd_width))
            )
            cont_arr3.dmovey(gate_width + end_cap + contact_enclosure[1])
            cont_arr5 = c.add_ref(
                rect_c,
                rows=1,
                columns=nc_p,
                column_pitch=con_sp[0],
                row_pitch=con_sp[1],
            )
            cont_arr5.dmovex(
                sd_width
                + ((gate_length - (cont_arr5.dxmax - cont_arr5.dxmin)) / 2)
                + (i * (gate_length + sd_width))
            )
            cont_arr5.dmovey(-contact_size[1] - end_cap - contact_enclosure[1])

            mcont_arr3 = c.add_ref(
                rect_mc,
                rows=1,
                columns=nc_p,
                column_pitch=con_sp[0],
                row_pitch=con_sp[1],
            )
            mcont_arr3.dmovex(
                sd_width
                + ((gate_length - (cont_arr3.dxmax - cont_arr3.dxmin)) / 2)
                + (i * (gate_length + sd_width))
            )
            mcont_arr3.dmovey(gate_width + end_cap + contact_enclosure[1])
            mcont_arr5 = c.add_ref(
                rect_mc,
                rows=1,
                columns=nc_p,
                column_pitch=con_sp[0],
                row_pitch=con_sp[1],
            )
            mcont_arr5.dmovex(
                sd_width
                + ((gate_length - (cont_arr5.dxmax - cont_arr5.dxmin)) / 2)
                + (i * (gate_length + sd_width))
            )
            mcont_arr5.dmovey(-contact_size[1] - end_cap - contact_enclosure[1])

    pc_size = (
        pc_x,
        contact_enclosure[1] + contact_size[1] + contact_enclosure[1],
    )  # poly size to contain contact
    rect_pc = gf.components.rectangle(size=pc_size, layer=poly_layer)
    rect_m1p = gf.components.rectangle(
        size=(
            pc_x + 2 * mcon_enclosure[0] - 2 * contact_enclosure[0],
            contact_size[1] + 2 * mcon_enclosure[1],
        ),
        layer=m1_layer,
    )

    pc_u = c.add_ref(rect_pc, rows=1, columns=nf, column_pitch=sd_width + gate_length)
    pc_u.dmovex(sd_width - ((pc_x - gate_length) / 2))
    pc_u.dmovey(gate_width + end_cap)

    pc_d = c.add_ref(rect_pc, rows=1, columns=nf, column_pitch=sd_width + gate_length)
    pc_d.dmovex(sd_width - ((pc_x - gate_length) / 2))
    pc_d.dmovey(-pc_size[1] - end_cap)

    m1p_u = c.add_ref(rect_m1p, rows=1, columns=nf, column_pitch=sd_width + gate_length)
    m1p_u.dmovex(
        sd_width - ((pc_x - gate_length) / 2) + contact_enclosure[0] - mcon_enclosure[0]
    )
    m1p_u.dmovey(gate_width + end_cap + contact_enclosure[1] - mcon_enclosure[1])

    m1p_d = c.add_ref(rect_m1p, rows=1, columns=nf, column_pitch=sd_width + gate_length)
    m1p_d.dmovex(
        sd_width - ((pc_x - gate_length) / 2) + contact_enclosure[0] - mcon_enclosure[0]
    )
    m1p_d.dmovey(-pc_size[1] - end_cap + contact_enclosure[1] - contact_enclosure[1])

    rect_lip = gf.components.rectangle(
        size=(pc_size[0] + li_enclosure, li_width), layer=li_layer
    )
    lip_u = c.add_ref(rect_lip, rows=1, columns=nf, column_pitch=sd_width + gate_length)
    lip_u.dmovex(sd_width - ((pc_x - gate_length) / 2) - li_enclosure / 2)
    lip_u.dmovey(gate_width + end_cap + contact_enclosure[1])

    lip_d = c.add_ref(rect_lip, rows=1, columns=nf, column_pitch=sd_width + gate_length)
    lip_d.dmovex(sd_width - ((pc_x - gate_length) / 2) - li_enclosure / 2)
    lip_d.dmovey(-pc_size[1] - end_cap + contact_enclosure[1])

    # generating npc for poly contacts

    npc_en = end_cap - npc_spacing
    rect_npc = gf.components.rectangle(
        size=(pc_size[0] + npc_en, pc_size[1] + npc_en), layer=npc_layer
    )

    npc_u = c.add_ref(rect_npc, rows=1, columns=nf, column_pitch=sd_width + gate_length)
    npc_u.dmovex(sd_width - ((pc_x - gate_length) / 2) - npc_en / 2)
    npc_u.dmovey(gate_width + npc_spacing + npc_en / 2)

    npc_d = c.add_ref(rect_npc, rows=1, columns=nf, column_pitch=sd_width + gate_length)
    npc_d.dmovex(sd_width - ((pc_x - gate_length) / 2) - npc_en / 2)
    npc_d.dmovey(-pc_size[1] - npc_en - npc_spacing - npc_en / 2)

    # generaing n+ bulk tie and its contact and mcon and m1
    rect_dn = gf.components.rectangle(size=(sd_width, gate_width), layer=diffn_layer)
    diff_n = c.add_ref(rect_dn)
    diff_n.connect(
        "e1", diff_p.ports["e3"], allow_layer_mismatch=True, allow_width_mismatch=True
    )
    diff_n.dmovex(diff_spacing + sdm_spacing)

    cont_arr4 = c.add_ref(
        rect_c, rows=nr, columns=nc, column_pitch=con_sp[0], row_pitch=con_sp[1]
    )
    cont_arr4.dmovey((min_gate_wid - contact_size[1]) / 2)

    mcont_arr4 = c.add_ref(
        rect_mc, rows=nr, columns=nc, column_pitch=con_sp[0], row_pitch=con_sp[1]
    )
    mcont_arr4.dmovey((min_gate_wid - contact_size[1]) / 2)

    rect_m1dn = gf.components.rectangle(
        size=(contact_size[0] + 2 * mcon_enclosure[0], gate_width), layer=m1_layer
    )
    m1dn = c.add_ref(
        rect_m1dn, rows=1, columns=nc, column_pitch=con_sp[0], row_pitch=con_sp[1]
    )

    # generate its local interconnects
    li4 = c.add_ref(
        rect_lid, rows=1, columns=nc, column_pitch=con_sp[0], row_pitch=con_sp[1]
    )

    if nc > 1:
        cont_arr4.dmovex(
            l_d
            + diff_spacing
            + sdm_spacing
            + ((sd_width - (cont_arr4.dxmax - cont_arr4.dxmin)) / 2)
        )
        mcont_arr4.dmovex(
            l_d
            + diff_spacing
            + sdm_spacing
            + ((sd_width - (cont_arr4.dxmax - cont_arr4.dxmin)) / 2)
        )
        li4.dmovex(
            l_d
            + diff_spacing
            + sdm_spacing
            + ((sd_width - (cont_arr4.dxmax - cont_arr4.dxmin)) / 2)
        )
        m1dn.dmovex(
            l_d
            + diff_spacing
            + sdm_spacing
            + ((sd_width - (cont_arr4.dxmax - cont_arr4.dxmin)) / 2)
            - mcon_enclosure[0]
        )
    else:
        cont_arr4.dmovex(
            l_d + diff_spacing + sdm_spacing + ((sd_width - contact_size[0]) / 2)
        )
        mcont_arr4.dmovex(
            l_d + diff_spacing + sdm_spacing + ((sd_width - contact_size[0]) / 2)
        )
        li4.dmovex(
            l_d + diff_spacing + sdm_spacing + ((sd_width - contact_size[0]) / 2)
        )
        m1dn.dmovex(
            l_d
            + diff_spacing
            + sdm_spacing
            + ((sd_width - contact_size[0]) / 2)
            - mcon_enclosure[0]
        )

    li4.dmovey(-li_enclosure / 2)

    # generating n+ implant for bulk tie
    rect_nm = gf.components.rectangle(
        size=(sd_width + 2 * sdm_enclosure[0], gate_width + 2 * sdm_enclosure[1]),
        layer=nsdm_layer,
    )
    nsdm = c.add_ref(rect_nm)
    nsdm.connect(
        "e1", diff_p.ports["e3"], allow_layer_mismatch=True, allow_width_mismatch=True
    )
    nsdm.dmovex(diff_spacing + sdm_spacing - sdm_enclosure[0])

    # generating nwell
    rect_nw = gf.components.rectangle(
        size=(
            2 * diff_enclosure[0] + l_d + diff_spacing + sdm_spacing + sd_width,
            2 * diff_enclosure[1] + gate_width,
        ),
        layer=nwell_layer,
    )
    nwell = c.add_ref(rect_nw)
    nwell.dmovex(-diff_enclosure[0])
    nwell.dmovey(-diff_enclosure[1])

    # generating deep nwell
    rect_dnw = gf.components.rectangle(
        size=(
            rect_nw.dxmax - rect_nw.dxmin + 2 * dnwell_enclosure[0],
            rect_nw.dymax - rect_nw.dymin + 2 * dnwell_enclosure[1],
        ),
        layer=dnwell_layer,
    )
    dnwell = c.add_ref(rect_dnw)
    dnwell.dmovex(-diff_enclosure[0] - dnwell_enclosure[0])
    dnwell.dmovey(-diff_enclosure[1] - dnwell_enclosure[1])
    return c


if __name__ == "__main__":
    # c = pmos(gate_length= 2, gate_width=10, sd_width=5)
    c = pmos()
    c.show()
