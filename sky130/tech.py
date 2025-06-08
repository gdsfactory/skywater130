"""Technology definitions."""

from collections.abc import Callable
from functools import partial, wraps
from typing import Any

import gdsfactory as gf
from gdsfactory.cross_section import CrossSection
from gdsfactory.typings import LayerSpec

############################
# Cross-sections functions
############################

cross_sections: dict[str, Callable[..., CrossSection]] = {}
_cross_section_default_names: dict[str, str] = {}


def xsection(func: Callable[..., CrossSection]) -> Callable[..., CrossSection]:
    """Returns decorated to register a cross section function.

    Ensures that the cross-section name matches the name of the function that generated it when created using default parameters

    .. code-block:: python

        @xsection
        def strip(width=TECH.width_strip, radius=TECH.radius_strip):
            return gf.cross_section.cross_section(width=width, radius=radius)
    """
    default_xs = func()
    _cross_section_default_names[default_xs.name] = func.__name__

    @wraps(func)
    def newfunc(**kwargs: Any) -> CrossSection:
        xs = func(**kwargs)
        if xs.name in _cross_section_default_names:
            xs._name = _cross_section_default_names[xs.name]
        return xs

    cross_sections[func.__name__] = newfunc
    return newfunc


@xsection
def metal1(
    width: float = 0.2,
    layer: LayerSpec = "met1drawing",
    radius: float | None = None,
) -> CrossSection:
    """Return Metal Strip cross_section."""
    return gf.cross_section.metal1(
        width=width,
        layer=layer,
        radius=radius,
    )


@xsection
def metal2(
    width: float = 0.2,
    layer: LayerSpec = "met2drawing",
    radius: float | None = None,
) -> CrossSection:
    """Return Metal Strip cross_section."""
    return gf.cross_section.metal1(
        width=width,
        layer=layer,
        radius=radius,
    )


@xsection
def metal3(
    width: float = 0.2,
    layer: LayerSpec = "met3drawing",
    radius: float | None = None,
) -> CrossSection:
    """Return Metal Strip cross_section."""
    return gf.cross_section.metal1(
        width=width,
        layer=layer,
        radius=radius,
    )


@xsection
def metal4(
    width: float = 0.2,
    layer: LayerSpec = "met4drawing",
    radius: float | None = None,
) -> CrossSection:
    """Return Metal Strip cross_section."""
    return gf.cross_section.metal1(
        width=width,
        layer=layer,
        radius=radius,
    )


@xsection
def metal5(
    width: float = 0.2,
    layer: LayerSpec = "met5drawing",
    radius: float | None = None,
) -> CrossSection:
    """Return Metal Strip cross_section."""
    return gf.cross_section.metal1(
        width=width,
        layer=layer,
        radius=radius,
    )


route_bundle = partial(
    gf.routing.route_bundle_electrical, cross_section="metal1", auto_taper=False
)
route_bundle_metal1 = partial(route_bundle, cross_section="metal1")
route_bundle_metal2 = partial(route_bundle, cross_section="metal2")
route_bundle_metal3 = partial(route_bundle, cross_section="metal3")
route_bundle_metal4 = partial(route_bundle, cross_section="metal4")
route_bundle_metal5 = partial(route_bundle, cross_section="metal5")

routing_strategies = dict(
    route_bundle=route_bundle,
    route_bundle_metal1=route_bundle_metal1,
    route_bundle_metal2=route_bundle_metal2,
    route_bundle_metal3=route_bundle_metal3,
    route_bundle_metal4=route_bundle_metal4,
    route_bundle_metal5=route_bundle_metal5,
)


if __name__ == "__main__":
    print(cross_sections.keys())
