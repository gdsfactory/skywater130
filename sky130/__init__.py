"""sky130 - skywater gdsfactory pdk"""
import gdsfactory as gf
from gdsfactory.config import logger
from gdsfactory.get_factories import get_cells
from gdsfactory.pdk import Pdk

from sky130 import components
from sky130.config import module_path
from sky130.tech import cross_sections

__version__ = "0.0.4"

gf.asserts.version(">=5.2.5")

cells = get_cells(components)
PDK = Pdk(name="sky130", cells=cells, cross_sections=cross_sections)
gf.set_active_pdk(PDK)

logger.info(f"load sky130 PDK {__version__!r} installed at {str(module_path)!r}")

__all__ = ["cells", "PDK"]
