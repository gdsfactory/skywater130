from math import ceil

import gdsfactory as gf
from gdsfactory.types import Float2, LayerSpec


@gf.cell
def npn_W1L1(
    E_width: float = 1,
    E_length: float = 1,
    B_width: float = 0.4,
    C_width: float = 0.4,
    np_spacing: float = 0.27,
    diffusion_layer: LayerSpec = (65, 20),
    tap_layer: LayerSpec = (65, 44),
    diff_enclosure: Float2 = (0.18, 0.18),
    contact_size: Float2 = (0.17, 0.17),
    contact_spacing: Float2 = (0.17, 0.17),
    contact_layer: LayerSpec = (66, 44),
    contact_enclosure: Float2 = (0.06, 0.06),
    pwell_layer: LayerSpec = (64, 13),
    dnwell_enclosure: Float2 = (0.4, 0.4),
    dnwell_layer: LayerSpec = (64, 18),
    sdm_enclosure: Float2 = (0.125, 0.125),
    nsdm_layer: LayerSpec = (93, 44),
    sdm_spacing: float = 0.13,
    psdm_layer: LayerSpec = (94, 20),
    npn_layer: LayerSpec = (82, 20),
    li_width: float = 0.17,
    li_spacing: float = 0.17,
    li_layer: LayerSpec = (67, 20),
    li_enclosure: float = 0.08,
    mcon_layer: LayerSpec = (67, 44),
    mcon_enclosure: Float2 = (0.09, 0.09),
    m1_layer: LayerSpec = (68, 20),
) -> gf.Component:
    """Return npn_W1L1.

    npn device with emitter size 1u*1u

    .. plot::
      :include-source:

      import sky130

      c = sky130.pcells.npn_W1L1(np_spacing=1, B_width=0.8, C_width=0.8, E_length=2)
      c.plot()
    """
    c = gf.Component()

    # generating Emitter

    rect_E = gf.components.rectangle(size=(E_width, E_length), layer=diffusion_layer)
    E = c.add_ref(rect_E)

    # generate its n+ implant
    rect_nme = gf.components.rectangle(
        size=(E_width + 2 * sdm_enclosure[0], E_length + 2 * sdm_enclosure[1]),
        layer=nsdm_layer,
    )
    nsdm_e = c.add_ref(rect_nme)
    nsdm_e.move((-sdm_enclosure[0], -sdm_enclosure[1]))

    # generate its contacts and local interconnects and mcon and metal1

    rect_c = gf.components.rectangle(size=contact_size, layer=contact_layer)

    nr_e = ceil(E_length / (contact_size[1] + contact_spacing[1]))
    nc_e = ceil(E_width / (contact_size[0] + contact_spacing[0]))

    if (
        E_width - nc_e * contact_size[0] - (nc_e - 1) * contact_spacing[0]
    ) / 2 < contact_enclosure[0]:
        nc_e -= 1

    if (
        E_length - nr_e * contact_size[1] - (nr_e - 1) * contact_spacing[1]
    ) / 2 < contact_enclosure[1]:
        nr_e -= 1

    rect_mc = gf.components.rectangle(size=contact_size, layer=mcon_layer)
    rect_c_mc = [rect_c, rect_mc]

    for i in rect_c_mc:
        con_sp = (
            contact_size[0] + contact_spacing[0],
            contact_size[1] + contact_spacing[1],
        )
        cont_e_arr = c.add_array(i, rows=nr_e, columns=nc_e, spacing=con_sp)
        cont_e_arr.movex(
            (E_width - nc_e * contact_size[0] - (nc_e - 1) * contact_spacing[0]) / 2
        )
        cont_e_arr.movey(
            (E_length - nr_e * contact_size[1] - (nr_e - 1) * contact_spacing[1]) / 2
        )

    rect_eli = gf.components.rectangle(
        size=(
            nc_e * contact_size[0] + (nc_e - 1) * contact_spacing[0] + 2 * li_enclosure,
            nr_e * contact_size[1] + (nr_e - 1) * contact_spacing[1] + 2 * li_enclosure,
        ),
        layer=li_layer,
    )
    # rect_eli = gf.components.rectangle(size = (nc_e*contact_size[0] + (nc_e -1)*contact_spacing[0] , nr_e*contact_size[1] + (nr_e-1)*contact_spacing[1] ), layer= li_layer)
    li_e = c.add_ref(rect_eli)
    li_e.movex(
        (
            E_width
            - nc_e * contact_size[0]
            - (nc_e - 1) * contact_spacing[0]
            - 2 * li_enclosure
        )
        / 2
    )
    li_e.movey(
        (
            E_length
            - nr_e * contact_size[1]
            - (nr_e - 1) * contact_spacing[1]
            - 2 * li_enclosure
        )
        / 2
    )

    rect_em1 = gf.components.rectangle(
        size=(
            nc_e * contact_size[0]
            + (nc_e - 1) * contact_spacing[0]
            + 2 * mcon_enclosure[0],
            nr_e * contact_size[1]
            + (nr_e - 1) * contact_spacing[1]
            + 2 * mcon_enclosure[1],
        ),
        layer=m1_layer,
    )
    m1_e = c.add_ref(rect_em1)
    m1_e.movex(
        (
            E_width
            - nc_e * contact_size[0]
            - (nc_e - 1) * contact_spacing[0]
            - 2 * mcon_enclosure[0]
        )
        / 2
    )
    m1_e.movey(
        (
            E_length
            - nr_e * contact_size[1]
            - (nr_e - 1) * contact_spacing[1]
            - 2 * mcon_enclosure[1]
        )
        / 2
    )

    # generating Base

    rect_B_in = gf.components.rectangle(
        size=(E_width + 2 * np_spacing, E_length + 2 * np_spacing), layer=tap_layer
    )
    rect_B_out = gf.components.rectangle(
        size=(
            E_width + 2 * np_spacing + 2 * B_width,
            E_length + 2 * np_spacing + 2 * B_width,
        ),
        layer=tap_layer,
    )
    c_B = gf.Component()
    c_B.add_ref(rect_E)

    B_in = c_B.add_ref(rect_B_in)
    B_out = c_B.add_ref(rect_B_out)

    B_in.connect("e1", destination=E.ports["e1"])
    B_in.movex(E_width + np_spacing)

    B_out.connect("e1", destination=E.ports["e1"])
    B_out.movex(E_width + np_spacing + B_width)

    c.add_ref(gf.geometry.boolean(A=B_out, B=B_in, operation="A-B", layer=tap_layer))

    # generate its p+ implants

    rect_pmB_in = gf.components.rectangle(
        size=(
            E_width + 2 * np_spacing - 2 * sdm_enclosure[0],
            E_length + 2 * np_spacing - 2 * sdm_enclosure[1],
        ),
        layer=psdm_layer,
    )
    rect_pmB_out = gf.components.rectangle(
        size=(
            E_width + 2 * np_spacing + 2 * B_width + 2 * sdm_enclosure[0],
            E_length + 2 * np_spacing + 2 * B_width + 2 * sdm_enclosure[1],
        ),
        layer=psdm_layer,
    )

    pmB_in = c_B.add_ref(rect_pmB_in)
    pmB_out = c_B.add_ref(rect_pmB_out)

    pmB_in.connect("e1", destination=E.ports["e1"])
    pmB_in.movex(E_width + np_spacing - sdm_enclosure[0])

    pmB_out.connect("e1", destination=E.ports["e1"])
    pmB_out.movex(E_width + np_spacing + B_width + sdm_enclosure[1])

    c.add_ref(
        gf.geometry.boolean(A=pmB_out, B=pmB_in, operation="A-B", layer=psdm_layer)
    )

    # generate its contacts and local interconnects and mcon and metal1

    nr = ceil((B_in.ymax - B_in.ymin) / (contact_size[1] + contact_spacing[1]))
    nc = ceil((B_width) / (contact_size[0] + contact_spacing[0]))

    if (
        (B_width - nc * contact_size[0] - (nc - 1) * contact_spacing[0]) / 2
    ) < contact_enclosure[0]:
        nc -= 1

    if (
        (B_in.ymax - B_in.ymin - nr * contact_size[1] - (nr - 1) * contact_spacing[1])
        / 2
    ) < contact_enclosure[1]:
        nr -= 1

    rect_layer = [li_layer, m1_layer]
    for i in range(2):
        rect_in = gf.components.rectangle(
            size=(
                E_width
                + 2 * np_spacing
                + (B_width - nc * contact_size[0] - (nc - 1) * contact_spacing[0])
                - 2 * i * mcon_enclosure[0]
                - 2 * (1 - i) * li_enclosure,
                E_length
                + 2 * np_spacing
                + (
                    (B_width - nc * contact_size[1] - (nc - 1) * contact_spacing[1])
                    - 2 * i * mcon_enclosure[1]
                    - 2 * (1 - i) * li_enclosure
                ),
            ),
            layer=rect_layer[i],
        )
        rect_out = gf.components.rectangle(
            size=(
                E_width
                + 2 * np_spacing
                + 2 * B_width
                - (B_width - nc * contact_size[0] - (nc - 1) * contact_spacing[0])
                + 2 * i * mcon_enclosure[0]
                + 2 * (1 - i) * li_enclosure,
                E_length
                + 2 * np_spacing
                + 2 * B_width
                - (B_width - nc * contact_size[1] - (nc - 1) * contact_spacing[1])
                + 2 * i * mcon_enclosure[1]
                + 2 * (1 - i) * li_enclosure,
            ),
            layer=rect_layer[i],
        )

        li_m1_b_in = c_B.add_ref(rect_in)
        li_m1_b_out = c_B.add_ref(rect_out)

        li_m1_b_in.connect("e1", destination=E.ports["e1"])
        li_m1_b_in.movex(
            (
                E_width
                + np_spacing
                + (B_width - nc * contact_size[0] - (nc - 1) * contact_spacing[0]) / 2
            )
            - i * mcon_enclosure[0]
            - (1 - i) * li_enclosure
        )

        li_m1_b_out.connect("e1", destination=E.ports["e1"])
        li_m1_b_out.movex(
            (
                E_width
                + np_spacing
                + B_width
                - ((B_width - nc * contact_size[0] - (nc - 1) * contact_spacing[0]) / 2)
                + i * mcon_enclosure[0]
            )
            + (1 - i) * li_enclosure
        )

        c.add_ref(
            gf.geometry.boolean(
                A=li_m1_b_out, B=li_m1_b_in, operation="A-B", layer=rect_layer[i]
            )
        )

    for i in rect_c_mc:

        nr_b = nr
        nc_b = nc

        cont_B_arr1 = c.add_array(
            i, rows=nr_b, columns=nc_b, spacing=con_sp
        )  # left side
        cont_B_arr1.move((-np_spacing - B_width, -np_spacing))
        cont_B_arr1.movex(
            (B_width - nc_b * contact_size[0] - (nc_b - 1) * contact_spacing[0]) / 2
        )
        cont_B_arr1.movey(
            (
                B_in.ymax
                - B_in.ymin
                - nr_b * contact_size[1]
                - (nr_b - 1) * contact_spacing[1]
            )
            / 2
        )

        cont_B_arr2 = c.add_array(
            i, rows=nr_b, columns=nc_b, spacing=con_sp
        )  # right side
        cont_B_arr2.move((E_width + np_spacing, -np_spacing))
        cont_B_arr2.movex(
            (B_width - nc_b * contact_size[0] - (nc_b - 1) * contact_spacing[0]) / 2
        )
        cont_B_arr2.movey(
            (
                B_in.ymax
                - B_in.ymin
                - nr_b * contact_size[1]
                - (nr_b - 1) * contact_spacing[1]
            )
            / 2
        )

        nr_b, nc_b = nc_b, nr_b
        cont_B_arr3 = c.add_array(
            i, rows=nr_b, columns=nc_b, spacing=con_sp
        )  # upper side
        cont_B_arr3.move((-np_spacing, E_length + np_spacing))
        cont_B_arr3.movex(
            (
                B_in.xmax
                - B_in.xmin
                - nc_b * contact_size[0]
                - (nc_b - 1) * contact_spacing[0]
            )
            / 2
        )
        cont_B_arr3.movey(
            (B_width - nr_b * contact_size[1] - (nr_b - 1) * contact_spacing[1]) / 2
        )

        cont_B_arr4 = c.add_array(
            i, rows=nr_b, columns=nc_b, spacing=con_sp
        )  # bottom side
        cont_B_arr4.move((-np_spacing, -np_spacing - B_width))
        cont_B_arr4.movex(
            (
                B_in.xmax
                - B_in.xmin
                - nc_b * contact_size[0]
                - (nc_b - 1) * contact_spacing[0]
            )
            / 2
        )
        cont_B_arr4.movey(
            (B_width - nr_b * contact_size[1] - (nr_b - 1) * contact_spacing[1]) / 2
        )

        cont_B_arrc1 = c.add_array(
            i, rows=nr_b, columns=nr_b, spacing=con_sp
        )  # corners
        cont_B_arrc1.move((-np_spacing - B_width, -np_spacing - B_width))
        cont_B_arrc1.move(
            (
                (B_width - nr_b * contact_size[0] - (nr_b - 1) * contact_spacing[0])
                / 2,
                (B_width - nr_b * contact_size[1] - (nr_b - 1) * contact_spacing[1])
                / 2,
            )
        )

        cont_B_arrc2 = c.add_array(i, rows=nr_b, columns=nr_b, spacing=con_sp)
        cont_B_arrc2.move((-np_spacing - B_width, E_length + np_spacing))
        cont_B_arrc2.move(
            (
                (B_width - nr_b * contact_size[0] - (nr_b - 1) * contact_spacing[0])
                / 2,
                (B_width - nr_b * contact_size[1] - (nr_b - 1) * contact_spacing[1])
                / 2,
            )
        )

        cont_B_arrc3 = c.add_array(i, rows=nr_b, columns=nr_b, spacing=con_sp)
        cont_B_arrc3.move((E_width + np_spacing, -np_spacing - B_width))
        cont_B_arrc3.move(
            (
                (B_width - nr_b * contact_size[0] - (nr_b - 1) * contact_spacing[0])
                / 2,
                (B_width - nr_b * contact_size[1] - (nr_b - 1) * contact_spacing[1])
                / 2,
            )
        )

        cont_B_arrc4 = c.add_array(i, rows=nr_b, columns=nr_b, spacing=con_sp)
        cont_B_arrc4.move((E_width + np_spacing, E_length + np_spacing))
        cont_B_arrc4.move(
            (
                (B_width - nr_b * contact_size[0] - (nr_b - 1) * contact_spacing[0])
                / 2,
                (B_width - nr_b * contact_size[1] - (nr_b - 1) * contact_spacing[1])
                / 2,
            )
        )

    # generating Collector

    rect_C_in = gf.components.rectangle(
        size=(
            E_width + 4.5 * np_spacing + 2 * B_width,
            E_length + 4.5 * np_spacing + 2 * B_width,
        ),
        layer=tap_layer,
    )
    rect_C_out = gf.components.rectangle(
        size=(
            E_width + 4.5 * np_spacing + 2 * B_width + 2 * C_width,
            E_length + 4.5 * np_spacing + 2 * B_width + 2 * C_width,
        ),
        layer=tap_layer,
    )
    c_C = gf.Component()
    c_C.add_ref(rect_E)

    C_in = c_C.add_ref(rect_C_in)
    C_out = c_C.add_ref(rect_C_out)

    C_in.connect("e1", destination=E.ports["e1"])
    C_in.movex(E_width + 2.25 * np_spacing + B_width)

    C_out.connect("e1", destination=E.ports["e1"])
    C_out.movex(E_width + 2.25 * np_spacing + B_width + C_width)

    c.add_ref(gf.geometry.boolean(A=C_out, B=C_in, operation="A-B", layer=tap_layer))

    # generate its n+ implants

    rect_nmC_in = gf.components.rectangle(
        size=(
            E_width + 4.5 * np_spacing + 2 * B_width - 2 * sdm_enclosure[0],
            E_length + 4.5 * np_spacing + 2 * B_width - 2 * sdm_enclosure[1],
        ),
        layer=nsdm_layer,
    )
    rect_nmC_out = gf.components.rectangle(
        size=(
            E_width
            + 4.5 * np_spacing
            + 2 * B_width
            + 2 * C_width
            + 2 * sdm_enclosure[0],
            E_length
            + 4.5 * np_spacing
            + 2 * B_width
            + 2 * C_width
            + 2 * sdm_enclosure[1],
        ),
        layer=nsdm_layer,
    )

    nmC_in = c_C.add_ref(rect_nmC_in)
    nmC_out = c_C.add_ref(rect_nmC_out)

    nmC_in.connect("e1", destination=E.ports["e1"])
    nmC_in.movex(E_width + 2.25 * np_spacing + B_width - sdm_enclosure[0])

    nmC_out.connect("e1", destination=E.ports["e1"])
    nmC_out.movex(E_width + 2.25 * np_spacing + B_width + C_width + sdm_enclosure[0])

    c.add_ref(
        gf.geometry.boolean(A=nmC_out, B=nmC_in, operation="A-B", layer=nsdm_layer)
    )

    # generate its contact and local interconnects
    nr = ceil((C_in.ymax - C_in.ymin) / (contact_size[1] + contact_spacing[1]))
    nc = ceil((C_width) / (contact_size[0] + contact_spacing[0]))

    if (
        (C_width - nc * contact_size[0] - (nc - 1) * contact_spacing[0]) / 2
    ) < contact_enclosure[0]:
        nc -= 1

    if (
        (C_in.ymax - C_in.ymin - nr * contact_size[1] - (nr - 1) * contact_spacing[1])
        / 2
    ) < contact_enclosure[1]:
        nr -= 1

    for i in range(2):

        rect_in = gf.components.rectangle(
            size=(
                E_width
                + 4.5 * np_spacing
                + 2 * B_width
                + (C_width - nc * contact_size[0] - (nc - 1) * contact_spacing[0])
                - 2 * i * mcon_enclosure[0]
                - 2 * (1 - i) * li_enclosure,
                E_length
                + 4.5 * np_spacing
                + 2 * B_width
                + (C_width - nc * contact_size[1] - (nc - 1) * contact_spacing[1])
                - 2 * i * mcon_enclosure[1]
                - 2 * (1 - i) * li_enclosure,
            ),
            layer=rect_layer[i],
        )

        rect_out = gf.components.rectangle(
            size=(
                E_width
                + 4.5 * np_spacing
                + 2 * B_width
                + 2 * C_width
                - (C_width - nc * contact_size[0] - (nc - 1) * contact_spacing[0])
                + 2 * i * mcon_enclosure[0]
                + 2 * (1 - i) * li_enclosure,
                E_length
                + 4.5 * np_spacing
                + 2 * B_width
                + 2 * C_width
                - (C_width - nc * contact_size[0] - (nc - 1) * contact_spacing[0])
                + 2 * i * mcon_enclosure[1]
                + 2 * (1 - i) * li_enclosure,
            ),
            layer=rect_layer[i],
        )

        li_m1_c_in = c_C.add_ref(rect_in)
        li_m1_c_out = c_C.add_ref(rect_out)

        li_m1_c_in.connect("e1", destination=E.ports["e1"])
        li_m1_c_in.movex(
            E_width
            + 2.25 * np_spacing
            + B_width
            + (C_width - nc * contact_size[0] - (nc - 1) * contact_spacing[0]) / 2
            - i * mcon_enclosure[0]
            - (1 - i) * li_enclosure
        )

        li_m1_c_out.connect("e1", destination=E.ports["e1"])
        li_m1_c_out.movex(
            E_width
            + 2.25 * np_spacing
            + B_width
            + C_width
            - (C_width - nc * contact_size[0] - (nc - 1) * contact_spacing[0]) / 2
            + i * mcon_enclosure[0]
            + (1 - i) * li_enclosure
        )

        c.add_ref(
            gf.geometry.boolean(
                A=li_m1_c_out, B=li_m1_c_in, operation="A-B", layer=rect_layer[i]
            )
        )

    for i in rect_c_mc:
        nr_c = nr
        nc_c = nc
        cont_C_arr1 = c.add_array(
            i, rows=nr_c, columns=nc_c, spacing=con_sp
        )  # left side
        cont_C_arr1.move(
            (-2.25 * np_spacing - B_width - C_width, -2.25 * np_spacing - B_width)
        )
        cont_C_arr1.movex(
            (C_width - nc_c * contact_size[0] - (nc_c - 1) * contact_spacing[0]) / 2
        )
        cont_C_arr1.movey(
            (
                C_in.ymax
                - C_in.ymin
                - nr_c * contact_size[1]
                - (nr_c - 1) * contact_spacing[1]
            )
            / 2
        )

        cont_C_arr2 = c.add_array(
            i, rows=nr_c, columns=nc_c, spacing=con_sp
        )  # right side
        cont_C_arr2.move(
            (E_width + 2.25 * np_spacing + B_width, -2.25 * np_spacing - B_width)
        )
        cont_C_arr2.movex(
            (C_width - nc_c * contact_size[0] - (nc_c - 1) * contact_spacing[0]) / 2
        )
        cont_C_arr2.movey(
            (
                C_in.ymax
                - C_in.ymin
                - nr_c * contact_size[1]
                - (nr_c - 1) * contact_spacing[1]
            )
            / 2
        )

        nr_c, nc_c = nc_c, nr_c
        cont_C_arr3 = c.add_array(
            i, rows=nr_c, columns=nc_c, spacing=con_sp
        )  # upper side
        cont_C_arr3.move(
            (-2.25 * np_spacing - B_width, E_length + 2.25 * np_spacing + B_width)
        )
        cont_C_arr3.movex(
            (
                C_in.xmax
                - C_in.xmin
                - nc_c * contact_size[0]
                - (nc_c - 1) * contact_spacing[0]
            )
            / 2
        )
        cont_C_arr3.movey(
            (C_width - nr_c * contact_size[1] - (nr_c - 1) * contact_spacing[1]) / 2
        )

        cont_C_arr4 = c.add_array(
            i, rows=nr_c, columns=nc_c, spacing=con_sp
        )  # bottom side
        cont_C_arr4.move(
            (-2.25 * np_spacing - B_width, -2.25 * np_spacing - B_width - C_width)
        )
        cont_C_arr4.movex(
            (
                C_in.xmax
                - C_in.xmin
                - nc_c * contact_size[0]
                - (nc_c - 1) * contact_spacing[0]
            )
            / 2
        )
        cont_C_arr4.movey(
            (C_width - nr_c * contact_size[1] - (nr_c - 1) * contact_spacing[1]) / 2
        )

        cont_C_arrc1 = c.add_array(
            i, rows=nr_c, columns=nr_c, spacing=con_sp
        )  # corners
        cont_C_arrc1.move(
            (
                -2.25 * np_spacing - B_width - C_width,
                -2.25 * np_spacing - B_width - C_width,
            )
        )
        cont_C_arrc1.move(
            (
                (C_width - nr_c * contact_size[0] - (nr_c - 1) * contact_spacing[0])
                / 2,
                (C_width - nr_c * contact_size[1] - (nr_c - 1) * contact_spacing[1])
                / 2,
            )
        )

        cont_C_arrc2 = c.add_array(
            i, rows=nr_c, columns=nr_c, spacing=con_sp
        )  # corners
        cont_C_arrc2.move(
            (
                -2.25 * np_spacing - B_width - C_width,
                E_length + 2.25 * np_spacing + B_width,
            )
        )
        cont_C_arrc2.move(
            (
                (C_width - nr_c * contact_size[0] - (nr_c - 1) * contact_spacing[0])
                / 2,
                (C_width - nr_c * contact_size[1] - (nr_c - 1) * contact_spacing[1])
                / 2,
            )
        )

        cont_C_arrc3 = c.add_array(
            i, rows=nr_c, columns=nr_c, spacing=con_sp
        )  # corners
        cont_C_arrc3.move(
            (
                E_width + 2.25 * np_spacing + B_width,
                E_length + 2.25 * np_spacing + B_width,
            )
        )
        cont_C_arrc3.move(
            (
                (C_width - nr_c * contact_size[0] - (nr_c - 1) * contact_spacing[0])
                / 2,
                (C_width - nr_c * contact_size[1] - (nr_c - 1) * contact_spacing[1])
                / 2,
            )
        )

        cont_C_arrc4 = c.add_array(
            i, rows=nr_c, columns=nr_c, spacing=con_sp
        )  # corners
        cont_C_arrc4.move(
            (
                E_width + 2.25 * np_spacing + B_width,
                -2.25 * np_spacing - B_width - C_width,
            )
        )
        cont_C_arrc4.move(
            (
                (C_width - nr_c * contact_size[0] - (nr_c - 1) * contact_spacing[0])
                / 2,
                (C_width - nr_c * contact_size[1] - (nr_c - 1) * contact_spacing[1])
                / 2,
            )
        )

    # generating pwell around E & B

    rect_pwell = gf.components.rectangle(
        size=(
            B_out.xmax - B_out.xmin + 2 * diff_enclosure[0],
            B_out.ymax - B_out.ymin + 2 * diff_enclosure[1],
        ),
        layer=pwell_layer,
    )
    pwell = c.add_ref(rect_pwell)
    pwell.connect("e1", destination=B_out.ports["e3"])
    pwell.movex(B_out.xmax - B_out.xmin + diff_enclosure[0])

    # generating deep nwell

    rect_dnw = gf.components.rectangle(
        size=(
            C_out.xmax - C_out.xmin + 2 * diff_enclosure[0],
            C_out.ymax - C_out.ymin + 2 * diff_enclosure[1],
        ),
        layer=dnwell_layer,
    )
    dnwell = c.add_ref(rect_dnw)
    dnwell.connect("e1", destination=C_out.ports["e3"])
    dnwell.movex(C_out.xmax - C_out.xmin + diff_enclosure[0])

    # generating npn identifier

    npn = c.add_ref(
        gf.components.rectangle(
            size=(C_out.xmax - C_out.xmin, C_out.ymax - C_out.ymin), layer=npn_layer
        )
    )
    npn.connect("e1", destination=C_out.ports["e3"])
    npn.movex(C_out.xmax - C_out.xmin)

    return c


if __name__ == "__main__":

    c = npn_W1L1()
    # c = npn_W1L1(np_spacing=1, B_width=0.8, C_width=0.8, E_length=2)
    c.show(show_ports=True)
