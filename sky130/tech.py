""" technology definitions """
import sys

from gdsfactory.cross_section import metal1, get_cross_section_factories
import gdsfactory as gf
from sky130.layers import LAYER


xs_metal1 = gf.partial(metal1, layer=LAYER.met1drawing, width=10.0)
xs_metal2 = gf.partial(metal1, layer=LAYER.met2drawing, width=10.0)


cross_sections = get_cross_section_factories(sys.modules[__name__])


if __name__ == "__main__":
    print(cross_sections.keys())
