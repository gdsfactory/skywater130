import gdsfactory as gf
from sky130.layers import LAYER


def test_esd_nfet_instantiates():
    from sky130.pcells.esd import sky130_fd_pr__esd_nfet_01v8
    c = sky130_fd_pr__esd_nfet_01v8()
    assert isinstance(c, gf.Component)


def test_esd_nfet_has_ports():
    from sky130.pcells.esd import sky130_fd_pr__esd_nfet_01v8
    c = sky130_fd_pr__esd_nfet_01v8()
    port_names = {p.name for p in c.ports}
    assert "GATE" in port_names
    assert "DRAIN" in port_names
    assert "SOURCE" in port_names


def test_esd_nfet_is_large():
    from sky130.pcells.esd import sky130_fd_pr__esd_nfet_01v8
    c = sky130_fd_pr__esd_nfet_01v8()
    bb = c.bbox()
    # ESD device should be large (default W=20um, nf=4)
    assert bb.width() > 2.0
    assert bb.height() > 10.0
