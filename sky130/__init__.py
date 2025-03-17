"""sky130 - skywater gdsfactory pdk"""

import pathlib

import gdsfactory as gf
from gdsfactory.get_factories import get_cells
from gdsfactory.pdk import Pdk

from sky130 import components, pcells
from sky130.layers import LAYER, LAYER_STACK, LAYER_VIEWS
from sky130.tech import cross_sections

__version__ = "0.13.1"

gf.CONF.allow_layer_mismatch = True
gf.CONF.allow_width_mismatch = True

cells = get_cells([components, pcells])
PDK = Pdk(
    name="sky130",
    cells=cells,
    cross_sections=cross_sections,
    layers=LAYER,
    layer_stack=LAYER_STACK,
    layer_views=LAYER_VIEWS,
)
PDK.register_cells_yaml(dirpath=pathlib.Path(__file__).parent.absolute())
PDK.activate()

__all__ = ["cells", "PDK", "components"]

if __name__ == "__main__":
    f = PDK.cells
    print(f.keys())
    # import gdsfactory as gf

    # script = gf.write_cells.get_import_gds_script("gds", module="sky130.components")
    # filepath = pathlib.Path("components2.py")
    # filepath.write_text(script)
    # print(script)
