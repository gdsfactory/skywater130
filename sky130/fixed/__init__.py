"""SKY130 fixed analog/RF primitive cells (sky130_fd_pr).

These are fixed-geometry cells imported from GDS (RF FETs, VPP caps, etc).
"""

from functools import partial

import gdsfactory as gf
from gdsfactory import cell

from sky130.config import PATH
from sky130.layers import LAYER

add_ports_m1 = gf.partial(
    gf.add_ports.add_ports_from_labels,
    port_layer=LAYER.met1drawing,
    layer_label=LAYER.met1label,
    port_type="electrical",
    port_width=0.2,
    get_name_from_label=True,
    guess_port_orientation=True,
)
add_ports_m2 = gf.partial(
    gf.add_ports.add_ports_from_labels,
    port_layer=LAYER.met2drawing,
    layer_label=LAYER.met2label,
    port_type="electrical",
    port_width=0.2,
    get_name_from_label=True,
    guess_port_orientation=True,
)
add_ports = (add_ports_m1, add_ports_m2)

gdsdir = PATH.module
import_gds = partial(gf.import_gds, post_process=add_ports)


@cell
def sky130_fd_pr__rf_nfet_20v0_nvt_noptap_iso() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_20v0_nvt_noptap_iso fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_20v0_nvt_noptap_iso()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_20v0_nvt_noptap_iso/sky130_fd_pr__rf_nfet_20v0_nvt_noptap_iso.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_20v0_noptap_iso() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_20v0_noptap_iso fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_20v0_noptap_iso()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_20v0_noptap_iso/sky130_fd_pr__rf_nfet_20v0_noptap_iso.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_02p7x21p1_m1m2m3m4_shieldl1_fingercap() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_02p7x21p1_m1m2m3m4_shieldl1_fingercap fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_02p7x21p1_m1m2m3m4_shieldl1_fingercap()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_02p7x21p1_m1m2m3m4_shieldl1/sky130_fd_pr__cap_vpp_02p7x21p1_m1m2m3m4_shieldl1_fingercap.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_g5v0d10v5_aM04W7p00L0p50() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_g5v0d10v5_aM04W7p00L0p50 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_g5v0d10v5_aM04W7p00L0p50()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_g5v0d10v5/sky130_fd_pr__rf_nfet_g5v0d10v5_aM04W7p00L0p50.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_g5v0d10v5_bM04W5p00L0p50() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_g5v0d10v5_bM04W5p00L0p50 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_g5v0d10v5_bM04W5p00L0p50()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_g5v0d10v5/sky130_fd_pr__rf_nfet_g5v0d10v5_bM04W5p00L0p50.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_g5v0d10v5_bM10W5p00L0p50() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_g5v0d10v5_bM10W5p00L0p50 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_g5v0d10v5_bM10W5p00L0p50()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_g5v0d10v5/sky130_fd_pr__rf_nfet_g5v0d10v5_bM10W5p00L0p50.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_g5v0d10v5_aM10W7p00L0p50() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_g5v0d10v5_aM10W7p00L0p50 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_g5v0d10v5_aM10W7p00L0p50()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_g5v0d10v5/sky130_fd_pr__rf_nfet_g5v0d10v5_aM10W7p00L0p50.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_g5v0d10v5_bM04W3p00L0p50() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_g5v0d10v5_bM04W3p00L0p50 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_g5v0d10v5_bM04W3p00L0p50()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_g5v0d10v5/sky130_fd_pr__rf_nfet_g5v0d10v5_bM04W3p00L0p50.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_g5v0d10v5_bM10W3p00L0p50() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_g5v0d10v5_bM10W3p00L0p50 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_g5v0d10v5_bM10W3p00L0p50()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_g5v0d10v5/sky130_fd_pr__rf_nfet_g5v0d10v5_bM10W3p00L0p50.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_g5v0d10v5_bM02W3p00L0p50() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_g5v0d10v5_bM02W3p00L0p50 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_g5v0d10v5_bM02W3p00L0p50()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_g5v0d10v5/sky130_fd_pr__rf_nfet_g5v0d10v5_bM02W3p00L0p50.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_g5v0d10v5_aM04W3p00L0p50() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_g5v0d10v5_aM04W3p00L0p50 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_g5v0d10v5_aM04W3p00L0p50()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_g5v0d10v5/sky130_fd_pr__rf_nfet_g5v0d10v5_aM04W3p00L0p50.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_g5v0d10v5_aM10W3p00L0p50() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_g5v0d10v5_aM10W3p00L0p50 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_g5v0d10v5_aM10W3p00L0p50()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_g5v0d10v5/sky130_fd_pr__rf_nfet_g5v0d10v5_aM10W3p00L0p50.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_g5v0d10v5_bM02W5p00L0p50() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_g5v0d10v5_bM02W5p00L0p50 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_g5v0d10v5_bM02W5p00L0p50()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_g5v0d10v5/sky130_fd_pr__rf_nfet_g5v0d10v5_bM02W5p00L0p50.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_g5v0d10v5_aM04W5p00L0p50() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_g5v0d10v5_aM04W5p00L0p50 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_g5v0d10v5_aM04W5p00L0p50()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_g5v0d10v5/sky130_fd_pr__rf_nfet_g5v0d10v5_aM04W5p00L0p50.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_g5v0d10v5_bM04W7p00L0p50() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_g5v0d10v5_bM04W7p00L0p50 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_g5v0d10v5_bM04W7p00L0p50()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_g5v0d10v5/sky130_fd_pr__rf_nfet_g5v0d10v5_bM04W7p00L0p50.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_g5v0d10v5_bM10W7p00L0p50() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_g5v0d10v5_bM10W7p00L0p50 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_g5v0d10v5_bM10W7p00L0p50()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_g5v0d10v5/sky130_fd_pr__rf_nfet_g5v0d10v5_bM10W7p00L0p50.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_g5v0d10v5_aM10W5p00L0p50() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_g5v0d10v5_aM10W5p00L0p50 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_g5v0d10v5_aM10W5p00L0p50()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_g5v0d10v5/sky130_fd_pr__rf_nfet_g5v0d10v5_aM10W5p00L0p50.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_20v0_withptap_iso() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_20v0_withptap_iso fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_20v0_withptap_iso()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_20v0_withptap_iso/sky130_fd_pr__rf_nfet_20v0_withptap_iso.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_04p4x04p6_m1m2_shieldl1() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_04p4x04p6_m1m2_shieldl1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_04p4x04p6_m1m2_shieldl1()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_04p4x04p6_m1m2_shieldl1/sky130_fd_pr__cap_vpp_04p4x04p6_m1m2_shieldl1.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_lvt_aM04W5p00L0p35() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_lvt_aM04W5p00L0p35 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_lvt_aM04W5p00L0p35()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8_lvt/sky130_fd_pr__rf_pfet_01v8_lvt_aM04W5p00L0p35.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_lvt_aM04W3p00L0p50() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_lvt_aM04W3p00L0p50 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_lvt_aM04W3p00L0p50()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8_lvt/sky130_fd_pr__rf_pfet_01v8_lvt_aM04W3p00L0p50.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_lvt_aM04W3p00L0p35() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_lvt_aM04W3p00L0p35 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_lvt_aM04W3p00L0p35()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8_lvt/sky130_fd_pr__rf_pfet_01v8_lvt_aM04W3p00L0p35.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_lvt_aM04W5p00L0p50() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_lvt_aM04W5p00L0p50 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_lvt_aM04W5p00L0p50()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8_lvt/sky130_fd_pr__rf_pfet_01v8_lvt_aM04W5p00L0p50.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_lvt_aM02W3p00L0p35() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_lvt_aM02W3p00L0p35 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_lvt_aM02W3p00L0p35()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8_lvt/sky130_fd_pr__rf_pfet_01v8_lvt_aM02W3p00L0p35.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_lvt_aM02W5p00L0p50() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_lvt_aM02W5p00L0p50 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_lvt_aM02W5p00L0p50()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8_lvt/sky130_fd_pr__rf_pfet_01v8_lvt_aM02W5p00L0p50.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_lvt_aM02W5p00L0p35() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_lvt_aM02W5p00L0p35 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_lvt_aM02W5p00L0p35()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8_lvt/sky130_fd_pr__rf_pfet_01v8_lvt_aM02W5p00L0p35.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_lvt_aM02W3p00L0p50() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_lvt_aM02W3p00L0p50 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_lvt_aM02W3p00L0p50()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8_lvt/sky130_fd_pr__rf_pfet_01v8_lvt_aM02W3p00L0p50.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_08p6x07p8_m1m2_noshield() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_08p6x07p8_m1m2_noshield fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_08p6x07p8_m1m2_noshield()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_08p6x07p8_m1m2_noshield/sky130_fd_pr__cap_vpp_08p6x07p8_m1m2_noshield.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_02p4x04p6_m1m2_noshield() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_02p4x04p6_m1m2_noshield fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_02p4x04p6_m1m2_noshield()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_02p4x04p6_m1m2_noshield/sky130_fd_pr__cap_vpp_02p4x04p6_m1m2_noshield.gds"
    )


