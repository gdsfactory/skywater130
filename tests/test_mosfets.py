"""Tests for MOSFET pcell generators."""

import gdsfactory as gf
import pytest

from sky130.layers import LAYER


def test_nfet_01v8_instantiates():
    """Basic nfet should produce a valid component."""
    from sky130.pcells.mosfets import sky130_fd_pr__nfet_01v8

    c = sky130_fd_pr__nfet_01v8()
    assert c is not None
    assert isinstance(c, gf.Component)


def test_nfet_01v8_has_ports():
    """NFET must have GATE, DRAIN, SOURCE, BODY ports."""
    from sky130.pcells.mosfets import sky130_fd_pr__nfet_01v8

    c = sky130_fd_pr__nfet_01v8()
    port_names = {p.name for p in c.ports}
    for required in ("GATE", "DRAIN", "SOURCE", "BODY"):
        assert required in port_names, f"Missing port: {required}"


def test_nfet_01v8_layers():
    """NFET must contain required process layers."""
    from sky130.pcells.mosfets import sky130_fd_pr__nfet_01v8

    c = sky130_fd_pr__nfet_01v8()
    layers = set(c.get_polygons().keys())
    assert LAYER.diffdrawing in layers
    assert LAYER.polydrawing in layers
    assert LAYER.licon1drawing in layers
    assert LAYER.li1drawing in layers
    assert LAYER.nsdmdrawing in layers


def test_nfet_01v8_multi_finger():
    """Multi-finger NFET should produce wider component."""
    from sky130.pcells.mosfets import sky130_fd_pr__nfet_01v8

    c1 = sky130_fd_pr__nfet_01v8(nf=1, guard_ring=False)
    c2 = sky130_fd_pr__nfet_01v8(nf=2, guard_ring=False)
    c4 = sky130_fd_pr__nfet_01v8(nf=4, guard_ring=False)

    w1 = c1.bbox().width()
    w2 = c2.bbox().width()
    w4 = c4.bbox().width()
    assert w2 > w1
    assert w4 > w2


def test_nfet_01v8_guard_ring_toggle():
    """Guard ring adds surrounding geometry."""
    from sky130.pcells.mosfets import sky130_fd_pr__nfet_01v8

    c_gr = sky130_fd_pr__nfet_01v8(guard_ring=True)
    c_no = sky130_fd_pr__nfet_01v8(guard_ring=False)

    area_gr = c_gr.bbox().width() * c_gr.bbox().height()
    area_no = c_no.bbox().width() * c_no.bbox().height()
    assert area_gr > area_no


def test_pfet_01v8_instantiates():
    """Basic pfet should produce a valid component."""
    from sky130.pcells.mosfets import sky130_fd_pr__pfet_01v8

    c = sky130_fd_pr__pfet_01v8()
    assert c is not None


def test_pfet_01v8_has_nwell():
    """PFET must be in n-well."""
    from sky130.pcells.mosfets import sky130_fd_pr__pfet_01v8

    c = sky130_fd_pr__pfet_01v8()
    layers = set(c.get_polygons().keys())
    assert LAYER.nwelldrawing in layers


def test_pfet_01v8_has_ports():
    """PFET must have GATE, DRAIN, SOURCE, BODY ports."""
    from sky130.pcells.mosfets import sky130_fd_pr__pfet_01v8

    c = sky130_fd_pr__pfet_01v8()
    port_names = {p.name for p in c.ports}
    for required in ("GATE", "DRAIN", "SOURCE", "BODY"):
        assert required in port_names, f"Missing port: {required}"
