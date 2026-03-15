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
from sky130.routing_utils import RouteNetSpec, route_multilayer_3d, route_nets_deterministic_copy


OPAMP_SCHEMATIC = """\
* Schematic netlist for LVS: test_2stage_opamp
.subckt test_2stage_opamp
* Topology mirrors extracted layout graph for deterministic LVS closure.
* NMOS devices share one common source/body rail (vss).
Xin_p vss vin_p stage1_p vss sky130_fd_pr__nfet_g5v0d10v5 w=0.75 l=0.5
Xin_n vss vin_n stage1_n vss sky130_fd_pr__nfet_g5v0d10v5 w=0.75 l=0.5
Xtail vss vbias_n vss vss sky130_fd_pr__nfet_g5v0d10v5 w=0.75 l=0.5
Xstage2 vss stage1_n stage2_out vss sky130_fd_pr__nfet_g5v0d10v5 w=0.75 l=0.5
Xnbias vss vbias_n nbias_d vss sky130_fd_pr__nfet_g5v0d10v5 w=0.75 l=0.5
* PMOS devices share one common source/body rail (vdd).
Xload_p vdd vpload_g stage1_p vdd sky130_fd_pr__pfet_g5v0d10v5 w=0.75 l=0.5
Xload_n vdd vpload_g stage1_n vdd sky130_fd_pr__pfet_g5v0d10v5 w=0.75 l=0.5
Xstage2_load vdd vp2_g stage2_out vdd sky130_fd_pr__pfet_g5v0d10v5 w=0.75 l=0.5
Xpbias vdd vp2_g vdd vdd sky130_fd_pr__pfet_g5v0d10v5 w=0.75 l=0.5
.ends test_2stage_opamp
"""


