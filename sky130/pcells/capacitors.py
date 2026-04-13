"""MIM capacitor pcells for sky130.

Provides:
    sky130_fd_pr__cap_mim_m3_1 — MIM capacitor between M3 (bottom) and M4 (top)
    sky130_fd_pr__cap_mim_m3_2 — MIM capacitor between M4 (bottom) and M5 (top)
"""

import gdsfactory as gf

from sky130.layers import LAYER
from sky130.pcells.contact import contact_array


@gf.cell
def sky130_fd_pr__cap_mim_m3_1(
    cap_width: float = 2.0,
    cap_length: float = 2.0,
) -> gf.Component:
    """MIM capacitor between Metal 3 (bottom plate) and Metal 4 (top landing pad).

    Capacitance density ~2.0 fF/um^2.

    Bottom plate: met3drawing rectangle (cap_width x cap_length).
    Top plate: capm (MIM dielectric layer) inset by enclosure on each side.
    Via3 array connects capm/top region up to met4drawing landing pad.

    Ports:
        BOTTOM — centre of met3drawing, on met3drawing layer
        TOP    — centre of met4drawing landing pad, on met4drawing layer

    Args:
        cap_width: width of the capacitor bottom plate (um).
        cap_length: length of the capacitor bottom plate (um).

    .. plot::
      :include-source:

      import sky130

      c = sky130.pcells.sky130_fd_pr__cap_mim_m3_1()
      c.plot()
    """
    c = gf.Component()

    # Design rule enclosures (um)
    capm_enc = 0.14   # capm must be enclosed by met3 by at least 0.14 um on all sides
    via3_enc = 0.06   # via3 enclosure within capm / met4
    via3_size = (0.2, 0.2)
    via3_spacing = (0.2, 0.2)
    # met4 landing pad must enclose via3 by via3_enc on all sides
    met4_enc = via3_enc

    # --- Bottom plate: met3drawing ---
    bot_w = cap_width
    bot_l = cap_length
    bot_plate = c.add_ref(
        gf.components.rectangle(size=(bot_l, bot_w), layer=LAYER.met3drawing)
    )
    bot_plate.move((0, 0))

    # --- MIM dielectric layer (capm) --- smaller than met3 by capm_enc on each side
    capm_l = bot_l - 2 * capm_enc
    capm_w = bot_w - 2 * capm_enc
    if capm_l <= 0 or capm_w <= 0:
        raise ValueError(
            f"cap_width/cap_length too small for capm enclosure of {capm_enc} um: "
            f"capm_w={capm_w:.3f}, capm_l={capm_l:.3f}"
        )
    capm_plate = c.add_ref(
        gf.components.rectangle(size=(capm_l, capm_w), layer=LAYER.capm)
    )
    capm_plate.move((capm_enc, capm_enc))

    # --- Via3 array within the capm region ---
    via3_ref = c.add_ref(
        contact_array(
            width=capm_l,
            height=capm_w,
            contact_layer=LAYER.via3drawing,
            contact_size=via3_size,
            contact_spacing=via3_spacing,
            enclosure=(via3_enc, via3_enc),
        )
    )
    via3_ref.move((capm_enc, capm_enc))

    # --- Top landing pad: met4drawing --- encloses the via3 array by met4_enc
    met4_l = capm_l
    met4_w = capm_w
    top_plate = c.add_ref(
        gf.components.rectangle(size=(met4_l, met4_w), layer=LAYER.met4drawing)
    )
    top_plate.move((capm_enc, capm_enc))

    # --- Ports ---
    c.add_port(
        name="BOTTOM",
        center=(bot_l / 2, bot_w / 2),
        width=min(bot_l, bot_w),
        orientation=90,
        layer=LAYER.met3drawing,
    )
    c.add_port(
        name="TOP",
        center=(capm_enc + met4_l / 2, capm_enc + met4_w / 2),
        width=min(met4_l, met4_w),
        orientation=90,
        layer=LAYER.met4drawing,
    )

    return c


