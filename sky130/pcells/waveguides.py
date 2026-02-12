"""Primitives."""

import gdsfactory as gf
from gdsfactory.cross_section import port_names_electrical, port_types_electrical
from gdsfactory.typings import CrossSectionSpec, LayerSpec, Size


@gf.cell
def wire_corner(
    cross_section: CrossSectionSpec = "metal2",
    width: float | None = None,
    radius: float | None = None,  # Ignored, for route_astar compatibility
) -> gf.Component:
    """Returns 90 degrees electrical corner wire.

    Args:
        cross_section: spec.
        width: optional width. Defaults to cross_section width.
        radius: ignored (wire corners are 0-radius sharp corners).
    """
    return gf.c.wire_corner(
        cross_section=cross_section,
        width=width,
        port_names=port_names_electrical,
        port_types=port_types_electrical,
        radius=None,
    )


@gf.cell
def wire_corner45(
    cross_section: CrossSectionSpec = "metal2",
    radius: float = 10,
    width: float | None = None,
    layer: LayerSpec | None = None,
    with_corner90_ports: bool = True,
) -> gf.Component:
    """Returns 90 degrees electrical corner wire.

    Args:
        cross_section: spec.
        radius: ignored.
        width: optional width. Defaults to cross_section width.
        layer: ignored.
        with_corner90_ports: if True, adds ports at 90 degrees.
    """
    return gf.c.wire_corner45(
        cross_section=cross_section,
        radius=radius,
        width=width,
        layer=layer,
        with_corner90_ports=with_corner90_ports,
    )


####################
# Metal waveguides
####################


@gf.cell
def straight_metal1(
    length: float = 10,
    cross_section: CrossSectionSpec = "metal1",
    width: float | None = None,
) -> gf.Component:
    """Returns a Straight waveguide.

    Args:
        length: straight length (um).
        cross_section: specification (CrossSection, string or dict).
        width: width of the waveguide. If None, it will use the width of the cross_section.
    """
    return gf.c.straight(
        length=length, cross_section=cross_section, width=width, npoints=2
    )


@gf.cell
def straight_metal2(
    length: float = 10,
    cross_section: CrossSectionSpec = "metal2",
    width: float | None = None,
) -> gf.Component:
    """Returns a Straight waveguide.

    Args:
        length: straight length (um).
        cross_section: specification (CrossSection, string or dict).
        width: width of the waveguide. If None, it will use the width of the cross_section.
    """
    return gf.c.straight(
        length=length, cross_section=cross_section, width=width, npoints=2
    )


@gf.cell
def bend_metal1(
    radius: float | None = None,
    angle: float = 90,
    width: float | None = None,
    cross_section: CrossSectionSpec = "metal1",
) -> gf.Component:
    """Regular degree euler bend."""
    if radius is None:
        if width:
            xs = gf.get_cross_section(cross_section=cross_section, width=width)
        else:
            xs = gf.get_cross_section(cross_section=cross_section)
        radius = xs.radius or xs.width
    return gf.c.bend_circular(
        radius=radius,
        angle=angle,
        width=width,
        cross_section=cross_section,
        allow_min_radius_violation=False,
        npoints=None,
        layer=None,
    )


@gf.cell
def bend_metal2(
    radius: float | None = None,
    angle: float = 90,
    width: float | None = None,
    cross_section: CrossSectionSpec = "metal2",
) -> gf.Component:
    """Regular degree euler bend."""
    if radius is None:
        if width:
            xs = gf.get_cross_section(cross_section=cross_section, width=width)
        else:
            xs = gf.get_cross_section(cross_section=cross_section)
        radius = xs.radius or xs.width
    return gf.c.bend_circular(
        radius=radius,
        angle=angle,
        width=width,
        cross_section=cross_section,
        allow_min_radius_violation=False,
        npoints=None,
        layer=None,
    )


@gf.cell
def bend_s_metal1(
    size: Size = (11, 1.8),
    cross_section: CrossSectionSpec = "metal1",
    width: float | None = None,
) -> gf.Component:
    """Return S bend with bezier curve.

    stores min_bend_radius property in self.info['min_bend_radius']
    min_bend_radius depends on height and length

    Args:
        size: in x and y direction.
        cross_section: spec.
        width: width of the waveguide. If None, it will use the width of the cross_section.
    """
    return gf.c.bend_s(
        size=size,
        cross_section=cross_section,
        npoints=99,
        allow_min_radius_violation=False,
        width=width,
    )


@gf.cell
def bend_s_metal2(
    size: Size = (11, 1.8),
    cross_section: CrossSectionSpec = "metal2",
    width: float | None = None,
) -> gf.Component:
    """Return S bend with bezier curve.

    stores min_bend_radius property in self.info['min_bend_radius']
    min_bend_radius depends on height and length

    Args:
        size: in x and y direction.
        cross_section: spec.
        width: width of the waveguide. If None, it will use the width of the cross_section.
    """
    return gf.c.bend_s(
        size=size,
        cross_section=cross_section,
        npoints=99,
        allow_min_radius_violation=False,
        width=width,
    )


__all__ = [
    "wire_corner",
    "wire_corner45",
    "straight_metal1",
    "straight_metal2",
    "bend_metal1",
    "bend_metal2",
    "bend_s_metal1",
    "bend_s_metal2",
]

if __name__ == "__main__":
    from amf.cband import PDK

    PDK.activate()

    c = wire_corner45()
    c.pprint_ports()
    c.show()
