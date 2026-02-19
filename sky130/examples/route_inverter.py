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




def test_inverter(
    pmos_offset: tuple[float, float] = (5.0, 5.0),
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


def sweep_inverter_positions(step: float = 5.0) -> list[tuple[str, tuple[float, float], Component, str]]:
    """Sweep PMOS over 3x3 ring around NMOS center in clockwise order.

    Returns:
        List of (label, offset, component_or_none, error_message).
    """
    positions = [
        ("top_left", (-step, step)),
        ("top_middle", (0.0, step)),
        ("top_right", (step, step)),
        ("middle_right", (step, 0.0)),
        ("bottom_right", (step, -step)),
        ("bottom_middle", (0.0, -step)),
        ("bottom_left", (-step, -step)),
        ("middle_left", (-step, 0.0)),
    ]

    interactive = sys.stdin.isatty() and sys.stdout.isatty()
    results = []
    retry_profiles = [
        (15.0, 1.0),
        (30.0, 1.0),
        (50.0, 1.0),
        (50.0, 0.5),
    ]

    for idx, (label, offset) in enumerate(positions, start=1):
        print(f"\n[{idx}/{len(positions)}] Routing position '{label}' at offset={offset}")
        c = None
        err = ""
        for attempt_idx, (half_extent, grid_unit) in enumerate(retry_profiles, start=1):
            print(
                f"[{label}] attempt {attempt_idx}/{len(retry_profiles)} "
                f"window=+/-{half_extent}um grid={grid_unit}um"
            )
            try:
                c = test_inverter(
                    pmos_offset=offset,
                    component_name=f"test_inverter_{label}_a{attempt_idx}",
                    add_segment_ports=False,
                    routing_half_extent=half_extent,
                    grid_unit_um=grid_unit,
                    mirror_pmos=not label.startswith("middle_"),
                )
                err = ""
                break
            except Exception as e:
                c = None
                err = str(e)
                print(f"[{label}] attempt {attempt_idx} failed: {err}")

        if c is not None:
            c.flatten()
            c.pprint_ports()
            if interactive:
                c.show()
                input(f"Breakpoint at '{label}'. Press Enter to continue...")
            gds_path = f"./results/test_inverter_{label}.gds"
            c.write_gds(gds_path, with_metadata=False)
            results.append((label, offset, c, ""))
            print(f"[OK] Wrote {gds_path}")
        else:
            print(f"[FAIL] {label}: {err}")
            results.append((label, offset, None, err))
            if interactive:
                input(f"Breakpoint at failed '{label}'. Press Enter to continue...")

    return results

if __name__ == "__main__":
    results = sweep_inverter_positions(step=5.0)
    ok = sum(1 for _, _, c, _ in results if c is not None)
    fail = len(results) - ok
    print(f"\nSweep complete: {ok} succeeded, {fail} failed.")
    