@cell
def sky130_fd_pr__rf_aura_drc_flag_check() -> gf.Component:
    """Returns sky130_fd_pr__rf_aura_drc_flag_check fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_aura_drc_flag_check()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_aura_drc_flag_check/sky130_fd_pr__rf_aura_drc_flag_check.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_06p8x06p1_m1m2m3_shieldl1m4() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_06p8x06p1_m1m2m3_shieldl1m4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_06p8x06p1_m1m2m3_shieldl1m4()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_06p8x06p1_m1m2m3_shieldl1m4/sky130_fd_pr__cap_vpp_06p8x06p1_m1m2m3_shieldl1m4.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_06p8x06p1_m1m2m3_shieldl1m4_top() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_06p8x06p1_m1m2m3_shieldl1m4_top fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_06p8x06p1_m1m2m3_shieldl1m4_top()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_06p8x06p1_m1m2m3_shieldl1m4/sky130_fd_pr__cap_vpp_06p8x06p1_m1m2m3_shieldl1m4_top.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_04p4x04p6_l1m1m2_shieldpo_floatm3() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_04p4x04p6_l1m1m2_shieldpo_floatm3 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_04p4x04p6_l1m1m2_shieldpo_floatm3()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_04p4x04p6_l1m1m2_shieldpo_floatm3/sky130_fd_pr__cap_vpp_04p4x04p6_l1m1m2_shieldpo_floatm3.gds"
    )


@cell
def sky130_fd_pr__rf_npn_05v5_W1p00L1p00() -> gf.Component:
    """Returns sky130_fd_pr__rf_npn_05v5_W1p00L1p00 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_npn_05v5_W1p00L1p00()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_npn_05v5/sky130_fd_pr__rf_npn_05v5_W1p00L1p00.gds"
    )


@cell
def sky130_fd_pr__rf_npn_05v5_W1p00L2p00() -> gf.Component:
    """Returns sky130_fd_pr__rf_npn_05v5_W1p00L2p00 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_npn_05v5_W1p00L2p00()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_npn_05v5/sky130_fd_pr__rf_npn_05v5_W1p00L2p00.gds"
    )


@cell
def sky130_fd_pr__rf_npn_05v5_W2p00L8p00() -> gf.Component:
    """Returns sky130_fd_pr__rf_npn_05v5_W2p00L8p00 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_npn_05v5_W2p00L8p00()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_npn_05v5/sky130_fd_pr__rf_npn_05v5_W2p00L8p00.gds"
    )


@cell
def sky130_fd_pr__rf_npn_05v5_W2p00L4p00() -> gf.Component:
    """Returns sky130_fd_pr__rf_npn_05v5_W2p00L4p00 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_npn_05v5_W2p00L4p00()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_npn_05v5/sky130_fd_pr__rf_npn_05v5_W2p00L4p00.gds"
    )


@cell
def sky130_fd_pr__rf_npn_05v5_W5p00L5p00() -> gf.Component:
    """Returns sky130_fd_pr__rf_npn_05v5_W5p00L5p00 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_npn_05v5_W5p00L5p00()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_npn_05v5/sky130_fd_pr__rf_npn_05v5_W5p00L5p00.gds"
    )


@cell
def sky130_fd_pr__rf_npn_05v5_W1p00L4p00() -> gf.Component:
    """Returns sky130_fd_pr__rf_npn_05v5_W1p00L4p00 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_npn_05v5_W1p00L4p00()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_npn_05v5/sky130_fd_pr__rf_npn_05v5_W1p00L4p00.gds"
    )


@cell
def sky130_fd_pr__rf_npn_05v5_W1p00L8p00() -> gf.Component:
    """Returns sky130_fd_pr__rf_npn_05v5_W1p00L8p00 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_npn_05v5_W1p00L8p00()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_npn_05v5/sky130_fd_pr__rf_npn_05v5_W1p00L8p00.gds"
    )


@cell
def sky130_fd_pr__rf_npn_05v5_W2p00L2p00() -> gf.Component:
    """Returns sky130_fd_pr__rf_npn_05v5_W2p00L2p00 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_npn_05v5_W2p00L2p00()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_npn_05v5/sky130_fd_pr__rf_npn_05v5_W2p00L2p00.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_11p5x11p7_m1m2_shieldl1() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_11p5x11p7_m1m2_shieldl1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_11p5x11p7_m1m2_shieldl1()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_m1m2_shieldl1/sky130_fd_pr__cap_vpp_11p5x11p7_m1m2_shieldl1.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_04p4x04p6_m1m2m3_shieldl1m5_floatm4() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_04p4x04p6_m1m2m3_shieldl1m5_floatm4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_04p4x04p6_m1m2m3_shieldl1m5_floatm4()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_04p4x04p6_m1m2m3_shieldl1m5_floatm4/sky130_fd_pr__cap_vpp_04p4x04p6_m1m2m3_shieldl1m5_floatm4.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_04p4x04p6_m1m2m3_shieldl1m5_floatm4_top() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_04p4x04p6_m1m2m3_shieldl1m5_floatm4_top fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_04p4x04p6_m1m2m3_shieldl1m5_floatm4_top()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_04p4x04p6_m1m2m3_shieldl1m5_floatm4/sky130_fd_pr__cap_vpp_04p4x04p6_m1m2m3_shieldl1m5_floatm4_top.gds"
    )


@cell
def sky130_fd_pr__rf_test_coil2() -> gf.Component:
    """Returns sky130_fd_pr__rf_test_coil2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_test_coil2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_pr/cells/rf_test_coil2/sky130_fd_pr__rf_test_coil2.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_08p6x07p8_l1m1m2_noshield() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_08p6x07p8_l1m1m2_noshield fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_08p6x07p8_l1m1m2_noshield()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_08p6x07p8_l1m1m2_noshield/sky130_fd_pr__cap_vpp_08p6x07p8_l1m1m2_noshield.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_08p6x07p8_l1m1m2_noshield_o2subcell() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_08p6x07p8_l1m1m2_noshield_o2subcell fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_08p6x07p8_l1m1m2_noshield_o2subcell()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_08p6x07p8_l1m1m2_noshield/sky130_fd_pr__cap_vpp_08p6x07p8_l1m1m2_noshield_o2subcell.gds"
    )


