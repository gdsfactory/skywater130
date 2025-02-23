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
add_ports = gf.compose(add_ports_m1, add_ports_m2)

gdsdir = PATH.module
import_gds = partial(gf.import_gds, post_process=[add_ports])


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
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_l1m1m2m3_shieldm4/sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3_shieldm4_top.gds",
        cellname="sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3_shieldm4_top",
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
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_l1m1m2m3_shieldm4/sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3_shieldm4.gds",
        cellname="sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3_shieldm4",
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
        / "src/sky130_fd_pr/cells/cap_vpp_44p7x23p1_pol1m1m2m3m4m5_noshield/sky130_fd_pr__cap_vpp_44p7x23p1_pol1m1m2m3m4m5_noshield.gds",
        cellname="sky130_fd_pr__cap_vpp_44p7x23p1_pol1m1m2m3m4m5_noshield",
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
        / "src/sky130_fd_pr/cells/cap_vpp_02p9x06p1_m1m2m3m4_shieldl1/sky130_fd_pr__cap_vpp_02p9x06p1_m1m2m3m4_shieldl1_fingercap2.gds",
        cellname="sky130_fd_pr__cap_vpp_02p9x06p1_m1m2m3m4_shieldl1_fingercap2",
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
        / "src/sky130_fd_pr/cells/cap_vpp_08p6x07p8_l1m1m2_noshield/sky130_fd_pr__cap_vpp_08p6x07p8_l1m1m2_noshield_o2subcell.gds",
        cellname="sky130_fd_pr__cap_vpp_08p6x07p8_l1m1m2_noshield_o2subcell",
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
        / "src/sky130_fd_pr/cells/cap_vpp_08p6x07p8_l1m1m2_noshield/sky130_fd_pr__cap_vpp_08p6x07p8_l1m1m2_noshield.gds",
        cellname="sky130_fd_pr__cap_vpp_08p6x07p8_l1m1m2_noshield",
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
        / "src/sky130_fd_pr/cells/rf_nfet_20v0_nvt_withptap_iso/sky130_fd_pr__rf_nfet_20v0_nvt_withptap_iso.gds",
        cellname="sky130_fd_pr__rf_nfet_20v0_nvt_withptap_iso",
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
        / "src/sky130_fd_pr/cells/cap_vpp_33p6x11p7_pol1m1m2m3m4m5_noshield/sky130_fd_pr__cap_vpp_33p6x11p7_pol1m1m2m3m4m5_noshield.gds",
        cellname="sky130_fd_pr__cap_vpp_33p6x11p7_pol1m1m2m3m4m5_noshield",
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
        / "src/sky130_fd_pr/cells/cap_vpp_08p6x07p8_m1m2m3_shieldl1m5_floatm4/sky130_fd_pr__cap_vpp_08p6x07p8_m1m2m3_shieldl1m5_floatm4.gds",
        cellname="sky130_fd_pr__cap_vpp_08p6x07p8_m1m2m3_shieldl1m5_floatm4",
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
        / "src/sky130_fd_pr/cells/cap_vpp_08p6x07p8_m1m2m3_shieldl1m5_floatm4/sky130_fd_pr__cap_vpp_08p6x07p8_m1m2m3_shieldl1m5_floatm4_top.gds",
        cellname="sky130_fd_pr__cap_vpp_08p6x07p8_m1m2m3_shieldl1m5_floatm4_top",
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
        / "src/sky130_fd_pr/cells/esd_rf_nfet_20v0_hbm/sky130_fd_pr__esd_rf_nfet_20v0_hbm_21vW60p00.gds",
        cellname="sky130_fd_pr__esd_rf_nfet_20v0_hbm_21vW60p00",
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
        / "src/sky130_fd_pr/cells/esd_rf_nfet_20v0_hbm/sky130_fd_pr__esd_rf_nfet_20v0_hbm_32vW60p00.gds",
        cellname="sky130_fd_pr__esd_rf_nfet_20v0_hbm_32vW60p00",
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
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_pol1m1m2m3m4m5_noshield/sky130_fd_pr__cap_vpp_11p5x11p7_pol1m1m2m3m4m5_noshield.gds",
        cellname="sky130_fd_pr__cap_vpp_11p5x11p7_pol1m1m2m3m4m5_noshield",
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
        / "src/sky130_fd_pr/cells/cap_vpp_02p4x04p6_m1m2_noshield/sky130_fd_pr__cap_vpp_02p4x04p6_m1m2_noshield.gds",
        cellname="sky130_fd_pr__cap_vpp_02p4x04p6_m1m2_noshield",
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
        / "src/sky130_fd_pr/cells/cap_vpp_03p9x03p9_m1m2_shieldl1_floatm3/sky130_fd_pr__cap_vpp_03p9x03p9_m1m2_shieldl1_floatm3.gds",
        cellname="sky130_fd_pr__cap_vpp_03p9x03p9_m1m2_shieldl1_floatm3",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_cM04W5p00L0p18.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_cM04W5p00L0p18",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_cM04W3p00L0p25.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_cM04W3p00L0p25",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_cM04W3p00L0p18.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_cM04W3p00L0p18",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aF02W0p42L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_aF02W0p42L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aF08W0p42L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_aF08W0p42L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aF06W0p42L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_aF06W0p42L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aM02W3p00L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_aM02W3p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aM04W3p00L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_aM04W3p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aF06W0p84L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_aF06W0p84L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aF04W1p65L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_aF04W1p65L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_cM04W1p65L0p18.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_cM04W1p65L0p18",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aF04W0p84L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_aF04W0p84L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aM04W1p65L0p25.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_aM04W1p65L0p25",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aF06W3p00L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_aF06W3p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_cM02W1p65L0p18.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_cM02W1p65L0p18",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aM02W5p00L0p18.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_aM02W5p00L0p18",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_cM02W3p00L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_cM02W3p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_bM02W3p00L0p25.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_bM02W3p00L0p25",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_cM04W5p00L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_cM04W5p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_bM02W1p65L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_bM02W1p65L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aF04W0p42L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_aF04W0p42L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_bM04W1p65L0p18.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_bM04W1p65L0p18",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aF04W3p00L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_aF04W3p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_cM02W5p00L0p25.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_cM02W5p00L0p25",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_bM02W5p00L0p18.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_bM02W5p00L0p18",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_bM04W1p65L0p25.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_bM04W1p65L0p25",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_bM02W5p00L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_bM02W5p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_cM04W1p65L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_cM04W1p65L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_bM04W5p00L0p18.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_bM04W5p00L0p18",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_cM04W3p00L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_cM04W3p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aF08W1p65L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_aF08W1p65L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aM02W1p65L0p25.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_aM02W1p65L0p25",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_bM02W1p65L0p18.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_bM02W1p65L0p18",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aF02W3p00L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_aF02W3p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aF08W0p84L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_aF08W0p84L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_bM04W3p00L0p18.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_bM04W3p00L0p18",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aF08W3p00L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_aF08W3p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_cM04W1p65L0p25.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_cM04W1p65L0p25",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_bM04W5p00L0p25.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_bM04W5p00L0p25",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_bM04W1p65L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_bM04W1p65L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_bM02W5p00L0p25.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_bM02W5p00L0p25",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aM04W5p00L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_aM04W5p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aF06W1p65L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_aF06W1p65L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_bM02W3p00L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_bM02W3p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aM04W3p00L0p18.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_aM04W3p00L0p18",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_bM02W1p65L0p25.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_bM02W1p65L0p25",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aM02W3p00L0p18.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_aM02W3p00L0p18",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_bM04W5p00L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_bM04W5p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_cM02W5p00L0p18.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_cM02W5p00L0p18",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_bM04W3p00L0p25.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_bM04W3p00L0p25",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aM02W1p65L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_aM02W1p65L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_cM02W1p65L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_cM02W1p65L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_cM02W3p00L0p25.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_cM02W3p00L0p25",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aM04W1p65L0p18.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_aM04W1p65L0p18",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_cM02W3p00L0p18.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_cM02W3p00L0p18",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aM02W5p00L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_aM02W5p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_cM02W1p65L0p25.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_cM02W1p65L0p25",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aM02W1p65L0p18.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_aM02W1p65L0p18",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_bM02W3p00L0p18.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_bM02W3p00L0p18",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_cM04W5p00L0p25.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_cM04W5p00L0p25",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aM02W5p00L0p25.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_aM02W5p00L0p25",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aM04W3p00L0p25.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_aM04W3p00L0p25",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aM02W3p00L0p25.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_aM02W3p00L0p25",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_cM02W5p00L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_cM02W5p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_bM04W3p00L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_bM04W3p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aM04W5p00L0p25.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_aM04W5p00L0p25",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aM04W5p00L0p18.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_aM04W5p00L0p18",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aM04W1p65L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_aM04W1p65L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aF02W1p65L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_aF02W1p65L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8_lvt/sky130_fd_pr__rf_nfet_01v8_lvt_aF02W0p84L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_lvt_aF02W0p84L0p15",
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
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_l1m1m2_shieldpom3/sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2_shieldpom3.gds",
        cellname="sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2_shieldpom3",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8_mvt/sky130_fd_pr__rf_pfet_01v8_mvt_aF02W0p84L0p15.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_mvt_aF02W0p84L0p15",
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
        / "src/sky130_fd_pr/cells/rf_aura_blocking/sky130_fd_pr__rf_aura_blocking.gds",
        cellname="sky130_fd_pr__rf_aura_blocking",
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
        / "src/sky130_fd_pr/cells/cap_vpp_11p3x11p8_l1m1m2m3m4_shieldm5/sky130_fd_pr__cap_vpp_11p3x11p8_l1m1m2m3m4_shieldm5_nhvtop.gds",
        cellname="sky130_fd_pr__cap_vpp_11p3x11p8_l1m1m2m3m4_shieldm5_nhvtop",
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
        / "src/sky130_fd_pr/cells/cap_vpp_11p3x11p8_l1m1m2m3m4_shieldm5/sky130_fd_pr__cap_vpp_11p3x11p8_l1m1m2m3m4_shieldm5_nhv.gds",
        cellname="sky130_fd_pr__cap_vpp_11p3x11p8_l1m1m2m3m4_shieldm5_nhv",
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
        / "src/sky130_fd_pr/cells/cap_vpp_44p7x11p7_pol1m1m2m3m4m5_noshield/sky130_fd_pr__cap_vpp_44p7x11p7_pol1m1m2m3m4m5_noshield.gds",
        cellname="sky130_fd_pr__cap_vpp_44p7x11p7_pol1m1m2m3m4m5_noshield",
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
        / "src/sky130_fd_pr/cells/cap_vpp_22p5x11p7_pol1m1m2m3m4m5_noshield/sky130_fd_pr__cap_vpp_22p5x11p7_pol1m1m2m3m4m5_noshield.gds",
        cellname="sky130_fd_pr__cap_vpp_22p5x11p7_pol1m1m2m3m4m5_noshield",
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
        / "src/sky130_fd_pr/cells/cap_vpp_08p6x07p8_m1m2m3_shieldl1/sky130_fd_pr__cap_vpp_08p6x07p8_m1m2m3_shieldl1.gds",
        cellname="sky130_fd_pr__cap_vpp_08p6x07p8_m1m2m3_shieldl1",
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
        / "src/sky130_fd_pr/cells/cap_vpp_08p6x07p8_m1m2_shieldl1/sky130_fd_pr__cap_vpp_08p6x07p8_m1m2_shieldl1.gds",
        cellname="sky130_fd_pr__cap_vpp_08p6x07p8_m1m2_shieldl1",
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
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_m1m2_noshield/sky130_fd_pr__cap_vpp_11p5x11p7_m1m2_noshield.gds",
        cellname="sky130_fd_pr__cap_vpp_11p5x11p7_m1m2_noshield",
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
        / "src/sky130_fd_pr/cells/rf_aura_drc_flag_check/sky130_fd_pr__rf_aura_drc_flag_check.gds",
        cellname="sky130_fd_pr__rf_aura_drc_flag_check",
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
        / "src/sky130_fd_pr/cells/cap_vpp_04p4x04p6_m1m2m3_shieldl1/sky130_fd_pr__cap_vpp_04p4x04p6_m1m2m3_shieldl1.gds",
        cellname="sky130_fd_pr__cap_vpp_04p4x04p6_m1m2m3_shieldl1",
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
        / "src/sky130_fd_pr/cells/cap_vpp_08p6x07p8_l1m1m2_shieldpo_floatm3/sky130_fd_pr__cap_vpp_08p6x07p8_l1m1m2_shieldpo_floatm3.gds",
        cellname="sky130_fd_pr__cap_vpp_08p6x07p8_l1m1m2_shieldpo_floatm3",
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
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_m1m4_noshield/sky130_fd_pr__cap_vpp_11p5x11p7_m1m4_noshield.gds",
        cellname="sky130_fd_pr__cap_vpp_11p5x11p7_m1m4_noshield",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_bM02W1p65L0p25.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_bM02W1p65L0p25",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_hcM04W3p00L0p15.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_hcM04W3p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aM02W1p65L0p15.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_aM02W1p65L0p15",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aF06W2p00L0p15.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_aF06W2p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aM02W5p00L0p15.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_aM02W5p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_bM04W5p00L0p18.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_bM04W5p00L0p18",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_bM02W5p00L0p15.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_bM02W5p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aM02W5p00L0p25.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_aM02W5p00L0p25",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aM04W5p00L0p25.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_aM04W5p00L0p25",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_bM04W5p00L0p25.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_bM04W5p00L0p25",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aM04W3p00L0p15.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_aM04W3p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aF02W5p00L0p15.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_aF02W5p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_bM02W3p00L0p18.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_bM02W3p00L0p18",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aF06W1p68L0p15.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_aF06W1p68L0p15",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_bM04W1p65L0p15.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_bM04W1p65L0p15",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aM02W5p00L0p18.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_aM02W5p00L0p18",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aF04W1p68L0p15.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_aF04W1p68L0p15",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_bM04W1p65L0p18.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_bM04W1p65L0p18",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aM02W1p65L0p18.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_aM02W1p65L0p18",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aF06W0p84L0p15.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_aF06W0p84L0p15",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aF04W3p00L0p15.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_aF04W3p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_mcM04W5p00L0p15.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_mcM04W5p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_bM04W1p65L0p25.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_bM04W1p65L0p25",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aF02W2p00L0p15.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_aF02W2p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aF08W1p68L0p15.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_aF08W1p68L0p15",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_bM02W1p65L0p18.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_bM02W1p65L0p18",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aF06W3p00L0p15.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_aF06W3p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aF04W0p84L0p15.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_aF04W0p84L0p15",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aF08W0p84L0p15.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_aF08W0p84L0p15",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_bM04W3p00L0p15.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_bM04W3p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_bM02W5p00L0p25.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_bM02W5p00L0p25",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aM04W1p65L0p25.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_aM04W1p65L0p25",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_hcM04W5p00L0p15.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_hcM04W5p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_bM02W3p00L0p25.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_bM02W3p00L0p25",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_bM04W3p00L0p18.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_bM04W3p00L0p18",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aF04W2p00L0p15.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_aF04W2p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aF04W5p00L0p15.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_aF04W5p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aM04W5p00L0p18.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_aM04W5p00L0p18",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aF02W0p84L0p15.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_aF02W0p84L0p15",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aM04W3p00L0p25.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_aM04W3p00L0p25",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aM02W1p65L0p25.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_aM02W1p65L0p25",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aM02W3p00L0p25.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_aM02W3p00L0p25",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aM04W1p65L0p18.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_aM04W1p65L0p18",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_bM02W5p00L0p18.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_bM02W5p00L0p18",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aM02W3p00L0p15.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_aM02W3p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aM04W3p00L0p18.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_aM04W3p00L0p18",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aM02W3p00L0p18.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_aM02W3p00L0p18",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_bM04W5p00L0p15.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_bM04W5p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aF02W3p00L0p15.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_aF02W3p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_bM02W3p00L0p15.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_bM02W3p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_bM04W3p00L0p25.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_bM04W3p00L0p25",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aF02W1p68L0p15.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_aF02W1p68L0p15",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_bM02W1p65L0p15.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_bM02W1p65L0p15",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aM04W5p00L0p15.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_aM04W5p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_aM04W1p65L0p15.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_aM04W1p65L0p15",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8/sky130_fd_pr__rf_pfet_01v8_mcM04W3p00L0p15.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_mcM04W3p00L0p15",
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
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_m1m2_shieldl1/sky130_fd_pr__cap_vpp_11p5x11p7_m1m2_shieldl1.gds",
        cellname="sky130_fd_pr__cap_vpp_11p5x11p7_m1m2_shieldl1",
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
        / "src/sky130_fd_pr/cells/cap_vpp_02p7x06p1_m1m2m3m4_shieldl1/sky130_fd_pr__cap_vpp_02p7x06p1_m1m2m3m4_shieldl1_fingercap.gds",
        cellname="sky130_fd_pr__cap_vpp_02p7x06p1_m1m2m3m4_shieldl1_fingercap",
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
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x23p1_pol1m1m2m3m4m5_noshield/sky130_fd_pr__cap_vpp_11p5x23p1_pol1m1m2m3m4m5_noshield.gds",
        cellname="sky130_fd_pr__cap_vpp_11p5x23p1_pol1m1m2m3m4m5_noshield",
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
        / "src/sky130_fd_pr/cells/cap_vpp_55p8x11p7_pol1m1m2m3m4m5_noshield/sky130_fd_pr__cap_vpp_55p8x11p7_pol1m1m2m3m4m5_noshield.gds",
        cellname="sky130_fd_pr__cap_vpp_55p8x11p7_pol1m1m2m3m4m5_noshield",
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
        / "src/sky130_fd_pr/cells/cap_vpp_55p8x11p7_pol1m1m2m3m4m5_noshield/sky130_fd_pr__cap_vpp_55p8x11p7_pol1m1m2m3m4m5_noshield_m5pullin.gds",
        cellname="sky130_fd_pr__cap_vpp_55p8x11p7_pol1m1m2m3m4m5_noshield_m5pullin",
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
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5/sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_x.gds",
        cellname="sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_x",
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
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5/sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_x6.gds",
        cellname="sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_x6",
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
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5/sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5.gds",
        cellname="sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5",
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
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5/sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_x9.gds",
        cellname="sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_x9",
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
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5/sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_x7.gds",
        cellname="sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_x7",
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
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5/sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_xtop.gds",
        cellname="sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_xtop",
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
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5/sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_top.gds",
        cellname="sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_top",
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
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5/sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_x8.gds",
        cellname="sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldpom5_x8",
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
        / "src/sky130_fd_pr/cells/rf_npn_11v0/sky130_fd_pr__rf_npn_11v0_W1p00L1p00.gds",
        cellname="sky130_fd_pr__rf_npn_11v0_W1p00L1p00",
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
        / "src/sky130_fd_pr/cells/rf_aura_lvs_drc/sky130_fd_pr__rf_aura_lvs_drc.gds",
        cellname="sky130_fd_pr__rf_aura_lvs_drc",
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
        gdsdir / "src/sky130_fd_pr/cells/rf_test_coil1/sky130_fd_pr__rf_test_coil1.gds",
        cellname="sky130_fd_pr__rf_test_coil1",
    )


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
        / "src/sky130_fd_pr/cells/rf_nfet_20v0_nvt_noptap_iso/sky130_fd_pr__rf_nfet_20v0_nvt_noptap_iso.gds",
        cellname="sky130_fd_pr__rf_nfet_20v0_nvt_noptap_iso",
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
        gdsdir / "src/sky130_fd_pr/cells/rf_test_coil2/sky130_fd_pr__rf_test_coil2.gds",
        cellname="sky130_fd_pr__rf_test_coil2",
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
        / "src/sky130_fd_pr/cells/cap_vpp_06p8x06p1_l1m1m2m3_shieldpom4/sky130_fd_pr__cap_vpp_06p8x06p1_l1m1m2m3_shieldpom4.gds",
        cellname="sky130_fd_pr__cap_vpp_06p8x06p1_l1m1m2m3_shieldpom4",
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
        / "src/sky130_fd_pr/cells/cap_vpp_06p8x06p1_l1m1m2m3_shieldpom4/sky130_fd_pr__cap_vpp_06p8x06p1_l1m1m2m3_shieldpom4_top.gds",
        cellname="sky130_fd_pr__cap_vpp_06p8x06p1_l1m1m2m3_shieldpom4_top",
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
        / "src/sky130_fd_pr/cells/rf_npn_05v5/sky130_fd_pr__rf_npn_05v5_W1p00L8p00.gds",
        cellname="sky130_fd_pr__rf_npn_05v5_W1p00L8p00",
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
        / "src/sky130_fd_pr/cells/rf_npn_05v5/sky130_fd_pr__rf_npn_05v5_W5p00L5p00.gds",
        cellname="sky130_fd_pr__rf_npn_05v5_W5p00L5p00",
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
        / "src/sky130_fd_pr/cells/rf_npn_05v5/sky130_fd_pr__rf_npn_05v5_W1p00L1p00.gds",
        cellname="sky130_fd_pr__rf_npn_05v5_W1p00L1p00",
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
        / "src/sky130_fd_pr/cells/rf_npn_05v5/sky130_fd_pr__rf_npn_05v5_W2p00L8p00.gds",
        cellname="sky130_fd_pr__rf_npn_05v5_W2p00L8p00",
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
        / "src/sky130_fd_pr/cells/rf_npn_05v5/sky130_fd_pr__rf_npn_05v5_W1p00L4p00.gds",
        cellname="sky130_fd_pr__rf_npn_05v5_W1p00L4p00",
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
        / "src/sky130_fd_pr/cells/rf_npn_05v5/sky130_fd_pr__rf_npn_05v5_W1p00L2p00.gds",
        cellname="sky130_fd_pr__rf_npn_05v5_W1p00L2p00",
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
        / "src/sky130_fd_pr/cells/rf_npn_05v5/sky130_fd_pr__rf_npn_05v5_W2p00L4p00.gds",
        cellname="sky130_fd_pr__rf_npn_05v5_W2p00L4p00",
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
        / "src/sky130_fd_pr/cells/rf_npn_05v5/sky130_fd_pr__rf_npn_05v5_W2p00L2p00.gds",
        cellname="sky130_fd_pr__rf_npn_05v5_W2p00L2p00",
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
        / "src/sky130_fd_pr/cells/cap_vpp_55p8x23p1_pol1m1m2m3m4m5_noshield/sky130_fd_pr__cap_vpp_55p8x23p1_pol1m1m2m3m4m5_noshield_m5pullin.gds",
        cellname="sky130_fd_pr__cap_vpp_55p8x23p1_pol1m1m2m3m4m5_noshield_m5pullin",
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
        / "src/sky130_fd_pr/cells/cap_vpp_55p8x23p1_pol1m1m2m3m4m5_noshield/sky130_fd_pr__cap_vpp_55p8x23p1_pol1m1m2m3m4m5_noshield_test.gds",
        cellname="sky130_fd_pr__cap_vpp_55p8x23p1_pol1m1m2m3m4m5_noshield_test",
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
        / "src/sky130_fd_pr/cells/cap_vpp_55p8x23p1_pol1m1m2m3m4m5_noshield/sky130_fd_pr__cap_vpp_55p8x23p1_pol1m1m2m3m4m5_noshield.gds",
        cellname="sky130_fd_pr__cap_vpp_55p8x23p1_pol1m1m2m3m4m5_noshield",
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
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_m1m2m3_shieldl1m5_floatm4/sky130_fd_pr__cap_vpp_11p5x11p7_m1m2m3_shieldl1m5_floatm4_top.gds",
        cellname="sky130_fd_pr__cap_vpp_11p5x11p7_m1m2m3_shieldl1m5_floatm4_top",
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
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_m1m2m3_shieldl1m5_floatm4/sky130_fd_pr__cap_vpp_11p5x11p7_m1m2m3_shieldl1m5_floatm4.gds",
        cellname="sky130_fd_pr__cap_vpp_11p5x11p7_m1m2m3_shieldl1m5_floatm4",
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
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_m1m2m3_shieldl1/sky130_fd_pr__cap_vpp_11p5x11p7_m1m2m3_shieldl1.gds",
        cellname="sky130_fd_pr__cap_vpp_11p5x11p7_m1m2m3_shieldl1",
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
        / "src/sky130_fd_pr/cells/cap_vpp_22p5x23p1_pol1m1m2m3m4m5_noshield/sky130_fd_pr__cap_vpp_22p5x23p1_pol1m1m2m3m4m5_noshield.gds",
        cellname="sky130_fd_pr__cap_vpp_22p5x23p1_pol1m1m2m3m4m5_noshield",
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
        / "src/sky130_fd_pr/cells/cap_vpp_02p7x11p1_m1m2m3m4_shieldl1/sky130_fd_pr__cap_vpp_02p7x11p1_m1m2m3m4_shieldl1_fingercap.gds",
        cellname="sky130_fd_pr__cap_vpp_02p7x11p1_m1m2m3m4_shieldl1_fingercap",
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
        / "src/sky130_fd_pr/cells/cap_vpp_33p6x23p1_pol1m1m2m3m4m5_noshield/sky130_fd_pr__cap_vpp_33p6x23p1_pol1m1m2m3m4m5_noshield.gds",
        cellname="sky130_fd_pr__cap_vpp_33p6x23p1_pol1m1m2m3m4m5_noshield",
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
        / "src/sky130_fd_pr/cells/rf_nfet_20v0_withptap_iso/sky130_fd_pr__rf_nfet_20v0_withptap_iso.gds",
        cellname="sky130_fd_pr__rf_nfet_20v0_withptap_iso",
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
        / "src/sky130_fd_pr/cells/cap_vpp_04p4x04p6_m1m2_noshield/sky130_fd_pr__cap_vpp_04p4x04p6_m1m2_noshield_o2.gds",
        cellname="sky130_fd_pr__cap_vpp_04p4x04p6_m1m2_noshield_o2",
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
        / "src/sky130_fd_pr/cells/cap_vpp_04p4x04p6_m1m2_noshield/sky130_fd_pr__cap_vpp_04p4x04p6_m1m2_noshield.gds",
        cellname="sky130_fd_pr__cap_vpp_04p4x04p6_m1m2_noshield",
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
        / "src/sky130_fd_pr/cells/rf_nfet_20v0_zvt_withptap/sky130_fd_pr__rf_nfet_20v0_zvt_withptap.gds",
        cellname="sky130_fd_pr__rf_nfet_20v0_zvt_withptap",
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
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_l1m1m2m3_shieldpom4/sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3_shieldpom4_top.gds",
        cellname="sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3_shieldpom4_top",
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
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_l1m1m2m3_shieldpom4/sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3_shieldpom4.gds",
        cellname="sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3_shieldpom4",
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
        / "src/sky130_fd_pr/cells/cap_vpp_05p9x05p9_m1m2m3m4_shieldl1/sky130_fd_pr__cap_vpp_05p9x05p9_m1m2m3m4_shieldl1_wafflecap.gds",
        cellname="sky130_fd_pr__cap_vpp_05p9x05p9_m1m2m3m4_shieldl1_wafflecap",
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
        / "src/sky130_fd_pr/cells/cap_vpp_04p4x04p6_l1m1m2_shieldpo_floatm3/sky130_fd_pr__cap_vpp_04p4x04p6_l1m1m2_shieldpo_floatm3.gds",
        cellname="sky130_fd_pr__cap_vpp_04p4x04p6_l1m1m2_shieldpo_floatm3",
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
        / "src/sky130_fd_pr/cells/cap_vpp_02p7x41p1_m1m2m3m4_shieldl1/sky130_fd_pr__cap_vpp_02p7x41p1_m1m2m3m4_shieldl1_fingercap.gds",
        cellname="sky130_fd_pr__cap_vpp_02p7x41p1_m1m2m3m4_shieldl1_fingercap",
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
        gdsdir / "src/sky130_fd_pr/cells/rf_test_coil3/sky130_fd_pr__rf_test_coil3.gds",
        cellname="sky130_fd_pr__rf_test_coil3",
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
        / "src/sky130_fd_pr/cells/cap_vpp_04p4x04p6_m1m2m3_shieldl1m5_floatm4/sky130_fd_pr__cap_vpp_04p4x04p6_m1m2m3_shieldl1m5_floatm4_top.gds",
        cellname="sky130_fd_pr__cap_vpp_04p4x04p6_m1m2m3_shieldl1m5_floatm4_top",
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
        / "src/sky130_fd_pr/cells/cap_vpp_04p4x04p6_m1m2m3_shieldl1m5_floatm4/sky130_fd_pr__cap_vpp_04p4x04p6_m1m2m3_shieldl1m5_floatm4.gds",
        cellname="sky130_fd_pr__cap_vpp_04p4x04p6_m1m2m3_shieldl1m5_floatm4",
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
        / "src/sky130_fd_pr/cells/rf_nfet_20v0_aup/sky130_fd_pr__rf_nfet_20v0_aup.gds",
        cellname="sky130_fd_pr__rf_nfet_20v0_aup",
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
        / "src/sky130_fd_pr/cells/rf_pnp_05v5/sky130_fd_pr__rf_pnp_05v5_W0p68L0p68.gds",
        cellname="sky130_fd_pr__rf_pnp_05v5_W0p68L0p68",
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
        / "src/sky130_fd_pr/cells/rf_pnp_05v5/sky130_fd_pr__rf_pnp_05v5_W3p40L3p40.gds",
        cellname="sky130_fd_pr__rf_pnp_05v5_W3p40L3p40",
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
        / "src/sky130_fd_pr/cells/cap_vpp_06p8x06p1_m1m2m3_shieldl1m4/sky130_fd_pr__cap_vpp_06p8x06p1_m1m2m3_shieldl1m4_top.gds",
        cellname="sky130_fd_pr__cap_vpp_06p8x06p1_m1m2m3_shieldl1m4_top",
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
        / "src/sky130_fd_pr/cells/cap_vpp_06p8x06p1_m1m2m3_shieldl1m4/sky130_fd_pr__cap_vpp_06p8x06p1_m1m2m3_shieldl1m4.gds",
        cellname="sky130_fd_pr__cap_vpp_06p8x06p1_m1m2m3_shieldl1m4",
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
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_m1m2m3m4_shieldm5/sky130_fd_pr__cap_vpp_11p5x11p7_m1m2m3m4_shieldm5.gds",
        cellname="sky130_fd_pr__cap_vpp_11p5x11p7_m1m2m3m4_shieldm5",
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
        / "src/sky130_fd_pr/cells/cap_vpp_02p7x21p1_m1m2m3m4_shieldl1/sky130_fd_pr__cap_vpp_02p7x21p1_m1m2m3m4_shieldl1_fingercap.gds",
        cellname="sky130_fd_pr__cap_vpp_02p7x21p1_m1m2m3m4_shieldl1_fingercap",
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
        / "src/sky130_fd_pr/cells/rf_nfet_20v0_nvt_aup/sky130_fd_pr__rf_nfet_20v0_nvt_aup.gds",
        cellname="sky130_fd_pr__rf_nfet_20v0_nvt_aup",
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
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_l1m1m2m3m4_shieldm5/sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldm5.gds",
        cellname="sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldm5",
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
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_l1m1m2m3m4_shieldm5/sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldm5_top.gds",
        cellname="sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2m3m4_shieldm5_top",
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
        / "src/sky130_fd_pr/cells/esd_rf_nfet_20v0_iec/sky130_fd_pr__esd_rf_nfet_20v0_iec_21vW60p00.gds",
        cellname="sky130_fd_pr__esd_rf_nfet_20v0_iec_21vW60p00",
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
        / "src/sky130_fd_pr/cells/esd_rf_nfet_20v0_iec/sky130_fd_pr__esd_rf_nfet_20v0_iec_32vW60p00.gds",
        cellname="sky130_fd_pr__esd_rf_nfet_20v0_iec_32vW60p00",
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
        / "src/sky130_fd_pr/cells/rf_nfet_g5v0d10v5/sky130_fd_pr__rf_nfet_g5v0d10v5_aM10W5p00L0p50.gds",
        cellname="sky130_fd_pr__rf_nfet_g5v0d10v5_aM10W5p00L0p50",
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
        / "src/sky130_fd_pr/cells/rf_nfet_g5v0d10v5/sky130_fd_pr__rf_nfet_g5v0d10v5_bM02W3p00L0p50.gds",
        cellname="sky130_fd_pr__rf_nfet_g5v0d10v5_bM02W3p00L0p50",
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
        / "src/sky130_fd_pr/cells/rf_nfet_g5v0d10v5/sky130_fd_pr__rf_nfet_g5v0d10v5_bM04W7p00L0p50.gds",
        cellname="sky130_fd_pr__rf_nfet_g5v0d10v5_bM04W7p00L0p50",
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
        / "src/sky130_fd_pr/cells/rf_nfet_g5v0d10v5/sky130_fd_pr__rf_nfet_g5v0d10v5_aM04W7p00L0p50.gds",
        cellname="sky130_fd_pr__rf_nfet_g5v0d10v5_aM04W7p00L0p50",
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
        / "src/sky130_fd_pr/cells/rf_nfet_g5v0d10v5/sky130_fd_pr__rf_nfet_g5v0d10v5_bM10W5p00L0p50.gds",
        cellname="sky130_fd_pr__rf_nfet_g5v0d10v5_bM10W5p00L0p50",
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
        / "src/sky130_fd_pr/cells/rf_nfet_g5v0d10v5/sky130_fd_pr__rf_nfet_g5v0d10v5_bM04W3p00L0p50.gds",
        cellname="sky130_fd_pr__rf_nfet_g5v0d10v5_bM04W3p00L0p50",
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
        / "src/sky130_fd_pr/cells/rf_nfet_g5v0d10v5/sky130_fd_pr__rf_nfet_g5v0d10v5_bM04W5p00L0p50.gds",
        cellname="sky130_fd_pr__rf_nfet_g5v0d10v5_bM04W5p00L0p50",
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
        / "src/sky130_fd_pr/cells/rf_nfet_g5v0d10v5/sky130_fd_pr__rf_nfet_g5v0d10v5_aM10W3p00L0p50.gds",
        cellname="sky130_fd_pr__rf_nfet_g5v0d10v5_aM10W3p00L0p50",
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
        / "src/sky130_fd_pr/cells/rf_nfet_g5v0d10v5/sky130_fd_pr__rf_nfet_g5v0d10v5_bM10W7p00L0p50.gds",
        cellname="sky130_fd_pr__rf_nfet_g5v0d10v5_bM10W7p00L0p50",
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
        / "src/sky130_fd_pr/cells/rf_nfet_g5v0d10v5/sky130_fd_pr__rf_nfet_g5v0d10v5_aM10W7p00L0p50.gds",
        cellname="sky130_fd_pr__rf_nfet_g5v0d10v5_aM10W7p00L0p50",
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
        / "src/sky130_fd_pr/cells/rf_nfet_g5v0d10v5/sky130_fd_pr__rf_nfet_g5v0d10v5_bM10W3p00L0p50.gds",
        cellname="sky130_fd_pr__rf_nfet_g5v0d10v5_bM10W3p00L0p50",
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
        / "src/sky130_fd_pr/cells/rf_nfet_g5v0d10v5/sky130_fd_pr__rf_nfet_g5v0d10v5_bM02W5p00L0p50.gds",
        cellname="sky130_fd_pr__rf_nfet_g5v0d10v5_bM02W5p00L0p50",
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
        / "src/sky130_fd_pr/cells/rf_nfet_g5v0d10v5/sky130_fd_pr__rf_nfet_g5v0d10v5_aM04W5p00L0p50.gds",
        cellname="sky130_fd_pr__rf_nfet_g5v0d10v5_aM04W5p00L0p50",
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
        / "src/sky130_fd_pr/cells/rf_nfet_g5v0d10v5/sky130_fd_pr__rf_nfet_g5v0d10v5_aM04W3p00L0p50.gds",
        cellname="sky130_fd_pr__rf_nfet_g5v0d10v5_aM04W3p00L0p50",
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
        / "src/sky130_fd_pr/cells/rf_nfet_20v0_nvt_withptap/sky130_fd_pr__rf_nfet_20v0_nvt_withptap.gds",
        cellname="sky130_fd_pr__rf_nfet_20v0_nvt_withptap",
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
        / "src/sky130_fd_pr/cells/rf_pfet_20v0_withptap/sky130_fd_pr__rf_pfet_20v0_withptap.gds",
        cellname="sky130_fd_pr__rf_pfet_20v0_withptap",
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
        / "src/sky130_fd_pr/cells/cap_vpp_11p3x11p3_m1m2m3m4_shieldl1/sky130_fd_pr__cap_vpp_11p3x11p3_m1m2m3m4_shieldl1_wafflecap.gds",
        cellname="sky130_fd_pr__cap_vpp_11p3x11p3_m1m2m3m4_shieldl1_wafflecap",
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
        / "src/sky130_fd_pr/cells/rf_nfet_20v0_noptap_iso/sky130_fd_pr__rf_nfet_20v0_noptap_iso.gds",
        cellname="sky130_fd_pr__rf_nfet_20v0_noptap_iso",
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
        / "src/sky130_fd_pr/cells/cap_vpp_04p4x04p6_m1m2_shieldl1/sky130_fd_pr__cap_vpp_04p4x04p6_m1m2_shieldl1.gds",
        cellname="sky130_fd_pr__cap_vpp_04p4x04p6_m1m2_shieldl1",
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
        / "src/sky130_fd_pr/cells/cap_vpp_08p6x07p8_m1m2_noshield/sky130_fd_pr__cap_vpp_08p6x07p8_m1m2_noshield.gds",
        cellname="sky130_fd_pr__cap_vpp_08p6x07p8_m1m2_noshield",
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
        / "src/sky130_fd_pr/cells/cap_vpp_04p4x04p6_l1m1m2_noshield/sky130_fd_pr__cap_vpp_04p4x04p6_l1m1m2_noshield_o2subcell.gds",
        cellname="sky130_fd_pr__cap_vpp_04p4x04p6_l1m1m2_noshield_o2subcell",
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
        / "src/sky130_fd_pr/cells/cap_vpp_04p4x04p6_l1m1m2_noshield/sky130_fd_pr__cap_vpp_04p4x04p6_l1m1m2_noshield.gds",
        cellname="sky130_fd_pr__cap_vpp_04p4x04p6_l1m1m2_noshield",
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
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_l1m1m2_noshield/sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2_noshield.gds",
        cellname="sky130_fd_pr__cap_vpp_11p5x11p7_l1m1m2_noshield",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8_lvt/sky130_fd_pr__rf_pfet_01v8_lvt_aM04W3p00L0p50.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_lvt_aM04W3p00L0p50",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8_lvt/sky130_fd_pr__rf_pfet_01v8_lvt_aM04W3p00L0p35.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_lvt_aM04W3p00L0p35",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8_lvt/sky130_fd_pr__rf_pfet_01v8_lvt_aM02W5p00L0p50.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_lvt_aM02W5p00L0p50",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8_lvt/sky130_fd_pr__rf_pfet_01v8_lvt_aM02W3p00L0p35.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_lvt_aM02W3p00L0p35",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8_lvt/sky130_fd_pr__rf_pfet_01v8_lvt_aM04W5p00L0p50.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_lvt_aM04W5p00L0p50",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8_lvt/sky130_fd_pr__rf_pfet_01v8_lvt_aM04W5p00L0p35.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_lvt_aM04W5p00L0p35",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8_lvt/sky130_fd_pr__rf_pfet_01v8_lvt_aM02W3p00L0p50.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_lvt_aM02W3p00L0p50",
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
        / "src/sky130_fd_pr/cells/rf_pfet_01v8_lvt/sky130_fd_pr__rf_pfet_01v8_lvt_aM02W5p00L0p35.gds",
        cellname="sky130_fd_pr__rf_pfet_01v8_lvt_aM02W5p00L0p35",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_bM04W5p00L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_bM04W5p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_bM04W1p65L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_bM04W1p65L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_aM02W1p65L0p25.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_aM02W1p65L0p25",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_aM04W5p00L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_aM04W5p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_aM02W5p00L0p25.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_aM02W5p00L0p25",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_bM04W3p00L0p25.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_bM04W3p00L0p25",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_bM04W5p00L0p25.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_bM04W5p00L0p25",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_bM04W1p65L0p18.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_bM04W1p65L0p18",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_aM04W3p00L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_aM04W3p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_bM02W1p65L0p18.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_bM02W1p65L0p18",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_aM04W3p00L0p25.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_aM04W3p00L0p25",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_bM02W1p65L0p25.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_bM02W1p65L0p25",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_bM02W1p65L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_bM02W1p65L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_aM04W3p00L0p18.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_aM04W3p00L0p18",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_aM04W1p65L0p18.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_aM04W1p65L0p18",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_mcM04W5p00L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_mcM04W5p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_aM02W3p00L0p25.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_aM02W3p00L0p25",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_bM02W3p00L0p18.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_bM02W3p00L0p18",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_aM02W5p00L0p18.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_aM02W5p00L0p18",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_bM04W3p00L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_bM04W3p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_aM02W3p00L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_aM02W3p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_bM04W3p00L0p18.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_bM04W3p00L0p18",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_bM02W3p00L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_bM02W3p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_bM04W5p00L0p18.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_bM04W5p00L0p18",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_aM04W5p00L0p18.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_aM04W5p00L0p18",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_aM02W3p00L0p18.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_aM02W3p00L0p18",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_hcM04W5p00L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_hcM04W5p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_bM02W5p00L0p25.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_bM02W5p00L0p25",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_aM04W1p65L0p25.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_aM04W1p65L0p25",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_bM02W5p00L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_bM02W5p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_hcM04W3p00L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_hcM04W3p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_bM02W3p00L0p25.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_bM02W3p00L0p25",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_aM04W1p65L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_aM04W1p65L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_aM02W1p65L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_aM02W1p65L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_bM02W5p00L0p18.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_bM02W5p00L0p18",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_bM04W1p65L0p25.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_bM04W1p65L0p25",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_aM02W5p00L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_aM02W5p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_mcM04W3p00L0p15.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_mcM04W3p00L0p15",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_aM04W5p00L0p25.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_aM04W5p00L0p25",
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
        / "src/sky130_fd_pr/cells/rf_nfet_01v8/sky130_fd_pr__rf_nfet_01v8_aM02W1p65L0p18.gds",
        cellname="sky130_fd_pr__rf_nfet_01v8_aM02W1p65L0p18",
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
        / "src/sky130_fd_pr/cells/rf_nfet_20v0_withptap/sky130_fd_pr__rf_nfet_20v0_withptap.gds",
        cellname="sky130_fd_pr__rf_nfet_20v0_withptap",
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
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_m1m2m3m4_shieldl1m5/sky130_fd_pr__cap_vpp_11p5x11p7_m1m2m3m4_shieldl1m5_top.gds",
        cellname="sky130_fd_pr__cap_vpp_11p5x11p7_m1m2m3m4_shieldl1m5_top",
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
        / "src/sky130_fd_pr/cells/cap_vpp_11p5x11p7_m1m2m3m4_shieldl1m5/sky130_fd_pr__cap_vpp_11p5x11p7_m1m2m3m4_shieldl1m5.gds",
        cellname="sky130_fd_pr__cap_vpp_11p5x11p7_m1m2m3m4_shieldl1m5",
    )


