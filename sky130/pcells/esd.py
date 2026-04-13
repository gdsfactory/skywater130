"""ESD protection device generators for sky130.

Provides ESD NMOS pcell that matches the ESD-optimised geometry with
a large gate width, multi-finger layout, and the areaidesd marker layer.
"""

import gdsfactory as gf

from sky130.layers import LAYER
from sky130.pcells.guard_ring import pwell_guard_ring
from sky130.pcells.mosfets import _add_ports, _add_rect, _mosfet_core


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

    info = _mosfet_core(
        c,
        gate_width=gate_width,
        gate_length=gate_length,
        sd_width=sd_width,
        nf=nf,
        end_cap=end_cap,
        is_pmos=False,
    )

    diff_w = info["diff_w"]
    diff_h = info["diff_h"]
    implant_enc = info["implant_enc"]

    # ---- areaidesd marker layer ----
    # Cover the full diffusion area plus the implant enclosure margin.
    _add_rect(
        c,
        LAYER.areaidesd,
        -implant_enc,
        -implant_enc,
        diff_w + 2 * implant_enc,
        diff_h + 2 * implant_enc,
    )

    # ---- Guard ring ----
    if guard_ring:
        ring_spacing = 0.27
        ring_width = 0.34
        pc_pad_h = info["pc_pad_h"]
        device_top = diff_h + end_cap + pc_pad_h
        device_bottom = -(end_cap + pc_pad_h)
        device_height = device_top - device_bottom

        gr = c.add_ref(
            pwell_guard_ring(
                inner_width=diff_w,
                inner_height=device_height,
                ring_width=ring_width,
                spacing=ring_spacing,
            )
        )
        gr.move((0, device_bottom))

    # ---- Ports ----
    _add_ports(c, info, gate_width, gate_length, sd_width, end_cap)

    return c


if __name__ == "__main__":
    c = sky130_fd_pr__esd_nfet_01v8()
    c.show()
