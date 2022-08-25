import gdsfactory as gf
import numpy as np
from gdsfactory.types import Float2, LayerSpec


@gf.cell
def nmos(
    diffusion_layer: LayerSpec = (65, 20),
    poly_layer: LayerSpec = (66, 22),
    gate_width: float = 0.25,
    gate_length: float = 0.15,
    sd_width: float = 0.2,
    end_cap_length: float = 0.1,
    contact_size: Float2 = (0.15, 0.15),
    contact_spacing: Float2 = (0.15, 0.15),
    contact_layer: LayerSpec = (66, 44),
    contact_enclosure: float = 0.1,
) -> gf.Component:

    """Return NMOS.

    Args:
        diffusion_layer: spec.
        poly_layer: spec.
        gate_width: for poly.
        gate_length: for poly.
        sd_width: source drain width.
        end_cap_length: end cap length.
        contact_size: for via.
        contact_spacing: for via.
        contact_layer: for via.
        contact_enclosure: of the contact inside the diffusion_layer.

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

    """
    c = gf.Component()
    poly = c << gf.components.rectangle(
        size=(gate_length, gate_width + 2 * end_cap_length),
        layer=poly_layer,
    )

    diff = c << gf.components.rectangle(
        size=(sd_width + gate_length + sd_width, gate_width),
        layer=diffusion_layer,
    )

    poly.ymin = -end_cap_length
    poly.xmin = 0

    diff.xmin = -sd_width

    spacing = np.array(contact_size) + contact_spacing
    spacing = tuple(spacing)

    contact = gf.components.via(
        size=contact_size,
        layer=contact_layer,
        spacing=spacing,
        enclosure=contact_enclosure,
    )
    contact_array = gf.components.via_stack(
        size=(sd_width, gate_width),
        vias=(contact,),
        layers=None,
    )
    contact_array_left = c << contact_array
    contact_array_right = c << contact_array

    contact_array_left.xmin = -sd_width + contact_enclosure
    contact_array_left.ymin = contact_enclosure

    contact_array_right.xmax = diff.xmax - contact_enclosure
    contact_array_right.ymin = contact_enclosure
    return c


if __name__ == "__main__":
    c = nmos(gate_width=10, gate_length=1, sd_width=5)
    c.show()
