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


CURRENT_MIRROR_SCHEMATIC = """\
* Schematic netlist for LVS: test_current_mirror
.subckt test_current_mirror
Xref_bot stack_ref gate_bot vss vss sky130_fd_pr__nfet_g5v0d10v5 w=0.75 l=0.5
Xref_top nref_top_d gate_top stack_ref vss sky130_fd_pr__nfet_g5v0d10v5 w=0.75 l=0.5
Xout_bot stack_out gate_bot vss vss sky130_fd_pr__nfet_g5v0d10v5 w=0.75 l=0.5
Xout_top nout_top_d gate_top stack_out vss sky130_fd_pr__nfet_g5v0d10v5 w=0.75 l=0.5
.ends test_current_mirror
"""


def test_current_mirror(
    component_name: str = "test_current_mirror",
    add_segment_ports: bool = True,
    routing_half_extent: float = 25.0,
    grid_unit_um: float = 1.0,
    col_pitch_um: float = 14.0,
    row_pitch_um: float = 14.0,
    dynamic_width: bool = False,
) -> Component:
    pdk = get_active_pdk()
    c = Component(component_name)

    # 4T NMOS cascode mirror: two stacked NMOS in reference and output branches.
    nmos_ref_bot = c.add_ref(
        pdk.get_component("nmos_5v", instance_name="nmos_ref_bot"), name="nmos_ref_bot"
    )
    nmos_ref_top = c.add_ref(
        pdk.get_component("nmos_5v", instance_name="nmos_ref_top"), name="nmos_ref_top"
    )
    nmos_out_bot = c.add_ref(
        pdk.get_component("nmos_5v", instance_name="nmos_out_bot"), name="nmos_out_bot"
    )
    nmos_out_top = c.add_ref(
        pdk.get_component("nmos_5v", instance_name="nmos_out_top"), name="nmos_out_top"
    )

    # Place in 2x2 branch grid.
    nmos_ref_bot.move((0.0, 0.0))
    nmos_ref_top.move((0.0, row_pitch_um))
    nmos_out_bot.move((col_pitch_um, 0.0))
    nmos_out_top.move((col_pitch_um, row_pitch_um))

    # Add routing area marker to ensure grid extends beyond the obstacle region
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

    # Layers to avoid - ALL metal on these layers including device metal
    layers_to_avoid = [(68, 20), (69, 20)]

    print("Routing 4T cascode current mirror with 3D multi-layer A* (M1=H, M2=V with via transitions)...")

    # Core cascode-mirror connectivity:
    # - stacked branches (ref/out)
    # - shared gate biases (bottom and top cascode)
    nets = [
        RouteNetSpec(
            name="stack_ref",
            start=nmos_ref_bot.ports["nmos_ref_bot_DRAIN"],
            stop=nmos_ref_top.ports["nmos_ref_top_SOURCE"],
            port_name_prefix="stack_ref",
        ),
        RouteNetSpec(
            name="stack_out",
            start=nmos_out_bot.ports["nmos_out_bot_DRAIN"],
            stop=nmos_out_top.ports["nmos_out_top_SOURCE"],
            port_name_prefix="stack_out",
        ),
        RouteNetSpec(
            name="bias_bot_gate",
            start=nmos_ref_bot.ports["nmos_ref_bot_GATE"],
            stop=nmos_out_bot.ports["nmos_out_bot_GATE"],
            port_name_prefix="bias_bot_gate",
        ),
        RouteNetSpec(
            name="bias_top_gate",
            start=nmos_ref_top.ports["nmos_ref_top_GATE"],
            stop=nmos_out_top.ports["nmos_out_top_GATE"],
            port_name_prefix="bias_top_gate",
        ),
        RouteNetSpec(
            name="vss_src_join",
            start=nmos_ref_bot.ports["nmos_ref_bot_SOURCE"],
            stop=nmos_out_bot.ports["nmos_out_bot_SOURCE"],
            port_name_prefix="vss_src_join",
        ),
        RouteNetSpec(
            name="vss_body_ref_bot",
            start=nmos_ref_bot.ports["nmos_ref_bot_SOURCE"],
            stop=nmos_ref_bot.ports["nmos_ref_bot_BODY"],
            port_name_prefix="vss_body_ref_bot",
        ),
        RouteNetSpec(
            name="vss_body_out_bot",
            start=nmos_out_bot.ports["nmos_out_bot_SOURCE"],
            stop=nmos_out_bot.ports["nmos_out_bot_BODY"],
            port_name_prefix="vss_body_out_bot",
        ),
        RouteNetSpec(
            name="vss_body_ref_top",
            start=nmos_ref_bot.ports["nmos_ref_bot_SOURCE"],
            stop=nmos_ref_top.ports["nmos_ref_top_BODY"],
            port_name_prefix="vss_body_ref_top",
        ),
        RouteNetSpec(
            name="vss_body_out_top",
            start=nmos_out_bot.ports["nmos_out_bot_SOURCE"],
            stop=nmos_out_top.ports["nmos_out_top_BODY"],
            port_name_prefix="vss_body_out_top",
        ),
    ]

    c, _ = route_nets_deterministic_copy(
        c,
        nets=nets,
        grid_unit=grid_unit_um,
        dynamic_width=dynamic_width,
        layers_to_avoid=layers_to_avoid,
        add_segment_ports=add_segment_ports,
        require_all=True,
        deterministic=True,
    )

    # Reacquire instances after routing attempts to avoid stale reference handles.
    add_instance_label(c, c.insts["nmos_ref_bot"], instance_name="nmos_ref_bot")
    add_instance_label(c, c.insts["nmos_ref_top"], instance_name="nmos_ref_top")
    add_instance_label(c, c.insts["nmos_out_bot"], instance_name="nmos_out_bot")
    add_instance_label(c, c.insts["nmos_out_top"], instance_name="nmos_out_top")

    return c


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Route current mirror example (headless by default).")
    parser.add_argument(
        "--skip-lvs",
        action="store_true",
        help="Skip LVS run after writing GDS.",
    )
    parser.add_argument(
        "--out-gds",
        default="./results/test_current_mirror.gds",
        help="Output GDS path.",
    )
    args = parser.parse_args()

    c = test_current_mirror(
        component_name="test_current_mirror",
        add_segment_ports=False,
        routing_half_extent=25.0,
        grid_unit_um=1.0,
        col_pitch_um=14.0,
        row_pitch_um=14.0,
        dynamic_width=False,
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
        from sky130.examples.lvs_graph_checks import check_current_mirror_layout_graph
        from sky130.examples.lvs_magic_utils import run_lvs

        run_lvs(
            gds_path,
            "test_current_mirror",
            CURRENT_MIRROR_SCHEMATIC,
            graph_check_fn=check_current_mirror_layout_graph,
        )

