"""ESD protection device generators for sky130.

Provides ESD NMOS pcell that matches the ESD-optimised geometry with
a large gate width, multi-finger layout, and the areaidesd marker layer.
"""

import gdsfactory as gf

from sky130.layers import LAYER
from sky130.pcells.mosfets import _add_guard_ring, _mosfet_core, _rect


@gf.cell
def sky130_fd_pr__esd_nfet_01v8(
    gate_width: float = 20.0,
    gate_length: float = 0.15,
    sd_width: float = 0.28,
    nf: int = 4,
    guard_ring: bool = True,
    end_cap: float = 0.13,
) -> gf.Component:
    """ESD protection 1.8V NMOS (sky130_fd_pr__esd_nfet_01v8).

    Large multi-finger NMOS optimised for ESD current handling.  Geometry
    follows the standard sky130 MOSFET construction but adds the ``areaidesd``
    (81, 19) marker layer over the entire device area.

    Args:
        gate_width: transistor width (um); large default (20 um) for ESD.
        gate_length: gate poly length (um) in the direction of current flow.
        sd_width: source/drain contact region width (um).
        nf: number of gate fingers; default 4 for ESD current spreading.
        guard_ring: if True, add a pwell (P+ substrate) guard ring.
        end_cap: poly extension beyond diffusion edge (um).
    """
    c = gf.Component()

    info = _mosfet_core(c, gate_width, gate_length, nf, is_pmos=False)

    dhx = info["diff_half_x"]
    hw = info["hw"]
    enc = info["implant_enc"]

    # ---- areaidesd marker layer ----
    _rect(c, LAYER.areaidesd, -(dhx + enc), -(hw + enc), dhx + enc, hw + enc)

    # ---- Guard ring ----
    if guard_ring:
        _add_guard_ring(c, info, is_pmos=False)

    # ---- Ports ----
    sd = info["sd_centers_x"]
    gpc = info["gate_to_polycont"]
    c.add_port(
        name="GATE",
        center=(info["gate_centers_x"][0], 0.0),
        width=gate_width,
        orientation=0,
        layer=LAYER.polydrawing,
        port_type="electrical",
    )
    c.add_port(
        name="SOURCE",
        center=(sd[-1], 0.0),
        width=gate_width,
        orientation=0,
        layer=LAYER.li1drawing,
        port_type="electrical",
    )
    c.add_port(
        name="DRAIN",
        center=(sd[0], 0.0),
        width=gate_width,
        orientation=180,
        layer=LAYER.li1drawing,
        port_type="electrical",
    )
    c.add_port(
        name="BODY",
        center=(0.0, -(hw + gpc)),
        width=gate_width,
        orientation=270,
        layer=LAYER.li1drawing,
        port_type="electrical",
    )

    return c


if __name__ == "__main__":
    c = sky130_fd_pr__esd_nfet_01v8()
    c.show()
