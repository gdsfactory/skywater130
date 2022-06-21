"""sky130 - skywater gdsfactory pdk"""
import pathlib

from gdsfactory.config import logger
from gdsfactory.get_factories import get_cells
from gdsfactory.pdk import Pdk

from sky130 import components
from sky130.config import PATH, module_path
from sky130.layers import LAYER
from sky130.tech import cross_sections

__version__ = "0.0.12"

cells = get_cells(components)
PDK = Pdk(
    name="sky130",
    cells=cells,
    cross_sections=cross_sections,
    layers=LAYER.dict(),
    sparameters_path=PATH.sparameters,
)
PDK.register_cells_yaml(dirpath=pathlib.Path(__file__).parent.absolute())
PDK.activate()

logger.info(f"load sky130 PDK {__version__!r} installed at {str(module_path)!r}")

__all__ = ["cells", "PDK"]

if __name__ == "__main__":
    f = PDK.cells
    print(f.keys())