@cell
def sky130_fd_sc_hd__a222oi_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a222oi_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a222oi_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a222oi/sky130_fd_sc_hd__a222oi_1.gds",
        cellname="sky130_fd_sc_hd__a222oi_1",
    )


@cell
def sky130_fd_sc_hd__or4b_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__or4b_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__or4b_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/or4b/sky130_fd_sc_hd__or4b_1.gds",
        cellname="sky130_fd_sc_hd__or4b_1",
    )


@cell
def sky130_fd_sc_hd__or4b_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__or4b_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__or4b_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/or4b/sky130_fd_sc_hd__or4b_2.gds",
        cellname="sky130_fd_sc_hd__or4b_2",
    )


@cell
def sky130_fd_sc_hd__or4b_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__or4b_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__or4b_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/or4b/sky130_fd_sc_hd__or4b_4.gds",
        cellname="sky130_fd_sc_hd__or4b_4",
    )


@cell
def sky130_fd_sc_hd__a311oi_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__a311oi_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a311oi_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a311oi/sky130_fd_sc_hd__a311oi_2.gds",
        cellname="sky130_fd_sc_hd__a311oi_2",
    )


@cell
def sky130_fd_sc_hd__a311oi_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a311oi_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a311oi_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a311oi/sky130_fd_sc_hd__a311oi_1.gds",
        cellname="sky130_fd_sc_hd__a311oi_1",
    )


