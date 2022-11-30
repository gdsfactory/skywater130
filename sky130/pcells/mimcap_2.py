from math import floor

import gdsfactory as gf
from gdsfactory.types import Float2, LayerSpec


@gf.cell
def mimcap_2(
    m4_layer: LayerSpec = (71, 20),
    via4_size: Float2 = (0.8, 0.8),
    via4_layer: LayerSpec = (71, 44),
    via4_enclosure: Float2 = (0.32, 0.32),
    via4_spacing: Float2 = (0.8, 0.8),
    m5_spacing: float = 1.6,
    m5_r_length: float = 1.6,
    m5_layer: LayerSpec = (72, 20),
    m5_length: float = 1.6,
    m5_width: float = 1.6,
    capm2_layer: LayerSpec = (97, 44),
    m5_enclosure: Float2 = (0.14, 0.14),
    capm2_enclosure: Float2 = (0.5, 0.5),
) -> gf.Component:
    """Return mim cap between metal 4 and 5.

    .. plot::
      :include-source:

      import sky130

      c = sky130.pcells.mimcap_2(m5_length=15, m5_width=15, m5_r_length=5)
      c.plot()
    """
    c = gf.Component()

    en = (0.02, 0.04)  # for enclosure
    # generating m4 plate
    m4_length = (
        capm2_enclosure[0]
        + 2 * m5_enclosure[0]
        + m5_length
        + m5_spacing
        + m5_r_length
        + en[0]
    )
    m4_width = 2 * capm2_enclosure[1] + 2 * m5_enclosure[1] + m5_width + en[1]
    rect_m4 = gf.components.rectangle(size=(m4_length, m4_width), layer=m4_layer)
    m4 = c.add_ref(rect_m4)

    # generate m4 plates

    rect_m5_r = gf.components.rectangle(
        size=(m5_r_length, m4_width - en[1]), layer=m5_layer
    )
    m5_r = c.add_ref(rect_m5_r)
    m5_r.movex(m4_length - m5_r_length - en[0] / 2)
    m5_r.movey(en[1] / 2)

    rect_m5_l = gf.components.rectangle(size=(m5_length, m5_width), layer=m5_layer)
    m5_l = c.add_ref(rect_m5_l)
    m5_l.connect("e3", destination=m4.ports["e1"])
    m5_l.movex(m5_length + capm2_enclosure[0] + m5_enclosure[0] + en[0] / 2)

    # generate capm2
    rect_capm2 = gf.components.rectangle(
        size=(m5_length + 2 * m5_enclosure[0], m5_width + 2 * m5_enclosure[1]),
        layer=capm2_layer,
    )
    capm2 = c.add_ref(rect_capm2)
    capm2.connect("e3", destination=m5_l.ports["e1"])
    capm2.movex(m5_length + m5_enclosure[0])

    # generat3 via4
    rect_via4 = gf.components.rectangle(size=via4_size, layer=via4_layer)

    # for the left m5 plate
    nc1 = floor((m5_length) / (via4_size[0] + via4_spacing[0]))
    nr1 = floor((m5_width) / (via4_size[1] + via4_spacing[1]))
    via4_arr1 = c.add_array(
        rect_via4,
        rows=nr1,
        columns=nc1,
        spacing=(via4_spacing[0] + via4_size[0], via4_spacing[1] + via4_size[1]),
    )
    via4_arr1.movex(
        capm2_enclosure[0]
        + m5_enclosure[0]
        + ((m5_length - nc1 * via4_size[0] - (nc1 - 1) * via4_spacing[0]) / 2)
    )
    via4_arr1.movey(
        capm2_enclosure[1]
        + m5_enclosure[1]
        + ((m5_width - nr1 * via4_size[1] - (nr1 - 1) * via4_spacing[1]) / 2)
    )

    # for the right m4 plate
    nr2 = floor((m4_width - en[1]) / (via4_size[1] + via4_spacing[1]))
    nc2 = floor((m5_r_length) / (via4_size[0] + via4_spacing[0]))
    via3_arr2 = c.add_array(
        rect_via4,
        rows=nr2,
        columns=nc2,
        spacing=(via4_spacing[0] + via4_size[0], via4_spacing[1] + via4_size[1]),
    )
    via3_arr2.movex(m4_length - en[0] / 2 - m5_r_length)
    via3_arr2.movex(
        (m5_r_length - nc2 * via4_size[0] - (nc2 - 1) * via4_spacing[0]) / 2
    )
    via3_arr2.movey(
        (m4_width - en[1] / 2 - nr2 * via4_size[1] - (nr2 - 1) * via4_spacing[1]) / 2
    )

    return c


if __name__ == "__main__":

    # c = mimcap_2()
    c = mimcap_2(m5_length=15, m5_width=15, m5_r_length=5)
    c.show(show_ports=True)
