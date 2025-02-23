from math import ceil

import gdsfactory as gf
from gdsfactory.typings import Float2, LayerSpec


@gf.cell
def pnp(
    E_width: float = 0.68,
    E_length: float = 0.68,
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
    nwell_layer: LayerSpec = (64, 20),
    sdm_enclosure: Float2 = (0.125, 0.125),
    nsdm_layer: LayerSpec = (93, 44),
    psdm_layer: LayerSpec = (94, 20),
    pnp_layer: LayerSpec = (82, 44),
    li_layer: LayerSpec = (67, 20),
    li_enclosure: float = 0.08,
    mcon_layer: LayerSpec = (67, 44),
    mcon_enclosure: Float2 = (0.09, 0.09),
    m1_layer: LayerSpec = (68, 20),
) -> gf.Component:
    """Return pnp.

    Args:
        E_width: Emitter width.
        E_length: Emitter length.
        B_width: Base width.
        C_width: Collector width.
        np_spacing: Spacing between N+ and P+ implants.
        diffusion_layer: Layer for the diffusion.
        tap_layer: Layer for the tap.
        diff_enclosure: Enclosure for the diffusion.
        contact_size: Contact size.
        contact_spacing: Contact spacing.
        contact_layer: Layer for the contact.
        contact_enclosure: Enclosure for the contact.
        nwell_layer: Layer for the nwell.
        sdm_enclosure: Enclosure for the source/drain implants.
        nsdm_layer: Layer for the n+ source/drain implants.
        psdm_layer: Layer for the p+ source/drain implants.
        pnp_layer: Layer for the pnp.
        li_layer: Layer for the local interconnect.
        li_enclosure: Enclosure for the local interconnect.
        mcon_layer: Layer for the mcon.
        mcon_enclosure: Enclosure for the mcon.
        m1_layer: Layer for the metal1.

    .. plot::
      :include-source:

      import sky130

      c = sky130.pcells.pnp(E_length=3.4, E_width=3.4, np_spacing=1, B_width=1, C_width=1)
      c.plot()
    """
    c = gf.Component()

    # generating Emitter

    rect_E = gf.components.rectangle(size=(E_width, E_length), layer=diffusion_layer)
    E = c.add_ref(rect_E)

    # generate its p+ implant
    rect_pme = gf.components.rectangle(
        size=(E_width + 2 * sdm_enclosure[0], E_length + 2 * sdm_enclosure[1]),
        layer=psdm_layer,
    )
    psdm_e = c.add_ref(rect_pme)
    psdm_e.dmove((-sdm_enclosure[0], -sdm_enclosure[1]))

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
        cont_e_arr = c.add_ref(
            i, rows=nr_e, columns=nc_e, column_pitch=con_sp[0], row_pitch=con_sp[1]
        )
        cont_e_arr.dmovex(
            (E_width - nc_e * contact_size[0] - (nc_e - 1) * contact_spacing[0]) / 2
        )
        cont_e_arr.dmovey(
            (E_length - nr_e * contact_size[1] - (nr_e - 1) * contact_spacing[1]) / 2
        )

    rect_layer = [li_layer, m1_layer]
    for i in range(2):
        rect_eli_m1 = gf.components.rectangle(
            size=(
                nc_e * contact_size[0]
                + (nc_e - 1) * contact_spacing[0]
                + 2 * (1 - i) * li_enclosure
                + 2 * i * mcon_enclosure[0],
                nr_e * contact_size[1]
                + (nr_e - 1) * contact_spacing[1]
                + 2 * (1 - i) * li_enclosure
                + 2 * i * mcon_enclosure[1],
            ),
            layer=rect_layer[i],
        )
        li_m1_e = c.add_ref(rect_eli_m1)
        li_m1_e.dmovex(
            (
                E_width
                - nc_e * contact_size[0]
                - (nc_e - 1) * contact_spacing[0]
                - 2 * (1 - i) * li_enclosure
                - 2 * i * mcon_enclosure[0]
            )
            / 2
        )
        li_m1_e.dmovey(
            (
                E_length
                - nr_e * contact_size[1]
                - (nr_e - 1) * contact_spacing[1]
                - 2 * (1 - i) * li_enclosure
                - 2 * i * mcon_enclosure[1]
            )
            / 2
        )

    # generating base

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

    B_in.connect(
        "e1", E.ports["e1"], allow_layer_mismatch=True, allow_width_mismatch=True
    )
    B_in.dmovex(E_width + np_spacing)

    B_out.connect(
        "e1", E.ports["e1"], allow_layer_mismatch=True, allow_width_mismatch=True
    )
    B_out.dmovex(E_width + np_spacing + B_width)

    c.add_ref(gf.boolean(A=B_out, B=B_in, operation="not", layer=tap_layer))

    # generate its n+ implants

    rect_nmB_in = gf.components.rectangle(
        size=(
            E_width + 2 * np_spacing - 2 * sdm_enclosure[0],
            E_length + 2 * np_spacing - 2 * sdm_enclosure[1],
        ),
        layer=nsdm_layer,
    )
    rect_nmB_out = gf.components.rectangle(
        size=(
            E_width + 2 * np_spacing + 2 * B_width + 2 * sdm_enclosure[0],
            E_length + 2 * np_spacing + 2 * B_width + 2 * sdm_enclosure[1],
        ),
        layer=nsdm_layer,
    )

    nmB_in = c_B.add_ref(rect_nmB_in)
    nmB_out = c_B.add_ref(rect_nmB_out)

    nmB_in.connect(
        "e1", E.ports["e1"], allow_layer_mismatch=True, allow_width_mismatch=True
    )
    nmB_in.dmovex(E_width + np_spacing - sdm_enclosure[0])

    nmB_out.connect(
        "e1", E.ports["e1"], allow_layer_mismatch=True, allow_width_mismatch=True
    )
    nmB_out.dmovex(E_width + np_spacing + B_width + sdm_enclosure[1])

    c.add_ref(gf.boolean(A=nmB_out, B=nmB_in, operation="not", layer=nsdm_layer))

    # generate its contacts and local interconnects and mcon and metal1

    nr_v = ceil((B_in.dymax - B_in.dymin) / (contact_size[1] + contact_spacing[1]))
    nc_v = ceil((B_width) / (contact_size[0] + contact_spacing[0]))

    if (
        (B_width - nc_v * contact_size[0] - (nc_v - 1) * contact_spacing[0]) / 2
    ) < contact_enclosure[0]:
        nc_v -= 1

    if (
        (
            B_in.dymax
            - B_in.dymin
            - nr_v * contact_size[1]
            - (nr_v - 1) * contact_spacing[1]
        )
        / 2
    ) < contact_enclosure[1]:
        nr_v -= 1

    nc_h = ceil((B_in.dxmax - B_in.dxmin) / (contact_size[0] + contact_spacing[0]))
    nr_h = ceil((B_width) / (contact_size[1] + contact_spacing[1]))

    if (
        (B_width - nr_h * contact_size[0] - (nr_h - 1) * contact_spacing[0]) / 2
    ) < contact_enclosure[0]:
        nr_h -= 1

    if (
        (
            B_in.dxmax
            - B_in.dxmin
            - nc_h * contact_size[1]
            - (nc_h - 1) * contact_spacing[1]
        )
        / 2
    ) < contact_enclosure[1]:
        nc_h -= 1

    for i in range(2):
        rect_in = gf.components.rectangle(
            size=(
                E_width
                + 2 * np_spacing
                + (B_width - nc_v * contact_size[0] - (nc_v - 1) * contact_spacing[0])
                - 2 * i * mcon_enclosure[0]
                - 2 * (1 - i) * li_enclosure,
                E_length
                + 2 * np_spacing
                + (
                    (B_width - nr_h * contact_size[1] - (nr_h - 1) * contact_spacing[1])
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
                - (B_width - nc_v * contact_size[0] - (nc_v - 1) * contact_spacing[0])
                + 2 * i * mcon_enclosure[0]
                + 2 * (1 - i) * li_enclosure,
                E_length
                + 2 * np_spacing
                + 2 * B_width
                - (B_width - nr_h * contact_size[1] - (nr_h - 1) * contact_spacing[1])
                + 2 * i * mcon_enclosure[1]
                + 2 * (1 - i) * li_enclosure,
            ),
            layer=rect_layer[i],
        )

        li_m1_b_in = c_B.add_ref(rect_in)
        li_m1_b_out = c_B.add_ref(rect_out)

        li_m1_b_in.connect(
            "e1", E.ports["e1"], allow_layer_mismatch=True, allow_width_mismatch=True
        )
        li_m1_b_in.dmovex(
            (
                E_width
                + np_spacing
                + (B_width - nc_v * contact_size[0] - (nc_v - 1) * contact_spacing[0])
                / 2
            )
            - i * mcon_enclosure[0]
            - (1 - i) * li_enclosure
        )

        li_m1_b_out.connect(
            "e1", E.ports["e1"], allow_layer_mismatch=True, allow_width_mismatch=True
        )
        li_m1_b_out.dmovex(
            (
                E_width
                + np_spacing
                + B_width
                - (
                    (B_width - nc_v * contact_size[0] - (nc_v - 1) * contact_spacing[0])
                    / 2
                )
                + i * mcon_enclosure[0]
            )
            + (1 - i) * li_enclosure
        )

        c.add_ref(
            gf.boolean(
                A=li_m1_b_out, B=li_m1_b_in, operation="not", layer=rect_layer[i]
            )
        )

    for i in rect_c_mc:
        cont_B_arr1 = c.add_ref(
            i, rows=nr_v, columns=nc_v, column_pitch=con_sp[0], row_pitch=con_sp[1]
        )  # left side
        cont_B_arr1.dmove((-np_spacing - B_width, -np_spacing))
        cont_B_arr1.dmovex(
            (B_width - nc_v * contact_size[0] - (nc_v - 1) * contact_spacing[0]) / 2
        )
        cont_B_arr1.dmovey(
            (
                B_in.dymax
                - B_in.dymin
                - nr_v * contact_size[1]
                - (nr_v - 1) * contact_spacing[1]
            )
            / 2
        )

        cont_B_arr2 = c.add_ref(
            i, rows=nr_v, columns=nc_v, column_pitch=con_sp[0], row_pitch=con_sp[1]
        )  # right side
        cont_B_arr2.dmove((E_width + np_spacing, -np_spacing))
        cont_B_arr2.dmovex(
            (B_width - nc_v * contact_size[0] - (nc_v - 1) * contact_spacing[0]) / 2
        )
        cont_B_arr2.dmovey(
            (
                B_in.dymax
                - B_in.dymin
                - nr_v * contact_size[1]
                - (nr_v - 1) * contact_spacing[1]
            )
            / 2
        )

        cont_B_arr3 = c.add_ref(
            i, rows=nr_h, columns=nc_h, column_pitch=con_sp[0], row_pitch=con_sp[1]
        )  # upper side
        cont_B_arr3.dmove((-np_spacing, E_length + np_spacing))
        cont_B_arr3.dmovex(
            (
                B_in.dxmax
                - B_in.dxmin
                - nc_h * contact_size[0]
                - (nc_h - 1) * contact_spacing[0]
            )
            / 2
        )
        cont_B_arr3.dmovey(
            (B_width - nr_h * contact_size[1] - (nr_h - 1) * contact_spacing[1]) / 2
        )

        cont_B_arr4 = c.add_ref(
            i, rows=nr_h, columns=nc_h, column_pitch=con_sp[0], row_pitch=con_sp[1]
        )  # bottom side
        cont_B_arr4.dmove((-np_spacing, -np_spacing - B_width))
        cont_B_arr4.dmovex(
            (
                B_in.dxmax
                - B_in.dxmin
                - nc_h * contact_size[0]
                - (nc_h - 1) * contact_spacing[0]
            )
            / 2
        )
        cont_B_arr4.dmovey(
            (B_width - nr_h * contact_size[1] - (nr_h - 1) * contact_spacing[1]) / 2
        )

        cont_B_arrc1 = c.add_ref(
            i, rows=nr_h, columns=nc_v, column_pitch=con_sp[0], row_pitch=con_sp[1]
        )  # corners
        cont_B_arrc1.dmove((-np_spacing - B_width, -np_spacing - B_width))
        cont_B_arrc1.dmove(
            (
                (B_width - nc_v * contact_size[0] - (nc_v - 1) * contact_spacing[0])
                / 2,
                (B_width - nr_h * contact_size[1] - (nr_h - 1) * contact_spacing[1])
                / 2,
            )
        )

        cont_B_arrc2 = c.add_ref(
            i, rows=nr_h, columns=nc_v, column_pitch=con_sp[0], row_pitch=con_sp[1]
        )
        cont_B_arrc2.dmove((-np_spacing - B_width, E_length + np_spacing))
        cont_B_arrc2.dmove(
            (
                (B_width - nc_v * contact_size[0] - (nc_v - 1) * contact_spacing[0])
                / 2,
                (B_width - nr_h * contact_size[1] - (nr_h - 1) * contact_spacing[1])
                / 2,
            )
        )

        cont_B_arrc3 = c.add_ref(
            i, rows=nr_h, columns=nc_v, column_pitch=con_sp[0], row_pitch=con_sp[1]
        )
        cont_B_arrc3.dmove((E_width + np_spacing, -np_spacing - B_width))
        cont_B_arrc3.dmove(
            (
                (B_width - nc_v * contact_size[0] - (nc_v - 1) * contact_spacing[0])
                / 2,
                (B_width - nr_h * contact_size[1] - (nr_h - 1) * contact_spacing[1])
                / 2,
            )
        )

        cont_B_arrc4 = c.add_ref(
            i, rows=nr_h, columns=nc_v, column_pitch=con_sp[0], row_pitch=con_sp[1]
        )
        cont_B_arrc4.dmove((E_width + np_spacing, E_length + np_spacing))
        cont_B_arrc4.dmove(
            (
                (B_width - nc_v * contact_size[0] - (nc_v - 1) * contact_spacing[0])
                / 2,
                (B_width - nr_h * contact_size[1] - (nr_h - 1) * contact_spacing[1])
                / 2,
            )
        )

    # generating collector

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

    C_in.connect(
        "e1", E.ports["e1"], allow_layer_mismatch=True, allow_width_mismatch=True
    )
    C_in.dmovex(E_width + 2.25 * np_spacing + B_width)

    C_out.connect(
        "e1", E.ports["e1"], allow_layer_mismatch=True, allow_width_mismatch=True
    )
    C_out.dmovex(E_width + 2.25 * np_spacing + B_width + C_width)

    c.add_ref(gf.boolean(A=C_out, B=C_in, operation="not", layer=tap_layer))

    # generate its p+ implants

    rect_pmC_in = gf.components.rectangle(
        size=(
            E_width + 4.5 * np_spacing + 2 * B_width - 2 * sdm_enclosure[0],
            E_length + 4.5 * np_spacing + 2 * B_width - 2 * sdm_enclosure[1],
        ),
        layer=psdm_layer,
    )
    rect_pmC_out = gf.components.rectangle(
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
        layer=psdm_layer,
    )

    pmC_in = c_C.add_ref(rect_pmC_in)
    pmC_out = c_C.add_ref(rect_pmC_out)

    pmC_in.connect(
        "e1", E.ports["e1"], allow_layer_mismatch=True, allow_width_mismatch=True
    )
    pmC_in.dmovex(E_width + 2.25 * np_spacing + B_width - sdm_enclosure[0])

    pmC_out.connect(
        "e1", E.ports["e1"], allow_layer_mismatch=True, allow_width_mismatch=True
    )
    pmC_out.dmovex(E_width + 2.25 * np_spacing + B_width + C_width + sdm_enclosure[0])

    c.add_ref(gf.boolean(A=pmC_out, B=pmC_in, operation="A-B", layer=psdm_layer))

    # generate its contact and local interconnects
    nr_v = ceil((C_in.dymax - C_in.dymin) / (contact_size[1] + contact_spacing[1]))
    nc_v = ceil((C_width) / (contact_size[0] + contact_spacing[0]))

    if (
        (C_width - nc_v * contact_size[0] - (nc_v - 1) * contact_spacing[0]) / 2
    ) < contact_enclosure[0]:
        nc_v -= 1

    if (
        (
            C_in.dymax
            - C_in.dymin
            - nr_v * contact_size[1]
            - (nr_v - 1) * contact_spacing[1]
        )
        / 2
    ) < contact_enclosure[1]:
        nr_v -= 1

    nc_h = ceil((C_in.dxmax - C_in.dxmin) / (contact_size[0] + contact_spacing[0]))
    nr_h = ceil((C_width) / (contact_size[1] + contact_spacing[1]))

    if (
        (C_width - nr_h * contact_size[0] - (nr_h - 1) * contact_spacing[1]) / 2
    ) < contact_enclosure[1]:
        nr_h -= 1

    if (
        (
            C_in.dxmax
            - C_in.dxmin
            - nc_h * contact_size[1]
            - (nc_h - 1) * contact_spacing[0]
        )
        / 2
    ) < contact_enclosure[0]:
        nc_h -= 1

    for i in range(2):
        rect_in = gf.components.rectangle(
            size=(
                E_width
                + 4.5 * np_spacing
                + 2 * B_width
                + (C_width - nc_v * contact_size[0] - (nc_v - 1) * contact_spacing[0])
                - 2 * i * mcon_enclosure[0]
                - 2 * (1 - i) * li_enclosure,
                E_length
                + 4.5 * np_spacing
                + 2 * B_width
                + (C_width - nr_h * contact_size[1] - (nr_h - 1) * contact_spacing[1])
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
                - (C_width - nc_v * contact_size[0] - (nc_v - 1) * contact_spacing[0])
                + 2 * i * mcon_enclosure[0]
                + 2 * (1 - i) * li_enclosure,
                E_length
                + 4.5 * np_spacing
                + 2 * B_width
                + 2 * C_width
                - (C_width - nr_h * contact_size[0] - (nr_h - 1) * contact_spacing[0])
                + 2 * i * mcon_enclosure[1]
                + 2 * (1 - i) * li_enclosure,
            ),
            layer=rect_layer[i],
        )

        li_m1_c_in = c_C.add_ref(rect_in)
        li_m1_c_out = c_C.add_ref(rect_out)

        li_m1_c_in.connect(
            "e1", E.ports["e1"], allow_layer_mismatch=True, allow_width_mismatch=True
        )
        li_m1_c_in.dmovex(
            E_width
            + 2.25 * np_spacing
            + B_width
            + (C_width - nc_v * contact_size[0] - (nc_v - 1) * contact_spacing[0]) / 2
            - i * mcon_enclosure[0]
            - (1 - i) * li_enclosure
        )

        li_m1_c_out.connect(
            "e1", E.ports["e1"], allow_layer_mismatch=True, allow_width_mismatch=True
        )
        li_m1_c_out.dmovex(
            E_width
            + 2.25 * np_spacing
            + B_width
            + C_width
            - (C_width - nc_v * contact_size[0] - (nc_v - 1) * contact_spacing[0]) / 2
            + i * mcon_enclosure[0]
            + (1 - i) * li_enclosure
        )

        c.add_ref(
            gf.boolean(
                A=li_m1_c_out, B=li_m1_c_in, operation="A-B", layer=rect_layer[i]
            )
        )

    for i in rect_c_mc:
        cont_C_arr1 = c.add_ref(
            i, rows=nr_v, columns=nc_v, column_pitch=con_sp[0], row_pitch=con_sp[1]
        )  # left side
        cont_C_arr1.dmove(
            (-2.25 * np_spacing - B_width - C_width, -2.25 * np_spacing - B_width)
        )
        cont_C_arr1.dmovex(
            (C_width - nc_v * contact_size[0] - (nc_v - 1) * contact_spacing[0]) / 2
        )
        cont_C_arr1.dmovey(
            (
                C_in.dymax
                - C_in.dymin
                - nr_v * contact_size[1]
                - (nr_v - 1) * contact_spacing[1]
            )
            / 2
        )

        cont_C_arr2 = c.add_ref(
            i, rows=nr_v, columns=nc_v, column_pitch=con_sp[0], row_pitch=con_sp[1]
        )  # right side
        cont_C_arr2.dmove(
            (E_width + 2.25 * np_spacing + B_width, -2.25 * np_spacing - B_width)
        )
        cont_C_arr2.dmovex(
            (C_width - nc_v * contact_size[0] - (nc_v - 1) * contact_spacing[0]) / 2
        )
        cont_C_arr2.dmovey(
            (
                C_in.dymax
                - C_in.dymin
                - nr_v * contact_size[1]
                - (nr_v - 1) * contact_spacing[1]
            )
            / 2
        )

        cont_C_arr3 = c.add_ref(
            i, rows=nr_h, columns=nc_h, column_pitch=con_sp[0], row_pitch=con_sp[1]
        )  # upper side
        cont_C_arr3.dmove(
            (-2.25 * np_spacing - B_width, E_length + 2.25 * np_spacing + B_width)
        )
        cont_C_arr3.dmovex(
            (
                C_in.dxmax
                - C_in.dxmin
                - nc_h * contact_size[0]
                - (nc_h - 1) * contact_spacing[0]
            )
            / 2
        )
        cont_C_arr3.dmovey(
            (C_width - nr_h * contact_size[1] - (nr_h - 1) * contact_spacing[1]) / 2
        )

        cont_C_arr4 = c.add_ref(
            i, rows=nr_h, columns=nc_h, column_pitch=con_sp[0], row_pitch=con_sp[1]
        )  # bottom side
        cont_C_arr4.dmove(
            (-2.25 * np_spacing - B_width, -2.25 * np_spacing - B_width - C_width)
        )
        cont_C_arr4.dmovex(
            (
                C_in.dxmax
                - C_in.dxmin
                - nc_h * contact_size[0]
                - (nc_h - 1) * contact_spacing[0]
            )
            / 2
        )
        cont_C_arr4.dmovey(
            (C_width - nr_h * contact_size[1] - (nr_h - 1) * contact_spacing[1]) / 2
        )

        cont_C_arrc1 = c.add_ref(
            i, rows=nr_h, columns=nc_v, column_pitch=con_sp[0], row_pitch=con_sp[1]
        )  # corners
        cont_C_arrc1.dmove(
            (
                -2.25 * np_spacing - B_width - C_width,
                -2.25 * np_spacing - B_width - C_width,
            )
        )
        cont_C_arrc1.dmove(
            (
                (C_width - nc_v * contact_size[0] - (nc_v - 1) * contact_spacing[0])
                / 2,
                (C_width - nr_h * contact_size[1] - (nr_h - 1) * contact_spacing[1])
                / 2,
            )
        )

        cont_C_arrc2 = c.add_ref(
            i, rows=nr_h, columns=nc_v, column_pitch=con_sp[0], row_pitch=con_sp[1]
        )  # corners
        cont_C_arrc2.dmove(
            (
                -2.25 * np_spacing - B_width - C_width,
                E_length + 2.25 * np_spacing + B_width,
            )
        )
        cont_C_arrc2.dmove(
            (
                (C_width - nc_v * contact_size[0] - (nc_v - 1) * contact_spacing[0])
                / 2,
                (C_width - nr_h * contact_size[1] - (nr_h - 1) * contact_spacing[1])
                / 2,
            )
        )

        cont_C_arrc3 = c.add_ref(
            i, rows=nr_h, columns=nc_v, column_pitch=con_sp[0], row_pitch=con_sp[1]
        )  # corners
        cont_C_arrc3.dmove(
            (
                E_width + 2.25 * np_spacing + B_width,
                E_length + 2.25 * np_spacing + B_width,
            )
        )
        cont_C_arrc3.dmove(
            (
                (C_width - nc_v * contact_size[0] - (nc_v - 1) * contact_spacing[0])
                / 2,
                (C_width - nr_h * contact_size[1] - (nr_h - 1) * contact_spacing[1])
                / 2,
            )
        )

        cont_C_arrc4 = c.add_ref(
            i, rows=nr_h, columns=nc_v, column_pitch=con_sp[0], row_pitch=con_sp[1]
        )  # corners
        cont_C_arrc4.dmove(
            (
                E_width + 2.25 * np_spacing + B_width,
                -2.25 * np_spacing - B_width - C_width,
            )
        )
        cont_C_arrc4.dmove(
            (
                (C_width - nc_v * contact_size[0] - (nc_v - 1) * contact_spacing[0])
                / 2,
                (C_width - nc_v * contact_size[1] - (nc_v - 1) * contact_spacing[1])
                / 2,
            )
        )

    # generating nwell around E & B

    rect_nwell = gf.components.rectangle(
        size=(
            B_out.dxmax - B_out.dxmin + 2 * diff_enclosure[0],
            B_out.dymax - B_out.dymin + 2 * diff_enclosure[1],
        ),
        layer=nwell_layer,
    )
    nwell = c.add_ref(rect_nwell)
    nwell.connect(
        "e1", B_out.ports["e3"], allow_layer_mismatch=True, allow_width_mismatch=True
    )
    nwell.dmovex(B_out.dxmax - B_out.dxmin + diff_enclosure[0])

    # generating pnp identifier
    npn = c.add_ref(
        gf.components.rectangle(
            size=(C_out.dxmax - C_out.dxmin, C_out.dymax - C_out.dymin), layer=pnp_layer
        )
    )
    npn.connect(
        "e1", C_out.ports["e3"], allow_layer_mismatch=True, allow_width_mismatch=True
    )
    npn.dmovex(C_out.dxmax - C_out.dxmin)
    return c


if __name__ == "__main__":
    c = pnp(E_length=3.4, E_width=3.4, np_spacing=1, B_width=1, C_width=1)
    # c = pnp(np_spacing=1, B_width= 0.65, C_width=0.65)
    c.show()
