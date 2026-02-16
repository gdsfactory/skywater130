
import gdsfactory as gf
from gdsfactory.typings import LayerSpec


@gf.cell
def waypoint(
    width: float = 0.2,
    layer: LayerSpec = (235, 4),
    instance_name: str = "",
) -> gf.Component:
    """Returns a waypoint square with ports exposed.

    Args:
        width: width of the square.
        layer: layer of the square.
        instance_name: unique name for the instance.
    """
    c = gf.Component()
    c.add_ref(gf.components.rectangle(size=(width, width), layer=layer))

    port_prefix = f"{instance_name}_" if instance_name else ""
    c.add_port(f"{port_prefix}waypoint", center=(width / 2, width / 2), width=0.01, orientation=180, layer=layer, port_type="electrical")
   #c.add_port("e1", center=(width, width / 2), width=width, orientation=0, layer=layer)
   #c.add_port(
   #    "e2", center=(width / 2, width), width=width, orientation=90, layer=layer
   #)
   #c.add_port(
   #    "e3", center=(0, width / 2), width=width, orientation=180, layer=layer
   #)
   #c.add_port(
   #    "e4", center=(width / 2, 0), width=width, orientation=270, layer=layer
   #)
    c.pprint_ports()
    c.draw_ports()
    return c

if __name__ == "__main__":
    import sys
    import pathlib

    # Add project root to path so we can import sky130
    sys.path.append(str(pathlib.Path(__file__).parent.parent.parent))

    import sky130

    c = waypoint()
    c.show()