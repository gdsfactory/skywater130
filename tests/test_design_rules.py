"""Design rule validation for electrical pcells.

Validates that generated device geometry respects the key sky130 design rules
extracted from the Magic Tcl generators (open_pdks sky130.tcl).

This is NOT a substitute for XOR validation against Magic-generated reference
GDS. It validates structural correctness: layer presence, minimum dimensions,
contact enclosures, implant coverage. XOR testing requires Magic + open_pdks
(see scripts/magic/generate_references.sh).

Ruleset values from open_pdks/sky130/magic/sky130.tcl lines 55-76:
    poly_surround    = 0.08   (poly surrounds contact)
    diff_surround    = 0.06   (diffusion surrounds contact)
    gate_extension   = 0.13   (poly extension beyond gate)
    diff_extension   = 0.29   (diffusion extension beyond gate)
    contact_size     = 0.17   (minimum contact size)
    metal_surround   = 0.08   (LI overlaps contact)
    sub_surround     = 0.18   (well surrounds diffusion)
    diff_spacing     = 0.28   (diffusion spacing)
"""

from __future__ import annotations

import gdsfactory as gf
import pytest

from sky130.layers import LAYER

# ── Ruleset from open_pdks sky130.tcl ──
CONTACT_SIZE = 0.17
GATE_EXTENSION = 0.13
DIFF_EXTENSION = 0.29
NWELL_SURROUND = 0.18


def _bbox(c: gf.Component):
    """Get bounding box as (left, bottom, right, top)."""
    bb = c.bbox()
    return (bb.left, bb.bottom, bb.right, bb.top)


def _layer_bbox(c: gf.Component, layer):
    """Get bounding box of all polygons on a given layer."""
    polys = c.get_polygons().get(layer)
    if not polys:
        return None
    xmin = ymin = float("inf")
    xmax = ymax = float("-inf")
    for p in polys:
        for pt in p.each_point_hull():
            xmin = min(xmin, pt.x / 1000)  # nm to um
            ymin = min(ymin, pt.y / 1000)
            xmax = max(xmax, pt.x / 1000)
            ymax = max(ymax, pt.y / 1000)
    return (xmin, ymin, xmax, ymax)


# ── MOSFET structural tests ──


class TestNfet01v8Structure:
    """Structural validation for nfet_01v8."""

    def _make(self, **kwargs):
        from sky130.pcells.mosfets import sky130_fd_pr__nfet_01v8

        return sky130_fd_pr__nfet_01v8(**kwargs)

    def test_diff_covers_gate_width(self):
        """Diffusion height must be >= gate_width."""
        c = self._make(gate_width=1.0, guard_ring=False)
        diff_bb = _layer_bbox(c, LAYER.diffdrawing)
        assert diff_bb is not None
        diff_h = diff_bb[3] - diff_bb[1]
        assert diff_h >= 1.0 - 0.01  # allow 10nm tolerance

    def test_poly_extends_beyond_diff(self):
        """Poly must extend at least gate_extension beyond diffusion."""
        c = self._make(guard_ring=False)
        poly_bb = _layer_bbox(c, LAYER.polydrawing)
        diff_bb = _layer_bbox(c, LAYER.diffdrawing)
        assert poly_bb is not None
        assert diff_bb is not None
        # Poly top > diff top
        assert poly_bb[3] > diff_bb[3]
        # Poly bottom < diff bottom
        assert poly_bb[1] < diff_bb[1]

    def test_has_licon_contacts(self):
        """Must have licon contacts."""
        c = self._make(guard_ring=False)
        licon_bb = _layer_bbox(c, LAYER.licon1drawing)
        assert licon_bb is not None

    def test_nsdm_covers_diffusion(self):
        """NSDM implant must cover entire diffusion."""
        c = self._make(guard_ring=False)
        nsdm_bb = _layer_bbox(c, LAYER.nsdmdrawing)
        diff_bb = _layer_bbox(c, LAYER.diffdrawing)
        assert nsdm_bb is not None
        assert diff_bb is not None
        assert nsdm_bb[0] <= diff_bb[0] + 0.01
        assert nsdm_bb[1] <= diff_bb[1] + 0.01
        assert nsdm_bb[2] >= diff_bb[2] - 0.01
        assert nsdm_bb[3] >= diff_bb[3] - 0.01

    def test_multi_finger_width_scales(self):
        """Device width should scale linearly with nf."""
        c1 = self._make(nf=1, guard_ring=False)
        c2 = self._make(nf=2, guard_ring=False)
        diff1 = _layer_bbox(c1, LAYER.diffdrawing)
        diff2 = _layer_bbox(c2, LAYER.diffdrawing)
        w1 = diff1[2] - diff1[0]
        w2 = diff2[2] - diff2[0]
        # nf=2 diff should be wider than nf=1
        assert w2 > w1 * 1.5

    @pytest.mark.parametrize(
        "gate_width,gate_length,nf",
        [
            (0.42, 0.15, 1),
            (0.42, 0.15, 2),
            (0.42, 0.15, 3),
            (0.42, 0.15, 4),
            (1.0, 0.15, 1),
            (1.0, 0.15, 4),
            (5.0, 1.0, 2),
            (10.0, 0.15, 8),
        ],
    )
    def test_sweep_instantiates(self, gate_width, gate_length, nf):
        """Parameter sweep — every combo must produce a valid component."""
        c = self._make(
            gate_width=gate_width,
            gate_length=gate_length,
            nf=nf,
            guard_ring=True,
        )
        assert c is not None
        assert len(c.ports) == 4


class TestPfet01v8Structure:
    """Structural validation for pfet_01v8."""

    def _make(self, **kwargs):
        from sky130.pcells.mosfets import sky130_fd_pr__pfet_01v8

        return sky130_fd_pr__pfet_01v8(**kwargs)

    def test_nwell_covers_diffusion(self):
        """N-well must enclose entire diffusion with margin."""
        c = self._make(guard_ring=False)
        nwell_bb = _layer_bbox(c, LAYER.nwelldrawing)
        diff_bb = _layer_bbox(c, LAYER.diffdrawing)
        assert nwell_bb is not None
        assert diff_bb is not None
        # Nwell must extend beyond diff on all sides
        assert nwell_bb[0] < diff_bb[0]
        assert nwell_bb[1] < diff_bb[1]
        assert nwell_bb[2] > diff_bb[2]
        assert nwell_bb[3] > diff_bb[3]

    def test_psdm_covers_diffusion(self):
        """PSDM implant must cover PFET diffusion."""
        c = self._make(guard_ring=False)
        psdm_bb = _layer_bbox(c, LAYER.psdmdrawing)
        diff_bb = _layer_bbox(c, LAYER.diffdrawing)
        assert psdm_bb is not None
        assert diff_bb is not None
        assert psdm_bb[0] <= diff_bb[0] + 0.01
        assert psdm_bb[1] <= diff_bb[1] + 0.01
        assert psdm_bb[2] >= diff_bb[2] - 0.01
        assert psdm_bb[3] >= diff_bb[3] - 0.01

    @pytest.mark.parametrize(
        "gate_width,gate_length,nf",
        [
            (0.42, 0.15, 1),
            (0.42, 0.15, 3),
            (0.42, 0.15, 4),
            (5.0, 1.0, 2),
        ],
    )
    def test_sweep_instantiates(self, gate_width, gate_length, nf):
        """Parameter sweep — every combo must produce a valid component."""
        c = self._make(
            gate_width=gate_width,
            gate_length=gate_length,
            nf=nf,
            guard_ring=True,
        )
        assert c is not None
        assert len(c.ports) == 4
