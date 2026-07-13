"""Tests verifying geometric and logical electrical pins on Sky130 PCells."""

from __future__ import annotations

import pytest
import kfactory as kf

from sky130 import PDK

kdb = kf.kdb


@pytest.fixture(autouse=True)
def activate_pdk():
    PDK.activate()


# Drawing layer → pin layer mapping (datatype 20 → datatype 16)
_PIN_LAYER_MAP: dict[tuple[int, int], tuple[int, int]] = {
    (66, 20): (66, 16),   # polydrawing → polypin
    (67, 20): (67, 16),   # li1drawing  → li1pin
    (68, 20): (68, 16),   # met1drawing → met1pin
    (69, 20): (69, 16),   # met2drawing → met2pin
    (70, 20): (70, 16),   # met3drawing → met3pin
    (71, 20): (71, 16),   # met4drawing → met4pin
    (72, 20): (72, 16),   # met5drawing → met5pin
}

# Electrical PCells that have geometric/logical pins added
CELL_NAMES = [
    # MOSFETs
    "sky130_fd_pr__nfet_01v8",
    "sky130_fd_pr__pfet_01v8",
    "sky130_fd_pr__nfet_01v8_lvt",
    "sky130_fd_pr__pfet_01v8_lvt",
    "sky130_fd_pr__pfet_01v8_hvt",
    "sky130_fd_pr__nfet_g5v0d10v5",
    "sky130_fd_pr__pfet_g5v0d10v5",
    # Capacitors
    "sky130_fd_pr__cap_mim_m3_1",
    "sky130_fd_pr__cap_mim_m3_2",
    # Resistors
    "sky130_fd_pr__res_generic_po",
    "sky130_fd_pr__res_high_po_0p35",
    # Diodes
    "sky130_fd_pr__diode_pw2nd_05v5",
    "sky130_fd_pr__diode_pd2nw_05v5",
    # ESD
    "sky130_fd_pr__esd_nfet_01v8",
]


def _has_pin_polygon_near_port(comp, port, pin_layer_tuple: tuple[int, int]) -> bool:
    """Return True if there is at least one polygon on pin_layer_tuple near the port center."""
    layout = comp.kcl.layout
    layer_idx = layout.find_layer(*pin_layer_tuple)
    if layer_idx < 0:
        return False
    dbu = layout.dbu
    cx = int(port.dcenter[0] / dbu)
    cy = int(port.dcenter[1] / dbu)
    half = int(0.1 / dbu)
    probe = kdb.Region(kdb.Box(cx - half, cy - half, cx + half, cy + half))
    region = kdb.Region(comp.begin_shapes_rec(layer_idx))
    return not (region & probe).is_empty()


def _port_pin_layer(comp, port) -> tuple[int, int]:
    """Map the port's drawing layer to its pin layer (datatype 20 → 16)."""
    info = comp.kcl.layout.get_info(port.layer)
    drawing = (info.layer, info.datatype)
    return _PIN_LAYER_MAP.get(drawing, drawing)


@pytest.mark.parametrize("cell_name", CELL_NAMES)
def test_geometric_pin_present(cell_name):
    """Each electrical port must have at least one polygon on the pin layer near it."""
    c = PDK.cells[cell_name]()
    electrical_ports = [p for p in c.ports if p.port_type == "electrical"]
    assert electrical_ports, f"No electrical ports on {cell_name}"
    for port in electrical_ports:
        pin_layer = _port_pin_layer(c, port)
        assert _has_pin_polygon_near_port(c, port, pin_layer), (
            f"No geometric pin polygon near port '{port.name}' on layer {pin_layer} in {cell_name}"
        )


@pytest.mark.parametrize("cell_name", CELL_NAMES)
def test_logical_pin_registered(cell_name):
    """create_pin() must have been called — c.pins must be non-empty."""
    c = PDK.cells[cell_name]()
    assert len(c.pins) > 0, f"No logical pins registered on {cell_name}"


@pytest.mark.parametrize("cell_name", CELL_NAMES)
def test_port_type_is_electrical(cell_name):
    """Every electrical port on these PCells must have port_type == 'electrical'."""
    c = PDK.cells[cell_name]()
    electrical_ports = [p for p in c.ports if p.port_type == "electrical"]
    assert electrical_ports, f"No electrical ports found on {cell_name}"
    for port in electrical_ports:
        assert port.port_type == "electrical", (
            f"Port '{port.name}' has type '{port.port_type}', expected 'electrical' in {cell_name}"
        )
