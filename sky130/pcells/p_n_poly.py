from math import ceil

import gdsfactory as gf
from gdsfactory.types import Float2, LayerSpec


@gf.cell
def p_n_poly(
    p_poly_width: float = 0.35,
    p_poly_length: float = 0.5,
    poly_res_layer: LayerSpec = (66, 13),
    poly_layer: LayerSpec = (66, 20),
    psdm_layer: LayerSpec = (94, 20),
    sdm_enclosure: Float2 = (0.125, 0.125),
    contact_size: Float2 = (0.17, 0.17),
    contact_spacing: Float2 = (0.17, 0.17),
    licon_slots_size: Float2 = (0.19, 2),
    licon_slots_spacing: Float2 = (0.51, 0.51),
    contact_layer: LayerSpec = (66, 44),
    contact_enclosure: Float2 = (0.06, 0.06),
    li_layer: LayerSpec = (67, 20),
    li_enclosure: float = 0.08,
    mcon_layer: LayerSpec = (67, 44),
    mcon_enclosure: Float2 = (0.09, 0.09),
    m1_layer: LayerSpec = (68, 20),
    urpm_layer: LayerSpec = (79, 20),
    urpm_min_width: float = 1.27,
    urpm_enclosure: Float2 = (0.2, 0.2),
    npc_layer: LayerSpec = (95, 20),
    npc_enclosure: Float2 = (0.095, 0.095),
) -> gf.Component:
    """Return p- poly resistor with sheet resistance of 2000 ohms/square.

    .. plot::
      :include-source:

      import sky130

      c = sky130.pcells.p_n_poly(p_poly_width= 5.73, p_poly_length=2)
      c.plot()
    """
    c = gf.Component()

    # generate poly res R1

    rect_r = gf.components.rectangle(
        size=(p_poly_width, p_poly_length), layer=poly_res_layer
    )
    c.add_ref(rect_r)

    # generate polysilicon R0
    p_length = licon_slots_size[1] + 2 * contact_enclosure[1]
    rect_p = gf.components.rectangle(
        size=(p_poly_width, p_poly_length + 2 * p_length), layer=poly_layer
    )
    R_0 = c.add_ref(rect_p)
    R_0.movey(-p_length)

    # generate contacts (licon )
    rect_lc = gf.components.rectangle(size=licon_slots_size, layer=contact_layer)

    # nr = ceil((p_length / (licon_slots_size[1]+licon_slots_spacing[1])))
    # if (p_length- nr*licon_slots_size[1] - (nr-1)*licon_slots_spacing[1])/2 < contact_enclosure[1] :
    #    nr-=1

    nc = ceil(p_poly_width / (licon_slots_size[0] + licon_slots_spacing[0]))
    if (
        p_poly_width - nc * licon_slots_size[0] - (nc - 1) * licon_slots_spacing[0]
    ) / 2 < contact_enclosure[0]:
        nc -= 1

    lic_sp = (
        licon_slots_size[0] + licon_slots_spacing[0],
        licon_slots_size[1] + licon_slots_spacing[1],
    )

    for i in range(2):
        cont_arr = c.add_array(rect_lc, rows=1, columns=nc, spacing=lic_sp)
        cont_arr.movex(
            (
                p_poly_width
                - nc * licon_slots_size[0]
                - (nc - 1) * licon_slots_spacing[0]
            )
            / 2
        )
        cont_arr.movey(
            i * (p_poly_length + (p_length - licon_slots_size[1]) / 2)
            - (1 - i) * (licon_slots_size[1] + (p_length - licon_slots_size[1]) / 2)
        )

    # generate li (local interconnects) and m1

    rect_layer = [m1_layer, li_layer]

    for i in range(2):
        rect_li_m1 = gf.components.rectangle(
            size=(
                p_poly_width + 2 * (1 - i) * (mcon_enclosure[0] - li_enclosure),
                licon_slots_size[1]
                + 2 * i * li_enclosure
                + 2 * (1 - i) * mcon_enclosure[1],
            ),
            layer=rect_layer[i],
        )

        li_m1 = c.add_array(
            rect_li_m1,
            rows=2,
            columns=1,
            spacing=(
                0,
                p_poly_length
                + 2 * contact_enclosure[1]
                + licon_slots_size[1]
                - (1 - i) * (mcon_enclosure[1] - li_enclosure),
            ),
        )
        li_m1.movey(
            -licon_slots_size[1]
            - contact_enclosure[1]
            - i * li_enclosure
            - (1 - i) * mcon_enclosure[1]
        )
        li_m1.movex((1 - i) * (-mcon_enclosure[0] + li_enclosure))

    # generate mcon

    rect_mc = gf.components.rectangle(size=contact_size, layer=mcon_layer)

    nr_m = ceil(
        (rect_li_m1.ymax - rect_li_m1.ymin) / (contact_size[1] + contact_spacing[1])
    )
    if (
        rect_li_m1.ymax
        - rect_li_m1.ymin
        - nr_m * contact_size[1]
        - (nr_m - 1) * contact_spacing[1]
    ) / 2 < contact_enclosure[1]:
        nr_m -= 1

    nc_m = ceil(
        (rect_li_m1.xmax - rect_li_m1.xmin) / (contact_size[0] + contact_spacing[0])
    )
    if (
        rect_li_m1.xmax
        - rect_li_m1.xmin
        - nc_m * contact_size[0]
        - (nc_m - 1) * contact_spacing[0]
    ) < contact_enclosure[0]:
        nc_m -= 1

    con_sp = (
        contact_size[0] + contact_spacing[0],
        contact_size[1] + contact_spacing[1],
    )

    for i in range(2):
        mcon_arr = c.add_array(rect_mc, rows=nr_m, columns=nc_m, spacing=con_sp)
        # mcon_arr.movex((p_poly_width - nc*licon_slots_size[0] - (nc-1)*licon_slots_spacing[0] - 2*li_enclosure )/2)
        mcon_arr.movey(
            (1 - i) * (-licon_slots_size[1] - contact_enclosure[1] - li_enclosure)
            + i * (p_poly_length)
        )
        mcon_arr.movex(
            (
                rect_li_m1.xmax
                - rect_li_m1.xmin
                - nc_m * contact_size[0]
                - (nc_m - 1) * contact_spacing[0]
            )
            / 2
        )
        mcon_arr.movey(
            (
                rect_li_m1.ymax
                - rect_li_m1.ymin
                - nr_m * contact_size[1]
                - (nr_m - 1) * contact_spacing[1]
            )
            / 2
        )

    # generate npc (nitride poly cut)

    rect_npc = gf.components.rectangle(
        size=(
            p_poly_width + 2 * npc_enclosure[0],
            p_poly_length + 2 * p_length + 2 * npc_enclosure[1],
        ),
        layer=npc_layer,
    )
    npc = c.add_ref(rect_npc)
    npc.connect("e1", destination=R_0.ports["e1"])
    npc.movex(p_poly_width + npc_enclosure[0])

    # generate rpm (poly resistor implant)
    if p_poly_width <= urpm_min_width:
        urpm_width = urpm_min_width + 2 * urpm_enclosure[0]
    else:
        urpm_width = p_poly_width + 2 * urpm_enclosure[0]

    urpm_length = p_poly_length + 2 * p_length + 2 * urpm_enclosure[1]

    rect_urpm = gf.components.rectangle(
        size=(urpm_width, urpm_length), layer=urpm_layer
    )
    urpm = c.add_ref(rect_urpm)
    urpm.connect("e1", destination=R_0.ports["e1"])
    urpm.movex(p_poly_width + ((urpm_width - p_poly_width) / 2))

    # generate p+ implants
    rect_psdm = gf.components.rectangle(
        size=(urpm_width + 2 * sdm_enclosure[0], urpm_length + 2 * sdm_enclosure[1]),
        layer=psdm_layer,
    )
    psdm = c.add_ref(rect_psdm)
    psdm.connect("e1", destination=urpm.ports["e3"])
    psdm.movex(urpm_width + sdm_enclosure[0])

    return c


if __name__ == "__main__":

    # c = p_n_poly(p_poly_width= 5.73, p_poly_length=2)
    c = p_n_poly()
    c.show(show_ports=True)