@cell
def sky130_fd_pr__esd_rf_nfet_20v0_iec_21vW60p00() -> gf.Component:
    """Returns sky130_fd_pr__esd_rf_nfet_20v0_iec_21vW60p00 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__esd_rf_nfet_20v0_iec_21vW60p00()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/esd_rf_nfet_20v0_iec/sky130_fd_pr__esd_rf_nfet_20v0_iec_21vW60p00.gds"
    )


@cell
def sky130_fd_pr__esd_rf_nfet_20v0_iec_32vW60p00() -> gf.Component:
    """Returns sky130_fd_pr__esd_rf_nfet_20v0_iec_32vW60p00 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__esd_rf_nfet_20v0_iec_32vW60p00()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/esd_rf_nfet_20v0_iec/sky130_fd_pr__esd_rf_nfet_20v0_iec_32vW60p00.gds"
    )


@cell
def sky130_fd_pr__rf_test_coil3() -> gf.Component:
    """Returns sky130_fd_pr__rf_test_coil3 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_test_coil3()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_pr/cells/rf_test_coil3/sky130_fd_pr__rf_test_coil3.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_11p5x11p7_m1m2m3_shieldl1() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_11p5x11p7_m1m2m3_shieldl1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_11p5x11p7_m1m2m3_shieldl1()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_m1m2m3_shieldl1/sky130_fd_pr__cap_vpp_11p5x11p7_m1m2m3_shieldl1.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_11p3x11p8_l1m1m2m3m4_shieldm5_nhvtop() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_11p3x11p8_l1m1m2m3m4_shieldm5_nhvtop fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_11p3x11p8_l1m1m2m3m4_shieldm5_nhvtop()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_11p3x11p8_l1m1m2m3m4_shieldm5/sky130_fd_pr__cap_vpp_11p3x11p8_l1m1m2m3m4_shieldm5_nhvtop.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_11p3x11p8_l1m1m2m3m4_shieldm5_nhv() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_11p3x11p8_l1m1m2m3m4_shieldm5_nhv fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_11p3x11p8_l1m1m2m3m4_shieldm5_nhv()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_11p3x11p8_l1m1m2m3m4_shieldm5/sky130_fd_pr__cap_vpp_11p3x11p8_l1m1m2m3m4_shieldm5_nhv.gds"
    )


@cell
def sky130_fd_pr__rf_aura_lvs_drc() -> gf.Component:
    """Returns sky130_fd_pr__rf_aura_lvs_drc fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_aura_lvs_drc()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_aura_lvs_drc/sky130_fd_pr__rf_aura_lvs_drc.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_11p5x11p7_m1m2m3m4_shieldl1m5() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_11p5x11p7_m1m2m3m4_shieldl1m5 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_11p5x11p7_m1m2m3m4_shieldl1m5()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_m1m2m3m4_shieldl1m5/sky130_fd_pr__cap_vpp_11p5x11p7_m1m2m3m4_shieldl1m5.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_11p5x11p7_m1m2m3m4_shieldl1m5_top() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_11p5x11p7_m1m2m3m4_shieldl1m5_top fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_11p5x11p7_m1m2m3m4_shieldl1m5_top()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_m1m2m3m4_shieldl1m5/sky130_fd_pr__cap_vpp_11p5x11p7_m1m2m3m4_shieldl1m5_top.gds"
    )


@cell
def sky130_fd_pr__rf_pnp_05v5_W3p40L3p40() -> gf.Component:
    """Returns sky130_fd_pr__rf_pnp_05v5_W3p40L3p40 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pnp_05v5_W3p40L3p40()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pnp_05v5/sky130_fd_pr__rf_pnp_05v5_W3p40L3p40.gds"
    )


@cell
def sky130_fd_pr__rf_pnp_05v5_W0p68L0p68() -> gf.Component:
    """Returns sky130_fd_pr__rf_pnp_05v5_W0p68L0p68 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pnp_05v5_W0p68L0p68()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pnp_05v5/sky130_fd_pr__rf_pnp_05v5_W0p68L0p68.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2_shieldpom3() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2_shieldpom3 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2_shieldpom3()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_l1m1m2_shieldpom3/sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2_shieldpom3.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3_shieldpom4_top() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3_shieldpom4_top fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3_shieldpom4_top()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_l1m1m2m3_shieldpom4/sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3_shieldpom4_top.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3_shieldpom4() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3_shieldpom4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3_shieldpom4()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_l1m1m2m3_shieldpom4/sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3_shieldpom4.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_22p5x11p7_pol1m1m2m3m4m5_noshield() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_22p5x11p7_pol1m1m2m3m4m5_noshield fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_22p5x11p7_pol1m1m2m3m4m5_noshield()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_22p5x11p7_pol1m1m2m3m4m5_noshield/sky130_fd_pr__cap_vpp_22p5x11p7_pol1m1m2m3m4m5_noshield.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_04p4x04p6_m1m2m3_shieldl1() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_04p4x04p6_m1m2m3_shieldl1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_04p4x04p6_m1m2m3_shieldl1()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_04p4x04p6_m1m2m3_shieldl1/sky130_fd_pr__cap_vpp_04p4x04p6_m1m2m3_shieldl1.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_22p5x23p1_pol1m1m2m3m4m5_noshield() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_22p5x23p1_pol1m1m2m3m4m5_noshield fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_22p5x23p1_pol1m1m2m3m4m5_noshield()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_22p5x23p1_pol1m1m2m3m4m5_noshield/sky130_fd_pr__cap_vpp_22p5x23p1_pol1m1m2m3m4m5_noshield.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_20v0_nvt_withptap() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_20v0_nvt_withptap fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_20v0_nvt_withptap()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_20v0_nvt_withptap/sky130_fd_pr__rf_nfet_20v0_nvt_withptap.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3_shieldm4_top() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3_shieldm4_top fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3_shieldm4_top()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_l1m1m2m3_shieldm4/sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3_shieldm4_top.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3_shieldm4() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3_shieldm4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3_shieldm4()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_l1m1m2m3_shieldm4/sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3_shieldm4.gds"
    )