@cell
def sky130_fd_sc_hd__a311oi_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__a311oi_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a311oi_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a311oi/sky130_fd_sc_hd__a311oi_4.gds",
        cellname="sky130_fd_sc_hd__a311oi_4",
    )


@cell
def sky130_fd_sc_hd__lpflow_inputiso0n_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_inputiso0n_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_inputiso0n_1()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/lpflow_inputiso0n/sky130_fd_sc_hd__lpflow_inputiso0n_1.gds",
        cellname="sky130_fd_sc_hd__lpflow_inputiso0n_1",
    )


@cell
def sky130_fd_sc_hd__lpflow_isobufsrc_16() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_isobufsrc_16 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_isobufsrc_16()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/lpflow_isobufsrc/sky130_fd_sc_hd__lpflow_isobufsrc_16.gds",
        cellname="sky130_fd_sc_hd__lpflow_isobufsrc_16",
    )


@cell
def sky130_fd_sc_hd__lpflow_isobufsrc_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_isobufsrc_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_isobufsrc_1()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/lpflow_isobufsrc/sky130_fd_sc_hd__lpflow_isobufsrc_1.gds",
        cellname="sky130_fd_sc_hd__lpflow_isobufsrc_1",
    )


@cell
def sky130_fd_sc_hd__lpflow_isobufsrc_8() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_isobufsrc_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_isobufsrc_8()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/lpflow_isobufsrc/sky130_fd_sc_hd__lpflow_isobufsrc_8.gds",
        cellname="sky130_fd_sc_hd__lpflow_isobufsrc_8",
    )


@cell
def sky130_fd_sc_hd__lpflow_isobufsrc_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_isobufsrc_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_isobufsrc_4()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/lpflow_isobufsrc/sky130_fd_sc_hd__lpflow_isobufsrc_4.gds",
        cellname="sky130_fd_sc_hd__lpflow_isobufsrc_4",
    )


@cell
def sky130_fd_sc_hd__lpflow_isobufsrc_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_isobufsrc_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_isobufsrc_2()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/lpflow_isobufsrc/sky130_fd_sc_hd__lpflow_isobufsrc_2.gds",
        cellname="sky130_fd_sc_hd__lpflow_isobufsrc_2",
    )


@cell
def sky130_fd_sc_hd__ebufn_8() -> gf.Component:
    """Returns sky130_fd_sc_hd__ebufn_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__ebufn_8()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/ebufn/sky130_fd_sc_hd__ebufn_8.gds",
        cellname="sky130_fd_sc_hd__ebufn_8",
    )


@cell
def sky130_fd_sc_hd__ebufn_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__ebufn_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__ebufn_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/ebufn/sky130_fd_sc_hd__ebufn_1.gds",
        cellname="sky130_fd_sc_hd__ebufn_1",
    )


@cell
def sky130_fd_sc_hd__ebufn_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__ebufn_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__ebufn_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/ebufn/sky130_fd_sc_hd__ebufn_4.gds",
        cellname="sky130_fd_sc_hd__ebufn_4",
    )


@cell
def sky130_fd_sc_hd__ebufn_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__ebufn_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__ebufn_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/ebufn/sky130_fd_sc_hd__ebufn_2.gds",
        cellname="sky130_fd_sc_hd__ebufn_2",
    )


@cell
def sky130_fd_sc_hd__o2111a_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__o2111a_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o2111a_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o2111a/sky130_fd_sc_hd__o2111a_1.gds",
        cellname="sky130_fd_sc_hd__o2111a_1",
    )


@cell
def sky130_fd_sc_hd__o2111a_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__o2111a_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o2111a_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o2111a/sky130_fd_sc_hd__o2111a_4.gds",
        cellname="sky130_fd_sc_hd__o2111a_4",
    )


@cell
def sky130_fd_sc_hd__o2111a_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__o2111a_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o2111a_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o2111a/sky130_fd_sc_hd__o2111a_2.gds",
        cellname="sky130_fd_sc_hd__o2111a_2",
    )


@cell
def sky130_fd_sc_hd__einvn_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__einvn_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__einvn_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/einvn/sky130_fd_sc_hd__einvn_1.gds",
        cellname="sky130_fd_sc_hd__einvn_1",
    )


@cell
def sky130_fd_sc_hd__einvn_0() -> gf.Component:
    """Returns sky130_fd_sc_hd__einvn_0 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__einvn_0()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/einvn/sky130_fd_sc_hd__einvn_0.gds",
        cellname="sky130_fd_sc_hd__einvn_0",
    )


@cell
def sky130_fd_sc_hd__einvn_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__einvn_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__einvn_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/einvn/sky130_fd_sc_hd__einvn_4.gds",
        cellname="sky130_fd_sc_hd__einvn_4",
    )


@cell
def sky130_fd_sc_hd__einvn_8() -> gf.Component:
    """Returns sky130_fd_sc_hd__einvn_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__einvn_8()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/einvn/sky130_fd_sc_hd__einvn_8.gds",
        cellname="sky130_fd_sc_hd__einvn_8",
    )


@cell
def sky130_fd_sc_hd__einvn_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__einvn_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__einvn_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/einvn/sky130_fd_sc_hd__einvn_2.gds",
        cellname="sky130_fd_sc_hd__einvn_2",
    )


@cell
def sky130_fd_sc_hd__clkdlybuf4s18_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__clkdlybuf4s18_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__clkdlybuf4s18_2()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/clkdlybuf4s18/sky130_fd_sc_hd__clkdlybuf4s18_2.gds",
        cellname="sky130_fd_sc_hd__clkdlybuf4s18_2",
    )


@cell
def sky130_fd_sc_hd__clkdlybuf4s18_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__clkdlybuf4s18_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__clkdlybuf4s18_1()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/clkdlybuf4s18/sky130_fd_sc_hd__clkdlybuf4s18_1.gds",
        cellname="sky130_fd_sc_hd__clkdlybuf4s18_1",
    )


@cell
def sky130_fd_sc_hd__a22o_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__a22o_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a22o_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a22o/sky130_fd_sc_hd__a22o_4.gds",
        cellname="sky130_fd_sc_hd__a22o_4",
    )


@cell
def sky130_fd_sc_hd__a22o_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__a22o_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a22o_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a22o/sky130_fd_sc_hd__a22o_2.gds",
        cellname="sky130_fd_sc_hd__a22o_2",
    )


@cell
def sky130_fd_sc_hd__a22o_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a22o_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a22o_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a22o/sky130_fd_sc_hd__a22o_1.gds",
        cellname="sky130_fd_sc_hd__a22o_1",
    )


@cell
def sky130_fd_sc_hd__dfbbp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dfbbp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dfbbp_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/dfbbp/sky130_fd_sc_hd__dfbbp_1.gds",
        cellname="sky130_fd_sc_hd__dfbbp_1",
    )


@cell
def sky130_fd_sc_hd__edfxbp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__edfxbp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__edfxbp_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/edfxbp/sky130_fd_sc_hd__edfxbp_1.gds",
        cellname="sky130_fd_sc_hd__edfxbp_1",
    )


@cell
def sky130_fd_sc_hd__fah_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__fah_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__fah_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/fah/sky130_fd_sc_hd__fah_1.gds",
        cellname="sky130_fd_sc_hd__fah_1",
    )


@cell
def sky130_fd_sc_hd__lpflow_inputisolatch_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_inputisolatch_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_inputisolatch_1()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/lpflow_inputisolatch/sky130_fd_sc_hd__lpflow_inputisolatch_1.gds",
        cellname="sky130_fd_sc_hd__lpflow_inputisolatch_1",
    )


@cell
def sky130_fd_sc_hd__a211o_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a211o_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a211o_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a211o/sky130_fd_sc_hd__a211o_1.gds",
        cellname="sky130_fd_sc_hd__a211o_1",
    )


@cell
def sky130_fd_sc_hd__a211o_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__a211o_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a211o_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a211o/sky130_fd_sc_hd__a211o_4.gds",
        cellname="sky130_fd_sc_hd__a211o_4",
    )


@cell
def sky130_fd_sc_hd__a211o_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__a211o_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a211o_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a211o/sky130_fd_sc_hd__a211o_2.gds",
        cellname="sky130_fd_sc_hd__a211o_2",
    )


@cell
def sky130_fd_sc_hd__bufinv_8() -> gf.Component:
    """Returns sky130_fd_sc_hd__bufinv_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__bufinv_8()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/bufinv/sky130_fd_sc_hd__bufinv_8.gds",
        cellname="sky130_fd_sc_hd__bufinv_8",
    )


@cell
def sky130_fd_sc_hd__bufinv_16() -> gf.Component:
    """Returns sky130_fd_sc_hd__bufinv_16 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__bufinv_16()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/bufinv/sky130_fd_sc_hd__bufinv_16.gds",
        cellname="sky130_fd_sc_hd__bufinv_16",
    )


@cell
def sky130_fd_sc_hd__dlxbp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlxbp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlxbp_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/dlxbp/sky130_fd_sc_hd__dlxbp_1.gds",
        cellname="sky130_fd_sc_hd__dlxbp_1",
    )


@cell
def sky130_fd_sc_hd__dfbbn_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__dfbbn_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dfbbn_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/dfbbn/sky130_fd_sc_hd__dfbbn_2.gds",
        cellname="sky130_fd_sc_hd__dfbbn_2",
    )


@cell
def sky130_fd_sc_hd__dfbbn_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dfbbn_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dfbbn_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/dfbbn/sky130_fd_sc_hd__dfbbn_1.gds",
        cellname="sky130_fd_sc_hd__dfbbn_1",
    )


@cell
def sky130_fd_sc_hd__o21bai_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__o21bai_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o21bai_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o21bai/sky130_fd_sc_hd__o21bai_1.gds",
        cellname="sky130_fd_sc_hd__o21bai_1",
    )


@cell
def sky130_fd_sc_hd__o21bai_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__o21bai_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o21bai_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o21bai/sky130_fd_sc_hd__o21bai_2.gds",
        cellname="sky130_fd_sc_hd__o21bai_2",
    )


@cell
def sky130_fd_sc_hd__o21bai_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__o21bai_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o21bai_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o21bai/sky130_fd_sc_hd__o21bai_4.gds",
        cellname="sky130_fd_sc_hd__o21bai_4",
    )


@cell
def sky130_fd_sc_hd__o2bb2a_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__o2bb2a_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o2bb2a_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o2bb2a/sky130_fd_sc_hd__o2bb2a_1.gds",
        cellname="sky130_fd_sc_hd__o2bb2a_1",
    )


@cell
def sky130_fd_sc_hd__o2bb2a_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__o2bb2a_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o2bb2a_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o2bb2a/sky130_fd_sc_hd__o2bb2a_2.gds",
        cellname="sky130_fd_sc_hd__o2bb2a_2",
    )


@cell
def sky130_fd_sc_hd__o2bb2a_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__o2bb2a_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o2bb2a_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o2bb2a/sky130_fd_sc_hd__o2bb2a_4.gds",
        cellname="sky130_fd_sc_hd__o2bb2a_4",
    )


@cell
def sky130_fd_sc_hd__dlygate4sd1_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlygate4sd1_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlygate4sd1_1()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/dlygate4sd1/sky130_fd_sc_hd__dlygate4sd1_1.gds",
        cellname="sky130_fd_sc_hd__dlygate4sd1_1",
    )


@cell
def sky130_fd_sc_hd__dfsbp_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__dfsbp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dfsbp_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/dfsbp/sky130_fd_sc_hd__dfsbp_2.gds",
        cellname="sky130_fd_sc_hd__dfsbp_2",
    )


@cell
def sky130_fd_sc_hd__dfsbp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dfsbp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dfsbp_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/dfsbp/sky130_fd_sc_hd__dfsbp_1.gds",
        cellname="sky130_fd_sc_hd__dfsbp_1",
    )


@cell
def sky130_fd_sc_hd__o311ai_0() -> gf.Component:
    """Returns sky130_fd_sc_hd__o311ai_0 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o311ai_0()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o311ai/sky130_fd_sc_hd__o311ai_0.gds",
        cellname="sky130_fd_sc_hd__o311ai_0",
    )


