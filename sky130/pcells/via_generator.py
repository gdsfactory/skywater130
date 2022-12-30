from math import ceil

import gdsfactory as gf
from gdsfactory.types import Float2, LayerSpec


@gf.cell
def via_generator(
    width: float = 1,
    length: float = 1,
    via_size: Float2 = (0.17, 0.17),
    via_layer: LayerSpec = (66, 44),
    via_enclosure: Float2 = (0.06, 0.06),
    via_spacing: Float2 = (0.17, 0.17),
) -> gf.Component:
    """Return vias within the area of width x length \
    and set number of rows and number of columns as a \
    global variable to be used outside the function.

    .. plot::
      :include-source:

      import sky130

      c = sky130.pcells.via_generator()
      c.plot()
    """
    c = gf.Component()

    nr = ceil(length / (via_size[1] + via_spacing[1]))
    nc = ceil(width / (via_size[0] + via_spacing[0]))

    if (length - nr * via_size[1] - (nr - 1) * via_spacing[1]) / 2 < via_enclosure[1]:
        nr -= 1

    nr = max(nr, 1)
    if (width - nc * via_size[0] - (nc - 1) * via_spacing[0]) / 2 < via_enclosure[0]:
        nc -= 1

    nc = max(nc, 1)
    via_sp = (via_size[0] + via_spacing[0], via_size[1] + via_spacing[1])
    rect_via = gf.components.rectangle(size=via_size, layer=via_layer)

    c.add_array(rect_via, rows=nr, columns=nc, spacing=via_sp)
    return c


def demo_via():
    width = 1.5
    length = 1.5
    via_size = (
        0.17,
        0.17,
    )  # via4:(0.8,0.8),via3,via2 : (0.2,0.2) ,via1 : (0.15,0.15),licon: (0.17,0.17)
    via_spacing = (
        0.17,
        0.17,
    )  # via4:(0.8,0.8) via2 :(0.2,0.2), via1,licon :(0.17,0.17)
    via_layer = (
        66,
        44,
    )  # via4:(71,44),via3 :(70,44)via2 : (69,44) ,via1 : (68,44),licon: (66,44)
    via_enclosure = (
        0.06,
        0.06,
    )  # via4: (0.19,0.19)via2 : (0.04,0.04) via1 : (0.055,0.055),via3,licon: (0.06,0.06)
    bottom_layer: LayerSpec = (
        65,
        44,
    )  # m4 :(71,20),m3:(70:20) , m2 :(69,20),  m1 :(68,20),tap: (65,44)

    rect = gf.components.rectangle(size=(width, length), layer=bottom_layer)
    nr = ceil(length / (via_size[1] + via_spacing[1]))
    nc = ceil(width / (via_size[0] + via_spacing[0]))

    c1 = gf.Component("via test for rectangle")
    c1.add_label(
        f"test for via4 over met4 within {width} x {length} area",
        position=(width / 2, length + via_enclosure[1]),
    )
    c1.add_ref(rect)
    c = via_generator(
        width=width,
        length=length,
        via_size=via_size,
        via_spacing=via_spacing,
        via_layer=via_layer,
    )
    v = c1.add_ref(c)
    v.move(
        (
            (width - nc * via_size[0] - (nc - 1) * via_spacing[0]) / 2,
            (length - nr * via_size[1] - (nr - 1) * via_spacing[1]) / 2,
        )
    )

    c2 = gf.Component("via test for bending structure")
    rect_out = gf.components.rectangle(size=(4 * width, 4 * length))
    d = gf.Component()
    x1 = d.add_ref(rect)
    x2 = d.add_ref(rect_out)
    x1.move((1.5 * width, 1.5 * length))
    c2.add_ref(gf.geometry.boolean(A=x2, B=x1, operation="A-B", layer=bottom_layer))
    c2.add_label(
        "test for via4 over met4 within a bending area",
        position=(width, 4 * length + via_enclosure[1]),
    )

    for i in range(2):
        v = via_generator(
            width=x2.xmax - x1.xmax,
            length=x1.ymax - x1.ymin,
            via_enclosure=via_enclosure,
            via_size=via_size,
            via_spacing=via_spacing,
            via_layer=via_layer,
        )
        vi = c2.add_ref(v)
        vi.movex(
            (x2.xmax - x1.xmax - nc * via_size[0] - (nc - 1) * via_spacing[0]) / 2
            + i * (x2.xmax - x1.xmin)
        )
        vi.movey(
            x1.ymin
            - x2.ymin
            + (x1.ymax - x1.ymin - nr * via_size[1] - (nr - 1) * via_spacing[1]) / 2
        )

    for i in range(2):
        h = via_generator(
            width=x1.xmax - x1.xmin,
            length=x2.ymax - x1.ymax,
            via_enclosure=via_enclosure,
            via_size=via_size,
            via_spacing=via_spacing,
            via_layer=via_layer,
        )
        vi = c2.add_ref(h)
        vi.movey(
            (x2.ymax - x1.ymax - nr * via_size[1] - (nr - 1) * via_spacing[1]) / 2
            + i * (x2.ymax - x1.ymin)
        )
        vi.movex(
            x1.xmin
            - x2.xmin
            + (x1.xmax - x1.xmin - nc * via_size[0] - (nc - 1) * via_spacing[0]) / 2
        )

    for i in range(2):
        for j in range(2):
            cor = via_generator(
                width=x2.xmax - x1.xmax,
                length=x2.ymax - x1.ymax,
                via_enclosure=via_enclosure,
                via_size=via_size,
                via_spacing=via_spacing,
                via_layer=via_layer,
            )

            co = c2.add_ref(cor)
            co.movex(
                (x2.xmax - x1.xmax - nc * via_size[0] - (nc - 1) * via_spacing[0]) / 2
            )
            co.movey(
                (x1.ymin - x2.ymin - nr * via_size[1] - (nr - 1) * via_spacing[1]) / 2
            )
            co.movex(j * (x2.xmax - x1.xmin))
            co.movey(i * (x2.ymax - x1.ymin))

    return c2


if __name__ == "__main__":
    # c = via_generator()
    c = demo_via()
    c.show(show_ports=True)