@cell
def sky130_fd_pr__rf_npn_11v0_W1p00L1p00() -> gf.Component:
    """Returns sky130_fd_pr__rf_npn_11v0_W1p00L1p00 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_npn_11v0_W1p00L1p00()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_npn_11v0/sky130_fd_pr__rf_npn_11v0_W1p00L1p00.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_04p4x04p6_l1m1m2_noshield() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_04p4x04p6_l1m1m2_noshield fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_04p4x04p6_l1m1m2_noshield()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_04p4x04p6_l1m1m2_noshield/sky130_fd_pr__cap_vpp_04p4x04p6_l1m1m2_noshield.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_04p4x04p6_l1m1m2_noshield_o2subcell() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_04p4x04p6_l1m1m2_noshield_o2subcell fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_04p4x04p6_l1m1m2_noshield_o2subcell()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_04p4x04p6_l1m1m2_noshield/sky130_fd_pr__cap_vpp_04p4x04p6_l1m1m2_noshield_o2subcell.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_x7() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_x7 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_x7()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5/sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_x7.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_x6() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_x6 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_x6()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5/sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_x6.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_top() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_top fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_top()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5/sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_top.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_x() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_x fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_x()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5/sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_x.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_xtop() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_xtop fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_xtop()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5/sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_xtop.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5/sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_x8() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_x8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_x8()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5/sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_x8.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_x9() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_x9 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_x9()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5/sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_x9.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_02p7x06p1_m1m2m3m4_shieldl1_fingercap() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_02p7x06p1_m1m2m3m4_shieldl1_fingercap fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_02p7x06p1_m1m2m3m4_shieldl1_fingercap()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_02p7x06p1_m1m2m3m4_shieldl1/sky130_fd_pr__cap_vpp_02p7x06p1_m1m2m3m4_shieldl1_fingercap.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_11p5x11p7_m1m2m3_shieldl1m5_floatm4() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_11p5x11p7_m1m2m3_shieldl1m5_floatm4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_11p5x11p7_m1m2m3_shieldl1m5_floatm4()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_m1m2m3_shieldl1m5_floatm4/sky130_fd_pr__cap_vpp_11p5x11p7_m1m2m3_shieldl1m5_floatm4.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_11p5x11p7_m1m2m3_shieldl1m5_floatm4_top() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_11p5x11p7_m1m2m3_shieldl1m5_floatm4_top fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_11p5x11p7_m1m2m3_shieldl1m5_floatm4_top()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_m1m2m3_shieldl1m5_floatm4/sky130_fd_pr__cap_vpp_11p5x11p7_m1m2m3_shieldl1m5_floatm4_top.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_55p8x23p1_pol1m1m2m3m4m5_noshield_test() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_55p8x23p1_pol1m1m2m3m4m5_noshield_test fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_55p8x23p1_pol1m1m2m3m4m5_noshield_test()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_55p8x23p1_pol1m1m2m3m4m5_noshield/sky130_fd_pr__cap_vpp_55p8x23p1_pol1m1m2m3m4m5_noshield_test.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_55p8x23p1_pol1m1m2m3m4m5_noshield() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_55p8x23p1_pol1m1m2m3m4m5_noshield fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_55p8x23p1_pol1m1m2m3m4m5_noshield()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_55p8x23p1_pol1m1m2m3m4m5_noshield/sky130_fd_pr__cap_vpp_55p8x23p1_pol1m1m2m3m4m5_noshield.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_55p8x23p1_pol1m1m2m3m4m5_noshield_m5pullin() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_55p8x23p1_pol1m1m2m3m4m5_noshield_m5pullin fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_55p8x23p1_pol1m1m2m3m4m5_noshield_m5pullin()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_55p8x23p1_pol1m1m2m3m4m5_noshield/sky130_fd_pr__cap_vpp_55p8x23p1_pol1m1m2m3m4m5_noshield_m5pullin.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_08p6x07p8_m1m2m3_shieldl1() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_08p6x07p8_m1m2m3_shieldl1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_08p6x07p8_m1m2m3_shieldl1()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_08p6x07p8_m1m2m3_shieldl1/sky130_fd_pr__cap_vpp_08p6x07p8_m1m2m3_shieldl1.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_11p5x11p7_m1m4_noshield() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_11p5x11p7_m1m4_noshield fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_11p5x11p7_m1m4_noshield()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_m1m4_noshield/sky130_fd_pr__cap_vpp_11p5x11p7_m1m4_noshield.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_20v0_withptap() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_20v0_withptap fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_20v0_withptap()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_20v0_withptap/sky130_fd_pr__rf_nfet_20v0_withptap.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_55p8x11p7_pol1m1m2m3m4m5_noshield_m5pullin() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_55p8x11p7_pol1m1m2m3m4m5_noshield_m5pullin fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_55p8x11p7_pol1m1m2m3m4m5_noshield_m5pullin()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_55p8x11p7_pol1m1m2m3m4m5_noshield/sky130_fd_pr__cap_vpp_55p8x11p7_pol1m1m2m3m4m5_noshield_m5pullin.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_55p8x11p7_pol1m1m2m3m4m5_noshield() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_55p8x11p7_pol1m1m2m3m4m5_noshield fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_55p8x11p7_pol1m1m2m3m4m5_noshield()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_55p8x11p7_pol1m1m2m3m4m5_noshield/sky130_fd_pr__cap_vpp_55p8x11p7_pol1m1m2m3m4m5_noshield.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_08p6x07p8_m1m2m3_shieldl1m5_floatm4_top() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_08p6x07p8_m1m2m3_shieldl1m5_floatm4_top fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_08p6x07p8_m1m2m3_shieldl1m5_floatm4_top()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_08p6x07p8_m1m2m3_shieldl1m5_floatm4/sky130_fd_pr__cap_vpp_08p6x07p8_m1m2m3_shieldl1m5_floatm4_top.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_08p6x07p8_m1m2m3_shieldl1m5_floatm4() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_08p6x07p8_m1m2m3_shieldl1m5_floatm4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_08p6x07p8_m1m2m3_shieldl1m5_floatm4()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_08p6x07p8_m1m2m3_shieldl1m5_floatm4/sky130_fd_pr__cap_vpp_08p6x07p8_m1m2m3_shieldl1m5_floatm4.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_02p9x06p1_m1m2m3m4_shieldl1_fingercap2() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_02p9x06p1_m1m2m3m4_shieldl1_fingercap2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_02p9x06p1_m1m2m3m4_shieldl1_fingercap2()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_02p9x06p1_m1m2m3m4_shieldl1/sky130_fd_pr__cap_vpp_02p9x06p1_m1m2m3m4_shieldl1_fingercap2.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_mcM04W5p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_mcM04W5p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_mcM04W5p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_mcM04W5p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_aF06W3p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_aF06W3p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_aF06W3p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aF06W3p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_aF02W3p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_aF02W3p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_aF02W3p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aF02W3p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_hcM04W5p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_hcM04W5p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_hcM04W5p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_hcM04W5p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_aM04W5p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_aM04W5p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_aM04W5p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aM04W5p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_bM02W5p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_bM02W5p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_bM02W5p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_bM02W5p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_aF08W0p84L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_aF08W0p84L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_aF08W0p84L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aF08W0p84L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_aM02W5p00L0p18() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_aM02W5p00L0p18 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_aM02W5p00L0p18()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aM02W5p00L0p18.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_bM04W5p00L0p18() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_bM04W5p00L0p18 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_bM04W5p00L0p18()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_bM04W5p00L0p18.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_bM04W5p00L0p25() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_bM04W5p00L0p25 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_bM04W5p00L0p25()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_bM04W5p00L0p25.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_aM02W5p00L0p25() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_aM02W5p00L0p25 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_aM02W5p00L0p25()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aM02W5p00L0p25.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_aF08W1p68L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_aF08W1p68L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_aF08W1p68L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aF08W1p68L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_bM04W1p65L0p18() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_bM04W1p65L0p18 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_bM04W1p65L0p18()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_bM04W1p65L0p18.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_aF02W1p68L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_aF02W1p68L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_aF02W1p68L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aF02W1p68L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_aF02W5p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_aF02W5p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_aF02W5p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aF02W5p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_aM02W1p65L0p18() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_aM02W1p65L0p18 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_aM02W1p65L0p18()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aM02W1p65L0p18.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_aM02W1p65L0p25() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_aM02W1p65L0p25 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_aM02W1p65L0p25()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aM02W1p65L0p25.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_mcM04W3p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_mcM04W3p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_mcM04W3p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_mcM04W3p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_bM04W1p65L0p25() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_bM04W1p65L0p25 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_bM04W1p65L0p25()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_bM04W1p65L0p25.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_aF06W1p68L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_aF06W1p68L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_aF06W1p68L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aF06W1p68L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_aM04W3p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_aM04W3p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_aM04W3p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aM04W3p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_bM02W3p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_bM02W3p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_bM02W3p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_bM02W3p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_aF02W0p84L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_aF02W0p84L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_aF02W0p84L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aF02W0p84L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_hcM04W3p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_hcM04W3p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_hcM04W3p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_hcM04W3p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_aF06W0p84L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_aF06W0p84L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_aF06W0p84L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aF06W0p84L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_aF04W2p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_aF04W2p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_aF04W2p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aF04W2p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_bM02W1p65L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_bM02W1p65L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_bM02W1p65L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_bM02W1p65L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_aM04W1p65L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_aM04W1p65L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_aM04W1p65L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aM04W1p65L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_bM04W3p00L0p25() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_bM04W3p00L0p25 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_bM04W3p00L0p25()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_bM04W3p00L0p25.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_aM02W3p00L0p25() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_aM02W3p00L0p25 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_aM02W3p00L0p25()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aM02W3p00L0p25.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_aM02W3p00L0p18() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_aM02W3p00L0p18 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_aM02W3p00L0p18()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aM02W3p00L0p18.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_bM04W3p00L0p18() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_bM04W3p00L0p18 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_bM04W3p00L0p18()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_bM04W3p00L0p18.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_aF04W0p84L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_aF04W0p84L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_aF04W0p84L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aF04W0p84L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_bM04W3p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_bM04W3p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_bM04W3p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_bM04W3p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_aM02W3p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_aM02W3p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_aM02W3p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aM02W3p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_aM04W1p65L0p18() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_aM04W1p65L0p18 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_aM04W1p65L0p18()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aM04W1p65L0p18.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_aF04W5p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_aF04W5p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_aF04W5p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aF04W5p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_aF04W1p68L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_aF04W1p68L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_aF04W1p68L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aF04W1p68L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_bM02W1p65L0p18() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_bM02W1p65L0p18 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_bM02W1p65L0p18()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_bM02W1p65L0p18.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_bM02W1p65L0p25() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_bM02W1p65L0p25 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_bM02W1p65L0p25()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_bM02W1p65L0p25.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_aM04W1p65L0p25() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_aM04W1p65L0p25 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_aM04W1p65L0p25()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aM04W1p65L0p25.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_aM04W3p00L0p25() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_aM04W3p00L0p25 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_aM04W3p00L0p25()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aM04W3p00L0p25.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_bM02W3p00L0p25() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_bM02W3p00L0p25 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_bM02W3p00L0p25()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_bM02W3p00L0p25.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_bM02W3p00L0p18() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_bM02W3p00L0p18 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_bM02W3p00L0p18()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_bM02W3p00L0p18.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_aM04W3p00L0p18() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_aM04W3p00L0p18 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_aM04W3p00L0p18()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aM04W3p00L0p18.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_aF02W2p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_aF02W2p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_aF02W2p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aF02W2p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_aM02W1p65L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_aM02W1p65L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_aM02W1p65L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aM02W1p65L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_bM04W1p65L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_bM04W1p65L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_bM04W1p65L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_bM04W1p65L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_aF06W2p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_aF06W2p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_aF06W2p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aF06W2p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_bM04W5p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_bM04W5p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_bM04W5p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_bM04W5p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_aM02W5p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_aM02W5p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_aM02W5p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aM02W5p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_aF04W3p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_aF04W3p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_aF04W3p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aF04W3p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_bM02W5p00L0p18() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_bM02W5p00L0p18 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_bM02W5p00L0p18()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_bM02W5p00L0p18.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_aM04W5p00L0p18() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_aM04W5p00L0p18 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_aM04W5p00L0p18()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aM04W5p00L0p18.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_aM04W5p00L0p25() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_aM04W5p00L0p25 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_aM04W5p00L0p25()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aM04W5p00L0p25.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_bM02W5p00L0p25() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_bM02W5p00L0p25 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_bM02W5p00L0p25()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_bM02W5p00L0p25.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2_noshield() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2_noshield fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2_noshield()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_l1m1m2_noshield/sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2_noshield.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_cM02W5p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_cM02W5p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_cM02W5p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_cM02W5p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_aM04W3p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_aM04W3p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_aM04W3p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aM04W3p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_bM02W3p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_bM02W3p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_bM02W3p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_bM02W3p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_aF02W0p84L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_aF02W0p84L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_aF02W0p84L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aF02W0p84L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_aF06W0p84L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_aF06W0p84L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_aF06W0p84L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aF06W0p84L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_bM04W1p65L0p18() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_bM04W1p65L0p18 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_bM04W1p65L0p18()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_bM04W1p65L0p18.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_aM02W1p65L0p18() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_aM02W1p65L0p18 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_aM02W1p65L0p18()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aM02W1p65L0p18.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_aM02W1p65L0p25() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_aM02W1p65L0p25 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_aM02W1p65L0p25()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aM02W1p65L0p25.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_aF08W1p65L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_aF08W1p65L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_aF08W1p65L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aF08W1p65L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_bM04W1p65L0p25() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_bM04W1p65L0p25 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_bM04W1p65L0p25()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_bM04W1p65L0p25.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_bM04W3p00L0p25() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_bM04W3p00L0p25 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_bM04W3p00L0p25()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_bM04W3p00L0p25.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_aF08W3p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_aF08W3p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_aF08W3p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aF08W3p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_cM04W5p00L0p25() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_cM04W5p00L0p25 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_cM04W5p00L0p25()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_cM04W5p00L0p25.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_aM02W3p00L0p25() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_aM02W3p00L0p25 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_aM02W3p00L0p25()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aM02W3p00L0p25.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_aM02W3p00L0p18() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_aM02W3p00L0p18 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_aM02W3p00L0p18()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aM02W3p00L0p18.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_cM04W5p00L0p18() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_cM04W5p00L0p18 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_cM04W5p00L0p18()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_cM04W5p00L0p18.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_bM04W3p00L0p18() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_bM04W3p00L0p18 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_bM04W3p00L0p18()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_bM04W3p00L0p18.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_aF02W0p42L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_aF02W0p42L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_aF02W0p42L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aF02W0p42L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_aF06W0p42L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_aF06W0p42L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_aF06W0p42L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aF06W0p42L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_bM02W1p65L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_bM02W1p65L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_bM02W1p65L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_bM02W1p65L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_aM04W1p65L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_aM04W1p65L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_aM04W1p65L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aM04W1p65L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_aF08W0p42L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_aF08W0p42L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_aF08W0p42L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aF08W0p42L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_cM02W3p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_cM02W3p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_cM02W3p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_cM02W3p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_aM04W5p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_aM04W5p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_aM04W5p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aM04W5p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_bM02W5p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_bM02W5p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_bM02W5p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_bM02W5p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_cM04W1p65L0p25() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_cM04W1p65L0p25 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_cM04W1p65L0p25()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_cM04W1p65L0p25.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_aF06W3p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_aF06W3p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_aF06W3p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aF06W3p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_cM04W1p65L0p18() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_cM04W1p65L0p18 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_cM04W1p65L0p18()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_cM04W1p65L0p18.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_aF02W3p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_aF02W3p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_aF02W3p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aF02W3p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_aF02W1p65L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_aF02W1p65L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_aF02W1p65L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aF02W1p65L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_aM02W5p00L0p18() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_aM02W5p00L0p18 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_aM02W5p00L0p18()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aM02W5p00L0p18.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_cM04W3p00L0p18() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_cM04W3p00L0p18 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_cM04W3p00L0p18()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_cM04W3p00L0p18.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_bM04W5p00L0p18() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_bM04W5p00L0p18 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_bM04W5p00L0p18()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_bM04W5p00L0p18.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_bM04W5p00L0p25() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_bM04W5p00L0p25 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_bM04W5p00L0p25()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_bM04W5p00L0p25.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_aF06W1p65L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_aF06W1p65L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_aF06W1p65L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aF06W1p65L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_cM04W3p00L0p25() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_cM04W3p00L0p25 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_cM04W3p00L0p25()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_cM04W3p00L0p25.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_aM02W5p00L0p25() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_aM02W5p00L0p25 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_aM02W5p00L0p25()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aM02W5p00L0p25.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_cM02W1p65L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_cM02W1p65L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_cM02W1p65L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_cM02W1p65L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_aF08W0p84L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_aF08W0p84L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_aF08W0p84L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aF08W0p84L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_cM02W1p65L0p25() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_cM02W1p65L0p25 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_cM02W1p65L0p25()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_cM02W1p65L0p25.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_aF04W3p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_aF04W3p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_aF04W3p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aF04W3p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_cM02W1p65L0p18() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_cM02W1p65L0p18 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_cM02W1p65L0p18()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_cM02W1p65L0p18.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_bM04W5p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_bM04W5p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_bM04W5p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_bM04W5p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_cM04W3p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_cM04W3p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_cM04W3p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_cM04W3p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_aM02W5p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_aM02W5p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_aM02W5p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aM02W5p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_cM04W1p65L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_cM04W1p65L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_cM04W1p65L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_cM04W1p65L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_bM02W5p00L0p18() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_bM02W5p00L0p18 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_bM02W5p00L0p18()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_bM02W5p00L0p18.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_aM04W5p00L0p18() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_aM04W5p00L0p18 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_aM04W5p00L0p18()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aM04W5p00L0p18.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_cM02W3p00L0p18() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_cM02W3p00L0p18 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_cM02W3p00L0p18()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_cM02W3p00L0p18.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_aF04W1p65L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_aF04W1p65L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_aF04W1p65L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aF04W1p65L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_cM02W3p00L0p25() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_cM02W3p00L0p25 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_cM02W3p00L0p25()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_cM02W3p00L0p25.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_aM04W5p00L0p25() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_aM04W5p00L0p25 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_aM04W5p00L0p25()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aM04W5p00L0p25.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_bM02W5p00L0p25() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_bM02W5p00L0p25 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_bM02W5p00L0p25()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_bM02W5p00L0p25.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_aM04W1p65L0p18() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_aM04W1p65L0p18 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_aM04W1p65L0p18()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aM04W1p65L0p18.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_bM02W1p65L0p18() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_bM02W1p65L0p18 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_bM02W1p65L0p18()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_bM02W1p65L0p18.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_bM02W1p65L0p25() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_bM02W1p65L0p25 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_bM02W1p65L0p25()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_bM02W1p65L0p25.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_aM04W1p65L0p25() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_aM04W1p65L0p25 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_aM04W1p65L0p25()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aM04W1p65L0p25.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_aF04W0p84L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_aF04W0p84L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_aF04W0p84L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aF04W0p84L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_bM04W3p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_bM04W3p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_bM04W3p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_bM04W3p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_cM04W5p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_cM04W5p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_cM04W5p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_cM04W5p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_aM02W3p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_aM02W3p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_aM02W3p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aM02W3p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_aF04W0p42L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_aF04W0p42L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_aF04W0p42L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aF04W0p42L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_aM02W1p65L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_aM02W1p65L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_aM02W1p65L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aM02W1p65L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_bM04W1p65L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_bM04W1p65L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_bM04W1p65L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_bM04W1p65L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_cM02W5p00L0p25() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_cM02W5p00L0p25 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_cM02W5p00L0p25()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_cM02W5p00L0p25.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_aM04W3p00L0p25() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_aM04W3p00L0p25 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_aM04W3p00L0p25()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aM04W3p00L0p25.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_bM02W3p00L0p25() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_bM02W3p00L0p25 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_bM02W3p00L0p25()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_bM02W3p00L0p25.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_bM02W3p00L0p18() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_bM02W3p00L0p18 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_bM02W3p00L0p18()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_bM02W3p00L0p18.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_aM04W3p00L0p18() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_aM04W3p00L0p18 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_aM04W3p00L0p18()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aM04W3p00L0p18.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_lvt_cM02W5p00L0p18() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_lvt_cM02W5p00L0p18 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_lvt_cM02W5p00L0p18()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_cM02W5p00L0p18.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_06p8x06p1_l1m1m2m3_shieldpom4() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_06p8x06p1_l1m1m2m3_shieldpom4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_06p8x06p1_l1m1m2m3_shieldpom4()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_06p8x06p1_l1m1m2m3_shieldpom4/sky130_fd_pr__cap_vpp_06p8x06p1_l1m1m2m3_shieldpom4.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_06p8x06p1_l1m1m2m3_shieldpom4_top() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_06p8x06p1_l1m1m2m3_shieldpom4_top fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_06p8x06p1_l1m1m2m3_shieldpom4_top()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_06p8x06p1_l1m1m2m3_shieldpom4/sky130_fd_pr__cap_vpp_06p8x06p1_l1m1m2m3_shieldpom4_top.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_11p5x23p1_pol1m1m2m3m4m5_noshield() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_11p5x23p1_pol1m1m2m3m4m5_noshield fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_11p5x23p1_pol1m1m2m3m4m5_noshield()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x23p1_pol1m1m2m3m4m5_noshield/sky130_fd_pr__cap_vpp_11p5x23p1_pol1m1m2m3m4m5_noshield.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_11p5x11p7_m1m2_noshield() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_11p5x11p7_m1m2_noshield fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_11p5x11p7_m1m2_noshield()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_m1m2_noshield/sky130_fd_pr__cap_vpp_11p5x11p7_m1m2_noshield.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_bM02W5p00L0p25() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_bM02W5p00L0p25 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_bM02W5p00L0p25()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_bM02W5p00L0p25.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_aM04W5p00L0p25() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_aM04W5p00L0p25 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_aM04W5p00L0p25()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_aM04W5p00L0p25.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_aM04W5p00L0p18() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_aM04W5p00L0p18 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_aM04W5p00L0p18()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_aM04W5p00L0p18.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_bM02W5p00L0p18() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_bM02W5p00L0p18 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_bM02W5p00L0p18()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_bM02W5p00L0p18.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_aM02W5p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_aM02W5p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_aM02W5p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_aM02W5p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_bM04W5p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_bM04W5p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_bM04W5p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_bM04W5p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_aM04W3p00L0p18() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_aM04W3p00L0p18 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_aM04W3p00L0p18()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_aM04W3p00L0p18.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_bM02W3p00L0p18() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_bM02W3p00L0p18 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_bM02W3p00L0p18()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_bM02W3p00L0p18.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_bM02W3p00L0p25() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_bM02W3p00L0p25 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_bM02W3p00L0p25()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_bM02W3p00L0p25.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_aM04W3p00L0p25() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_aM04W3p00L0p25 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_aM04W3p00L0p25()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_aM04W3p00L0p25.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_bM04W1p65L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_bM04W1p65L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_bM04W1p65L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_bM04W1p65L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_aM02W1p65L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_aM02W1p65L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_aM02W1p65L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_aM02W1p65L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_aM02W3p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_aM02W3p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_aM02W3p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_aM02W3p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_bM04W3p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_bM04W3p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_bM04W3p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_bM04W3p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_aM04W1p65L0p25() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_aM04W1p65L0p25 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_aM04W1p65L0p25()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_aM04W1p65L0p25.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_bM02W1p65L0p25() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_bM02W1p65L0p25 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_bM02W1p65L0p25()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_bM02W1p65L0p25.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_bM02W1p65L0p18() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_bM02W1p65L0p18 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_bM02W1p65L0p18()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_bM02W1p65L0p18.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_aM04W1p65L0p18() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_aM04W1p65L0p18 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_aM04W1p65L0p18()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_aM04W1p65L0p18.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_aM04W1p65L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_aM04W1p65L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_aM04W1p65L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_aM04W1p65L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_bM02W1p65L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_bM02W1p65L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_bM02W1p65L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_bM02W1p65L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_mcM04W3p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_mcM04W3p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_mcM04W3p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_mcM04W3p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_bM04W3p00L0p18() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_bM04W3p00L0p18 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_bM04W3p00L0p18()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_bM04W3p00L0p18.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_aM02W3p00L0p18() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_aM02W3p00L0p18 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_aM02W3p00L0p18()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_aM02W3p00L0p18.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_aM02W3p00L0p25() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_aM02W3p00L0p25 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_aM02W3p00L0p25()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_aM02W3p00L0p25.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_bM04W3p00L0p25() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_bM04W3p00L0p25 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_bM04W3p00L0p25()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_bM04W3p00L0p25.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_hcM04W3p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_hcM04W3p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_hcM04W3p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_hcM04W3p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_bM04W1p65L0p25() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_bM04W1p65L0p25 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_bM04W1p65L0p25()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_bM04W1p65L0p25.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_aM02W1p65L0p25() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_aM02W1p65L0p25 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_aM02W1p65L0p25()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_aM02W1p65L0p25.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_aM02W1p65L0p18() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_aM02W1p65L0p18 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_aM02W1p65L0p18()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_aM02W1p65L0p18.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_bM04W1p65L0p18() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_bM04W1p65L0p18 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_bM04W1p65L0p18()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_bM04W1p65L0p18.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_bM02W3p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_bM02W3p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_bM02W3p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_bM02W3p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_aM04W3p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_aM04W3p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_aM04W3p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_aM04W3p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_mcM04W5p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_mcM04W5p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_mcM04W5p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_mcM04W5p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_aM02W5p00L0p25() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_aM02W5p00L0p25 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_aM02W5p00L0p25()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_aM02W5p00L0p25.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_hcM04W5p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_hcM04W5p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_hcM04W5p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_hcM04W5p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_bM04W5p00L0p25() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_bM04W5p00L0p25 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_bM04W5p00L0p25()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_bM04W5p00L0p25.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_bM04W5p00L0p18() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_bM04W5p00L0p18 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_bM04W5p00L0p18()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_bM04W5p00L0p18.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_aM02W5p00L0p18() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_aM02W5p00L0p18 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_aM02W5p00L0p18()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_aM02W5p00L0p18.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_bM02W5p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_bM02W5p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_bM02W5p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_bM02W5p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_01v8_aM04W5p00L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_01v8_aM04W5p00L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_01v8_aM04W5p00L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_aM04W5p00L0p15.gds"
    )


@cell
def sky130_fd_pr__rf_test_coil1() -> gf.Component:
    """Returns sky130_fd_pr__rf_test_coil1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_test_coil1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_pr/cells/rf_test_coil1/sky130_fd_pr__rf_test_coil1.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_11p5x11p7_pol1m1m2m3m4m5_noshield() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_11p5x11p7_pol1m1m2m3m4m5_noshield fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_11p5x11p7_pol1m1m2m3m4m5_noshield()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_pol1m1m2m3m4m5_noshield/sky130_fd_pr__cap_vpp_11p5x11p7_pol1m1m2m3m4m5_noshield.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_01v8_mvt_aF02W0p84L0p15() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_01v8_mvt_aF02W0p84L0p15 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_01v8_mvt_aF02W0p84L0p15()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_01v8_mvt/sky130_fd_pr__rf_pfet_01v8_mvt_aF02W0p84L0p15.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_05p9x05p9_m1m2m3m4_shieldl1_wafflecap() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_05p9x05p9_m1m2m3m4_shieldl1_wafflecap fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_05p9x05p9_m1m2m3m4_shieldl1_wafflecap()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_05p9x05p9_m1m2m3m4_shieldl1/sky130_fd_pr__cap_vpp_05p9x05p9_m1m2m3m4_shieldl1_wafflecap.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_20v0_nvt_withptap_iso() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_20v0_nvt_withptap_iso fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_20v0_nvt_withptap_iso()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_20v0_nvt_withptap_iso/sky130_fd_pr__rf_nfet_20v0_nvt_withptap_iso.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_11p3x11p3_m1m2m3m4_shieldl1_wafflecap() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_11p3x11p3_m1m2m3m4_shieldl1_wafflecap fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_11p3x11p3_m1m2m3m4_shieldl1_wafflecap()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_11p3x11p3_m1m2m3m4_shieldl1/sky130_fd_pr__cap_vpp_11p3x11p3_m1m2m3m4_shieldl1_wafflecap.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_44p7x11p7_pol1m1m2m3m4m5_noshield() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_44p7x11p7_pol1m1m2m3m4m5_noshield fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_44p7x11p7_pol1m1m2m3m4m5_noshield()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_44p7x11p7_pol1m1m2m3m4m5_noshield/sky130_fd_pr__cap_vpp_44p7x11p7_pol1m1m2m3m4m5_noshield.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_33p6x11p7_pol1m1m2m3m4m5_noshield() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_33p6x11p7_pol1m1m2m3m4m5_noshield fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_33p6x11p7_pol1m1m2m3m4m5_noshield()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_33p6x11p7_pol1m1m2m3m4m5_noshield/sky130_fd_pr__cap_vpp_33p6x11p7_pol1m1m2m3m4m5_noshield.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_20v0_aup() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_20v0_aup fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_20v0_aup()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_20v0_aup/sky130_fd_pr__rf_nfet_20v0_aup.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_44p7x23p1_pol1m1m2m3m4m5_noshield() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_44p7x23p1_pol1m1m2m3m4m5_noshield fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_44p7x23p1_pol1m1m2m3m4m5_noshield()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_44p7x23p1_pol1m1m2m3m4m5_noshield/sky130_fd_pr__cap_vpp_44p7x23p1_pol1m1m2m3m4m5_noshield.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_33p6x23p1_pol1m1m2m3m4m5_noshield() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_33p6x23p1_pol1m1m2m3m4m5_noshield fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_33p6x23p1_pol1m1m2m3m4m5_noshield()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_33p6x23p1_pol1m1m2m3m4m5_noshield/sky130_fd_pr__cap_vpp_33p6x23p1_pol1m1m2m3m4m5_noshield.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_20v0_nvt_aup() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_20v0_nvt_aup fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_20v0_nvt_aup()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_20v0_nvt_aup/sky130_fd_pr__rf_nfet_20v0_nvt_aup.gds"
    )