@cell
def sky130_fd_sc_hd__o311ai_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__o311ai_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o311ai_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o311ai/sky130_fd_sc_hd__o311ai_2.gds",
        cellname="sky130_fd_sc_hd__o311ai_2",
    )


@cell
def sky130_fd_sc_hd__o311ai_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__o311ai_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o311ai_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o311ai/sky130_fd_sc_hd__o311ai_4.gds",
        cellname="sky130_fd_sc_hd__o311ai_4",
    )


@cell
def sky130_fd_sc_hd__o311ai_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__o311ai_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o311ai_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o311ai/sky130_fd_sc_hd__o311ai_1.gds",
        cellname="sky130_fd_sc_hd__o311ai_1",
    )


@cell
def sky130_fd_sc_hd__or4bb_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__or4bb_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__or4bb_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/or4bb/sky130_fd_sc_hd__or4bb_1.gds",
        cellname="sky130_fd_sc_hd__or4bb_1",
    )


@cell
def sky130_fd_sc_hd__or4bb_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__or4bb_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__or4bb_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/or4bb/sky130_fd_sc_hd__or4bb_4.gds",
        cellname="sky130_fd_sc_hd__or4bb_4",
    )


@cell
def sky130_fd_sc_hd__or4bb_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__or4bb_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__or4bb_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/or4bb/sky130_fd_sc_hd__or4bb_2.gds",
        cellname="sky130_fd_sc_hd__or4bb_2",
    )


@cell
def sky130_fd_sc_hd__dlymetal6s4s_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlymetal6s4s_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlymetal6s4s_1()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/dlymetal6s4s/sky130_fd_sc_hd__dlymetal6s4s_1.gds",
        cellname="sky130_fd_sc_hd__dlymetal6s4s_1",
    )


@cell
def sky130_fd_sc_hd__lpflow_inputiso1p_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_inputiso1p_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_inputiso1p_1()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/lpflow_inputiso1p/sky130_fd_sc_hd__lpflow_inputiso1p_1.gds",
        cellname="sky130_fd_sc_hd__lpflow_inputiso1p_1",
    )


@cell
def sky130_fd_sc_hd__a311o_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a311o_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a311o_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a311o/sky130_fd_sc_hd__a311o_1.gds",
        cellname="sky130_fd_sc_hd__a311o_1",
    )


@cell
def sky130_fd_sc_hd__a311o_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__a311o_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a311o_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a311o/sky130_fd_sc_hd__a311o_2.gds",
        cellname="sky130_fd_sc_hd__a311o_2",
    )


@cell
def sky130_fd_sc_hd__a311o_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__a311o_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a311o_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a311o/sky130_fd_sc_hd__a311o_4.gds",
        cellname="sky130_fd_sc_hd__a311o_4",
    )


@cell
def sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_4()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/lpflow_lsbuf_lh_hl_isowell_tap/sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_4.gds",
        cellname="sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_4",
    )


@cell
def sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_1()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/lpflow_lsbuf_lh_hl_isowell_tap/sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_1.gds",
        cellname="sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_1",
    )


@cell
def sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_2()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/lpflow_lsbuf_lh_hl_isowell_tap/sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_2.gds",
        cellname="sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_2",
    )


@cell
def sky130_fd_sc_hd__nor2b_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__nor2b_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nor2b_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/nor2b/sky130_fd_sc_hd__nor2b_1.gds",
        cellname="sky130_fd_sc_hd__nor2b_1",
    )


@cell
def sky130_fd_sc_hd__nor2b_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__nor2b_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nor2b_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/nor2b/sky130_fd_sc_hd__nor2b_4.gds",
        cellname="sky130_fd_sc_hd__nor2b_4",
    )


@cell
def sky130_fd_sc_hd__nor2b_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__nor2b_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nor2b_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/nor2b/sky130_fd_sc_hd__nor2b_2.gds",
        cellname="sky130_fd_sc_hd__nor2b_2",
    )


@cell
def sky130_fd_sc_hd__clkdlybuf4s15_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__clkdlybuf4s15_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__clkdlybuf4s15_2()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/clkdlybuf4s15/sky130_fd_sc_hd__clkdlybuf4s15_2.gds",
        cellname="sky130_fd_sc_hd__clkdlybuf4s15_2",
    )


@cell
def sky130_fd_sc_hd__clkdlybuf4s15_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__clkdlybuf4s15_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__clkdlybuf4s15_1()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/clkdlybuf4s15/sky130_fd_sc_hd__clkdlybuf4s15_1.gds",
        cellname="sky130_fd_sc_hd__clkdlybuf4s15_1",
    )


@cell
def sky130_fd_sc_hd__sdfxtp_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__sdfxtp_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sdfxtp_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/sdfxtp/sky130_fd_sc_hd__sdfxtp_4.gds",
        cellname="sky130_fd_sc_hd__sdfxtp_4",
    )


@cell
def sky130_fd_sc_hd__sdfxtp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__sdfxtp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sdfxtp_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/sdfxtp/sky130_fd_sc_hd__sdfxtp_1.gds",
        cellname="sky130_fd_sc_hd__sdfxtp_1",
    )


@cell
def sky130_fd_sc_hd__sdfxtp_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__sdfxtp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sdfxtp_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/sdfxtp/sky130_fd_sc_hd__sdfxtp_2.gds",
        cellname="sky130_fd_sc_hd__sdfxtp_2",
    )


@cell
def sky130_fd_sc_hd__sdfsbp_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__sdfsbp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sdfsbp_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/sdfsbp/sky130_fd_sc_hd__sdfsbp_2.gds",
        cellname="sky130_fd_sc_hd__sdfsbp_2",
    )


@cell
def sky130_fd_sc_hd__sdfsbp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__sdfsbp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sdfsbp_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/sdfsbp/sky130_fd_sc_hd__sdfsbp_1.gds",
        cellname="sky130_fd_sc_hd__sdfsbp_1",
    )


@cell
def sky130_fd_sc_hd__o221ai_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__o221ai_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o221ai_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o221ai/sky130_fd_sc_hd__o221ai_4.gds",
        cellname="sky130_fd_sc_hd__o221ai_4",
    )


@cell
def sky130_fd_sc_hd__o221ai_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__o221ai_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o221ai_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o221ai/sky130_fd_sc_hd__o221ai_1.gds",
        cellname="sky130_fd_sc_hd__o221ai_1",
    )


@cell
def sky130_fd_sc_hd__o221ai_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__o221ai_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o221ai_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o221ai/sky130_fd_sc_hd__o221ai_2.gds",
        cellname="sky130_fd_sc_hd__o221ai_2",
    )


@cell
def sky130_fd_sc_hd__sdfbbn_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__sdfbbn_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sdfbbn_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/sdfbbn/sky130_fd_sc_hd__sdfbbn_2.gds",
        cellname="sky130_fd_sc_hd__sdfbbn_2",
    )


@cell
def sky130_fd_sc_hd__sdfbbn_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__sdfbbn_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sdfbbn_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/sdfbbn/sky130_fd_sc_hd__sdfbbn_1.gds",
        cellname="sky130_fd_sc_hd__sdfbbn_1",
    )


@cell
def sky130_fd_sc_hd__dlrtn_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlrtn_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlrtn_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/dlrtn/sky130_fd_sc_hd__dlrtn_4.gds",
        cellname="sky130_fd_sc_hd__dlrtn_4",
    )


@cell
def sky130_fd_sc_hd__dlrtn_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlrtn_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlrtn_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/dlrtn/sky130_fd_sc_hd__dlrtn_1.gds",
        cellname="sky130_fd_sc_hd__dlrtn_1",
    )


@cell
def sky130_fd_sc_hd__dlrtn_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlrtn_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlrtn_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/dlrtn/sky130_fd_sc_hd__dlrtn_2.gds",
        cellname="sky130_fd_sc_hd__dlrtn_2",
    )


@cell
def sky130_fd_sc_hd__dlxbn_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlxbn_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlxbn_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/dlxbn/sky130_fd_sc_hd__dlxbn_1.gds",
        cellname="sky130_fd_sc_hd__dlxbn_1",
    )


@cell
def sky130_fd_sc_hd__dlxbn_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlxbn_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlxbn_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/dlxbn/sky130_fd_sc_hd__dlxbn_2.gds",
        cellname="sky130_fd_sc_hd__dlxbn_2",
    )


@cell
def sky130_fd_sc_hd__o32a_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__o32a_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o32a_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o32a/sky130_fd_sc_hd__o32a_2.gds",
        cellname="sky130_fd_sc_hd__o32a_2",
    )


@cell
def sky130_fd_sc_hd__o32a_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__o32a_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o32a_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o32a/sky130_fd_sc_hd__o32a_4.gds",
        cellname="sky130_fd_sc_hd__o32a_4",
    )


@cell
def sky130_fd_sc_hd__o32a_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__o32a_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o32a_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o32a/sky130_fd_sc_hd__o32a_1.gds",
        cellname="sky130_fd_sc_hd__o32a_1",
    )


@cell
def sky130_fd_sc_hd__tap_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__tap_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__tap_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/tap/sky130_fd_sc_hd__tap_2.gds",
        cellname="sky130_fd_sc_hd__tap_2",
    )


@cell
def sky130_fd_sc_hd__tap_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__tap_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__tap_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/tap/sky130_fd_sc_hd__tap_1.gds",
        cellname="sky130_fd_sc_hd__tap_1",
    )


@cell
def sky130_fd_sc_hd__dlygate4sd3_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlygate4sd3_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlygate4sd3_1()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/dlygate4sd3/sky130_fd_sc_hd__dlygate4sd3_1.gds",
        cellname="sky130_fd_sc_hd__dlygate4sd3_1",
    )


@cell
def sky130_fd_sc_hd__a2bb2o_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a2bb2o_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a2bb2o_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a2bb2o/sky130_fd_sc_hd__a2bb2o_1.gds",
        cellname="sky130_fd_sc_hd__a2bb2o_1",
    )


@cell
def sky130_fd_sc_hd__a2bb2o_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__a2bb2o_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a2bb2o_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a2bb2o/sky130_fd_sc_hd__a2bb2o_2.gds",
        cellname="sky130_fd_sc_hd__a2bb2o_2",
    )


@cell
def sky130_fd_sc_hd__a2bb2o_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__a2bb2o_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a2bb2o_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a2bb2o/sky130_fd_sc_hd__a2bb2o_4.gds",
        cellname="sky130_fd_sc_hd__a2bb2o_4",
    )


@cell
def sky130_fd_sc_hd__macro_sparecell() -> gf.Component:
    """Returns sky130_fd_sc_hd__macro_sparecell fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__macro_sparecell()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/macro_sparecell/sky130_fd_sc_hd__macro_sparecell.gds",
        cellname="sky130_fd_sc_hd__macro_sparecell",
    )


@cell
def sky130_fd_sc_hd__sdfrtp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__sdfrtp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sdfrtp_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/sdfrtp/sky130_fd_sc_hd__sdfrtp_1.gds",
        cellname="sky130_fd_sc_hd__sdfrtp_1",
    )


@cell
def sky130_fd_sc_hd__sdfrtp_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__sdfrtp_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sdfrtp_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/sdfrtp/sky130_fd_sc_hd__sdfrtp_4.gds",
        cellname="sky130_fd_sc_hd__sdfrtp_4",
    )


@cell
def sky130_fd_sc_hd__sdfrtp_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__sdfrtp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sdfrtp_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/sdfrtp/sky130_fd_sc_hd__sdfrtp_2.gds",
        cellname="sky130_fd_sc_hd__sdfrtp_2",
    )


@cell
def sky130_fd_sc_hd__a221o_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__a221o_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a221o_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a221o/sky130_fd_sc_hd__a221o_4.gds",
        cellname="sky130_fd_sc_hd__a221o_4",
    )


@cell
def sky130_fd_sc_hd__a221o_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__a221o_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a221o_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a221o/sky130_fd_sc_hd__a221o_2.gds",
        cellname="sky130_fd_sc_hd__a221o_2",
    )


@cell
def sky130_fd_sc_hd__a221o_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a221o_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a221o_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a221o/sky130_fd_sc_hd__a221o_1.gds",
        cellname="sky130_fd_sc_hd__a221o_1",
    )


@cell
def sky130_fd_sc_hd__clkdlybuf4s25_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__clkdlybuf4s25_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__clkdlybuf4s25_1()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/clkdlybuf4s25/sky130_fd_sc_hd__clkdlybuf4s25_1.gds",
        cellname="sky130_fd_sc_hd__clkdlybuf4s25_1",
    )


@cell
def sky130_fd_sc_hd__clkdlybuf4s25_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__clkdlybuf4s25_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__clkdlybuf4s25_2()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/clkdlybuf4s25/sky130_fd_sc_hd__clkdlybuf4s25_2.gds",
        cellname="sky130_fd_sc_hd__clkdlybuf4s25_2",
    )


@cell
def sky130_fd_sc_hd__sdfrbp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__sdfrbp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sdfrbp_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/sdfrbp/sky130_fd_sc_hd__sdfrbp_1.gds",
        cellname="sky130_fd_sc_hd__sdfrbp_1",
    )


@cell
def sky130_fd_sc_hd__sdfrbp_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__sdfrbp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sdfrbp_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/sdfrbp/sky130_fd_sc_hd__sdfrbp_2.gds",
        cellname="sky130_fd_sc_hd__sdfrbp_2",
    )


@cell
def sky130_fd_sc_hd__nand2b_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__nand2b_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nand2b_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/nand2b/sky130_fd_sc_hd__nand2b_1.gds",
        cellname="sky130_fd_sc_hd__nand2b_1",
    )


@cell
def sky130_fd_sc_hd__nand2b_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__nand2b_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nand2b_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/nand2b/sky130_fd_sc_hd__nand2b_4.gds",
        cellname="sky130_fd_sc_hd__nand2b_4",
    )


@cell
def sky130_fd_sc_hd__nand2b_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__nand2b_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nand2b_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/nand2b/sky130_fd_sc_hd__nand2b_2.gds",
        cellname="sky130_fd_sc_hd__nand2b_2",
    )


@cell
def sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_4()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/lpflow_lsbuf_lh_isowell_tap/sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_4.gds",
        cellname="sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_4",
    )


@cell
def sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_2()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/lpflow_lsbuf_lh_isowell_tap/sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_2.gds",
        cellname="sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_2",
    )


@cell
def sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_1()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/lpflow_lsbuf_lh_isowell_tap/sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_1.gds",
        cellname="sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_1",
    )


@cell
def sky130_fd_sc_hd__o31ai_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__o31ai_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o31ai_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o31ai/sky130_fd_sc_hd__o31ai_2.gds",
        cellname="sky130_fd_sc_hd__o31ai_2",
    )


@cell
def sky130_fd_sc_hd__o31ai_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__o31ai_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o31ai_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o31ai/sky130_fd_sc_hd__o31ai_4.gds",
        cellname="sky130_fd_sc_hd__o31ai_4",
    )


@cell
def sky130_fd_sc_hd__o31ai_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__o31ai_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o31ai_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o31ai/sky130_fd_sc_hd__o31ai_1.gds",
        cellname="sky130_fd_sc_hd__o31ai_1",
    )


@cell
def sky130_fd_sc_hd__o21ai_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__o21ai_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o21ai_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o21ai/sky130_fd_sc_hd__o21ai_1.gds",
        cellname="sky130_fd_sc_hd__o21ai_1",
    )


@cell
def sky130_fd_sc_hd__o21ai_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__o21ai_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o21ai_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o21ai/sky130_fd_sc_hd__o21ai_4.gds",
        cellname="sky130_fd_sc_hd__o21ai_4",
    )


@cell
def sky130_fd_sc_hd__o21ai_0() -> gf.Component:
    """Returns sky130_fd_sc_hd__o21ai_0 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o21ai_0()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o21ai/sky130_fd_sc_hd__o21ai_0.gds",
        cellname="sky130_fd_sc_hd__o21ai_0",
    )


@cell
def sky130_fd_sc_hd__o21ai_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__o21ai_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o21ai_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o21ai/sky130_fd_sc_hd__o21ai_2.gds",
        cellname="sky130_fd_sc_hd__o21ai_2",
    )


@cell
def sky130_fd_sc_hd__a32o_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__a32o_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a32o_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a32o/sky130_fd_sc_hd__a32o_4.gds",
        cellname="sky130_fd_sc_hd__a32o_4",
    )


@cell
def sky130_fd_sc_hd__a32o_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a32o_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a32o_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a32o/sky130_fd_sc_hd__a32o_1.gds",
        cellname="sky130_fd_sc_hd__a32o_1",
    )


@cell
def sky130_fd_sc_hd__a32o_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__a32o_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a32o_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a32o/sky130_fd_sc_hd__a32o_2.gds",
        cellname="sky130_fd_sc_hd__a32o_2",
    )


@cell
def sky130_fd_sc_hd__nand4b_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__nand4b_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nand4b_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/nand4b/sky130_fd_sc_hd__nand4b_4.gds",
        cellname="sky130_fd_sc_hd__nand4b_4",
    )


@cell
def sky130_fd_sc_hd__nand4b_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__nand4b_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nand4b_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/nand4b/sky130_fd_sc_hd__nand4b_1.gds",
        cellname="sky130_fd_sc_hd__nand4b_1",
    )


@cell
def sky130_fd_sc_hd__nand4b_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__nand4b_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nand4b_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/nand4b/sky130_fd_sc_hd__nand4b_2.gds",
        cellname="sky130_fd_sc_hd__nand4b_2",
    )


@cell
def sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_4()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/lpflow_lsbuf_lh_isowell/sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_4.gds",
        cellname="sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_4",
    )


@cell
def sky130_fd_sc_hd__ha_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__ha_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__ha_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/ha/sky130_fd_sc_hd__ha_2.gds",
        cellname="sky130_fd_sc_hd__ha_2",
    )


@cell
def sky130_fd_sc_hd__ha_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__ha_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__ha_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/ha/sky130_fd_sc_hd__ha_4.gds",
        cellname="sky130_fd_sc_hd__ha_4",
    )


@cell
def sky130_fd_sc_hd__ha_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__ha_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__ha_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/ha/sky130_fd_sc_hd__ha_1.gds",
        cellname="sky130_fd_sc_hd__ha_1",
    )


@cell
def sky130_fd_sc_hd__and4_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__and4_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__and4_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/and4/sky130_fd_sc_hd__and4_4.gds",
        cellname="sky130_fd_sc_hd__and4_4",
    )


@cell
def sky130_fd_sc_hd__and4_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__and4_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__and4_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/and4/sky130_fd_sc_hd__and4_2.gds",
        cellname="sky130_fd_sc_hd__and4_2",
    )


