from math import floor

import gdsfactory as gf
from gdsfactory.typings import Float2, LayerSpec


@gf.cell
def mimcap_1(
    m3_layer: LayerSpec = (70, 20),
    via3_size: Float2 = (0.2, 0.2),
    via3_layer: LayerSpec = (70, 44),
    via3_spacing: Float2 = (0.2, 0.2),  # (0.2,0.35),
    m4_spacing: float = 0.3,
    m4_r_length: float = 0.4,
    m4_layer: LayerSpec = (71, 20),
    m4_length: float = 1,
    m4_width: float = 1,
    capm_layer: LayerSpec = (89, 44),
    m4_enclosure: Float2 = (0.14, 0.14),
    capm_enclosure: Float2 = (0.5, 0.5),
) -> gf.Component:
    """Return mimcap_1 Pcell

    mim cap between metal 3 and 4

    Args:
        m3_layer: metal 3 layer.
        via3_size: via3 size.
        via3_layer: via3 layer.
        via3_spacing: via3 spacing.
        m4_spacing: metal 4 spacing.
        m4_r_length: metal 4 right length.
        m4_layer: metal 4 layer.
        m4_length: metal 4 length.
        m4_width: metal 4 width.
        capm_layer: cap metal layer.
        m4_enclosure: metal 4 enclosure.
        capm_enclosure: cap metal enclosure.


    .. plot::
      :include-source:

      import sky130

      c = sky130.pcells.mimcap_1(
            m3_layer=(70, 20),
            via3_size=(0.2, 0.2),
            via3_layer=(70, 44),
            via3_spacing=(0.2, 0.2),
            m4_spacing=0.3,
            m4_r_length=0.4,
            m4_layer=(71, 20),
            m4_length=1,
            m4_width=1,
            capm_layer=(89, 44),
            m4_enclosure=(0.14, 0.14),
            capm_enclosure=(0.5, 0.5),
      )
      c.plot()
    """
    c = gf.Component()

    en = (0.02, 0.04)  # for enclosure
    # generating m3 plate
    m3_length = (
        capm_enclosure[0]
        + 2 * m4_enclosure[0]
        + m4_length
        + m4_spacing
        + m4_r_length
        + en[0]
    )
    m3_width = 2 * capm_enclosure[1] + 2 * m4_enclosure[1] + m4_width + en[1]
    rect_m3 = gf.components.rectangle(size=(m3_length, m3_width), layer=m3_layer)
    m3 = c.add_ref(rect_m3)

    # generate m4 plates

    rect_m4_r = gf.components.rectangle(
        size=(m4_r_length, m3_width - en[1]), layer=m4_layer
    )
    m4_r = c.add_ref(rect_m4_r)
    m4_r.dmovex(m3_length - m4_r_length - en[0] / 2)
    m4_r.dmovey(en[1] / 2)

    rect_m4_l = gf.components.rectangle(size=(m4_length, m4_width), layer=m4_layer)
    m4_l = c.add_ref(rect_m4_l)
    m4_l.connect(
        "e3", m3.ports["e1"], allow_layer_mismatch=True, allow_width_mismatch=True
    )
    m4_l.dmovex(m4_length + capm_enclosure[0] + m4_enclosure[0] + en[0] / 2)

    # generate capm
    rect_capm = gf.components.rectangle(
        size=(m4_length + 2 * m4_enclosure[0], m4_width + 2 * m4_enclosure[1]),
        layer=capm_layer,
    )
    capm = c.add_ref(rect_capm)
    capm.connect(
        "e3", m4_l.ports["e1"], allow_layer_mismatch=True, allow_width_mismatch=True
    )
    capm.dmovex(m4_length + m4_enclosure[0])

    # generat3 via3
    rect_via3 = gf.components.rectangle(size=via3_size, layer=via3_layer)

    # for the left m4 plate
    nc1 = floor((m4_length) / (via3_size[0] + via3_spacing[0]))
    nr1 = floor((m4_width) / (via3_size[1] + via3_spacing[1]))
    via3_arr1 = c.add_ref(
        rect_via3,
        rows=nr1,
        columns=nc1,
        column_pitch=via3_spacing[0] + via3_size[0],
        row_pitch=via3_spacing[1] + via3_size[1],
    )
    via3_arr1.dmovex(
        capm_enclosure[0]
        + m4_enclosure[0]
        + ((m4_length - nc1 * via3_size[0] - (nc1 - 1) * via3_spacing[0]) / 2)
    )
    via3_arr1.dmovey(
        capm_enclosure[1]
        + m4_enclosure[1]
        + ((m4_width - nr1 * via3_size[1] - (nr1 - 1) * via3_spacing[1]) / 2)
    )

    # for the right m4 plate
    nr2 = floor((m3_width - en[1]) / (via3_size[1] + via3_spacing[1]))
    nc2 = floor((m4_r_length) / (via3_size[0] + via3_spacing[0]))

    nc2 = max(nc2, 1)
    via3_arr2 = c.add_ref(
        rect_via3,
        rows=nr2,
        columns=nc2,
        column_pitch=via3_spacing[0] + via3_size[0],
        row_pitch=via3_spacing[1] + via3_size[1],
    )
    via3_arr2.dmovex(m3_length - en[0] / 2 - m4_r_length)
    via3_arr2.dmovex(
        (m4_r_length - nc2 * via3_size[0] - (nc2 - 1) * via3_spacing[0]) / 2
    )
    via3_arr2.dmovey(
        (m3_width - en[1] / 2 - nr2 * via3_size[1] - (nr2 - 1) * via3_spacing[1]) / 2
    )

    return c


if __name__ == "__main__":
    # c = mimcap_1()
    c = mimcap_1(m4_length=5, m4_width=5, m4_r_length=1)
    # c = mimcap_1(
    #     m3_layer=(70, 20),
    #     via3_size=(0.2, 0.2),
    #     via3_layer=(70, 44),
    #     via3_enclosure=(0.09, 0.09),
    #     via3_spacing=(0.2, 0.2),
    #     m4_spacing=0.3,
    #     m4_r_length=0.4,
    #     m4_layer=(71, 20),
    #     m4_length=1,
    #     m4_width=1,
    #     capm_layer=(89, 44),
    #     m4_enclosure=(0.14, 0.14),
    #     capm_enclosure=(0.5, 0.5),
    # )
    c.show()
