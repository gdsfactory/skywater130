from __future__ import annotations

from collections import defaultdict

from gdsfactory import Component
from gdsfactory.add_pins import AddPinFunction, add_pin_rectangle_inside
from gdsfactory.typings import LayerSpec
from kfactory.exceptions import LockedError


def add_pins(
    component: Component, port_pin_mapping: dict[str, list[str]] | None = None
) -> None:
    """Register logical electrical pins with per-metal label layers."""
    from sky130.layers import LAYER  # noqa: PLC0415

    _add_electric_pins(
        component,
        port_pin_mapping=port_pin_mapping,
        pin_label_layer_map={
            LAYER.polydrawing: LAYER.polylabel,
            LAYER.li1drawing: LAYER.li1label,
            LAYER.met1drawing: LAYER.met1label,
            LAYER.met2drawing: LAYER.met2label,
            LAYER.met3drawing: LAYER.met3label,
            LAYER.met4drawing: LAYER.met4label,
            LAYER.met5drawing: LAYER.met5label,
        },
    )


# TODO: replace _add_electric_pins with gdsfactory.add_pins.add_electric_pins in next gdsfactory release
def _add_electric_pins(
    component: Component,
    port_pin_mapping: dict[str, list[str]] | None = None,
    pin_layer_map: dict[LayerSpec, LayerSpec] | None = None,
    pin_label_layer_map: dict[LayerSpec, LayerSpec] | None = None,
    default_pin_layer: LayerSpec | None = None,
    default_label_layer: LayerSpec | None = None,
    pin_function: AddPinFunction = add_pin_rectangle_inside,  # type: ignore[assignment]
    pin_type: str = "DC",
) -> None:
    """Draw pin markers and register logical pins for all electrical ports."""
    if port_pin_mapping is not None:
        by_name: dict[str, list] = {
            pin_name: [component.ports[pn] for pn in port_names]
            for pin_name, port_names in port_pin_mapping.items()
        }
    else:
        by_name: dict[str, list] = defaultdict(list)
        [
            by_name[port.name].append(port)
            for port in component.ports
            if port.port_type == "electrical"
        ]

    for name, ports in by_name.items():
        for port in ports:
            pin_layer = (
                pin_layer_map.get(port.layer) if pin_layer_map else default_pin_layer
            )
            label_layer = (
                pin_label_layer_map.get(port.layer)
                if pin_label_layer_map
                else default_label_layer
            )
            if pin_layer or label_layer:
                try:
                    pin_function(
                        component, port, layer=pin_layer, layer_label=label_layer
                    )
                except LockedError:
                    pass
        existing_pin_names = {pin.name for pin in component.pins}
        if name not in existing_pin_names:
            component.create_pin(ports=ports, name=name, pin_type=pin_type)
