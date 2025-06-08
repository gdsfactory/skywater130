"""Sky130 - skywater gdsfactory pdk"""

import gdsfactory as gf
from gdsfactory.get_factories import get_cells
from gdsfactory.pdk import Pdk

from sky130 import components, pcells
from sky130.layers import LAYER, LAYER_STACK, LAYER_VIEWS, connectivity
from sky130.tech import cross_sections, routing_strategies

__version__ = "0.15.0"

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
    routing_strategies=routing_strategies,
    connectivity=connectivity,
)
PDK.activate()

__all__ = [
    "cells",
    "PDK",
    "components",
    "pcells",
    "LAYER",
    "LAYER_STACK",
]
