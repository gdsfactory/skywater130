"""Technology definitions."""

import sys
from functools import partial

import gdsfactory as gf
from gdsfactory.cross_section import get_cross_sections, metal1

from sky130.layers import LAYER

metal1 = gf.partial(metal1, layer=LAYER.met1drawing, width=0.2)
metal2 = gf.partial(metal1, layer=LAYER.met2drawing, width=0.2)
metal3 = gf.partial(metal1, layer=LAYER.met3drawing, width=0.2)
metal4 = gf.partial(metal1, layer=LAYER.met4drawing, width=0.2)
metal5 = gf.partial(metal1, layer=LAYER.met5drawing, width=0.2)

cross_sections = get_cross_sections(sys.modules[__name__])

route_bundle = partial(gf.routing.route_bundle, cross_section="metal1")
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
