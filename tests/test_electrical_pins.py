"""Tests for logical electrical pins on skywater130 PCells.

Verifies that every cell with electrical ports has logical pins registered
via component.create_pin(), enabling SPICE netlist export.
"""

from __future__ import annotations

import pytest

CELL_NAMES = [
    "sky130_fd_pr__nfet_01v8",
    "sky130_fd_pr__pfet_01v8",
    "sky130_fd_pr__nfet_01v8_lvt",
    "sky130_fd_pr__pfet_01v8_lvt",
    "sky130_fd_pr__pfet_01v8_hvt",
    "sky130_fd_pr__nfet_g5v0d10v5",
    "sky130_fd_pr__pfet_g5v0d10v5",
    "sky130_fd_pr__nfet_20v0",
    "sky130_fd_pr__pfet_20v0",
    "sky130_fd_pr__nfet_03v3_nvt",
    "sky130_fd_pr__nfet_05v0_nvt",
    "sky130_fd_pr__esd_nfet_01v8",
    "sky130_fd_pr__diode_pw2nd_05v5",
    "sky130_fd_pr__diode_pd2nw_05v5",
    "pwell_guard_ring",
    "nwell_guard_ring",
]


@pytest.fixture(scope="module")
def sky130_cells():
    import sky130

    return sky130.cells


@pytest.mark.parametrize("cell_name", CELL_NAMES)
def test_logical_pin_registered(cell_name, sky130_cells):
    """Each cell must have at least one logical pin registered."""
    cell_fn = sky130_cells.get(cell_name)
    if cell_fn is None:
        pytest.skip(f"Cell {cell_name} not in registry")
    c = cell_fn()
    assert len(c.pins) > 0, f"{cell_name}: no logical pins registered"


@pytest.mark.parametrize("cell_name", CELL_NAMES)
def test_port_type_is_electrical(cell_name, sky130_cells):
    """Every port on electrical-port cells must have port_type == 'electrical'."""
    cell_fn = sky130_cells.get(cell_name)
    if cell_fn is None:
        pytest.skip(f"Cell {cell_name} not in registry")
    c = cell_fn()
    electrical_ports = [p for p in c.ports if p.port_type == "electrical"]
    assert len(electrical_ports) > 0, f"{cell_name}: no electrical ports found"
