from math import floor

import gdsfactory as gf
from gdsfactory.typings import Float2, LayerSpec

from sky130.layers import LAYER


@gf.cell
def contact_array(
    width: float = 0.29,
    height: float = 0.29,
    contact_layer: LayerSpec = (66, 44),
    contact_size: Float2 = (0.17, 0.17),
    contact_spacing: Float2 = (0.17, 0.17),
    enclosure: Float2 = (0.06, 0.06),
) -> gf.Component:
    """Return a centered array of contacts/vias within the area of width x height.

    Uses floor rounding to match Magic's contact placement behavior.

    Args:
        width: width of the enclosing area.
        height: height of the enclosing area.
        contact_layer: layer for the contact rectangles.
        contact_size: (x, y) size of each contact.
        contact_spacing: (x, y) spacing between contacts.
        enclosure: (x, y) minimum enclosure of contacts within the area.

    .. plot::
      :include-source:

      import sky130

      c = sky130.pcells.contact_array()
      c.plot()
    """
    c = gf.Component()

    sx, sy = contact_size
    spx, spy = contact_spacing
    ex, ey = enclosure

    avail_w = width - 2 * ex
    avail_h = height - 2 * ey

    # Epsilon tolerance to avoid floating-point rounding artifacts.
    _EPS = 1e-6

    # Return empty component if area is too small for even one contact
    if avail_w < sx - _EPS or avail_h < sy - _EPS:
        return c

    # Floor rounding matches Magic's contact placement behavior.
    # Add epsilon before floor to compensate for floating-point drift
    # (e.g. 0.34/0.34 yielding 0.9999… instead of 1.0).
    nc = 1 + floor((avail_w - sx) / (sx + spx) + _EPS)
    nr = 1 + floor((avail_h - sy) / (sy + spy) + _EPS)

    nc = max(nc, 1)
    nr = max(nr, 1)

    pitch_x = sx + spx
    pitch_y = sy + spy

    # Total footprint of the contact array
    array_w = nc * sx + (nc - 1) * spx
    array_h = nr * sy + (nr - 1) * spy

    # Center the array within the available area
    ox = (width - array_w) / 2
    oy = (height - array_h) / 2

    rect = gf.components.rectangle(size=(sx, sy), layer=contact_layer)
    ref = c.add_ref(rect, columns=nc, rows=nr, column_pitch=pitch_x, row_pitch=pitch_y)
    ref.move((ox, oy))

    return c


def licon_array(width: float = 0.29, height: float = 0.29) -> gf.Component:
    """Convenience wrapper for licon contact arrays (LiCon, layer 66/44).

    Uses size=0.17, spacing=0.17, enclosure=0.06 on all sides.

    Args:
        width: width of the enclosing area.
        height: height of the enclosing area.
    """
    return contact_array(
        width=width,
        height=height,
        contact_layer=LAYER.licon1drawing,
        contact_size=(0.17, 0.17),
        contact_spacing=(0.17, 0.17),
        enclosure=(0.06, 0.06),
    )


def mcon_array(width: float = 0.29, height: float = 0.29) -> gf.Component:
    """Convenience wrapper for mcon contact arrays (Metal contact, layer 67/44).

    Uses size=0.17, spacing=0.19, enclosure=(0.03, 0.06).

    Args:
        width: width of the enclosing area.
        height: height of the enclosing area.
    """
    return contact_array(
        width=width,
        height=height,
        contact_layer=LAYER.mcondrawing,
        contact_size=(0.17, 0.17),
        contact_spacing=(0.19, 0.19),
        enclosure=(0.03, 0.06),
    )


if __name__ == "__main__":
    c = contact_array()
    c.show()
