"""Technology definitions."""

import sys

import gdsfactory as gf
from gdsfactory.cross_section import get_cross_sections, metal1

from sky130.layers import LAYER

xf_metal1 = gf.partial(metal1, layer=LAYER.met1drawing, width=0.2)
xf_metal2 = gf.partial(metal1, layer=LAYER.met2drawing, width=0.2)


xs_metal1 = xf_metal1()
xs_metal2 = xf_metal2()

cross_sections = get_cross_sections(sys.modules[__name__])


if __name__ == "__main__":
    print(cross_sections.keys())