@cell
def sky130_fd_pr__rf_nfet_20v0_zvt_withptap() -> gf.Component:
    """Returns sky130_fd_pr__rf_nfet_20v0_zvt_withptap fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_nfet_20v0_zvt_withptap()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_nfet_20v0_zvt_withptap/sky130_fd_pr__rf_nfet_20v0_zvt_withptap.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_04p4x04p6_m1m2_noshield_o2() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_04p4x04p6_m1m2_noshield_o2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_04p4x04p6_m1m2_noshield_o2()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_04p4x04p6_m1m2_noshield/sky130_fd_pr__cap_vpp_04p4x04p6_m1m2_noshield_o2.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_04p4x04p6_m1m2_noshield() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_04p4x04p6_m1m2_noshield fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_04p4x04p6_m1m2_noshield()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_04p4x04p6_m1m2_noshield/sky130_fd_pr__cap_vpp_04p4x04p6_m1m2_noshield.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldm5_top() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldm5_top fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldm5_top()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_l1m1m2m3m4_shieldm5/sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldm5_top.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldm5() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldm5 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldm5()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_l1m1m2m3m4_shieldm5/sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldm5.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_08p6x07p8_m1m2_shieldl1() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_08p6x07p8_m1m2_shieldl1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_08p6x07p8_m1m2_shieldl1()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_08p6x07p8_m1m2_shieldl1/sky130_fd_pr__cap_vpp_08p6x07p8_m1m2_shieldl1.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_08p6x07p8_l1m1m2_shieldpo_floatm3() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_08p6x07p8_l1m1m2_shieldpo_floatm3 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_08p6x07p8_l1m1m2_shieldpo_floatm3()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_08p6x07p8_l1m1m2_shieldpo_floatm3/sky130_fd_pr__cap_vpp_08p6x07p8_l1m1m2_shieldpo_floatm3.gds"
    )


@cell
def sky130_fd_pr__esd_rf_nfet_20v0_hbm_21vW60p00() -> gf.Component:
    """Returns sky130_fd_pr__esd_rf_nfet_20v0_hbm_21vW60p00 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__esd_rf_nfet_20v0_hbm_21vW60p00()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/esd_rf_nfet_20v0_hbm/sky130_fd_pr__esd_rf_nfet_20v0_hbm_21vW60p00.gds"
    )


