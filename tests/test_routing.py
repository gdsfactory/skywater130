"""Every routing strategy registered in the PDK must draw a connected route."""

import warnings

import gdsfactory as gf
import klayout.db as kdb
import pytest

from sky130 import PDK
from sky130.tech import routing_strategies

ROUTING_AREA_LAYER = (235, 4)

# port b (center, orientation) for a route starting at (0, 0) facing east
CASES = {
    "straight": ((30, 0), 180),
    "s_bend": ((30, 20), 180),
}


def _cross_section_name(strategy) -> str:
    keywords = getattr(strategy, "keywords", {})
    return keywords.get("cross_section", "metal1")


def _params():
    for strategy_name in sorted(routing_strategies):
        for case in CASES:
            marks = []
            if strategy_name.startswith("route_astar") and case != "straight":
                marks = pytest.mark.xfail(
                    strict=True,
                    reason="route_astar searches port-to-port, so the grid path "
                    "turns past the port standoff and route_single stops early",
                )
            yield pytest.param(strategy_name, case, marks=marks)


@pytest.mark.parametrize(("strategy_name", "case"), _params())
def test_routing_strategy_draws_route(strategy_name: str, case: str) -> None:
    PDK.activate()
    strategy = routing_strategies[strategy_name]
    xs = gf.get_cross_section(_cross_section_name(strategy))
    center_b, orientation_b = CASES[case]

    c = gf.Component()
    # give the A* grid an area to route in
    c.add_polygon(
        [(-10, -10), (40, -10), (40, 30), (-10, 30)], layer=ROUTING_AREA_LAYER
    )
    c.add_port(
        "a",
        center=(0, 0),
        width=xs.width,
        orientation=0,
        layer=xs.layer,
        port_type="electrical",
    )
    c.add_port(
        "b",
        center=center_b,
        width=xs.width,
        orientation=orientation_b,
        layer=xs.layer,
        port_type="electrical",
    )

    with warnings.catch_warnings():
        warnings.simplefilter("error")
        if strategy_name.startswith("route_astar"):
            strategy(c, c.ports["a"], c.ports["b"])
        else:
            strategy(c, [c.ports["a"]], [c.ports["b"]])

    metal = kdb.Region(c.begin_shapes_rec(gf.get_layer(xs.layer))).merged()
    assert not metal.is_empty(), f"{strategy_name} drew nothing on {xs.layer}"
    assert metal.count() == 1, f"{strategy_name} route is not connected"

    for port in c.ports:
        p = port.to_itype()
        probe = kdb.Region(kdb.Box(p.x - 1, p.y - 1, p.x + 1, p.y + 1))
        assert not (probe & metal).is_empty(), (
            f"{strategy_name} route does not reach port {port.name}"
        )
