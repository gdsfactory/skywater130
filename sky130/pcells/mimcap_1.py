from math import floor

import gdsfactory as gf
from gdsfactory.types import Float2, LayerSpec


@gf.cell
def mimcap_1(
    m3_layer: LayerSpec = (70, 20),
    via3_size: Float2 = (0.2, 0.2),
    via3_layer: LayerSpec = (70, 44),
    via3_enclosure: Float2 = (0.09, 0.09),
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


    .. plot::
      :include-source:

      import sky130

      c = sky130.pcells.mimcap_1(
            m3_layer=(70, 20),
            via3_size=(0.2, 0.2),
            via3_layer=(70, 44),
            via3_enclosure=(0.09, 0.09),
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
    m4_r.movex(m3_length - m4_r_length - en[0] / 2)
    m4_r.movey(en[1] / 2)

    rect_m4_l = gf.components.rectangle(size=(m4_length, m4_width), layer=m4_layer)
    m4_l = c.add_ref(rect_m4_l)
    m4_l.connect("e3", destination=m3.ports["e1"])
    m4_l.movex(m4_length + capm_enclosure[0] + m4_enclosure[0] + en[0] / 2)

    # generate capm
    rect_capm = gf.components.rectangle(
        size=(m4_length + 2 * m4_enclosure[0], m4_width + 2 * m4_enclosure[1]),
        layer=capm_layer,
    )
    capm = c.add_ref(rect_capm)
    capm.connect("e3", destination=m4_l.ports["e1"])
    capm.movex(m4_length + m4_enclosure[0])

    # generat3 via3
    rect_via3 = gf.components.rectangle(size=via3_size, layer=via3_layer)

    # for the left m4 plate
    nc1 = floor((m4_length) / (via3_size[0] + via3_spacing[0]))
    nr1 = floor((m4_width) / (via3_size[1] + via3_spacing[1]))
    via3_arr1 = c.add_array(
        rect_via3,
        rows=nr1,
        columns=nc1,
        spacing=(via3_spacing[0] + via3_size[0], via3_spacing[1] + via3_size[1]),
    )
    via3_arr1.movex(
        capm_enclosure[0]
        + m4_enclosure[0]
        + ((m4_length - nc1 * via3_size[0] - (nc1 - 1) * via3_spacing[0]) / 2)
    )
    via3_arr1.movey(
        capm_enclosure[1]
        + m4_enclosure[1]
        + ((m4_width - nr1 * via3_size[1] - (nr1 - 1) * via3_spacing[1]) / 2)
    )

    # for the right m4 plate
    nr2 = floor((m3_width - en[1]) / (via3_size[1] + via3_spacing[1]))
    nc2 = floor((m4_r_length) / (via3_size[0] + via3_spacing[0]))

    nc2 = max(nc2, 1)
    via3_arr2 = c.add_array(
        rect_via3,
        rows=nr2,
        columns=nc2,
        spacing=(via3_spacing[0] + via3_size[0], via3_spacing[1] + via3_size[1]),
    )
    via3_arr2.movex(m3_length - en[0] / 2 - m4_r_length)
    via3_arr2.movex(
        (m4_r_length - nc2 * via3_size[0] - (nc2 - 1) * via3_spacing[0]) / 2
    )
    via3_arr2.movey(
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
    c.show(show_ports=True)
