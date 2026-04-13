"""Tests for sky130/pcells/capacitors.py — MIM capacitor pcells."""

import gdsfactory as gf
import sky130

sky130.PDK.activate()

from sky130.layers import LAYER


def test_cap_mim_m3_1_instantiates():
    from sky130.pcells.capacitors import sky130_fd_pr__cap_mim_m3_1

    c = sky130_fd_pr__cap_mim_m3_1()
    assert isinstance(c, gf.Component)


def test_cap_mim_m3_1_has_ports():
    from sky130.pcells.capacitors import sky130_fd_pr__cap_mim_m3_1

    c = sky130_fd_pr__cap_mim_m3_1()
    port_names = {p.name for p in c.ports}
    assert "TOP" in port_names
    assert "BOTTOM" in port_names


def test_cap_mim_m3_1_has_cap_layer():
    from sky130.pcells.capacitors import sky130_fd_pr__cap_mim_m3_1

    c = sky130_fd_pr__cap_mim_m3_1()
    layers = set(c.get_polygons().keys())
    # Check for capm layer (MIM cap plate over metal 3): (89, 44)
    assert LAYER.capm in layers, f"capm layer {LAYER.capm} not found in {layers}"


def test_cap_mim_m3_1_has_met3_layer():
    from sky130.pcells.capacitors import sky130_fd_pr__cap_mim_m3_1

    c = sky130_fd_pr__cap_mim_m3_1()
    layers = set(c.get_polygons().keys())
    assert LAYER.met3drawing in layers, (
        f"met3drawing layer {LAYER.met3drawing} not found in {layers}"
    )


def test_cap_mim_m3_1_has_via3_layer():
    from sky130.pcells.capacitors import sky130_fd_pr__cap_mim_m3_1

    c = sky130_fd_pr__cap_mim_m3_1()
    layers = set(c.get_polygons().keys())
    assert LAYER.via3drawing in layers, (
        f"via3drawing layer {LAYER.via3drawing} not found in {layers}"
    )


def test_cap_mim_m3_2_instantiates():
    from sky130.pcells.capacitors import sky130_fd_pr__cap_mim_m3_2

    c = sky130_fd_pr__cap_mim_m3_2()
    assert isinstance(c, gf.Component)


def test_cap_mim_m3_2_has_ports():
    from sky130.pcells.capacitors import sky130_fd_pr__cap_mim_m3_2

    c = sky130_fd_pr__cap_mim_m3_2()
    port_names = {p.name for p in c.ports}
    assert "TOP" in port_names
    assert "BOTTOM" in port_names


def test_cap_mim_m3_2_has_cap2m_layer():
    from sky130.pcells.capacitors import sky130_fd_pr__cap_mim_m3_2

    c = sky130_fd_pr__cap_mim_m3_2()
    layers = set(c.get_polygons().keys())
    # Check for cap2m layer (MIM cap plate over metal 4): (97, 44)
    assert LAYER.cap2m in layers, f"cap2m layer {LAYER.cap2m} not found in {layers}"
