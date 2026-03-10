import argparse
import sys
from pathlib import Path

# Load environment variables from .env file (must be before doroutes import)
from dotenv import load_dotenv
load_dotenv(Path(__file__).parent.parent.parent / ".env")

sys.path.append(str(Path(__file__).parent.parent.parent))

from gdsfactory.component import Component
import sky130
from gdsfactory.pdk import get_active_pdk
from gdsfactory.add_pins import add_instance_label
from sky130.routing_utils import RouteNetSpec, route_nets_deterministic_copy


INVERTER_SCHEMATIC = """\
* Schematic netlist for LVS: test_inverter
.subckt test_inverter
X0 nmos_SOURCE pmos_GATE pmos_DRAIN nmos_SOURCE sky130_fd_pr__nfet_g5v0d10v5 w=0.75 l=0.5
X1 pmos_SOURCE pmos_GATE pmos_DRAIN pmos_SOURCE sky130_fd_pr__pfet_g5v0d10v5 w=0.75 l=0.5
.ends test_inverter
"""




def test_inverter(
    pmos_offset: tuple[float, float] = (0.0, 5.0),
    component_name: str = "test_inverter",
    add_segment_ports: bool = True,
    routing_half_extent: float = 15.0,
    grid_unit_um: float = 1.0,
    mirror_pmos: bool = True,
) -> Component:
    pdk = get_active_pdk()
    c = Component(component_name)

    # Create instances
    instance1 = c.add_ref(pdk.get_component('pmos_5v', instance_name='pmos'), name='pmos')
    instance2 = c.add_ref(pdk.get_component('nmos_5v', instance_name='nmos'), name='nmos')
    
    # Place instances
    instance1.move(pmos_offset)
    if mirror_pmos:
        instance1.mirror_y(instance1.dcenter[1])
    instance2.move((0, 0))

    # Important to add ports ONLY after finished moving instances
    c.add_ports(instance1)
    c.add_ports(instance2)

    # Add routing area markers to ensure grid extends beyond the obstacle
    routing_area_layer = (235, 4)  # Dummy layer for grid extent
    c.add_polygon(
        [
            (-routing_half_extent, -routing_half_extent),
            (routing_half_extent, -routing_half_extent),
            (routing_half_extent, routing_half_extent),
            (-routing_half_extent, routing_half_extent),
        ],
        layer=routing_area_layer,
    )

    # Grid resolution for A* pathfinding
    # Wire width is auto-detected from port polygon geometry
    
    # Layers to avoid - ALL metal on these layers including device metal
    # The router must route around everything on both M1 and M2
    layers_to_avoid = [(68, 20), (69, 20)]

    print("Routing with 3D multi-layer A* (M1=H, M2=V with via transitions)...")

    nets = [
        RouteNetSpec(
            name="out",
            start=instance1.ports["pmos_DRAIN"],
            stop=instance2.ports["nmos_DRAIN"],
            port_name_prefix="out",
        ),
        RouteNetSpec(
            name="in",
            start=instance1.ports["pmos_GATE"],
            stop=instance2.ports["nmos_GATE"],
            port_name_prefix="in",
        ),
        RouteNetSpec(
            name="vdd",
            start=instance1.ports["pmos_SOURCE"],
            stop=instance1.ports["pmos_BODY"],
            port_name_prefix="vdd",
        ),
        RouteNetSpec(
            name="vss",
            start=instance2.ports["nmos_SOURCE"],
            stop=instance2.ports["nmos_BODY"],
            port_name_prefix="vss",
        ),
    ]

    c, _ = route_nets_deterministic_copy(
        c,
        nets=nets,
        grid_unit=grid_unit_um,
        dynamic_width=True,
        layers_to_avoid=layers_to_avoid,
        add_segment_ports=add_segment_ports,
        require_all=True,
        deterministic=True,
    )

    # Reacquire instances after routing attempts to avoid stale reference handles.
    add_instance_label(c, c.insts["pmos"], instance_name='pmos')
    add_instance_label(c, c.insts["nmos"], instance_name='nmos')

    return c


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Route inverter example (headless by default).")
    parser.add_argument(
        "--skip-lvs",
        action="store_true",
        help="Skip LVS run after writing GDS.",
    )
    parser.add_argument(
        "--out-gds",
        default="./results/test_inverter.gds",
        help="Output GDS path.",
    )
    args = parser.parse_args()

    c = test_inverter(
        component_name="test_inverter",
        add_segment_ports=False,
        pmos_offset=(0.0, 5.0),
        mirror_pmos=True,
    )
    c.flatten()
    c.pprint_ports()
    c.show()
    gds_path = Path(args.out_gds)
    gds_path.parent.mkdir(parents=True, exist_ok=True)
    c.write_gds(str(gds_path), with_metadata=False)
    print(f"[OK] Wrote {gds_path}")
    if args.skip_lvs:
        print("[INFO] Skipping LVS (--skip-lvs)")
    else:
        from sky130.examples.lvs_magic_utils import run_lvs

        run_lvs(gds_path, "test_inverter", INVERTER_SCHEMATIC)