@cell
def sky130_fd_sc_hd__and4_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__and4_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__and4_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/and4/sky130_fd_sc_hd__and4_1.gds",
        cellname="sky130_fd_sc_hd__and4_1",
    )


@cell
def sky130_fd_sc_hd__dlygate4sd2_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlygate4sd2_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlygate4sd2_1()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/dlygate4sd2/sky130_fd_sc_hd__dlygate4sd2_1.gds",
        cellname="sky130_fd_sc_hd__dlygate4sd2_1",
    )


@cell
def sky130_fd_sc_hd__dlxtp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlxtp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlxtp_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/dlxtp/sky130_fd_sc_hd__dlxtp_1.gds",
        cellname="sky130_fd_sc_hd__dlxtp_1",
    )


@cell
def sky130_fd_sc_hd__sdfbbp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__sdfbbp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sdfbbp_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/sdfbbp/sky130_fd_sc_hd__sdfbbp_1.gds",
        cellname="sky130_fd_sc_hd__sdfbbp_1",
    )


@cell
def sky130_fd_sc_hd__o2111ai_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__o2111ai_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o2111ai_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o2111ai/sky130_fd_sc_hd__o2111ai_2.gds",
        cellname="sky130_fd_sc_hd__o2111ai_2",
    )


@cell
def sky130_fd_sc_hd__o2111ai_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__o2111ai_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o2111ai_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o2111ai/sky130_fd_sc_hd__o2111ai_4.gds",
        cellname="sky130_fd_sc_hd__o2111ai_4",
    )


@cell
def sky130_fd_sc_hd__o2111ai_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__o2111ai_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o2111ai_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o2111ai/sky130_fd_sc_hd__o2111ai_1.gds",
        cellname="sky130_fd_sc_hd__o2111ai_1",
    )


@cell
def sky130_fd_sc_hd__and3_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__and3_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__and3_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/and3/sky130_fd_sc_hd__and3_2.gds",
        cellname="sky130_fd_sc_hd__and3_2",
    )


@cell
def sky130_fd_sc_hd__and3_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__and3_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__and3_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/and3/sky130_fd_sc_hd__and3_1.gds",
        cellname="sky130_fd_sc_hd__and3_1",
    )


@cell
def sky130_fd_sc_hd__and3_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__and3_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__and3_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/and3/sky130_fd_sc_hd__and3_4.gds",
        cellname="sky130_fd_sc_hd__and3_4",
    )


@cell
def sky130_fd_sc_hd__bufbuf_16() -> gf.Component:
    """Returns sky130_fd_sc_hd__bufbuf_16 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__bufbuf_16()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/bufbuf/sky130_fd_sc_hd__bufbuf_16.gds",
        cellname="sky130_fd_sc_hd__bufbuf_16",
    )


@cell
def sky130_fd_sc_hd__bufbuf_8() -> gf.Component:
    """Returns sky130_fd_sc_hd__bufbuf_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__bufbuf_8()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/bufbuf/sky130_fd_sc_hd__bufbuf_8.gds",
        cellname="sky130_fd_sc_hd__bufbuf_8",
    )


@cell
def sky130_fd_sc_hd__a31oi_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__a31oi_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a31oi_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a31oi/sky130_fd_sc_hd__a31oi_2.gds",
        cellname="sky130_fd_sc_hd__a31oi_2",
    )


@cell
def sky130_fd_sc_hd__a31oi_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__a31oi_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a31oi_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a31oi/sky130_fd_sc_hd__a31oi_4.gds",
        cellname="sky130_fd_sc_hd__a31oi_4",
    )


@cell
def sky130_fd_sc_hd__a31oi_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a31oi_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a31oi_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a31oi/sky130_fd_sc_hd__a31oi_1.gds",
        cellname="sky130_fd_sc_hd__a31oi_1",
    )


@cell
def sky130_fd_sc_hd__and4bb_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__and4bb_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__and4bb_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/and4bb/sky130_fd_sc_hd__and4bb_1.gds",
        cellname="sky130_fd_sc_hd__and4bb_1",
    )


@cell
def sky130_fd_sc_hd__and4bb_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__and4bb_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__and4bb_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/and4bb/sky130_fd_sc_hd__and4bb_2.gds",
        cellname="sky130_fd_sc_hd__and4bb_2",
    )


@cell
def sky130_fd_sc_hd__and4bb_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__and4bb_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__and4bb_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/and4bb/sky130_fd_sc_hd__and4bb_4.gds",
        cellname="sky130_fd_sc_hd__and4bb_4",
    )


@cell
def sky130_fd_sc_hd__dlrtp_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlrtp_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlrtp_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/dlrtp/sky130_fd_sc_hd__dlrtp_4.gds",
        cellname="sky130_fd_sc_hd__dlrtp_4",
    )


@cell
def sky130_fd_sc_hd__dlrtp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlrtp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlrtp_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/dlrtp/sky130_fd_sc_hd__dlrtp_1.gds",
        cellname="sky130_fd_sc_hd__dlrtp_1",
    )


@cell
def sky130_fd_sc_hd__dlrtp_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlrtp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlrtp_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/dlrtp/sky130_fd_sc_hd__dlrtp_2.gds",
        cellname="sky130_fd_sc_hd__dlrtp_2",
    )


@cell
def sky130_fd_sc_hd__o41ai_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__o41ai_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o41ai_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o41ai/sky130_fd_sc_hd__o41ai_2.gds",
        cellname="sky130_fd_sc_hd__o41ai_2",
    )


@cell
def sky130_fd_sc_hd__o41ai_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__o41ai_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o41ai_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o41ai/sky130_fd_sc_hd__o41ai_1.gds",
        cellname="sky130_fd_sc_hd__o41ai_1",
    )


@cell
def sky130_fd_sc_hd__o41ai_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__o41ai_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o41ai_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o41ai/sky130_fd_sc_hd__o41ai_4.gds",
        cellname="sky130_fd_sc_hd__o41ai_4",
    )


@cell
def sky130_fd_sc_hd__conb_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__conb_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__conb_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/conb/sky130_fd_sc_hd__conb_1.gds",
        cellname="sky130_fd_sc_hd__conb_1",
    )


@cell
def sky130_fd_sc_hd__o41a_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__o41a_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o41a_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o41a/sky130_fd_sc_hd__o41a_2.gds",
        cellname="sky130_fd_sc_hd__o41a_2",
    )


@cell
def sky130_fd_sc_hd__o41a_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__o41a_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o41a_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o41a/sky130_fd_sc_hd__o41a_1.gds",
        cellname="sky130_fd_sc_hd__o41a_1",
    )


@cell
def sky130_fd_sc_hd__o41a_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__o41a_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o41a_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o41a/sky130_fd_sc_hd__o41a_4.gds",
        cellname="sky130_fd_sc_hd__o41a_4",
    )


@cell
def sky130_fd_sc_hd__dlxtn_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlxtn_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlxtn_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/dlxtn/sky130_fd_sc_hd__dlxtn_1.gds",
        cellname="sky130_fd_sc_hd__dlxtn_1",
    )


@cell
def sky130_fd_sc_hd__dlxtn_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlxtn_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlxtn_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/dlxtn/sky130_fd_sc_hd__dlxtn_2.gds",
        cellname="sky130_fd_sc_hd__dlxtn_2",
    )


@cell
def sky130_fd_sc_hd__dlxtn_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlxtn_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlxtn_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/dlxtn/sky130_fd_sc_hd__dlxtn_4.gds",
        cellname="sky130_fd_sc_hd__dlxtn_4",
    )


@cell
def sky130_fd_sc_hd__nor2_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__nor2_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nor2_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/nor2/sky130_fd_sc_hd__nor2_2.gds",
        cellname="sky130_fd_sc_hd__nor2_2",
    )


@cell
def sky130_fd_sc_hd__nor2_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__nor2_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nor2_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/nor2/sky130_fd_sc_hd__nor2_4.gds",
        cellname="sky130_fd_sc_hd__nor2_4",
    )


@cell
def sky130_fd_sc_hd__nor2_8() -> gf.Component:
    """Returns sky130_fd_sc_hd__nor2_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nor2_8()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/nor2/sky130_fd_sc_hd__nor2_8.gds",
        cellname="sky130_fd_sc_hd__nor2_8",
    )


@cell
def sky130_fd_sc_hd__nor2_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__nor2_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nor2_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/nor2/sky130_fd_sc_hd__nor2_1.gds",
        cellname="sky130_fd_sc_hd__nor2_1",
    )


@cell
def sky130_fd_sc_hd__diode_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__diode_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__diode_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/diode/sky130_fd_sc_hd__diode_2.gds",
        cellname="sky130_fd_sc_hd__diode_2",
    )


@cell
def sky130_fd_sc_hd__tapvpwrvgnd_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__tapvpwrvgnd_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__tapvpwrvgnd_1()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/tapvpwrvgnd/sky130_fd_sc_hd__tapvpwrvgnd_1.gds",
        cellname="sky130_fd_sc_hd__tapvpwrvgnd_1",
    )


@cell
def sky130_fd_sc_hd__lpflow_inputiso1n_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_inputiso1n_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_inputiso1n_1()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/lpflow_inputiso1n/sky130_fd_sc_hd__lpflow_inputiso1n_1.gds",
        cellname="sky130_fd_sc_hd__lpflow_inputiso1n_1",
    )


@cell
def sky130_fd_sc_hd__a211oi_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__a211oi_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a211oi_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a211oi/sky130_fd_sc_hd__a211oi_4.gds",
        cellname="sky130_fd_sc_hd__a211oi_4",
    )


@cell
def sky130_fd_sc_hd__a211oi_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__a211oi_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a211oi_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a211oi/sky130_fd_sc_hd__a211oi_2.gds",
        cellname="sky130_fd_sc_hd__a211oi_2",
    )


@cell
def sky130_fd_sc_hd__a211oi_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a211oi_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a211oi_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a211oi/sky130_fd_sc_hd__a211oi_1.gds",
        cellname="sky130_fd_sc_hd__a211oi_1",
    )


@cell
def sky130_fd_sc_hd__edfxtp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__edfxtp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__edfxtp_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/edfxtp/sky130_fd_sc_hd__edfxtp_1.gds",
        cellname="sky130_fd_sc_hd__edfxtp_1",
    )


@cell
def sky130_fd_sc_hd__dfrbp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dfrbp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dfrbp_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/dfrbp/sky130_fd_sc_hd__dfrbp_1.gds",
        cellname="sky130_fd_sc_hd__dfrbp_1",
    )


@cell
def sky130_fd_sc_hd__dfrbp_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__dfrbp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dfrbp_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/dfrbp/sky130_fd_sc_hd__dfrbp_2.gds",
        cellname="sky130_fd_sc_hd__dfrbp_2",
    )


@cell
def sky130_fd_sc_hd__a31o_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__a31o_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a31o_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a31o/sky130_fd_sc_hd__a31o_2.gds",
        cellname="sky130_fd_sc_hd__a31o_2",
    )


@cell
def sky130_fd_sc_hd__a31o_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__a31o_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a31o_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a31o/sky130_fd_sc_hd__a31o_4.gds",
        cellname="sky130_fd_sc_hd__a31o_4",
    )


@cell
def sky130_fd_sc_hd__a31o_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a31o_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a31o_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a31o/sky130_fd_sc_hd__a31o_1.gds",
        cellname="sky130_fd_sc_hd__a31o_1",
    )


@cell
def sky130_fd_sc_hd__probe_p_8() -> gf.Component:
    """Returns sky130_fd_sc_hd__probe_p_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__probe_p_8()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/probe_p/sky130_fd_sc_hd__probe_p_8.gds",
        cellname="sky130_fd_sc_hd__probe_p_8",
    )


@cell
def sky130_fd_sc_hd__dfrtp_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__dfrtp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dfrtp_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/dfrtp/sky130_fd_sc_hd__dfrtp_2.gds",
        cellname="sky130_fd_sc_hd__dfrtp_2",
    )


@cell
def sky130_fd_sc_hd__dfrtp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dfrtp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dfrtp_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/dfrtp/sky130_fd_sc_hd__dfrtp_1.gds",
        cellname="sky130_fd_sc_hd__dfrtp_1",
    )


@cell
def sky130_fd_sc_hd__dfrtp_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__dfrtp_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dfrtp_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/dfrtp/sky130_fd_sc_hd__dfrtp_4.gds",
        cellname="sky130_fd_sc_hd__dfrtp_4",
    )


@cell
def sky130_fd_sc_hd__nor4_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__nor4_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nor4_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/nor4/sky130_fd_sc_hd__nor4_2.gds",
        cellname="sky130_fd_sc_hd__nor4_2",
    )


@cell
def sky130_fd_sc_hd__nor4_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__nor4_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nor4_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/nor4/sky130_fd_sc_hd__nor4_4.gds",
        cellname="sky130_fd_sc_hd__nor4_4",
    )


@cell
def sky130_fd_sc_hd__nor4_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__nor4_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nor4_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/nor4/sky130_fd_sc_hd__nor4_1.gds",
        cellname="sky130_fd_sc_hd__nor4_1",
    )


@cell
def sky130_fd_sc_hd__a2111oi_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__a2111oi_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a2111oi_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a2111oi/sky130_fd_sc_hd__a2111oi_4.gds",
        cellname="sky130_fd_sc_hd__a2111oi_4",
    )


@cell
def sky130_fd_sc_hd__a2111oi_0() -> gf.Component:
    """Returns sky130_fd_sc_hd__a2111oi_0 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a2111oi_0()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a2111oi/sky130_fd_sc_hd__a2111oi_0.gds",
        cellname="sky130_fd_sc_hd__a2111oi_0",
    )


@cell
def sky130_fd_sc_hd__a2111oi_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__a2111oi_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a2111oi_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a2111oi/sky130_fd_sc_hd__a2111oi_2.gds",
        cellname="sky130_fd_sc_hd__a2111oi_2",
    )


@cell
def sky130_fd_sc_hd__a2111oi_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a2111oi_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a2111oi_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a2111oi/sky130_fd_sc_hd__a2111oi_1.gds",
        cellname="sky130_fd_sc_hd__a2111oi_1",
    )


@cell
def sky130_fd_sc_hd__mux2_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__mux2_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__mux2_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/mux2/sky130_fd_sc_hd__mux2_2.gds",
        cellname="sky130_fd_sc_hd__mux2_2",
    )


@cell
def sky130_fd_sc_hd__mux2_8() -> gf.Component:
    """Returns sky130_fd_sc_hd__mux2_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__mux2_8()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/mux2/sky130_fd_sc_hd__mux2_8.gds",
        cellname="sky130_fd_sc_hd__mux2_8",
    )


@cell
def sky130_fd_sc_hd__mux2_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__mux2_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__mux2_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/mux2/sky130_fd_sc_hd__mux2_1.gds",
        cellname="sky130_fd_sc_hd__mux2_1",
    )


@cell
def sky130_fd_sc_hd__mux2_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__mux2_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__mux2_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/mux2/sky130_fd_sc_hd__mux2_4.gds",
        cellname="sky130_fd_sc_hd__mux2_4",
    )


@cell
def sky130_fd_sc_hd__o21ba_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__o21ba_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o21ba_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o21ba/sky130_fd_sc_hd__o21ba_1.gds",
        cellname="sky130_fd_sc_hd__o21ba_1",
    )


@cell
def sky130_fd_sc_hd__o21ba_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__o21ba_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o21ba_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o21ba/sky130_fd_sc_hd__o21ba_4.gds",
        cellname="sky130_fd_sc_hd__o21ba_4",
    )


@cell
def sky130_fd_sc_hd__o21ba_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__o21ba_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o21ba_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o21ba/sky130_fd_sc_hd__o21ba_2.gds",
        cellname="sky130_fd_sc_hd__o21ba_2",
    )


@cell
def sky130_fd_sc_hd__sdlclkp_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__sdlclkp_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sdlclkp_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/sdlclkp/sky130_fd_sc_hd__sdlclkp_4.gds",
        cellname="sky130_fd_sc_hd__sdlclkp_4",
    )


@cell
def sky130_fd_sc_hd__sdlclkp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__sdlclkp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sdlclkp_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/sdlclkp/sky130_fd_sc_hd__sdlclkp_1.gds",
        cellname="sky130_fd_sc_hd__sdlclkp_1",
    )


@cell
def sky130_fd_sc_hd__sdlclkp_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__sdlclkp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sdlclkp_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/sdlclkp/sky130_fd_sc_hd__sdlclkp_2.gds",
        cellname="sky130_fd_sc_hd__sdlclkp_2",
    )


@cell
def sky130_fd_sc_hd__sdfrtn_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__sdfrtn_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sdfrtn_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/sdfrtn/sky130_fd_sc_hd__sdfrtn_1.gds",
        cellname="sky130_fd_sc_hd__sdfrtn_1",
    )


@cell
def sky130_fd_sc_hd__lpflow_inputiso0p_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_inputiso0p_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_inputiso0p_1()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/lpflow_inputiso0p/sky130_fd_sc_hd__lpflow_inputiso0p_1.gds",
        cellname="sky130_fd_sc_hd__lpflow_inputiso0p_1",
    )


@cell
def sky130_fd_sc_hd__a21oi_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a21oi_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a21oi_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a21oi/sky130_fd_sc_hd__a21oi_1.gds",
        cellname="sky130_fd_sc_hd__a21oi_1",
    )


@cell
def sky130_fd_sc_hd__a21oi_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__a21oi_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a21oi_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a21oi/sky130_fd_sc_hd__a21oi_4.gds",
        cellname="sky130_fd_sc_hd__a21oi_4",
    )


@cell
def sky130_fd_sc_hd__a21oi_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__a21oi_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a21oi_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a21oi/sky130_fd_sc_hd__a21oi_2.gds",
        cellname="sky130_fd_sc_hd__a21oi_2",
    )


@cell
def sky130_fd_sc_hd__o211ai_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__o211ai_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o211ai_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o211ai/sky130_fd_sc_hd__o211ai_4.gds",
        cellname="sky130_fd_sc_hd__o211ai_4",
    )


@cell
def sky130_fd_sc_hd__o211ai_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__o211ai_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o211ai_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o211ai/sky130_fd_sc_hd__o211ai_2.gds",
        cellname="sky130_fd_sc_hd__o211ai_2",
    )


@cell
def sky130_fd_sc_hd__o211ai_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__o211ai_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o211ai_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o211ai/sky130_fd_sc_hd__o211ai_1.gds",
        cellname="sky130_fd_sc_hd__o211ai_1",
    )


@cell
def sky130_fd_sc_hd__clkinvlp_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__clkinvlp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__clkinvlp_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/clkinvlp/sky130_fd_sc_hd__clkinvlp_2.gds",
        cellname="sky130_fd_sc_hd__clkinvlp_2",
    )


@cell
def sky130_fd_sc_hd__clkinvlp_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__clkinvlp_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__clkinvlp_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/clkinvlp/sky130_fd_sc_hd__clkinvlp_4.gds",
        cellname="sky130_fd_sc_hd__clkinvlp_4",
    )


