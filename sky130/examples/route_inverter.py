from gdsfactory.config import cwd
import subprocess
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
import gdsfactory as gf
from sky130.routing_utils import route_multilayer_3d




def test_inverter() -> Component:
    pdk = get_active_pdk()
    c = Component("test_inverter")

    # Create instances
    instance1 = c.add_ref(pdk.get_component('pmos_5v', instance_name='pmos'), name='pmos')
    instance2 = c.add_ref(pdk.get_component('nmos_5v', instance_name='nmos'), name='nmos')
    
    # Place instances
    instance1.move((5, 0))
    instance1.mirror_y(instance1.dcenter[1])
    instance2.move((0, 0))

    # Important to add ports ONLY after finished moving instances
    c.add_ports(instance1)
    c.add_ports(instance2)

    # Add routing area markers to ensure grid extends beyond the obstacle
    routing_area_layer = (235, 4)  # Dummy layer for grid extent
    c.add_polygon([(-50, -20), (110, -20), (110, 50), (-50, 50)], layer=routing_area_layer)

    # Grid resolution for A* pathfinding
    grid_unit_um = 1.0    # 1um grid resolution
    # Wire width is auto-detected from port polygon geometry
    
    # Layers to avoid - ALL metal on these layers including device metal
    # The router must route around everything on both M1 and M2
    layers_to_avoid = [(68, 20), (69, 20)]

    print("Routing with 3D multi-layer A* (M1=H, M2=V with via transitions)...")

    # Route 1: PMOS DRAIN -> NMOS DRAIN (output net)
    route_multilayer_3d(
        c,
        start=instance1.ports['pmos_DRAIN'],
        stop=instance2.ports['nmos_DRAIN'],
        grid_unit=grid_unit_um,
        layers_to_avoid=layers_to_avoid,
        add_segment_ports=True,
        port_name_prefix="out"
    )

    # Route 2: PMOS GATE -> NMOS GATE (input net)
    route_multilayer_3d(
        c,
        start=instance1.ports['pmos_GATE'],
        stop=instance2.ports['nmos_GATE'],
        grid_unit=grid_unit_um,
        layers_to_avoid=layers_to_avoid,
        add_segment_ports=True,
        port_name_prefix="in"
    )

    # Route 3: PMOS SOURCE -> PMOS BODY (VDD)
    route_multilayer_3d(
        c,
        start=instance1.ports['pmos_SOURCE'],
        stop=instance1.ports['pmos_BODY'],
        grid_unit=grid_unit_um,
        layers_to_avoid=layers_to_avoid,
        add_segment_ports=True,
        port_name_prefix="vdd"
    )

    # Route 4: NMOS SOURCE -> NMOS BODY (VSS)
    route_multilayer_3d(
        c,
        start=instance2.ports['nmos_SOURCE'],
        stop=instance2.ports['nmos_BODY'],
        grid_unit=grid_unit_um,
        layers_to_avoid=layers_to_avoid,
        add_segment_ports=True,
        port_name_prefix="vss"
    )

    # Add instance labels
    add_instance_label(c, instance1, instance_name='pmos')
    add_instance_label(c, instance2, instance_name='nmos')

    return c

if __name__ == "__main__":
    c = test_inverter()
    c.flatten()
    c.pprint_ports()
    c.show()
    input("Press Enter to continue...")
    c.write_gds("./results/test_inverter.gds", with_metadata=False)
    with open("./results/read_gds.tcl", "w") as f:
        f.write("box 0um 0um 0um 0um\n")
        f.write("gds read /home/flow/Vibe/gf-skywater130/results/test_inverter.gds\n")
        f.write("load test_inverter\n")
        f.write("select top cell\n")
        f.write("extract do local\n")
        f.write("extract all\n")
        f.write("ext2spice lvs\n")
        f.write("ext2spice -o test_inverter.sp\n")
    subprocess.run("magic -rcfile /usr/local/share/pdk/sky130A/libs.tech/magic/sky130A.magicrc ./read_gds.tcl".split(), cwd="/home/flow/Vibe/gf-skywater130/results")
    

