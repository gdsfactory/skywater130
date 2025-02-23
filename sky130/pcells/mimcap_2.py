from math import floor

import gdsfactory as gf
from gdsfactory.typings import Float2, LayerSpec


@gf.cell
def mimcap_2(
    m4_layer: LayerSpec = (71, 20),
    via4_size: Float2 = (0.8, 0.8),
    via4_layer: LayerSpec = (71, 44),
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

    Args:
        m4_layer: metal 4 layer.
        via4_size: via4 size.
        via4_layer: via4 layer.
        via4_spacing: via4 spacing.
        m5_spacing: metal 5 spacing.
        m5_r_length: metal 5 right length.
        m5_layer: metal 5 layer.
        m5_length: metal 5 length.
        m5_width: metal 5 width.
        capm2_layer: cap metal 2 layer.
        m5_enclosure: metal 5 enclosure.
        capm2_enclosure: cap metal 2 enclosure.


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
    m5_r.dmovex(m4_length - m5_r_length - en[0] / 2)
    m5_r.dmovey(en[1] / 2)

    rect_m5_l = gf.components.rectangle(size=(m5_length, m5_width), layer=m5_layer)
    m5_l = c.add_ref(rect_m5_l)
    m5_l.connect(
        "e3", m4.ports["e1"], allow_layer_mismatch=True, allow_width_mismatch=True
    )
    m5_l.dmovex(m5_length + capm2_enclosure[0] + m5_enclosure[0] + en[0] / 2)

    # generate capm2
    rect_capm2 = gf.components.rectangle(
        size=(m5_length + 2 * m5_enclosure[0], m5_width + 2 * m5_enclosure[1]),
        layer=capm2_layer,
    )
    capm2 = c.add_ref(rect_capm2)
    capm2.connect(
        "e3", m5_l.ports["e1"], allow_layer_mismatch=True, allow_width_mismatch=True
    )
    capm2.dmovex(m5_length + m5_enclosure[0])

    # generat3 via4
    rect_via4 = gf.components.rectangle(size=via4_size, layer=via4_layer)

    # for the left m5 plate
    nc1 = floor((m5_length) / (via4_size[0] + via4_spacing[0]))
    nr1 = floor((m5_width) / (via4_size[1] + via4_spacing[1]))
    via4_arr1 = c.add_ref(
        rect_via4,
        rows=nr1,
        columns=nc1,
        column_pitch=via4_spacing[0] + via4_size[0],
        row_pitch=via4_spacing[1] + via4_size[1],
    )
    via4_arr1.dmovex(
        capm2_enclosure[0]
        + m5_enclosure[0]
        + ((m5_length - nc1 * via4_size[0] - (nc1 - 1) * via4_spacing[0]) / 2)
    )
    via4_arr1.dmovey(
        capm2_enclosure[1]
        + m5_enclosure[1]
        + ((m5_width - nr1 * via4_size[1] - (nr1 - 1) * via4_spacing[1]) / 2)
    )

    # for the right m4 plate
    nr2 = floor((m4_width - en[1]) / (via4_size[1] + via4_spacing[1]))
    nc2 = floor((m5_r_length) / (via4_size[0] + via4_spacing[0]))
    via3_arr2 = c.add_ref(
        rect_via4,
        rows=nr2,
        columns=nc2,
        column_pitch=via4_spacing[0] + via4_size[0],
        row_pitch=via4_spacing[1] + via4_size[1],
    )
    via3_arr2.dmovex(m4_length - en[0] / 2 - m5_r_length)
    via3_arr2.dmovex(
        (m5_r_length - nc2 * via4_size[0] - (nc2 - 1) * via4_spacing[0]) / 2
    )
    via3_arr2.dmovey(
        (m4_width - en[1] / 2 - nr2 * via4_size[1] - (nr2 - 1) * via4_spacing[1]) / 2
    )
    return c


if __name__ == "__main__":
    # c = mimcap_2()
    c = mimcap_2(m5_length=15, m5_width=15, m5_r_length=5)
    c.show()