@cell
def sky130_fd_sc_hd__fa_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__fa_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__fa_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/fa/sky130_fd_sc_hd__fa_2.gds",
        cellname="sky130_fd_sc_hd__fa_2",
    )


@cell
def sky130_fd_sc_hd__fa_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__fa_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__fa_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/fa/sky130_fd_sc_hd__fa_1.gds",
        cellname="sky130_fd_sc_hd__fa_1",
    )


@cell
def sky130_fd_sc_hd__fa_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__fa_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__fa_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/fa/sky130_fd_sc_hd__fa_4.gds",
        cellname="sky130_fd_sc_hd__fa_4",
    )


@cell
def sky130_fd_sc_hd__maj3_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__maj3_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__maj3_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/maj3/sky130_fd_sc_hd__maj3_4.gds",
        cellname="sky130_fd_sc_hd__maj3_4",
    )


@cell
def sky130_fd_sc_hd__maj3_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__maj3_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__maj3_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/maj3/sky130_fd_sc_hd__maj3_1.gds",
        cellname="sky130_fd_sc_hd__maj3_1",
    )


@cell
def sky130_fd_sc_hd__maj3_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__maj3_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__maj3_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/maj3/sky130_fd_sc_hd__maj3_2.gds",
        cellname="sky130_fd_sc_hd__maj3_2",
    )


@cell
def sky130_fd_sc_hd__tapvgnd_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__tapvgnd_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__tapvgnd_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/tapvgnd/sky130_fd_sc_hd__tapvgnd_1.gds",
        cellname="sky130_fd_sc_hd__tapvgnd_1",
    )


@cell
def sky130_fd_sc_hd__o31a_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__o31a_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o31a_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o31a/sky130_fd_sc_hd__o31a_2.gds",
        cellname="sky130_fd_sc_hd__o31a_2",
    )


@cell
def sky130_fd_sc_hd__o31a_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__o31a_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o31a_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o31a/sky130_fd_sc_hd__o31a_4.gds",
        cellname="sky130_fd_sc_hd__o31a_4",
    )


@cell
def sky130_fd_sc_hd__o31a_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__o31a_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o31a_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o31a/sky130_fd_sc_hd__o31a_1.gds",
        cellname="sky130_fd_sc_hd__o31a_1",
    )


@cell
def sky130_fd_sc_hd__dlrbp_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlrbp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlrbp_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/dlrbp/sky130_fd_sc_hd__dlrbp_2.gds",
        cellname="sky130_fd_sc_hd__dlrbp_2",
    )


@cell
def sky130_fd_sc_hd__dlrbp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlrbp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlrbp_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/dlrbp/sky130_fd_sc_hd__dlrbp_1.gds",
        cellname="sky130_fd_sc_hd__dlrbp_1",
    )


@cell
def sky130_fd_sc_hd__and3b_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__and3b_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__and3b_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/and3b/sky130_fd_sc_hd__and3b_4.gds",
        cellname="sky130_fd_sc_hd__and3b_4",
    )


@cell
def sky130_fd_sc_hd__and3b_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__and3b_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__and3b_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/and3b/sky130_fd_sc_hd__and3b_2.gds",
        cellname="sky130_fd_sc_hd__and3b_2",
    )


@cell
def sky130_fd_sc_hd__and3b_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__and3b_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__and3b_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/and3b/sky130_fd_sc_hd__and3b_1.gds",
        cellname="sky130_fd_sc_hd__and3b_1",
    )


@cell
def sky130_fd_sc_hd__and2b_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__and2b_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__and2b_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/and2b/sky130_fd_sc_hd__and2b_2.gds",
        cellname="sky130_fd_sc_hd__and2b_2",
    )


@cell
def sky130_fd_sc_hd__and2b_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__and2b_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__and2b_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/and2b/sky130_fd_sc_hd__and2b_1.gds",
        cellname="sky130_fd_sc_hd__and2b_1",
    )


@cell
def sky130_fd_sc_hd__and2b_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__and2b_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__and2b_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/and2b/sky130_fd_sc_hd__and2b_4.gds",
        cellname="sky130_fd_sc_hd__and2b_4",
    )


@cell
def sky130_fd_sc_hd__or2_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__or2_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__or2_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/or2/sky130_fd_sc_hd__or2_4.gds",
        cellname="sky130_fd_sc_hd__or2_4",
    )


@cell
def sky130_fd_sc_hd__or2_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__or2_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__or2_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/or2/sky130_fd_sc_hd__or2_1.gds",
        cellname="sky130_fd_sc_hd__or2_1",
    )


@cell
def sky130_fd_sc_hd__or2_0() -> gf.Component:
    """Returns sky130_fd_sc_hd__or2_0 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__or2_0()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/or2/sky130_fd_sc_hd__or2_0.gds",
        cellname="sky130_fd_sc_hd__or2_0",
    )


@cell
def sky130_fd_sc_hd__or2_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__or2_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__or2_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/or2/sky130_fd_sc_hd__or2_2.gds",
        cellname="sky130_fd_sc_hd__or2_2",
    )


@cell
def sky130_fd_sc_hd__nand2_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__nand2_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nand2_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/nand2/sky130_fd_sc_hd__nand2_1.gds",
        cellname="sky130_fd_sc_hd__nand2_1",
    )


@cell
def sky130_fd_sc_hd__nand2_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__nand2_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nand2_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/nand2/sky130_fd_sc_hd__nand2_4.gds",
        cellname="sky130_fd_sc_hd__nand2_4",
    )


@cell
def sky130_fd_sc_hd__nand2_8() -> gf.Component:
    """Returns sky130_fd_sc_hd__nand2_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nand2_8()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/nand2/sky130_fd_sc_hd__nand2_8.gds",
        cellname="sky130_fd_sc_hd__nand2_8",
    )


@cell
def sky130_fd_sc_hd__nand2_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__nand2_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nand2_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/nand2/sky130_fd_sc_hd__nand2_2.gds",
        cellname="sky130_fd_sc_hd__nand2_2",
    )


@cell
def sky130_fd_sc_hd__decap_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__decap_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__decap_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/decap/sky130_fd_sc_hd__decap_4.gds",
        cellname="sky130_fd_sc_hd__decap_4",
    )


@cell
def sky130_fd_sc_hd__decap_12() -> gf.Component:
    """Returns sky130_fd_sc_hd__decap_12 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__decap_12()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/decap/sky130_fd_sc_hd__decap_12.gds",
        cellname="sky130_fd_sc_hd__decap_12",
    )


@cell
def sky130_fd_sc_hd__decap_3() -> gf.Component:
    """Returns sky130_fd_sc_hd__decap_3 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__decap_3()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/decap/sky130_fd_sc_hd__decap_3.gds",
        cellname="sky130_fd_sc_hd__decap_3",
    )


@cell
def sky130_fd_sc_hd__decap_6() -> gf.Component:
    """Returns sky130_fd_sc_hd__decap_6 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__decap_6()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/decap/sky130_fd_sc_hd__decap_6.gds",
        cellname="sky130_fd_sc_hd__decap_6",
    )


@cell
def sky130_fd_sc_hd__decap_8() -> gf.Component:
    """Returns sky130_fd_sc_hd__decap_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__decap_8()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/decap/sky130_fd_sc_hd__decap_8.gds",
        cellname="sky130_fd_sc_hd__decap_8",
    )


@cell
def sky130_fd_sc_hd__dfxbp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dfxbp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dfxbp_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/dfxbp/sky130_fd_sc_hd__dfxbp_1.gds",
        cellname="sky130_fd_sc_hd__dfxbp_1",
    )


@cell
def sky130_fd_sc_hd__dfxbp_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__dfxbp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dfxbp_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/dfxbp/sky130_fd_sc_hd__dfxbp_2.gds",
        cellname="sky130_fd_sc_hd__dfxbp_2",
    )


@cell
def sky130_fd_sc_hd__nor3_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__nor3_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nor3_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/nor3/sky130_fd_sc_hd__nor3_2.gds",
        cellname="sky130_fd_sc_hd__nor3_2",
    )


@cell
def sky130_fd_sc_hd__nor3_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__nor3_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nor3_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/nor3/sky130_fd_sc_hd__nor3_4.gds",
        cellname="sky130_fd_sc_hd__nor3_4",
    )


@cell
def sky130_fd_sc_hd__nor3_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__nor3_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nor3_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/nor3/sky130_fd_sc_hd__nor3_1.gds",
        cellname="sky130_fd_sc_hd__nor3_1",
    )


@cell
def sky130_fd_sc_hd__and2_0() -> gf.Component:
    """Returns sky130_fd_sc_hd__and2_0 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__and2_0()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/and2/sky130_fd_sc_hd__and2_0.gds",
        cellname="sky130_fd_sc_hd__and2_0",
    )


@cell
def sky130_fd_sc_hd__and2_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__and2_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__and2_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/and2/sky130_fd_sc_hd__and2_4.gds",
        cellname="sky130_fd_sc_hd__and2_4",
    )


@cell
def sky130_fd_sc_hd__and2_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__and2_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__and2_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/and2/sky130_fd_sc_hd__and2_1.gds",
        cellname="sky130_fd_sc_hd__and2_1",
    )


@cell
def sky130_fd_sc_hd__and2_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__and2_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__and2_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/and2/sky130_fd_sc_hd__and2_2.gds",
        cellname="sky130_fd_sc_hd__and2_2",
    )


@cell
def sky130_fd_sc_hd__tapvgnd2_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__tapvgnd2_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__tapvgnd2_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/tapvgnd2/sky130_fd_sc_hd__tapvgnd2_1.gds",
        cellname="sky130_fd_sc_hd__tapvgnd2_1",
    )


@cell
def sky130_fd_sc_hd__o211a_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__o211a_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o211a_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o211a/sky130_fd_sc_hd__o211a_4.gds",
        cellname="sky130_fd_sc_hd__o211a_4",
    )


@cell
def sky130_fd_sc_hd__o211a_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__o211a_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o211a_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o211a/sky130_fd_sc_hd__o211a_2.gds",
        cellname="sky130_fd_sc_hd__o211a_2",
    )


@cell
def sky130_fd_sc_hd__o211a_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__o211a_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o211a_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o211a/sky130_fd_sc_hd__o211a_1.gds",
        cellname="sky130_fd_sc_hd__o211a_1",
    )


@cell
def sky130_fd_sc_hd__nand3b_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__nand3b_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nand3b_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/nand3b/sky130_fd_sc_hd__nand3b_1.gds",
        cellname="sky130_fd_sc_hd__nand3b_1",
    )


@cell
def sky130_fd_sc_hd__nand3b_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__nand3b_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nand3b_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/nand3b/sky130_fd_sc_hd__nand3b_4.gds",
        cellname="sky130_fd_sc_hd__nand3b_4",
    )


@cell
def sky130_fd_sc_hd__nand3b_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__nand3b_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nand3b_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/nand3b/sky130_fd_sc_hd__nand3b_2.gds",
        cellname="sky130_fd_sc_hd__nand3b_2",
    )


@cell
def sky130_fd_sc_hd__and4b_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__and4b_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__and4b_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/and4b/sky130_fd_sc_hd__and4b_4.gds",
        cellname="sky130_fd_sc_hd__and4b_4",
    )


@cell
def sky130_fd_sc_hd__and4b_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__and4b_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__and4b_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/and4b/sky130_fd_sc_hd__and4b_1.gds",
        cellname="sky130_fd_sc_hd__and4b_1",
    )


@cell
def sky130_fd_sc_hd__and4b_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__and4b_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__and4b_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/and4b/sky130_fd_sc_hd__and4b_2.gds",
        cellname="sky130_fd_sc_hd__and4b_2",
    )


@cell
def sky130_fd_sc_hd__o2bb2ai_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__o2bb2ai_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o2bb2ai_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o2bb2ai/sky130_fd_sc_hd__o2bb2ai_4.gds",
        cellname="sky130_fd_sc_hd__o2bb2ai_4",
    )


@cell
def sky130_fd_sc_hd__o2bb2ai_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__o2bb2ai_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o2bb2ai_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o2bb2ai/sky130_fd_sc_hd__o2bb2ai_2.gds",
        cellname="sky130_fd_sc_hd__o2bb2ai_2",
    )


@cell
def sky130_fd_sc_hd__o2bb2ai_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__o2bb2ai_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o2bb2ai_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o2bb2ai/sky130_fd_sc_hd__o2bb2ai_1.gds",
        cellname="sky130_fd_sc_hd__o2bb2ai_1",
    )


@cell
def sky130_fd_sc_hd__a21o_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__a21o_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a21o_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a21o/sky130_fd_sc_hd__a21o_4.gds",
        cellname="sky130_fd_sc_hd__a21o_4",
    )


@cell
def sky130_fd_sc_hd__a21o_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__a21o_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a21o_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a21o/sky130_fd_sc_hd__a21o_2.gds",
        cellname="sky130_fd_sc_hd__a21o_2",
    )


@cell
def sky130_fd_sc_hd__a21o_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a21o_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a21o_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a21o/sky130_fd_sc_hd__a21o_1.gds",
        cellname="sky130_fd_sc_hd__a21o_1",
    )


@cell
def sky130_fd_sc_hd__lpflow_isobufsrckapwr_16() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_isobufsrckapwr_16 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_isobufsrckapwr_16()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/lpflow_isobufsrckapwr/sky130_fd_sc_hd__lpflow_isobufsrckapwr_16.gds",
        cellname="sky130_fd_sc_hd__lpflow_isobufsrckapwr_16",
    )


@cell
def sky130_fd_sc_hd__o22ai_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__o22ai_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o22ai_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o22ai/sky130_fd_sc_hd__o22ai_4.gds",
        cellname="sky130_fd_sc_hd__o22ai_4",
    )


@cell
def sky130_fd_sc_hd__o22ai_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__o22ai_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o22ai_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o22ai/sky130_fd_sc_hd__o22ai_2.gds",
        cellname="sky130_fd_sc_hd__o22ai_2",
    )


@cell
def sky130_fd_sc_hd__o22ai_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__o22ai_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o22ai_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o22ai/sky130_fd_sc_hd__o22ai_1.gds",
        cellname="sky130_fd_sc_hd__o22ai_1",
    )


@cell
def sky130_fd_sc_hd__sdfstp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__sdfstp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sdfstp_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/sdfstp/sky130_fd_sc_hd__sdfstp_1.gds",
        cellname="sky130_fd_sc_hd__sdfstp_1",
    )


@cell
def sky130_fd_sc_hd__sdfstp_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__sdfstp_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sdfstp_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/sdfstp/sky130_fd_sc_hd__sdfstp_4.gds",
        cellname="sky130_fd_sc_hd__sdfstp_4",
    )


@cell
def sky130_fd_sc_hd__sdfstp_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__sdfstp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sdfstp_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/sdfstp/sky130_fd_sc_hd__sdfstp_2.gds",
        cellname="sky130_fd_sc_hd__sdfstp_2",
    )


@cell
def sky130_fd_sc_hd__inv_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__inv_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__inv_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/inv/sky130_fd_sc_hd__inv_2.gds",
        cellname="sky130_fd_sc_hd__inv_2",
    )


@cell
def sky130_fd_sc_hd__inv_12() -> gf.Component:
    """Returns sky130_fd_sc_hd__inv_12 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__inv_12()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/inv/sky130_fd_sc_hd__inv_12.gds",
        cellname="sky130_fd_sc_hd__inv_12",
    )


@cell
def sky130_fd_sc_hd__inv_6() -> gf.Component:
    """Returns sky130_fd_sc_hd__inv_6 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__inv_6()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/inv/sky130_fd_sc_hd__inv_6.gds",
        cellname="sky130_fd_sc_hd__inv_6",
    )


@cell
def sky130_fd_sc_hd__inv_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__inv_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__inv_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/inv/sky130_fd_sc_hd__inv_4.gds",
        cellname="sky130_fd_sc_hd__inv_4",
    )


@cell
def sky130_fd_sc_hd__inv_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__inv_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__inv_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/inv/sky130_fd_sc_hd__inv_1.gds",
        cellname="sky130_fd_sc_hd__inv_1",
    )


@cell
def sky130_fd_sc_hd__inv_16() -> gf.Component:
    """Returns sky130_fd_sc_hd__inv_16 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__inv_16()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/inv/sky130_fd_sc_hd__inv_16.gds",
        cellname="sky130_fd_sc_hd__inv_16",
    )


@cell
def sky130_fd_sc_hd__inv_8() -> gf.Component:
    """Returns sky130_fd_sc_hd__inv_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__inv_8()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/inv/sky130_fd_sc_hd__inv_8.gds",
        cellname="sky130_fd_sc_hd__inv_8",
    )


@cell
def sky130_fd_sc_hd__einvp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__einvp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__einvp_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/einvp/sky130_fd_sc_hd__einvp_1.gds",
        cellname="sky130_fd_sc_hd__einvp_1",
    )


@cell
def sky130_fd_sc_hd__einvp_8() -> gf.Component:
    """Returns sky130_fd_sc_hd__einvp_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__einvp_8()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/einvp/sky130_fd_sc_hd__einvp_8.gds",
        cellname="sky130_fd_sc_hd__einvp_8",
    )


@cell
def sky130_fd_sc_hd__einvp_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__einvp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__einvp_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/einvp/sky130_fd_sc_hd__einvp_2.gds",
        cellname="sky130_fd_sc_hd__einvp_2",
    )


@cell
def sky130_fd_sc_hd__einvp_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__einvp_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__einvp_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/einvp/sky130_fd_sc_hd__einvp_4.gds",
        cellname="sky130_fd_sc_hd__einvp_4",
    )


@cell
def sky130_fd_sc_hd__o22a_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__o22a_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o22a_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o22a/sky130_fd_sc_hd__o22a_2.gds",
        cellname="sky130_fd_sc_hd__o22a_2",
    )


@cell
def sky130_fd_sc_hd__o22a_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__o22a_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o22a_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o22a/sky130_fd_sc_hd__o22a_1.gds",
        cellname="sky130_fd_sc_hd__o22a_1",
    )


@cell
def sky130_fd_sc_hd__o22a_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__o22a_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o22a_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o22a/sky130_fd_sc_hd__o22a_4.gds",
        cellname="sky130_fd_sc_hd__o22a_4",
    )


@cell
def sky130_fd_sc_hd__or3b_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__or3b_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__or3b_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/or3b/sky130_fd_sc_hd__or3b_4.gds",
        cellname="sky130_fd_sc_hd__or3b_4",
    )


@cell
def sky130_fd_sc_hd__or3b_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__or3b_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__or3b_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/or3b/sky130_fd_sc_hd__or3b_2.gds",
        cellname="sky130_fd_sc_hd__or3b_2",
    )


@cell
def sky130_fd_sc_hd__or3b_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__or3b_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__or3b_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/or3b/sky130_fd_sc_hd__or3b_1.gds",
        cellname="sky130_fd_sc_hd__or3b_1",
    )


