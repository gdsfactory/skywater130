"""Tests for sky130/pcells/guard_ring.py — pwell and nwell guard ring generators."""

from sky130.layers import LAYER
from sky130.pcells.guard_ring import nwell_guard_ring, pwell_guard_ring


def test_pwell_guard_ring_creates_component():
    """pwell_guard_ring should produce a component containing tapdrawing and licon1drawing."""
    c = pwell_guard_ring(inner_width=2.0, inner_height=2.0)
    polys = c.get_polygons()
    assert LAYER.tapdrawing in polys, "tapdrawing layer missing from pwell guard ring"
    assert LAYER.licon1drawing in polys, (
        "licon1drawing layer missing from pwell guard ring"
    )


def test_nwell_guard_ring_creates_component():
    """nwell_guard_ring should produce a component containing tapdrawing, nwelldrawing, and licon1drawing."""
    c = nwell_guard_ring(inner_width=2.0, inner_height=2.0)
    polys = c.get_polygons()
    assert LAYER.tapdrawing in polys, "tapdrawing layer missing from nwell guard ring"
    assert LAYER.nwelldrawing in polys, (
        "nwelldrawing layer missing from nwell guard ring"
    )
    assert LAYER.licon1drawing in polys, (
        "licon1drawing layer missing from nwell guard ring"
    )


def test_guard_ring_has_ports():
    """pwell_guard_ring should expose a port named 'VSS' or 'BODY'."""
    c = pwell_guard_ring(inner_width=2.0, inner_height=2.0)
    port_names = [p.name for p in c.ports]
    assert any("VSS" in name or "BODY" in name for name in port_names), (
        f"No VSS or BODY port found; ports are: {port_names}"
    )


def test_guard_ring_encloses_area():
    """Outer bounding box should be larger than the 2.0 x 2.0 inner area."""
    inner_w = 2.0
    inner_h = 2.0
    c = pwell_guard_ring(inner_width=inner_w, inner_height=inner_h)
    bb = c.bbox()
    assert bb.width() > inner_w, (
        f"Guard ring bbox width {bb.width()} should exceed inner width {inner_w}"
    )
    assert bb.height() > inner_h, (
        f"Guard ring bbox height {bb.height()} should exceed inner height {inner_h}"
    )
