import gdsfactory as gf
from sky130.layers import LAYER


def test_npn_instantiates():
    from sky130.pcells.bjts import sky130_fd_pr__npn_05v5
    c = sky130_fd_pr__npn_05v5()
    assert isinstance(c, gf.Component)


def test_npn_has_ports():
    from sky130.pcells.bjts import sky130_fd_pr__npn_05v5
    c = sky130_fd_pr__npn_05v5()
    port_names = {p.name for p in c.ports}
    assert "EMITTER" in port_names
    assert "BASE" in port_names
    assert "COLLECTOR" in port_names


def test_npn_has_nwell():
    from sky130.pcells.bjts import sky130_fd_pr__npn_05v5
    c = sky130_fd_pr__npn_05v5()
    layers = set(c.get_polygons().keys())
    assert LAYER.nwelldrawing in layers


def test_pnp_instantiates():
    from sky130.pcells.bjts import sky130_fd_pr__pnp_05v5
    c = sky130_fd_pr__pnp_05v5()
    assert isinstance(c, gf.Component)


def test_pnp_has_ports():
    from sky130.pcells.bjts import sky130_fd_pr__pnp_05v5
    c = sky130_fd_pr__pnp_05v5()
    port_names = {p.name for p in c.ports}
    assert "EMITTER" in port_names
    assert "BASE" in port_names
    assert "COLLECTOR" in port_names