@cell
def sky130_fd_sc_hd__a41oi_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__a41oi_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a41oi_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a41oi/sky130_fd_sc_hd__a41oi_2.gds",
        cellname="sky130_fd_sc_hd__a41oi_2",
    )


@cell
def sky130_fd_sc_hd__a41oi_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a41oi_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a41oi_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a41oi/sky130_fd_sc_hd__a41oi_1.gds",
        cellname="sky130_fd_sc_hd__a41oi_1",
    )


@cell
def sky130_fd_sc_hd__a41oi_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__a41oi_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a41oi_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a41oi/sky130_fd_sc_hd__a41oi_4.gds",
        cellname="sky130_fd_sc_hd__a41oi_4",
    )


@cell
def sky130_fd_sc_hd__nand4_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__nand4_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nand4_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/nand4/sky130_fd_sc_hd__nand4_2.gds",
        cellname="sky130_fd_sc_hd__nand4_2",
    )


@cell
def sky130_fd_sc_hd__nand4_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__nand4_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nand4_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/nand4/sky130_fd_sc_hd__nand4_1.gds",
        cellname="sky130_fd_sc_hd__nand4_1",
    )


@cell
def sky130_fd_sc_hd__nand4_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__nand4_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nand4_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/nand4/sky130_fd_sc_hd__nand4_4.gds",
        cellname="sky130_fd_sc_hd__nand4_4",
    )


@cell
def sky130_fd_sc_hd__o221a_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__o221a_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o221a_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o221a/sky130_fd_sc_hd__o221a_4.gds",
        cellname="sky130_fd_sc_hd__o221a_4",
    )


@cell
def sky130_fd_sc_hd__o221a_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__o221a_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o221a_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o221a/sky130_fd_sc_hd__o221a_1.gds",
        cellname="sky130_fd_sc_hd__o221a_1",
    )


@cell
def sky130_fd_sc_hd__o221a_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__o221a_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o221a_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o221a/sky130_fd_sc_hd__o221a_2.gds",
        cellname="sky130_fd_sc_hd__o221a_2",
    )


@cell
def sky130_fd_sc_hd__a221oi_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__a221oi_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a221oi_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a221oi/sky130_fd_sc_hd__a221oi_4.gds",
        cellname="sky130_fd_sc_hd__a221oi_4",
    )


@cell
def sky130_fd_sc_hd__a221oi_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__a221oi_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a221oi_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a221oi/sky130_fd_sc_hd__a221oi_2.gds",
        cellname="sky130_fd_sc_hd__a221oi_2",
    )


@cell
def sky130_fd_sc_hd__a221oi_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a221oi_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a221oi_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a221oi/sky130_fd_sc_hd__a221oi_1.gds",
        cellname="sky130_fd_sc_hd__a221oi_1",
    )


@cell
def sky130_fd_sc_hd__or3_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__or3_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__or3_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/or3/sky130_fd_sc_hd__or3_1.gds",
        cellname="sky130_fd_sc_hd__or3_1",
    )


@cell
def sky130_fd_sc_hd__or3_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__or3_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__or3_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/or3/sky130_fd_sc_hd__or3_4.gds",
        cellname="sky130_fd_sc_hd__or3_4",
    )


@cell
def sky130_fd_sc_hd__or3_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__or3_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__or3_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/or3/sky130_fd_sc_hd__or3_2.gds",
        cellname="sky130_fd_sc_hd__or3_2",
    )


@cell
def sky130_fd_sc_hd__o311a_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__o311a_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o311a_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o311a/sky130_fd_sc_hd__o311a_1.gds",
        cellname="sky130_fd_sc_hd__o311a_1",
    )


@cell
def sky130_fd_sc_hd__o311a_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__o311a_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o311a_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o311a/sky130_fd_sc_hd__o311a_4.gds",
        cellname="sky130_fd_sc_hd__o311a_4",
    )


@cell
def sky130_fd_sc_hd__o311a_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__o311a_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o311a_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o311a/sky130_fd_sc_hd__o311a_2.gds",
        cellname="sky130_fd_sc_hd__o311a_2",
    )


@cell
def sky130_fd_sc_hd__o32ai_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__o32ai_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o32ai_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o32ai/sky130_fd_sc_hd__o32ai_4.gds",
        cellname="sky130_fd_sc_hd__o32ai_4",
    )


@cell
def sky130_fd_sc_hd__o32ai_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__o32ai_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o32ai_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o32ai/sky130_fd_sc_hd__o32ai_1.gds",
        cellname="sky130_fd_sc_hd__o32ai_1",
    )


@cell
def sky130_fd_sc_hd__o32ai_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__o32ai_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o32ai_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o32ai/sky130_fd_sc_hd__o32ai_2.gds",
        cellname="sky130_fd_sc_hd__o32ai_2",
    )


@cell
def sky130_fd_sc_hd__dfstp_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__dfstp_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dfstp_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/dfstp/sky130_fd_sc_hd__dfstp_4.gds",
        cellname="sky130_fd_sc_hd__dfstp_4",
    )


@cell
def sky130_fd_sc_hd__dfstp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dfstp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dfstp_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/dfstp/sky130_fd_sc_hd__dfstp_1.gds",
        cellname="sky130_fd_sc_hd__dfstp_1",
    )


@cell
def sky130_fd_sc_hd__dfstp_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__dfstp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dfstp_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/dfstp/sky130_fd_sc_hd__dfstp_2.gds",
        cellname="sky130_fd_sc_hd__dfstp_2",
    )


@cell
def sky130_fd_sc_hd__xor3_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__xor3_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__xor3_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/xor3/sky130_fd_sc_hd__xor3_2.gds",
        cellname="sky130_fd_sc_hd__xor3_2",
    )


@cell
def sky130_fd_sc_hd__xor3_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__xor3_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__xor3_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/xor3/sky130_fd_sc_hd__xor3_4.gds",
        cellname="sky130_fd_sc_hd__xor3_4",
    )


@cell
def sky130_fd_sc_hd__xor3_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__xor3_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__xor3_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/xor3/sky130_fd_sc_hd__xor3_1.gds",
        cellname="sky130_fd_sc_hd__xor3_1",
    )


@cell
def sky130_fd_sc_hd__dlymetal6s2s_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlymetal6s2s_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlymetal6s2s_1()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/dlymetal6s2s/sky130_fd_sc_hd__dlymetal6s2s_1.gds",
        cellname="sky130_fd_sc_hd__dlymetal6s2s_1",
    )


@cell
def sky130_fd_sc_hd__probec_p_8() -> gf.Component:
    """Returns sky130_fd_sc_hd__probec_p_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__probec_p_8()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/probec_p/sky130_fd_sc_hd__probec_p_8.gds",
        cellname="sky130_fd_sc_hd__probec_p_8",
    )


@cell
def sky130_fd_sc_hd__nand3_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__nand3_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nand3_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/nand3/sky130_fd_sc_hd__nand3_2.gds",
        cellname="sky130_fd_sc_hd__nand3_2",
    )


@cell
def sky130_fd_sc_hd__nand3_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__nand3_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nand3_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/nand3/sky130_fd_sc_hd__nand3_1.gds",
        cellname="sky130_fd_sc_hd__nand3_1",
    )


@cell
def sky130_fd_sc_hd__nand3_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__nand3_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nand3_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/nand3/sky130_fd_sc_hd__nand3_4.gds",
        cellname="sky130_fd_sc_hd__nand3_4",
    )


@cell
def sky130_fd_sc_hd__sdfxbp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__sdfxbp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sdfxbp_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/sdfxbp/sky130_fd_sc_hd__sdfxbp_1.gds",
        cellname="sky130_fd_sc_hd__sdfxbp_1",
    )


@cell
def sky130_fd_sc_hd__sdfxbp_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__sdfxbp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sdfxbp_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/sdfxbp/sky130_fd_sc_hd__sdfxbp_2.gds",
        cellname="sky130_fd_sc_hd__sdfxbp_2",
    )


@cell
def sky130_fd_sc_hd__nand4bb_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__nand4bb_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nand4bb_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/nand4bb/sky130_fd_sc_hd__nand4bb_1.gds",
        cellname="sky130_fd_sc_hd__nand4bb_1",
    )


@cell
def sky130_fd_sc_hd__nand4bb_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__nand4bb_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nand4bb_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/nand4bb/sky130_fd_sc_hd__nand4bb_2.gds",
        cellname="sky130_fd_sc_hd__nand4bb_2",
    )


@cell
def sky130_fd_sc_hd__nand4bb_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__nand4bb_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nand4bb_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/nand4bb/sky130_fd_sc_hd__nand4bb_4.gds",
        cellname="sky130_fd_sc_hd__nand4bb_4",
    )


@cell
def sky130_fd_sc_hd__o21a_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__o21a_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o21a_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o21a/sky130_fd_sc_hd__o21a_1.gds",
        cellname="sky130_fd_sc_hd__o21a_1",
    )


@cell
def sky130_fd_sc_hd__o21a_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__o21a_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o21a_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o21a/sky130_fd_sc_hd__o21a_2.gds",
        cellname="sky130_fd_sc_hd__o21a_2",
    )


@cell
def sky130_fd_sc_hd__o21a_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__o21a_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o21a_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/o21a/sky130_fd_sc_hd__o21a_4.gds",
        cellname="sky130_fd_sc_hd__o21a_4",
    )


@cell
def sky130_fd_sc_hd__mux4_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__mux4_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__mux4_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/mux4/sky130_fd_sc_hd__mux4_1.gds",
        cellname="sky130_fd_sc_hd__mux4_1",
    )


@cell
def sky130_fd_sc_hd__mux4_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__mux4_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__mux4_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/mux4/sky130_fd_sc_hd__mux4_2.gds",
        cellname="sky130_fd_sc_hd__mux4_2",
    )


@cell
def sky130_fd_sc_hd__mux4_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__mux4_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__mux4_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/mux4/sky130_fd_sc_hd__mux4_4.gds",
        cellname="sky130_fd_sc_hd__mux4_4",
    )


@cell
def sky130_fd_sc_hd__xor2_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__xor2_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__xor2_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/xor2/sky130_fd_sc_hd__xor2_2.gds",
        cellname="sky130_fd_sc_hd__xor2_2",
    )


@cell
def sky130_fd_sc_hd__xor2_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__xor2_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__xor2_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/xor2/sky130_fd_sc_hd__xor2_1.gds",
        cellname="sky130_fd_sc_hd__xor2_1",
    )


@cell
def sky130_fd_sc_hd__xor2_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__xor2_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__xor2_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/xor2/sky130_fd_sc_hd__xor2_4.gds",
        cellname="sky130_fd_sc_hd__xor2_4",
    )


@cell
def sky130_fd_sc_hd__dlclkp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlclkp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlclkp_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/dlclkp/sky130_fd_sc_hd__dlclkp_1.gds",
        cellname="sky130_fd_sc_hd__dlclkp_1",
    )


@cell
def sky130_fd_sc_hd__dlclkp_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlclkp_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlclkp_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/dlclkp/sky130_fd_sc_hd__dlclkp_4.gds",
        cellname="sky130_fd_sc_hd__dlclkp_4",
    )


@cell
def sky130_fd_sc_hd__dlclkp_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlclkp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlclkp_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/dlclkp/sky130_fd_sc_hd__dlclkp_2.gds",
        cellname="sky130_fd_sc_hd__dlclkp_2",
    )


@cell
def sky130_fd_sc_hd__sedfxtp_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__sedfxtp_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sedfxtp_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/sedfxtp/sky130_fd_sc_hd__sedfxtp_4.gds",
        cellname="sky130_fd_sc_hd__sedfxtp_4",
    )


@cell
def sky130_fd_sc_hd__sedfxtp_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__sedfxtp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sedfxtp_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/sedfxtp/sky130_fd_sc_hd__sedfxtp_2.gds",
        cellname="sky130_fd_sc_hd__sedfxtp_2",
    )


@cell
def sky130_fd_sc_hd__sedfxtp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__sedfxtp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sedfxtp_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/sedfxtp/sky130_fd_sc_hd__sedfxtp_1.gds",
        cellname="sky130_fd_sc_hd__sedfxtp_1",
    )


@cell
def sky130_fd_sc_hd__lpflow_decapkapwr_6() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_decapkapwr_6 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_decapkapwr_6()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/lpflow_decapkapwr/sky130_fd_sc_hd__lpflow_decapkapwr_6.gds",
        cellname="sky130_fd_sc_hd__lpflow_decapkapwr_6",
    )


@cell
def sky130_fd_sc_hd__lpflow_decapkapwr_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_decapkapwr_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_decapkapwr_4()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/lpflow_decapkapwr/sky130_fd_sc_hd__lpflow_decapkapwr_4.gds",
        cellname="sky130_fd_sc_hd__lpflow_decapkapwr_4",
    )


@cell
def sky130_fd_sc_hd__lpflow_decapkapwr_8() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_decapkapwr_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_decapkapwr_8()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/lpflow_decapkapwr/sky130_fd_sc_hd__lpflow_decapkapwr_8.gds",
        cellname="sky130_fd_sc_hd__lpflow_decapkapwr_8",
    )


@cell
def sky130_fd_sc_hd__lpflow_decapkapwr_12() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_decapkapwr_12 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_decapkapwr_12()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/lpflow_decapkapwr/sky130_fd_sc_hd__lpflow_decapkapwr_12.gds",
        cellname="sky130_fd_sc_hd__lpflow_decapkapwr_12",
    )


@cell
def sky130_fd_sc_hd__lpflow_decapkapwr_3() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_decapkapwr_3 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_decapkapwr_3()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/lpflow_decapkapwr/sky130_fd_sc_hd__lpflow_decapkapwr_3.gds",
        cellname="sky130_fd_sc_hd__lpflow_decapkapwr_3",
    )


@cell
def sky130_fd_sc_hd__or2b_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__or2b_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__or2b_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/or2b/sky130_fd_sc_hd__or2b_1.gds",
        cellname="sky130_fd_sc_hd__or2b_1",
    )


@cell
def sky130_fd_sc_hd__or2b_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__or2b_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__or2b_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/or2b/sky130_fd_sc_hd__or2b_4.gds",
        cellname="sky130_fd_sc_hd__or2b_4",
    )


@cell
def sky130_fd_sc_hd__or2b_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__or2b_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__or2b_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/or2b/sky130_fd_sc_hd__or2b_2.gds",
        cellname="sky130_fd_sc_hd__or2b_2",
    )


@cell
def sky130_fd_sc_hd__clkbuf_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__clkbuf_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__clkbuf_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/clkbuf/sky130_fd_sc_hd__clkbuf_4.gds",
        cellname="sky130_fd_sc_hd__clkbuf_4",
    )


@cell
def sky130_fd_sc_hd__clkbuf_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__clkbuf_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__clkbuf_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/clkbuf/sky130_fd_sc_hd__clkbuf_1.gds",
        cellname="sky130_fd_sc_hd__clkbuf_1",
    )


@cell
def sky130_fd_sc_hd__clkbuf_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__clkbuf_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__clkbuf_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/clkbuf/sky130_fd_sc_hd__clkbuf_2.gds",
        cellname="sky130_fd_sc_hd__clkbuf_2",
    )


@cell
def sky130_fd_sc_hd__clkbuf_16() -> gf.Component:
    """Returns sky130_fd_sc_hd__clkbuf_16 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__clkbuf_16()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/clkbuf/sky130_fd_sc_hd__clkbuf_16.gds",
        cellname="sky130_fd_sc_hd__clkbuf_16",
    )


@cell
def sky130_fd_sc_hd__clkbuf_8() -> gf.Component:
    """Returns sky130_fd_sc_hd__clkbuf_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__clkbuf_8()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/clkbuf/sky130_fd_sc_hd__clkbuf_8.gds",
        cellname="sky130_fd_sc_hd__clkbuf_8",
    )


@cell
def sky130_fd_sc_hd__dlrbn_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlrbn_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlrbn_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/dlrbn/sky130_fd_sc_hd__dlrbn_1.gds",
        cellname="sky130_fd_sc_hd__dlrbn_1",
    )


@cell
def sky130_fd_sc_hd__dlrbn_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlrbn_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlrbn_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/dlrbn/sky130_fd_sc_hd__dlrbn_2.gds",
        cellname="sky130_fd_sc_hd__dlrbn_2",
    )


@cell
def sky130_fd_sc_hd__lpflow_bleeder_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_bleeder_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_bleeder_1()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/lpflow_bleeder/sky130_fd_sc_hd__lpflow_bleeder_1.gds",
        cellname="sky130_fd_sc_hd__lpflow_bleeder_1",
    )


@cell
def sky130_fd_sc_hd__dfxtp_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__dfxtp_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dfxtp_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/dfxtp/sky130_fd_sc_hd__dfxtp_4.gds",
        cellname="sky130_fd_sc_hd__dfxtp_4",
    )


@cell
def sky130_fd_sc_hd__dfxtp_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__dfxtp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dfxtp_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/dfxtp/sky130_fd_sc_hd__dfxtp_2.gds",
        cellname="sky130_fd_sc_hd__dfxtp_2",
    )


@cell
def sky130_fd_sc_hd__dfxtp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dfxtp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dfxtp_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/dfxtp/sky130_fd_sc_hd__dfxtp_1.gds",
        cellname="sky130_fd_sc_hd__dfxtp_1",
    )


@cell
def sky130_fd_sc_hd__or4_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__or4_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__or4_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/or4/sky130_fd_sc_hd__or4_2.gds",
        cellname="sky130_fd_sc_hd__or4_2",
    )


@cell
def sky130_fd_sc_hd__or4_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__or4_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__or4_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/or4/sky130_fd_sc_hd__or4_1.gds",
        cellname="sky130_fd_sc_hd__or4_1",
    )


@cell
def sky130_fd_sc_hd__or4_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__or4_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__or4_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/or4/sky130_fd_sc_hd__or4_4.gds",
        cellname="sky130_fd_sc_hd__or4_4",
    )


@cell
def sky130_fd_sc_hd__a21bo_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__a21bo_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a21bo_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a21bo/sky130_fd_sc_hd__a21bo_4.gds",
        cellname="sky130_fd_sc_hd__a21bo_4",
    )


@cell
def sky130_fd_sc_hd__a21bo_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__a21bo_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a21bo_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a21bo/sky130_fd_sc_hd__a21bo_2.gds",
        cellname="sky130_fd_sc_hd__a21bo_2",
    )


@cell
def sky130_fd_sc_hd__a21bo_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a21bo_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a21bo_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a21bo/sky130_fd_sc_hd__a21bo_1.gds",
        cellname="sky130_fd_sc_hd__a21bo_1",
    )


@cell
def sky130_fd_sc_hd__dlymetal6s6s_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlymetal6s6s_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlymetal6s6s_1()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/dlymetal6s6s/sky130_fd_sc_hd__dlymetal6s6s_1.gds",
        cellname="sky130_fd_sc_hd__dlymetal6s6s_1",
    )


@cell
def sky130_fd_sc_hd__fahcin_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__fahcin_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__fahcin_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/fahcin/sky130_fd_sc_hd__fahcin_1.gds",
        cellname="sky130_fd_sc_hd__fahcin_1",
    )


@cell
def sky130_fd_sc_hd__dfrtn_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dfrtn_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dfrtn_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/dfrtn/sky130_fd_sc_hd__dfrtn_1.gds",
        cellname="sky130_fd_sc_hd__dfrtn_1",
    )


@cell
def sky130_fd_sc_hd__mux2i_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__mux2i_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__mux2i_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/mux2i/sky130_fd_sc_hd__mux2i_1.gds",
        cellname="sky130_fd_sc_hd__mux2i_1",
    )


@cell
def sky130_fd_sc_hd__mux2i_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__mux2i_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__mux2i_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/mux2i/sky130_fd_sc_hd__mux2i_4.gds",
        cellname="sky130_fd_sc_hd__mux2i_4",
    )


@cell
def sky130_fd_sc_hd__mux2i_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__mux2i_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__mux2i_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/mux2i/sky130_fd_sc_hd__mux2i_2.gds",
        cellname="sky130_fd_sc_hd__mux2i_2",
    )


@cell
def sky130_fd_sc_hd__a2bb2oi_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a2bb2oi_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a2bb2oi_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a2bb2oi/sky130_fd_sc_hd__a2bb2oi_1.gds",
        cellname="sky130_fd_sc_hd__a2bb2oi_1",
    )


@cell
def sky130_fd_sc_hd__a2bb2oi_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__a2bb2oi_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a2bb2oi_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a2bb2oi/sky130_fd_sc_hd__a2bb2oi_4.gds",
        cellname="sky130_fd_sc_hd__a2bb2oi_4",
    )


@cell
def sky130_fd_sc_hd__a2bb2oi_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__a2bb2oi_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a2bb2oi_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a2bb2oi/sky130_fd_sc_hd__a2bb2oi_2.gds",
        cellname="sky130_fd_sc_hd__a2bb2oi_2",
    )


@cell
def sky130_fd_sc_hd__a41o_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__a41o_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a41o_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a41o/sky130_fd_sc_hd__a41o_4.gds",
        cellname="sky130_fd_sc_hd__a41o_4",
    )


@cell
def sky130_fd_sc_hd__a41o_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a41o_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a41o_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a41o/sky130_fd_sc_hd__a41o_1.gds",
        cellname="sky130_fd_sc_hd__a41o_1",
    )


@cell
def sky130_fd_sc_hd__a41o_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__a41o_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a41o_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a41o/sky130_fd_sc_hd__a41o_2.gds",
        cellname="sky130_fd_sc_hd__a41o_2",
    )


@cell
def sky130_fd_sc_hd__fahcon_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__fahcon_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__fahcon_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/fahcon/sky130_fd_sc_hd__fahcon_1.gds",
        cellname="sky130_fd_sc_hd__fahcon_1",
    )


@cell
def sky130_fd_sc_hd__a21boi_0() -> gf.Component:
    """Returns sky130_fd_sc_hd__a21boi_0 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a21boi_0()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a21boi/sky130_fd_sc_hd__a21boi_0.gds",
        cellname="sky130_fd_sc_hd__a21boi_0",
    )


