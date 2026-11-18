"""Consistency checks for the gfpex default PEX rules of SkyWater SKY130."""

from __future__ import annotations

import pytest

pytest.importorskip(
    "gfpex.gfpex"
)  # not bare "gfpex": a folder named gfpex on sys.path would satisfy it

from gfpex.gfpex import Techfile  # noqa: E402

from sky130.layers import LAYER  # noqa: E402
from sky130.pex.rules import DEFAULT_PEX_RULES_CONFIG as CFG  # noqa: E402

# Magic's implicit p-well (the substrate under everything without an nwell). The overlap and side-overlap tables
# carried over from gf-pex reference it, but no LayerInfo defines it.
MAGIC_IMPLICIT_LAYERS = {"pwell"}


def _known_names() -> set[str]:
    names = {layer.name for layer in CFG.layers}
    names |= {c.layer_info.name for c in CFG.lvs_computed_layers if c.layer_info}
    return names


def _contacts() -> list:
    contacts = []
    for s in CFG.process_stack.layers:
        holder = s.metal_layer or s.diffusion_layer or s.nwell_layer
        if (
            holder is not None
            and holder.contact_above is not None
            and holder.contact_above.name
        ):
            contacts.append(holder.contact_above)
    return contacts


def test_round_trip() -> None:
    assert isinstance(CFG, Techfile)
    assert Techfile.model_validate_json(CFG.to_json()) == CFG


def test_names_resolve() -> None:
    known = _known_names()
    used = {
        s.name for s in CFG.process_stack.layers if s.metal_layer or s.diffusion_layer
    }
    for c in _contacts():
        used |= {c.name, c.layer_below, c.metal_above}
    r = CFG.process_parasitics.resistance
    used |= {x.layer_name for x in r.layers}
    used |= {
        n
        for x in r.contacts
        for n in (x.contact_name, x.device_layer_name, x.layer_above)
    }
    used |= {x.via_name for x in r.vias}
    c = CFG.process_parasitics.capacitance
    used |= {x.layer_name for x in c.substrates}
    used |= {n for x in c.overlaps for n in (x.top_layer_name, x.bottom_layer_name)}
    used |= {x.layer_name for x in c.sidewalls}
    used |= {n for x in c.sideoverlaps for n in (x.in_layer_name, x.out_layer_name)}
    assert used - known - MAGIC_IMPLICIT_LAYERS == set()


def test_drawing_gds_pairs_match_layer_map() -> None:
    for layer in CFG.layers:
        member = getattr(LAYER, f"{layer.name}drawing", None) or getattr(
            LAYER, layer.name
        )
        assert (layer.drw_gds_pair.layer, layer.drw_gds_pair.datatype) == (
            member.layer,
            member.datatype,
        ), layer.name


def test_metal_z_monotonic() -> None:
    metals = [s.metal_layer for s in CFG.process_stack.layers if s.metal_layer]
    assert len(metals) > 1
    for below, above in zip(metals, metals[1:]):
        if above.z == below.z:  # ncap/cap variants of the same physical metal
            assert above.thickness == below.thickness
            continue
        assert above.z_bottom >= below.z_top


def test_z_lookup_covers_contacts() -> None:
    z = CFG.build_layer_z_lookup()
    contacts = _contacts()
    assert contacts
    missing = {c.name for c in contacts} - set(z)
    assert not missing
