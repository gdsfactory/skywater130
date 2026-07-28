from __future__ import annotations

from functools import partial

from gdsfactory.add_pins import add_electric_pins

from sky130.layers import LAYER

# NOTE: pin_layer_map values are set to None to skip Pin geometry drawing
# on the respective Pin layers, avoiding XOR-diff test failures for now.
# Only logical schematic pin aggregation of the ports is performed via
# component.create_pin(). A future pass will add actual Pin geometry on
# the PDK's pin drawing layers.
_add_pins = partial(
    add_electric_pins,
    pin_layer_map={
        LAYER.polydrawing: None,
        LAYER.li1drawing: None,
        LAYER.met1drawing: None,
        LAYER.met2drawing: None,
        LAYER.met3drawing: None,
        LAYER.met4drawing: None,
        LAYER.met5drawing: None,
    },
)
