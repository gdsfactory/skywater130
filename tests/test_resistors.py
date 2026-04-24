import gdsfactory as gf

from sky130.layers import LAYER


def test_res_generic_po_instantiates():
    from sky130.pcells.resistors import sky130_fd_pr__res_generic_po

    c = sky130_fd_pr__res_generic_po()
    assert isinstance(c, gf.Component)


def test_res_generic_po_has_ports():
    from sky130.pcells.resistors import sky130_fd_pr__res_generic_po

    c = sky130_fd_pr__res_generic_po()
    port_names = {p.name for p in c.ports}
    assert "PLUS" in port_names
    assert "MINUS" in port_names


def test_res_generic_po_has_poly():
    from sky130.pcells.resistors import sky130_fd_pr__res_generic_po

    c = sky130_fd_pr__res_generic_po()
    layers = set(c.get_polygons().keys())
    assert LAYER.polydrawing in layers
    assert LAYER.licon1drawing in layers


def test_res_high_po_instantiates():
    from sky130.pcells.resistors import sky130_fd_pr__res_high_po

    c = sky130_fd_pr__res_high_po()
    assert isinstance(c, gf.Component)


def test_res_generic_nd_instantiates():
    from sky130.pcells.resistors import sky130_fd_pr__res_generic_nd

    c = sky130_fd_pr__res_generic_nd()
    assert isinstance(c, gf.Component)


def test_res_generic_nd_has_diff():
    from sky130.pcells.resistors import sky130_fd_pr__res_generic_nd

    c = sky130_fd_pr__res_generic_nd()
    layers = set(c.get_polygons().keys())
    assert LAYER.diffdrawing in layers
    assert LAYER.nsdmdrawing in layers