@gf.cell
def sky130_fd_pr__cap_mim_m3_2(
    cap_width: float = 2.0,
    cap_length: float = 2.0,
) -> gf.Component:
    """MIM capacitor between Metal 4 (bottom plate) and Metal 5 (top landing pad).

    Capacitance density ~2.0 fF/um^2.

    Bottom plate: met4drawing rectangle (cap_width x cap_length).
    Top plate: cap2m (MIM dielectric layer over M4) inset by enclosure.
    Via4 array connects cap2m region up to met5drawing landing pad.

    Ports:
        BOTTOM — centre of met4drawing, on met4drawing layer
        TOP    — centre of met5drawing landing pad, on met5drawing layer

    Args:
        cap_width: width of the capacitor bottom plate (um).
        cap_length: length of the capacitor bottom plate (um).

    .. plot::
      :include-source:

      import sky130

      c = sky130.pcells.sky130_fd_pr__cap_mim_m3_2()
      c.plot()
    """
    c = gf.Component()

    # Design rule enclosures (um)
    cap2m_enc = 0.14   # cap2m must be enclosed by met4 by at least 0.14 um
    via4_enc = 0.06    # via4 enclosure within cap2m / met5
    via4_size = (0.8, 0.8)
    via4_spacing = (0.8, 0.8)

    # --- Bottom plate: met4drawing ---
    bot_w = cap_width
    bot_l = cap_length
    bot_plate = c.add_ref(
        gf.components.rectangle(size=(bot_l, bot_w), layer=LAYER.met4drawing)
    )
    bot_plate.move((0, 0))

    # --- MIM dielectric layer (cap2m) --- smaller than met4 by cap2m_enc on each side
    cap2m_l = bot_l - 2 * cap2m_enc
    cap2m_w = bot_w - 2 * cap2m_enc
    if cap2m_l <= 0 or cap2m_w <= 0:
        raise ValueError(
            f"cap_width/cap_length too small for cap2m enclosure of {cap2m_enc} um: "
            f"cap2m_w={cap2m_w:.3f}, cap2m_l={cap2m_l:.3f}"
        )
    cap2m_plate = c.add_ref(
        gf.components.rectangle(size=(cap2m_l, cap2m_w), layer=LAYER.cap2m)
    )
    cap2m_plate.move((cap2m_enc, cap2m_enc))

    # --- Via4 array within the cap2m region ---
    via4_ref = c.add_ref(
        contact_array(
            width=cap2m_l,
            height=cap2m_w,
            contact_layer=LAYER.via4drawing,
            contact_size=via4_size,
            contact_spacing=via4_spacing,
            enclosure=(via4_enc, via4_enc),
        )
    )
    via4_ref.move((cap2m_enc, cap2m_enc))

    # --- Top landing pad: met5drawing --- matches cap2m footprint
    met5_l = cap2m_l
    met5_w = cap2m_w
    top_plate = c.add_ref(
        gf.components.rectangle(size=(met5_l, met5_w), layer=LAYER.met5drawing)
    )
    top_plate.move((cap2m_enc, cap2m_enc))

    # --- Ports ---
    c.add_port(
        name="BOTTOM",
        center=(bot_l / 2, bot_w / 2),
        width=min(bot_l, bot_w),
        orientation=90,
        layer=LAYER.met4drawing,
    )
    c.add_port(
        name="TOP",
        center=(cap2m_enc + met5_l / 2, cap2m_enc + met5_w / 2),
        width=min(met5_l, met5_w),
        orientation=90,
        layer=LAYER.met5drawing,
    )

    return c


if __name__ == "__main__":
    c1 = sky130_fd_pr__cap_mim_m3_1()
    c1.show()
    c2 = sky130_fd_pr__cap_mim_m3_2()
    c2.show()
