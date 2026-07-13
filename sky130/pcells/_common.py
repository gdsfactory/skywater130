from __future__ import annotations

import gdsfactory as gf
from gdsfactory.add_pins import add_pin_rectangle_inside

from sky130.layers import LAYER

_LAYER_MAP = {
    LAYER.polydrawing: LAYER.polypin,
    LAYER.li1drawing: LAYER.li1pin,
    LAYER.met1drawing: LAYER.met1pin,
    LAYER.met2drawing: LAYER.met2pin,
    LAYER.met3drawing: LAYER.met3pin,
    LAYER.met4drawing: LAYER.met4pin,
    LAYER.met5drawing: LAYER.met5pin,
}


def _add_pins(c: gf.Component) -> None:
    """Draw pin rectangles and register logical pins for all electrical ports."""
    by_name: dict[str, list] = {}
    for port in c.ports:
        if port.port_type == "electrical":
            by_name.setdefault(port.name, []).append(port)
    for name, ports in by_name.items():
        for port in ports:
            pin_layer = _LAYER_MAP.get(port.layer)
            if pin_layer:
                add_pin_rectangle_inside(c, port, layer=pin_layer, layer_label=None)
        c.create_pin(ports=ports, name=name)