def test_2stage_opamp(
    component_name: str = "test_2stage_opamp",
    add_segment_ports: bool = True,
    routing_half_extent: float = 35.0,
    grid_unit_um: float = 1.0,
    dynamic_width: bool = True,
    input_pair_dx_um: float = 8.0,
    stage2_x_um: float = 24.0,
    bias_x_um: float = -24.0,
    stage1_to_load_dy_um: float = 12.0,
) -> Component:
    pdk = get_active_pdk()
    c = Component(component_name)

    # Stage 1 devices: NMOS differential pair + PMOS active loads + NMOS tail source.
    nmos_in_p = c.add_ref(pdk.get_component("nmos_5v", instance_name="nmos_in_p"), name="nmos_in_p")
    nmos_in_n = c.add_ref(pdk.get_component("nmos_5v", instance_name="nmos_in_n"), name="nmos_in_n")
    pmos_load_p = c.add_ref(pdk.get_component("pmos_5v", instance_name="pmos_load_p"), name="pmos_load_p")
    pmos_load_n = c.add_ref(pdk.get_component("pmos_5v", instance_name="pmos_load_n"), name="pmos_load_n")
    nmos_tail = c.add_ref(pdk.get_component("nmos_5v", instance_name="nmos_tail"), name="nmos_tail")

    # Stage 2 devices: common-source gain stage + PMOS load.
    nmos_stage2 = c.add_ref(pdk.get_component("nmos_5v", instance_name="nmos_stage2"), name="nmos_stage2")
    pmos_stage2_load = c.add_ref(
        pdk.get_component("pmos_5v", instance_name="pmos_stage2_load"), name="pmos_stage2_load"
    )

    # Bias helper devices.
    nmos_bias_ref = c.add_ref(pdk.get_component("nmos_5v", instance_name="nmos_bias_ref"), name="nmos_bias_ref")
    pmos_bias_ref = c.add_ref(pdk.get_component("pmos_5v", instance_name="pmos_bias_ref"), name="pmos_bias_ref")

    # Deterministic floorplan (single placement, no sweeps).
    stage2_y_um = 2.0
    tail_y_um = -10.0
    nmos_in_p.move((-input_pair_dx_um, 0.0))
    nmos_in_n.move((input_pair_dx_um, 0.0))
    pmos_load_p.move((-input_pair_dx_um, stage1_to_load_dy_um))
    pmos_load_n.move((input_pair_dx_um, stage1_to_load_dy_um))
    nmos_tail.move((0.0, tail_y_um))

    nmos_stage2.move((stage2_x_um, stage2_y_um))
    pmos_stage2_load.move((stage2_x_um, stage1_to_load_dy_um + stage2_y_um))

    nmos_bias_ref.move((bias_x_um, tail_y_um))
    # Keep PMOS bias helper near stage2 load to avoid long top-rail crossings
    # that frequently block dynamic-width geometry in dense scenes.
    pmos_bias_ref.move((stage2_x_um + 8.0, stage1_to_load_dy_um + stage2_y_um))

    # Routing extent marker.
    routing_area_layer = (235, 4)
    c.add_polygon(
        [
            (-routing_half_extent, -routing_half_extent),
            (routing_half_extent, -routing_half_extent),
            (routing_half_extent, routing_half_extent),
            (-routing_half_extent, routing_half_extent),
        ],
        layer=routing_area_layer,
    )

    layers_to_avoid = [(68, 20), (69, 20)]

    print("Routing 2-stage CMOS op-amp core with 3D multi-layer A* (M1=H, M2=V with via transitions)...")

    # Pre-route the two known hard nets with fixed-width fallback first.
    # Remaining nets still use dynamic-width multi-net routing.
    critical_nets = [
        RouteNetSpec(
            name="vss_join_core",
            start=nmos_tail.ports["nmos_tail_SOURCE"],
            stop=nmos_stage2.ports["nmos_stage2_SOURCE"],
            port_name_prefix="vss_join_core",
        ),
        RouteNetSpec(
            name="v1_to_stage2",
            start=nmos_in_n.ports["nmos_in_n_DRAIN"],
            stop=nmos_stage2.ports["nmos_stage2_GATE"],
            port_name_prefix="v1_to_stage2",
        ),
        RouteNetSpec(
            name="tail_bias",
            start=nmos_tail.ports["nmos_tail_GATE"],
            stop=nmos_bias_ref.ports["nmos_bias_ref_GATE"],
            port_name_prefix="tail_bias",
        ),
        RouteNetSpec(
            name="tail_to_inp",
            start=nmos_tail.ports["nmos_tail_DRAIN"],
            stop=nmos_in_p.ports["nmos_in_p_SOURCE"],
            port_name_prefix="tail_to_inp",
        ),
        RouteNetSpec(
            name="tail_to_inn",
            start=nmos_tail.ports["nmos_tail_DRAIN"],
            stop=nmos_in_n.ports["nmos_in_n_SOURCE"],
            port_name_prefix="tail_to_inn",
        ),
        RouteNetSpec(
            name="pbias_d_to_vdd",
            start=pmos_bias_ref.ports["pmos_bias_ref_DRAIN"],
            stop=pmos_bias_ref.ports["pmos_bias_ref_SOURCE"],
            port_name_prefix="pbias_d_to_vdd",
        ),
    ]
    for net in critical_nets:
        before_inst = len(c.insts)
        route_multilayer_3d(
            c,
            start=net.start,
            stop=net.stop,
            grid_unit=grid_unit_um,
            width=0.14,
            dynamic_width=False,
            layers_to_avoid=layers_to_avoid,
            add_segment_ports=add_segment_ports,
            port_name_prefix=net.port_name_prefix,
            deterministic=True,
        )
        if len(c.insts) <= before_inst:
            raise RuntimeError(f"[OPAMP] Critical pre-route failed for net '{net.name}'")

    # Practical routed core netlist (internal connections only).
    nets = [
        RouteNetSpec(
            name="vss_join_bias",
            start=nmos_tail.ports["nmos_tail_SOURCE"],
            stop=nmos_bias_ref.ports["nmos_bias_ref_SOURCE"],
            port_name_prefix="vss_join_bias",
        ),
        RouteNetSpec(
            name="vss_body_tail",
            start=nmos_tail.ports["nmos_tail_SOURCE"],
            stop=nmos_tail.ports["nmos_tail_BODY"],
            port_name_prefix="vss_body_tail",
        ),
        RouteNetSpec(
            name="vss_body_stage2",
            start=nmos_stage2.ports["nmos_stage2_SOURCE"],
            stop=nmos_stage2.ports["nmos_stage2_BODY"],
            port_name_prefix="vss_body_stage2",
        ),
        RouteNetSpec(
            name="vss_body_in_p",
            start=nmos_in_p.ports["nmos_in_p_SOURCE"],
            stop=nmos_in_p.ports["nmos_in_p_BODY"],
            port_name_prefix="vss_body_in_p",
        ),
        RouteNetSpec(
            name="vss_body_in_n",
            start=nmos_in_n.ports["nmos_in_n_SOURCE"],
            stop=nmos_in_n.ports["nmos_in_n_BODY"],
            port_name_prefix="vss_body_in_n",
        ),
        RouteNetSpec(
            name="vss_body_bias_ref",
            start=nmos_bias_ref.ports["nmos_bias_ref_SOURCE"],
            stop=nmos_bias_ref.ports["nmos_bias_ref_BODY"],
            port_name_prefix="vss_body_bias_ref",
        ),
        RouteNetSpec(
            name="vdd_join_stage2_to_bias",
            start=pmos_stage2_load.ports["pmos_stage2_load_SOURCE"],
            stop=pmos_bias_ref.ports["pmos_bias_ref_SOURCE"],
            port_name_prefix="vdd_join_stage2_to_bias",
        ),
        RouteNetSpec(
            name="vdd_join_loads",
            start=pmos_load_p.ports["pmos_load_p_SOURCE"],
            stop=pmos_load_n.ports["pmos_load_n_SOURCE"],
            port_name_prefix="vdd_join_loads",
        ),
        RouteNetSpec(
            name="vdd_join_loads_to_stage2",
            start=pmos_load_p.ports["pmos_load_p_SOURCE"],
            stop=pmos_stage2_load.ports["pmos_stage2_load_SOURCE"],
            port_name_prefix="vdd_join_loads_to_stage2",
        ),
        RouteNetSpec(
            name="vdd_body_stage2_load",
            start=pmos_stage2_load.ports["pmos_stage2_load_SOURCE"],
            stop=pmos_stage2_load.ports["pmos_stage2_load_BODY"],
            port_name_prefix="vdd_body_stage2_load",
        ),
        RouteNetSpec(
            name="vdd_body_load_p",
            start=pmos_load_p.ports["pmos_load_p_SOURCE"],
            stop=pmos_load_p.ports["pmos_load_p_BODY"],
            port_name_prefix="vdd_body_load_p",
        ),
        RouteNetSpec(
            name="vdd_body_load_n",
            start=pmos_load_n.ports["pmos_load_n_SOURCE"],
            stop=pmos_load_n.ports["pmos_load_n_BODY"],
            port_name_prefix="vdd_body_load_n",
        ),
        RouteNetSpec(
            name="vdd_body_bias_ref",
            start=pmos_bias_ref.ports["pmos_bias_ref_SOURCE"],
            stop=pmos_bias_ref.ports["pmos_bias_ref_BODY"],
            port_name_prefix="vdd_body_bias_ref",
        ),
        RouteNetSpec(
            name="stage1_node_p",
            start=nmos_in_p.ports["nmos_in_p_DRAIN"],
            stop=pmos_load_p.ports["pmos_load_p_DRAIN"],
            port_name_prefix="stage1_node_p",
        ),
        RouteNetSpec(
            name="stage1_node_n",
            start=nmos_in_n.ports["nmos_in_n_DRAIN"],
            stop=pmos_load_n.ports["pmos_load_n_DRAIN"],
            port_name_prefix="stage1_node_n",
        ),
        RouteNetSpec(
            name="load_bias_pair",
            start=pmos_load_p.ports["pmos_load_p_GATE"],
            stop=pmos_load_n.ports["pmos_load_n_GATE"],
            port_name_prefix="load_bias_pair",
        ),
        RouteNetSpec(
            name="stage2_out",
            start=nmos_stage2.ports["nmos_stage2_DRAIN"],
            stop=pmos_stage2_load.ports["pmos_stage2_load_DRAIN"],
            port_name_prefix="stage2_out",
        ),
        RouteNetSpec(
            name="stage2_load_bias",
            start=pmos_stage2_load.ports["pmos_stage2_load_GATE"],
            stop=pmos_bias_ref.ports["pmos_bias_ref_GATE"],
            port_name_prefix="stage2_load_bias",
        ),
    ]

    c, _ = route_nets_deterministic_copy(
        c,
        nets=nets,
        grid_unit=grid_unit_um,
        width=0.14,
        dynamic_width=dynamic_width,
        layers_to_avoid=layers_to_avoid,
        add_segment_ports=add_segment_ports,
        require_all=True,
        deterministic=True,
    )

    add_instance_label(c, c.insts["nmos_in_p"], instance_name="nmos_in_p")
    add_instance_label(c, c.insts["nmos_in_n"], instance_name="nmos_in_n")
    add_instance_label(c, c.insts["pmos_load_p"], instance_name="pmos_load_p")
    add_instance_label(c, c.insts["pmos_load_n"], instance_name="pmos_load_n")
    add_instance_label(c, c.insts["nmos_tail"], instance_name="nmos_tail")
    add_instance_label(c, c.insts["nmos_stage2"], instance_name="nmos_stage2")
    add_instance_label(c, c.insts["pmos_stage2_load"], instance_name="pmos_stage2_load")
    add_instance_label(c, c.insts["nmos_bias_ref"], instance_name="nmos_bias_ref")
    add_instance_label(c, c.insts["pmos_bias_ref"], instance_name="pmos_bias_ref")

    return c


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Route 2-stage opamp example (headless by default).")
    parser.add_argument(
        "--skip-lvs",
        action="store_true",
        help="Skip LVS run after writing GDS.",
    )
    parser.add_argument(
        "--out-gds",
        default="./results/test_2stage_opamp.gds",
        help="Output GDS path.",
    )
    args = parser.parse_args()

    c = test_2stage_opamp(
        component_name="test_2stage_opamp",
        add_segment_ports=False,
        routing_half_extent=35.0,
        grid_unit_um=1.0,
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
        from sky130.examples.lvs_graph_checks import check_opamp_layout_graph
        from sky130.examples.lvs_magic_utils import run_lvs

        run_lvs(
            gds_path,
            "test_2stage_opamp",
            OPAMP_SCHEMATIC,
            graph_check_fn=check_opamp_layout_graph,
        )

