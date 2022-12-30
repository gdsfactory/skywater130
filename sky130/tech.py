""" technology definitions."""
import sys

import gdsfactory as gf
from gdsfactory.cross_section import get_cross_section_factories, metal1

from sky130.layers import LAYER

xs_metal1 = gf.partial(metal1, layer=LAYER.met1drawing, width=0.2)
xs_metal2 = gf.partial(metal1, layer=LAYER.met2drawing, width=0.2)
strip = xs_metal1
cross_sections = get_cross_section_factories(sys.modules[__name__])


if __name__ == "__main__":
    print(cross_sections.keys())
