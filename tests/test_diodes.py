import gdsfactory as gf

from sky130.layers import LAYER


def test_diode_pw2nd_instantiates():
    from sky130.pcells.diodes import sky130_fd_pr__diode_pw2nd_05v5

    c = sky130_fd_pr__diode_pw2nd_05v5()
    assert isinstance(c, gf.Component)


def test_diode_pw2nd_has_ports():
    from sky130.pcells.diodes import sky130_fd_pr__diode_pw2nd_05v5

    c = sky130_fd_pr__diode_pw2nd_05v5()
    port_names = {p.name for p in c.ports}
    assert "CATHODE" in port_names
    assert "ANODE" in port_names


def test_diode_pw2nd_has_diff():
    from sky130.pcells.diodes import sky130_fd_pr__diode_pw2nd_05v5

    c = sky130_fd_pr__diode_pw2nd_05v5()
    layers = set(c.get_polygons().keys())
    assert LAYER.diffdrawing in layers
    assert LAYER.nsdmdrawing in layers


def test_diode_pd2nw_instantiates():
    from sky130.pcells.diodes import sky130_fd_pr__diode_pd2nw_05v5

    c = sky130_fd_pr__diode_pd2nw_05v5()
    assert isinstance(c, gf.Component)


def test_diode_pd2nw_has_nwell():
    from sky130.pcells.diodes import sky130_fd_pr__diode_pd2nw_05v5

    c = sky130_fd_pr__diode_pd2nw_05v5()
    layers = set(c.get_polygons().keys())
    assert LAYER.nwelldrawing in layers


def test_diode_pd2nw_has_ports():
    from sky130.pcells.diodes import sky130_fd_pr__diode_pd2nw_05v5

    c = sky130_fd_pr__diode_pd2nw_05v5()
    port_names = {p.name for p in c.ports}
    assert "ANODE" in port_names
    assert "CATHODE" in port_names
