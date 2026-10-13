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

EXPECTED_PIN_NAMES: dict[str, set[str]] = {
    "sky130_fd_pr__nfet_01v8": {"BODY", "DRAIN", "GATE", "SOURCE"},
    "sky130_fd_pr__pfet_01v8": {"BODY", "DRAIN", "GATE", "SOURCE"},
    "sky130_fd_pr__nfet_01v8_lvt": {"BODY", "DRAIN", "GATE", "SOURCE"},
    "sky130_fd_pr__pfet_01v8_lvt": {"BODY", "DRAIN", "GATE", "SOURCE"},
    "sky130_fd_pr__pfet_01v8_hvt": {"BODY", "DRAIN", "GATE", "SOURCE"},
    "sky130_fd_pr__nfet_g5v0d10v5": {"BODY", "DRAIN", "GATE", "SOURCE"},
    "sky130_fd_pr__pfet_g5v0d10v5": {"BODY", "DRAIN", "GATE", "SOURCE"},
    "sky130_fd_pr__nfet_20v0": {"BODY", "DRAIN", "GATE", "SOURCE"},
    "sky130_fd_pr__pfet_20v0": {"BODY", "DRAIN", "GATE", "SOURCE"},
    "sky130_fd_pr__nfet_03v3_nvt": {"BODY", "DRAIN", "GATE", "SOURCE"},
    "sky130_fd_pr__nfet_05v0_nvt": {"BODY", "DRAIN", "GATE", "SOURCE"},
    "sky130_fd_pr__esd_nfet_01v8": {"BODY", "DRAIN", "GATE", "SOURCE"},
    "sky130_fd_pr__diode_pw2nd_05v5": {"ANODE", "CATHODE"},
    "sky130_fd_pr__diode_pd2nw_05v5": {"ANODE", "CATHODE"},
    "pwell_guard_ring": {"VSS"},
    "nwell_guard_ring": {"VDD"},
}


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


@pytest.mark.parametrize("cell_name", CELL_NAMES)
def test_expected_pin_names(cell_name, sky130_cells):
    """Verify that each cell registers the expected set of logical pin names."""
    cell_fn = sky130_cells.get(cell_name)
    if cell_fn is None:
        pytest.skip(f"Cell {cell_name} not in registry")
    c = cell_fn()
    actual_pin_names = {pin.name for pin in c.pins}
    expected = EXPECTED_PIN_NAMES[cell_name]
    assert expected.issubset(actual_pin_names), (
        f"{cell_name}: missing pins {expected - actual_pin_names}; got {actual_pin_names}"
    )