@cell
def sky130_fd_pr__esd_rf_nfet_20v0_hbm_32vW60p00() -> gf.Component:
    """Returns sky130_fd_pr__esd_rf_nfet_20v0_hbm_32vW60p00 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__esd_rf_nfet_20v0_hbm_32vW60p00()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/esd_rf_nfet_20v0_hbm/sky130_fd_pr__esd_rf_nfet_20v0_hbm_32vW60p00.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_02p7x41p1_m1m2m3m4_shieldl1_fingercap() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_02p7x41p1_m1m2m3m4_shieldl1_fingercap fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_02p7x41p1_m1m2m3m4_shieldl1_fingercap()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_02p7x41p1_m1m2m3m4_shieldl1/sky130_fd_pr__cap_vpp_02p7x41p1_m1m2m3m4_shieldl1_fingercap.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_03p9x03p9_m1m2_shieldl1_floatm3() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_03p9x03p9_m1m2_shieldl1_floatm3 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_03p9x03p9_m1m2_shieldl1_floatm3()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_03p9x03p9_m1m2_shieldl1_floatm3/sky130_fd_pr__cap_vpp_03p9x03p9_m1m2_shieldl1_floatm3.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_11p5x11p7_m1m2m3m4_shieldm5() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_11p5x11p7_m1m2m3m4_shieldm5 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_11p5x11p7_m1m2m3m4_shieldm5()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_m1m2m3m4_shieldm5/sky130_fd_pr__cap_vpp_11p5x11p7_m1m2m3m4_shieldm5.gds"
    )


@cell
def sky130_fd_pr__rf_pfet_20v0_withptap() -> gf.Component:
    """Returns sky130_fd_pr__rf_pfet_20v0_withptap fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_pfet_20v0_withptap()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_pfet_20v0_withptap/sky130_fd_pr__rf_pfet_20v0_withptap.gds"
    )


@cell
def sky130_fd_pr__rf_aura_blocking() -> gf.Component:
    """Returns sky130_fd_pr__rf_aura_blocking fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__rf_aura_blocking()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/rf_aura_blocking/sky130_fd_pr__rf_aura_blocking.gds"
    )


@cell
def sky130_fd_pr__cap_vpp_02p7x11p1_m1m2m3m4_shieldl1_fingercap() -> gf.Component:
    """Returns sky130_fd_pr__cap_vpp_02p7x11p1_m1m2m3m4_shieldl1_fingercap fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_pr__cap_vpp_02p7x11p1_m1m2m3m4_shieldl1_fingercap()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_pr/cells/cap_vpp_02p7x11p1_m1m2m3m4_shieldl1/sky130_fd_pr__cap_vpp_02p7x11p1_m1m2m3m4_shieldl1_fingercap.gds"
    )