@cell
def sky130_fd_sc_hd__a21boi_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__a21boi_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a21boi_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a21boi/sky130_fd_sc_hd__a21boi_2.gds",
        cellname="sky130_fd_sc_hd__a21boi_2",
    )


@cell
def sky130_fd_sc_hd__a21boi_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a21boi_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a21boi_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a21boi/sky130_fd_sc_hd__a21boi_1.gds",
        cellname="sky130_fd_sc_hd__a21boi_1",
    )


@cell
def sky130_fd_sc_hd__a21boi_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__a21boi_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a21boi_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a21boi/sky130_fd_sc_hd__a21boi_4.gds",
        cellname="sky130_fd_sc_hd__a21boi_4",
    )


@cell
def sky130_fd_sc_hd__xnor2_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__xnor2_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__xnor2_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/xnor2/sky130_fd_sc_hd__xnor2_2.gds",
        cellname="sky130_fd_sc_hd__xnor2_2",
    )


@cell
def sky130_fd_sc_hd__xnor2_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__xnor2_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__xnor2_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/xnor2/sky130_fd_sc_hd__xnor2_1.gds",
        cellname="sky130_fd_sc_hd__xnor2_1",
    )


@cell
def sky130_fd_sc_hd__xnor2_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__xnor2_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__xnor2_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/xnor2/sky130_fd_sc_hd__xnor2_4.gds",
        cellname="sky130_fd_sc_hd__xnor2_4",
    )


@cell
def sky130_fd_sc_hd__nor4bb_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__nor4bb_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nor4bb_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/nor4bb/sky130_fd_sc_hd__nor4bb_1.gds",
        cellname="sky130_fd_sc_hd__nor4bb_1",
    )


@cell
def sky130_fd_sc_hd__nor4bb_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__nor4bb_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nor4bb_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/nor4bb/sky130_fd_sc_hd__nor4bb_2.gds",
        cellname="sky130_fd_sc_hd__nor4bb_2",
    )


@cell
def sky130_fd_sc_hd__nor4bb_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__nor4bb_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nor4bb_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/nor4bb/sky130_fd_sc_hd__nor4bb_4.gds",
        cellname="sky130_fd_sc_hd__nor4bb_4",
    )


@cell
def sky130_fd_sc_hd__xnor3_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__xnor3_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__xnor3_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/xnor3/sky130_fd_sc_hd__xnor3_1.gds",
        cellname="sky130_fd_sc_hd__xnor3_1",
    )


@cell
def sky130_fd_sc_hd__xnor3_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__xnor3_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__xnor3_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/xnor3/sky130_fd_sc_hd__xnor3_2.gds",
        cellname="sky130_fd_sc_hd__xnor3_2",
    )


@cell
def sky130_fd_sc_hd__xnor3_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__xnor3_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__xnor3_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/xnor3/sky130_fd_sc_hd__xnor3_4.gds",
        cellname="sky130_fd_sc_hd__xnor3_4",
    )


@cell
def sky130_fd_sc_hd__nor4b_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__nor4b_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nor4b_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/nor4b/sky130_fd_sc_hd__nor4b_4.gds",
        cellname="sky130_fd_sc_hd__nor4b_4",
    )


@cell
def sky130_fd_sc_hd__nor4b_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__nor4b_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nor4b_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/nor4b/sky130_fd_sc_hd__nor4b_2.gds",
        cellname="sky130_fd_sc_hd__nor4b_2",
    )


@cell
def sky130_fd_sc_hd__nor4b_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__nor4b_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nor4b_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/nor4b/sky130_fd_sc_hd__nor4b_1.gds",
        cellname="sky130_fd_sc_hd__nor4b_1",
    )


@cell
def sky130_fd_sc_hd__a2111o_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a2111o_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a2111o_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a2111o/sky130_fd_sc_hd__a2111o_1.gds",
        cellname="sky130_fd_sc_hd__a2111o_1",
    )


@cell
def sky130_fd_sc_hd__a2111o_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__a2111o_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a2111o_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a2111o/sky130_fd_sc_hd__a2111o_2.gds",
        cellname="sky130_fd_sc_hd__a2111o_2",
    )


@cell
def sky130_fd_sc_hd__a2111o_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__a2111o_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a2111o_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a2111o/sky130_fd_sc_hd__a2111o_4.gds",
        cellname="sky130_fd_sc_hd__a2111o_4",
    )


@cell
def sky130_fd_sc_hd__fill_8() -> gf.Component:
    """Returns sky130_fd_sc_hd__fill_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__fill_8()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/fill/sky130_fd_sc_hd__fill_8.gds",
        cellname="sky130_fd_sc_hd__fill_8",
    )


@cell
def sky130_fd_sc_hd__fill_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__fill_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__fill_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/fill/sky130_fd_sc_hd__fill_4.gds",
        cellname="sky130_fd_sc_hd__fill_4",
    )


@cell
def sky130_fd_sc_hd__fill_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__fill_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__fill_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/fill/sky130_fd_sc_hd__fill_1.gds",
        cellname="sky130_fd_sc_hd__fill_1",
    )


@cell
def sky130_fd_sc_hd__fill_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__fill_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__fill_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/fill/sky130_fd_sc_hd__fill_2.gds",
        cellname="sky130_fd_sc_hd__fill_2",
    )


@cell
def sky130_fd_sc_hd__a22oi_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a22oi_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a22oi_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a22oi/sky130_fd_sc_hd__a22oi_1.gds",
        cellname="sky130_fd_sc_hd__a22oi_1",
    )


@cell
def sky130_fd_sc_hd__a22oi_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__a22oi_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a22oi_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a22oi/sky130_fd_sc_hd__a22oi_2.gds",
        cellname="sky130_fd_sc_hd__a22oi_2",
    )


@cell
def sky130_fd_sc_hd__a22oi_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__a22oi_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a22oi_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a22oi/sky130_fd_sc_hd__a22oi_4.gds",
        cellname="sky130_fd_sc_hd__a22oi_4",
    )


@cell
def sky130_fd_sc_hd__nor3b_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__nor3b_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nor3b_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/nor3b/sky130_fd_sc_hd__nor3b_1.gds",
        cellname="sky130_fd_sc_hd__nor3b_1",
    )


@cell
def sky130_fd_sc_hd__nor3b_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__nor3b_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nor3b_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/nor3b/sky130_fd_sc_hd__nor3b_2.gds",
        cellname="sky130_fd_sc_hd__nor3b_2",
    )


@cell
def sky130_fd_sc_hd__nor3b_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__nor3b_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nor3b_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/nor3b/sky130_fd_sc_hd__nor3b_4.gds",
        cellname="sky130_fd_sc_hd__nor3b_4",
    )


@cell
def sky130_fd_sc_hd__lpflow_clkinvkapwr_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_clkinvkapwr_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_clkinvkapwr_4()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/lpflow_clkinvkapwr/sky130_fd_sc_hd__lpflow_clkinvkapwr_4.gds",
        cellname="sky130_fd_sc_hd__lpflow_clkinvkapwr_4",
    )


@cell
def sky130_fd_sc_hd__lpflow_clkinvkapwr_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_clkinvkapwr_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_clkinvkapwr_1()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/lpflow_clkinvkapwr/sky130_fd_sc_hd__lpflow_clkinvkapwr_1.gds",
        cellname="sky130_fd_sc_hd__lpflow_clkinvkapwr_1",
    )


@cell
def sky130_fd_sc_hd__lpflow_clkinvkapwr_8() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_clkinvkapwr_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_clkinvkapwr_8()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/lpflow_clkinvkapwr/sky130_fd_sc_hd__lpflow_clkinvkapwr_8.gds",
        cellname="sky130_fd_sc_hd__lpflow_clkinvkapwr_8",
    )


@cell
def sky130_fd_sc_hd__lpflow_clkinvkapwr_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_clkinvkapwr_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_clkinvkapwr_2()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/lpflow_clkinvkapwr/sky130_fd_sc_hd__lpflow_clkinvkapwr_2.gds",
        cellname="sky130_fd_sc_hd__lpflow_clkinvkapwr_2",
    )


@cell
def sky130_fd_sc_hd__lpflow_clkinvkapwr_16() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_clkinvkapwr_16 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_clkinvkapwr_16()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/lpflow_clkinvkapwr/sky130_fd_sc_hd__lpflow_clkinvkapwr_16.gds",
        cellname="sky130_fd_sc_hd__lpflow_clkinvkapwr_16",
    )


@cell
def sky130_fd_sc_hd__clkdlybuf4s50_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__clkdlybuf4s50_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__clkdlybuf4s50_2()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/clkdlybuf4s50/sky130_fd_sc_hd__clkdlybuf4s50_2.gds",
        cellname="sky130_fd_sc_hd__clkdlybuf4s50_2",
    )


@cell
def sky130_fd_sc_hd__clkdlybuf4s50_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__clkdlybuf4s50_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__clkdlybuf4s50_1()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/clkdlybuf4s50/sky130_fd_sc_hd__clkdlybuf4s50_1.gds",
        cellname="sky130_fd_sc_hd__clkdlybuf4s50_1",
    )


@cell
def sky130_fd_sc_hd__a32oi_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__a32oi_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a32oi_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a32oi/sky130_fd_sc_hd__a32oi_2.gds",
        cellname="sky130_fd_sc_hd__a32oi_2",
    )


@cell
def sky130_fd_sc_hd__a32oi_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__a32oi_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a32oi_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a32oi/sky130_fd_sc_hd__a32oi_4.gds",
        cellname="sky130_fd_sc_hd__a32oi_4",
    )


@cell
def sky130_fd_sc_hd__a32oi_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a32oi_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a32oi_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/a32oi/sky130_fd_sc_hd__a32oi_1.gds",
        cellname="sky130_fd_sc_hd__a32oi_1",
    )


@cell
def sky130_fd_sc_hd__buf_8() -> gf.Component:
    """Returns sky130_fd_sc_hd__buf_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__buf_8()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/buf/sky130_fd_sc_hd__buf_8.gds",
        cellname="sky130_fd_sc_hd__buf_8",
    )


@cell
def sky130_fd_sc_hd__buf_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__buf_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__buf_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/buf/sky130_fd_sc_hd__buf_1.gds",
        cellname="sky130_fd_sc_hd__buf_1",
    )


@cell
def sky130_fd_sc_hd__buf_16() -> gf.Component:
    """Returns sky130_fd_sc_hd__buf_16 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__buf_16()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/buf/sky130_fd_sc_hd__buf_16.gds",
        cellname="sky130_fd_sc_hd__buf_16",
    )


@cell
def sky130_fd_sc_hd__buf_6() -> gf.Component:
    """Returns sky130_fd_sc_hd__buf_6 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__buf_6()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/buf/sky130_fd_sc_hd__buf_6.gds",
        cellname="sky130_fd_sc_hd__buf_6",
    )


@cell
def sky130_fd_sc_hd__buf_12() -> gf.Component:
    """Returns sky130_fd_sc_hd__buf_12 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__buf_12()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/buf/sky130_fd_sc_hd__buf_12.gds",
        cellname="sky130_fd_sc_hd__buf_12",
    )


@cell
def sky130_fd_sc_hd__buf_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__buf_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__buf_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/buf/sky130_fd_sc_hd__buf_4.gds",
        cellname="sky130_fd_sc_hd__buf_4",
    )


@cell
def sky130_fd_sc_hd__buf_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__buf_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__buf_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/buf/sky130_fd_sc_hd__buf_2.gds",
        cellname="sky130_fd_sc_hd__buf_2",
    )


@cell
def sky130_fd_sc_hd__clkinv_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__clkinv_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__clkinv_4()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/clkinv/sky130_fd_sc_hd__clkinv_4.gds",
        cellname="sky130_fd_sc_hd__clkinv_4",
    )


@cell
def sky130_fd_sc_hd__clkinv_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__clkinv_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__clkinv_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/clkinv/sky130_fd_sc_hd__clkinv_1.gds",
        cellname="sky130_fd_sc_hd__clkinv_1",
    )


@cell
def sky130_fd_sc_hd__clkinv_8() -> gf.Component:
    """Returns sky130_fd_sc_hd__clkinv_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__clkinv_8()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/clkinv/sky130_fd_sc_hd__clkinv_8.gds",
        cellname="sky130_fd_sc_hd__clkinv_8",
    )


@cell
def sky130_fd_sc_hd__clkinv_16() -> gf.Component:
    """Returns sky130_fd_sc_hd__clkinv_16 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__clkinv_16()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/clkinv/sky130_fd_sc_hd__clkinv_16.gds",
        cellname="sky130_fd_sc_hd__clkinv_16",
    )


@cell
def sky130_fd_sc_hd__clkinv_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__clkinv_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__clkinv_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/clkinv/sky130_fd_sc_hd__clkinv_2.gds",
        cellname="sky130_fd_sc_hd__clkinv_2",
    )


@cell
def sky130_fd_sc_hd__sedfxbp_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__sedfxbp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sedfxbp_2()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/sedfxbp/sky130_fd_sc_hd__sedfxbp_2.gds",
        cellname="sky130_fd_sc_hd__sedfxbp_2",
    )


@cell
def sky130_fd_sc_hd__sedfxbp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__sedfxbp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sedfxbp_1()
      c.plot()
    """
    return import_gds(
        gdsdir / "src/sky130_fd_sc_hd/cells/sedfxbp/sky130_fd_sc_hd__sedfxbp_1.gds",
        cellname="sky130_fd_sc_hd__sedfxbp_1",
    )


@cell
def sky130_fd_sc_hd__lpflow_clkbufkapwr_16() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_clkbufkapwr_16 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_clkbufkapwr_16()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/lpflow_clkbufkapwr/sky130_fd_sc_hd__lpflow_clkbufkapwr_16.gds",
        cellname="sky130_fd_sc_hd__lpflow_clkbufkapwr_16",
    )


@cell
def sky130_fd_sc_hd__lpflow_clkbufkapwr_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_clkbufkapwr_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_clkbufkapwr_2()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/lpflow_clkbufkapwr/sky130_fd_sc_hd__lpflow_clkbufkapwr_2.gds",
        cellname="sky130_fd_sc_hd__lpflow_clkbufkapwr_2",
    )


@cell
def sky130_fd_sc_hd__lpflow_clkbufkapwr_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_clkbufkapwr_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_clkbufkapwr_1()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/lpflow_clkbufkapwr/sky130_fd_sc_hd__lpflow_clkbufkapwr_1.gds",
        cellname="sky130_fd_sc_hd__lpflow_clkbufkapwr_1",
    )


@cell
def sky130_fd_sc_hd__lpflow_clkbufkapwr_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_clkbufkapwr_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_clkbufkapwr_4()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/lpflow_clkbufkapwr/sky130_fd_sc_hd__lpflow_clkbufkapwr_4.gds",
        cellname="sky130_fd_sc_hd__lpflow_clkbufkapwr_4",
    )


@cell
def sky130_fd_sc_hd__lpflow_clkbufkapwr_8() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_clkbufkapwr_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_clkbufkapwr_8()
      c.plot()
    """
    return import_gds(
        gdsdir
        / "src/sky130_fd_sc_hd/cells/lpflow_clkbufkapwr/sky130_fd_sc_hd__lpflow_clkbufkapwr_8.gds",
        cellname="sky130_fd_sc_hd__lpflow_clkbufkapwr_8",
    )


if __name__ == "__main__":
    c = sky130_fd_sc_hd__a32oi_2()
    # c = sky130_fd_pr__rf_nfet_01v8_lvt_cM04W1p65L0p18()
    # c = sky130_fd_pr__rf_nfet_01v8_lvt_aM02W5p00L0p18()
    # c = sky130_fd_sc_hd__inv_1()
    c.show()
