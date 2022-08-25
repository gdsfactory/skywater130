from functools import partial

import gdsfactory as gf

from sky130.config import PATH
from sky130.layers import LAYER

# add_ports_m1 = gf.partial(
#     gf.add_ports.add_ports_from_markers_inside,
#     pin_layer=LAYER.met1pin,
#     port_layer=LAYER.met1drawing,
#     port_type="electrical",
# )
# add_ports_m2 = gf.partial(
#     gf.add_ports.add_ports_from_markers_inside,
#     pin_layer=LAYER.met2pin,
#     port_layer=LAYER.met2drawing,
#     port_type="electrical",
# )

add_ports_m1 = gf.partial(
    gf.add_ports.add_ports_from_labels,
    port_layer=LAYER.met1drawing,
    layer_label=LAYER.met1label,
    port_type="electrical",
    port_width=0.2,
    get_name_from_label=True,
    guess_port_orientation=False,
)
add_ports_m2 = gf.partial(
    gf.add_ports.add_ports_from_labels,
    port_layer=LAYER.met2drawing,
    layer_label=LAYER.met2label,
    port_type="electrical",
    port_width=0.2,
    get_name_from_label=True,
    guess_port_orientation=False,
)
add_ports = gf.compose(add_ports_m1, add_ports_m2)

gdsdir = PATH.gds

import_gds = partial(gf.import_gds, gdsdir=gdsdir, decorator=add_ports)


@gf.cell
def sky130_fd_sc_hd__a2111o_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a2111o_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a2111o_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a2111o_1.gds")


@gf.cell
def sky130_fd_sc_hd__a2111o_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__a2111o_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a2111o_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a2111o_2.gds")


@gf.cell
def sky130_fd_sc_hd__a2111o_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__a2111o_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a2111o_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a2111o_4.gds")


@gf.cell
def sky130_fd_sc_hd__a2111oi_0() -> gf.Component:
    """Returns sky130_fd_sc_hd__a2111oi_0 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a2111oi_0()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a2111oi_0.gds")


@gf.cell
def sky130_fd_sc_hd__a2111oi_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a2111oi_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a2111oi_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a2111oi_1.gds")


@gf.cell
def sky130_fd_sc_hd__a2111oi_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__a2111oi_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a2111oi_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a2111oi_2.gds")


@gf.cell
def sky130_fd_sc_hd__a2111oi_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__a2111oi_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a2111oi_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a2111oi_4.gds")


@gf.cell
def sky130_fd_sc_hd__a211o_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a211o_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a211o_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a211o_1.gds")


@gf.cell
def sky130_fd_sc_hd__a211o_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__a211o_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a211o_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a211o_2.gds")


@gf.cell
def sky130_fd_sc_hd__a211o_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__a211o_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a211o_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a211o_4.gds")


@gf.cell
def sky130_fd_sc_hd__a211oi_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a211oi_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a211oi_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a211oi_1.gds")


@gf.cell
def sky130_fd_sc_hd__a211oi_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__a211oi_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a211oi_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a211oi_2.gds")


@gf.cell
def sky130_fd_sc_hd__a211oi_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__a211oi_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a211oi_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a211oi_4.gds")


@gf.cell
def sky130_fd_sc_hd__a21bo_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a21bo_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a21bo_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a21bo_1.gds")


@gf.cell
def sky130_fd_sc_hd__a21bo_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__a21bo_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a21bo_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a21bo_2.gds")


@gf.cell
def sky130_fd_sc_hd__a21bo_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__a21bo_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a21bo_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a21bo_4.gds")


@gf.cell
def sky130_fd_sc_hd__a21boi_0() -> gf.Component:
    """Returns sky130_fd_sc_hd__a21boi_0 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a21boi_0()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a21boi_0.gds")


@gf.cell
def sky130_fd_sc_hd__a21boi_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a21boi_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a21boi_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a21boi_1.gds")


@gf.cell
def sky130_fd_sc_hd__a21boi_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__a21boi_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a21boi_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a21boi_2.gds")


@gf.cell
def sky130_fd_sc_hd__a21boi_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__a21boi_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a21boi_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a21boi_4.gds")


@gf.cell
def sky130_fd_sc_hd__a21o_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a21o_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a21o_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a21o_1.gds")


@gf.cell
def sky130_fd_sc_hd__a21o_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__a21o_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a21o_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a21o_2.gds")


@gf.cell
def sky130_fd_sc_hd__a21o_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__a21o_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a21o_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a21o_4.gds")


@gf.cell
def sky130_fd_sc_hd__a21oi_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a21oi_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a21oi_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a21oi_1.gds")


@gf.cell
def sky130_fd_sc_hd__a21oi_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__a21oi_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a21oi_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a21oi_2.gds")


@gf.cell
def sky130_fd_sc_hd__a21oi_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__a21oi_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a21oi_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a21oi_4.gds")


@gf.cell
def sky130_fd_sc_hd__a221o_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a221o_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a221o_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a221o_1.gds")


@gf.cell
def sky130_fd_sc_hd__a221o_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__a221o_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a221o_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a221o_2.gds")


@gf.cell
def sky130_fd_sc_hd__a221o_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__a221o_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a221o_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a221o_4.gds")


@gf.cell
def sky130_fd_sc_hd__a221oi_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a221oi_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a221oi_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a221oi_1.gds")


@gf.cell
def sky130_fd_sc_hd__a221oi_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__a221oi_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a221oi_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a221oi_2.gds")


@gf.cell
def sky130_fd_sc_hd__a221oi_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__a221oi_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a221oi_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a221oi_4.gds")


@gf.cell
def sky130_fd_sc_hd__a222oi_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a222oi_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a222oi_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a222oi_1.gds")


@gf.cell
def sky130_fd_sc_hd__a22o_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a22o_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a22o_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a22o_1.gds")


@gf.cell
def sky130_fd_sc_hd__a22o_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__a22o_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a22o_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a22o_2.gds")


@gf.cell
def sky130_fd_sc_hd__a22o_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__a22o_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a22o_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a22o_4.gds")


@gf.cell
def sky130_fd_sc_hd__a22oi_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a22oi_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a22oi_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a22oi_1.gds")


@gf.cell
def sky130_fd_sc_hd__a22oi_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__a22oi_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a22oi_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a22oi_2.gds")


@gf.cell
def sky130_fd_sc_hd__a22oi_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__a22oi_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a22oi_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a22oi_4.gds")


@gf.cell
def sky130_fd_sc_hd__a2bb2o_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a2bb2o_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a2bb2o_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a2bb2o_1.gds")


@gf.cell
def sky130_fd_sc_hd__a2bb2o_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__a2bb2o_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a2bb2o_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a2bb2o_2.gds")


@gf.cell
def sky130_fd_sc_hd__a2bb2o_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__a2bb2o_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a2bb2o_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a2bb2o_4.gds")


@gf.cell
def sky130_fd_sc_hd__a2bb2oi_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a2bb2oi_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a2bb2oi_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a2bb2oi_1.gds")


@gf.cell
def sky130_fd_sc_hd__a2bb2oi_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__a2bb2oi_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a2bb2oi_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a2bb2oi_2.gds")


@gf.cell
def sky130_fd_sc_hd__a2bb2oi_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__a2bb2oi_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a2bb2oi_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a2bb2oi_4.gds")


@gf.cell
def sky130_fd_sc_hd__a311o_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a311o_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a311o_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a311o_1.gds")


@gf.cell
def sky130_fd_sc_hd__a311o_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__a311o_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a311o_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a311o_2.gds")


@gf.cell
def sky130_fd_sc_hd__a311o_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__a311o_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a311o_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a311o_4.gds")


@gf.cell
def sky130_fd_sc_hd__a311oi_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a311oi_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a311oi_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a311oi_1.gds")


@gf.cell
def sky130_fd_sc_hd__a311oi_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__a311oi_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a311oi_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a311oi_2.gds")


@gf.cell
def sky130_fd_sc_hd__a311oi_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__a311oi_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a311oi_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a311oi_4.gds")


@gf.cell
def sky130_fd_sc_hd__a31o_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a31o_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a31o_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a31o_1.gds")


@gf.cell
def sky130_fd_sc_hd__a31o_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__a31o_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a31o_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a31o_2.gds")


@gf.cell
def sky130_fd_sc_hd__a31o_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__a31o_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a31o_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a31o_4.gds")


@gf.cell
def sky130_fd_sc_hd__a31oi_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a31oi_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a31oi_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a31oi_1.gds")


@gf.cell
def sky130_fd_sc_hd__a31oi_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__a31oi_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a31oi_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a31oi_2.gds")


@gf.cell
def sky130_fd_sc_hd__a31oi_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__a31oi_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a31oi_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a31oi_4.gds")


@gf.cell
def sky130_fd_sc_hd__a32o_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a32o_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a32o_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a32o_1.gds")


@gf.cell
def sky130_fd_sc_hd__a32o_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__a32o_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a32o_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a32o_2.gds")


@gf.cell
def sky130_fd_sc_hd__a32o_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__a32o_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a32o_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a32o_4.gds")


@gf.cell
def sky130_fd_sc_hd__a32oi_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a32oi_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a32oi_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a32oi_1.gds")


@gf.cell
def sky130_fd_sc_hd__a32oi_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__a32oi_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a32oi_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a32oi_2.gds")


@gf.cell
def sky130_fd_sc_hd__a32oi_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__a32oi_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a32oi_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a32oi_4.gds")


@gf.cell
def sky130_fd_sc_hd__a41o_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a41o_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a41o_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a41o_1.gds")


@gf.cell
def sky130_fd_sc_hd__a41o_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__a41o_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a41o_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a41o_2.gds")


@gf.cell
def sky130_fd_sc_hd__a41o_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__a41o_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a41o_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a41o_4.gds")


@gf.cell
def sky130_fd_sc_hd__a41oi_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__a41oi_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a41oi_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a41oi_1.gds")


@gf.cell
def sky130_fd_sc_hd__a41oi_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__a41oi_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a41oi_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a41oi_2.gds")


@gf.cell
def sky130_fd_sc_hd__a41oi_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__a41oi_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__a41oi_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__a41oi_4.gds")


@gf.cell
def sky130_fd_sc_hd__and2_0() -> gf.Component:
    """Returns sky130_fd_sc_hd__and2_0 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__and2_0()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__and2_0.gds")


@gf.cell
def sky130_fd_sc_hd__and2_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__and2_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__and2_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__and2_1.gds")


@gf.cell
def sky130_fd_sc_hd__and2_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__and2_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__and2_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__and2_2.gds")


@gf.cell
def sky130_fd_sc_hd__and2_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__and2_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__and2_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__and2_4.gds")


@gf.cell
def sky130_fd_sc_hd__and2b_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__and2b_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__and2b_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__and2b_1.gds")


@gf.cell
def sky130_fd_sc_hd__and2b_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__and2b_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__and2b_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__and2b_2.gds")


@gf.cell
def sky130_fd_sc_hd__and2b_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__and2b_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__and2b_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__and2b_4.gds")


@gf.cell
def sky130_fd_sc_hd__and3_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__and3_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__and3_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__and3_1.gds")


@gf.cell
def sky130_fd_sc_hd__and3_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__and3_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__and3_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__and3_2.gds")


@gf.cell
def sky130_fd_sc_hd__and3_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__and3_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__and3_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__and3_4.gds")


@gf.cell
def sky130_fd_sc_hd__and3b_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__and3b_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__and3b_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__and3b_1.gds")


@gf.cell
def sky130_fd_sc_hd__and3b_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__and3b_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__and3b_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__and3b_2.gds")


@gf.cell
def sky130_fd_sc_hd__and3b_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__and3b_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__and3b_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__and3b_4.gds")


@gf.cell
def sky130_fd_sc_hd__and4_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__and4_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__and4_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__and4_1.gds")


@gf.cell
def sky130_fd_sc_hd__and4_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__and4_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__and4_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__and4_2.gds")


@gf.cell
def sky130_fd_sc_hd__and4_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__and4_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__and4_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__and4_4.gds")


@gf.cell
def sky130_fd_sc_hd__and4b_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__and4b_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__and4b_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__and4b_1.gds")


@gf.cell
def sky130_fd_sc_hd__and4b_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__and4b_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__and4b_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__and4b_2.gds")


@gf.cell
def sky130_fd_sc_hd__and4b_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__and4b_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__and4b_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__and4b_4.gds")


@gf.cell
def sky130_fd_sc_hd__and4bb_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__and4bb_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__and4bb_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__and4bb_1.gds")


@gf.cell
def sky130_fd_sc_hd__and4bb_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__and4bb_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__and4bb_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__and4bb_2.gds")


@gf.cell
def sky130_fd_sc_hd__and4bb_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__and4bb_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__and4bb_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__and4bb_4.gds")


@gf.cell
def sky130_fd_sc_hd__buf_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__buf_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__buf_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__buf_1.gds")


@gf.cell
def sky130_fd_sc_hd__buf_12() -> gf.Component:
    """Returns sky130_fd_sc_hd__buf_12 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__buf_12()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__buf_12.gds")


@gf.cell
def sky130_fd_sc_hd__buf_16() -> gf.Component:
    """Returns sky130_fd_sc_hd__buf_16 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__buf_16()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__buf_16.gds")


@gf.cell
def sky130_fd_sc_hd__buf_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__buf_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__buf_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__buf_2.gds")


@gf.cell
def sky130_fd_sc_hd__buf_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__buf_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__buf_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__buf_4.gds")


@gf.cell
def sky130_fd_sc_hd__buf_6() -> gf.Component:
    """Returns sky130_fd_sc_hd__buf_6 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__buf_6()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__buf_6.gds")


@gf.cell
def sky130_fd_sc_hd__buf_8() -> gf.Component:
    """Returns sky130_fd_sc_hd__buf_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__buf_8()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__buf_8.gds")


@gf.cell
def sky130_fd_sc_hd__bufbuf_16() -> gf.Component:
    """Returns sky130_fd_sc_hd__bufbuf_16 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__bufbuf_16()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__bufbuf_16.gds")


@gf.cell
def sky130_fd_sc_hd__bufbuf_8() -> gf.Component:
    """Returns sky130_fd_sc_hd__bufbuf_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__bufbuf_8()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__bufbuf_8.gds")


@gf.cell
def sky130_fd_sc_hd__bufinv_16() -> gf.Component:
    """Returns sky130_fd_sc_hd__bufinv_16 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__bufinv_16()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__bufinv_16.gds")


@gf.cell
def sky130_fd_sc_hd__bufinv_8() -> gf.Component:
    """Returns sky130_fd_sc_hd__bufinv_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__bufinv_8()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__bufinv_8.gds")


@gf.cell
def sky130_fd_sc_hd__clkbuf_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__clkbuf_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__clkbuf_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__clkbuf_1.gds")


@gf.cell
def sky130_fd_sc_hd__clkbuf_16() -> gf.Component:
    """Returns sky130_fd_sc_hd__clkbuf_16 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__clkbuf_16()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__clkbuf_16.gds")


@gf.cell
def sky130_fd_sc_hd__clkbuf_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__clkbuf_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__clkbuf_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__clkbuf_2.gds")


@gf.cell
def sky130_fd_sc_hd__clkbuf_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__clkbuf_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__clkbuf_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__clkbuf_4.gds")


@gf.cell
def sky130_fd_sc_hd__clkbuf_8() -> gf.Component:
    """Returns sky130_fd_sc_hd__clkbuf_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__clkbuf_8()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__clkbuf_8.gds")


@gf.cell
def sky130_fd_sc_hd__clkdlybuf4s15_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__clkdlybuf4s15_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__clkdlybuf4s15_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__clkdlybuf4s15_1.gds")


@gf.cell
def sky130_fd_sc_hd__clkdlybuf4s15_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__clkdlybuf4s15_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__clkdlybuf4s15_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__clkdlybuf4s15_2.gds")


@gf.cell
def sky130_fd_sc_hd__clkdlybuf4s18_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__clkdlybuf4s18_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__clkdlybuf4s18_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__clkdlybuf4s18_1.gds")


@gf.cell
def sky130_fd_sc_hd__clkdlybuf4s18_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__clkdlybuf4s18_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__clkdlybuf4s18_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__clkdlybuf4s18_2.gds")


@gf.cell
def sky130_fd_sc_hd__clkdlybuf4s25_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__clkdlybuf4s25_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__clkdlybuf4s25_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__clkdlybuf4s25_1.gds")


@gf.cell
def sky130_fd_sc_hd__clkdlybuf4s25_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__clkdlybuf4s25_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__clkdlybuf4s25_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__clkdlybuf4s25_2.gds")


@gf.cell
def sky130_fd_sc_hd__clkdlybuf4s50_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__clkdlybuf4s50_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__clkdlybuf4s50_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__clkdlybuf4s50_1.gds")


@gf.cell
def sky130_fd_sc_hd__clkdlybuf4s50_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__clkdlybuf4s50_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__clkdlybuf4s50_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__clkdlybuf4s50_2.gds")


@gf.cell
def sky130_fd_sc_hd__clkinv_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__clkinv_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__clkinv_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__clkinv_1.gds")


@gf.cell
def sky130_fd_sc_hd__clkinv_16() -> gf.Component:
    """Returns sky130_fd_sc_hd__clkinv_16 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__clkinv_16()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__clkinv_16.gds")


@gf.cell
def sky130_fd_sc_hd__clkinv_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__clkinv_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__clkinv_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__clkinv_2.gds")


@gf.cell
def sky130_fd_sc_hd__clkinv_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__clkinv_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__clkinv_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__clkinv_4.gds")


@gf.cell
def sky130_fd_sc_hd__clkinv_8() -> gf.Component:
    """Returns sky130_fd_sc_hd__clkinv_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__clkinv_8()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__clkinv_8.gds")


@gf.cell
def sky130_fd_sc_hd__clkinvlp_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__clkinvlp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__clkinvlp_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__clkinvlp_2.gds")


@gf.cell
def sky130_fd_sc_hd__clkinvlp_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__clkinvlp_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__clkinvlp_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__clkinvlp_4.gds")


@gf.cell
def sky130_fd_sc_hd__conb_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__conb_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__conb_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__conb_1.gds")


@gf.cell
def sky130_fd_sc_hd__decap_12() -> gf.Component:
    """Returns sky130_fd_sc_hd__decap_12 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__decap_12()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__decap_12.gds")


@gf.cell
def sky130_fd_sc_hd__decap_3() -> gf.Component:
    """Returns sky130_fd_sc_hd__decap_3 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__decap_3()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__decap_3.gds")


@gf.cell
def sky130_fd_sc_hd__decap_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__decap_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__decap_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__decap_4.gds")


@gf.cell
def sky130_fd_sc_hd__decap_6() -> gf.Component:
    """Returns sky130_fd_sc_hd__decap_6 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__decap_6()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__decap_6.gds")


@gf.cell
def sky130_fd_sc_hd__decap_8() -> gf.Component:
    """Returns sky130_fd_sc_hd__decap_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__decap_8()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__decap_8.gds")


@gf.cell
def sky130_fd_sc_hd__dfbbn_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dfbbn_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dfbbn_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dfbbn_1.gds")


@gf.cell
def sky130_fd_sc_hd__dfbbn_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__dfbbn_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dfbbn_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dfbbn_2.gds")


@gf.cell
def sky130_fd_sc_hd__dfbbp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dfbbp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dfbbp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dfbbp_1.gds")


@gf.cell
def sky130_fd_sc_hd__dfrbp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dfrbp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dfrbp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dfrbp_1.gds")


@gf.cell
def sky130_fd_sc_hd__dfrbp_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__dfrbp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dfrbp_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dfrbp_2.gds")


@gf.cell
def sky130_fd_sc_hd__dfrtn_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dfrtn_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dfrtn_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dfrtn_1.gds")


@gf.cell
def sky130_fd_sc_hd__dfrtp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dfrtp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dfrtp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dfrtp_1.gds")


@gf.cell
def sky130_fd_sc_hd__dfrtp_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__dfrtp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dfrtp_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dfrtp_2.gds")


@gf.cell
def sky130_fd_sc_hd__dfrtp_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__dfrtp_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dfrtp_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dfrtp_4.gds")


@gf.cell
def sky130_fd_sc_hd__dfsbp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dfsbp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dfsbp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dfsbp_1.gds")


@gf.cell
def sky130_fd_sc_hd__dfsbp_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__dfsbp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dfsbp_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dfsbp_2.gds")


@gf.cell
def sky130_fd_sc_hd__dfstp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dfstp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dfstp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dfstp_1.gds")


@gf.cell
def sky130_fd_sc_hd__dfstp_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__dfstp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dfstp_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dfstp_2.gds")


@gf.cell
def sky130_fd_sc_hd__dfstp_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__dfstp_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dfstp_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dfstp_4.gds")


@gf.cell
def sky130_fd_sc_hd__dfxbp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dfxbp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dfxbp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dfxbp_1.gds")


@gf.cell
def sky130_fd_sc_hd__dfxbp_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__dfxbp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dfxbp_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dfxbp_2.gds")


@gf.cell
def sky130_fd_sc_hd__dfxtp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dfxtp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dfxtp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dfxtp_1.gds")


@gf.cell
def sky130_fd_sc_hd__dfxtp_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__dfxtp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dfxtp_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dfxtp_2.gds")


@gf.cell
def sky130_fd_sc_hd__dfxtp_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__dfxtp_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dfxtp_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dfxtp_4.gds")


@gf.cell
def sky130_fd_sc_hd__diode_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__diode_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__diode_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__diode_2.gds")


@gf.cell
def sky130_fd_sc_hd__dlclkp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlclkp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlclkp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dlclkp_1.gds")


@gf.cell
def sky130_fd_sc_hd__dlclkp_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlclkp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlclkp_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dlclkp_2.gds")


@gf.cell
def sky130_fd_sc_hd__dlclkp_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlclkp_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlclkp_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dlclkp_4.gds")


@gf.cell
def sky130_fd_sc_hd__dlrbn_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlrbn_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlrbn_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dlrbn_1.gds")


@gf.cell
def sky130_fd_sc_hd__dlrbn_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlrbn_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlrbn_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dlrbn_2.gds")


@gf.cell
def sky130_fd_sc_hd__dlrbp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlrbp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlrbp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dlrbp_1.gds")


@gf.cell
def sky130_fd_sc_hd__dlrbp_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlrbp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlrbp_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dlrbp_2.gds")


@gf.cell
def sky130_fd_sc_hd__dlrtn_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlrtn_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlrtn_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dlrtn_1.gds")


@gf.cell
def sky130_fd_sc_hd__dlrtn_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlrtn_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlrtn_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dlrtn_2.gds")


@gf.cell
def sky130_fd_sc_hd__dlrtn_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlrtn_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlrtn_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dlrtn_4.gds")


@gf.cell
def sky130_fd_sc_hd__dlrtp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlrtp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlrtp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dlrtp_1.gds")


@gf.cell
def sky130_fd_sc_hd__dlrtp_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlrtp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlrtp_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dlrtp_2.gds")


@gf.cell
def sky130_fd_sc_hd__dlrtp_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlrtp_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlrtp_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dlrtp_4.gds")


@gf.cell
def sky130_fd_sc_hd__dlxbn_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlxbn_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlxbn_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dlxbn_1.gds")


@gf.cell
def sky130_fd_sc_hd__dlxbn_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlxbn_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlxbn_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dlxbn_2.gds")


@gf.cell
def sky130_fd_sc_hd__dlxbp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlxbp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlxbp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dlxbp_1.gds")


@gf.cell
def sky130_fd_sc_hd__dlxtn_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlxtn_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlxtn_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dlxtn_1.gds")


@gf.cell
def sky130_fd_sc_hd__dlxtn_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlxtn_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlxtn_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dlxtn_2.gds")


@gf.cell
def sky130_fd_sc_hd__dlxtn_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlxtn_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlxtn_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dlxtn_4.gds")


@gf.cell
def sky130_fd_sc_hd__dlxtp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlxtp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlxtp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dlxtp_1.gds")


@gf.cell
def sky130_fd_sc_hd__dlygate4sd1_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlygate4sd1_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlygate4sd1_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dlygate4sd1_1.gds")


@gf.cell
def sky130_fd_sc_hd__dlygate4sd2_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlygate4sd2_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlygate4sd2_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dlygate4sd2_1.gds")


@gf.cell
def sky130_fd_sc_hd__dlygate4sd3_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlygate4sd3_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlygate4sd3_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dlygate4sd3_1.gds")


@gf.cell
def sky130_fd_sc_hd__dlymetal6s2s_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlymetal6s2s_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlymetal6s2s_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dlymetal6s2s_1.gds")


@gf.cell
def sky130_fd_sc_hd__dlymetal6s4s_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlymetal6s4s_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlymetal6s4s_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dlymetal6s4s_1.gds")


@gf.cell
def sky130_fd_sc_hd__dlymetal6s6s_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__dlymetal6s6s_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__dlymetal6s6s_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__dlymetal6s6s_1.gds")


@gf.cell
def sky130_fd_sc_hd__ebufn_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__ebufn_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__ebufn_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__ebufn_1.gds")


@gf.cell
def sky130_fd_sc_hd__ebufn_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__ebufn_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__ebufn_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__ebufn_2.gds")


@gf.cell
def sky130_fd_sc_hd__ebufn_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__ebufn_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__ebufn_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__ebufn_4.gds")


@gf.cell
def sky130_fd_sc_hd__ebufn_8() -> gf.Component:
    """Returns sky130_fd_sc_hd__ebufn_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__ebufn_8()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__ebufn_8.gds")


@gf.cell
def sky130_fd_sc_hd__edfxbp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__edfxbp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__edfxbp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__edfxbp_1.gds")


@gf.cell
def sky130_fd_sc_hd__edfxtp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__edfxtp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__edfxtp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__edfxtp_1.gds")


@gf.cell
def sky130_fd_sc_hd__einvn_0() -> gf.Component:
    """Returns sky130_fd_sc_hd__einvn_0 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__einvn_0()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__einvn_0.gds")


@gf.cell
def sky130_fd_sc_hd__einvn_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__einvn_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__einvn_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__einvn_1.gds")


@gf.cell
def sky130_fd_sc_hd__einvn_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__einvn_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__einvn_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__einvn_2.gds")


@gf.cell
def sky130_fd_sc_hd__einvn_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__einvn_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__einvn_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__einvn_4.gds")


@gf.cell
def sky130_fd_sc_hd__einvn_8() -> gf.Component:
    """Returns sky130_fd_sc_hd__einvn_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__einvn_8()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__einvn_8.gds")


@gf.cell
def sky130_fd_sc_hd__einvp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__einvp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__einvp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__einvp_1.gds")


@gf.cell
def sky130_fd_sc_hd__einvp_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__einvp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__einvp_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__einvp_2.gds")


@gf.cell
def sky130_fd_sc_hd__einvp_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__einvp_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__einvp_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__einvp_4.gds")


@gf.cell
def sky130_fd_sc_hd__einvp_8() -> gf.Component:
    """Returns sky130_fd_sc_hd__einvp_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__einvp_8()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__einvp_8.gds")


@gf.cell
def sky130_fd_sc_hd__fa_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__fa_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__fa_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__fa_1.gds")


@gf.cell
def sky130_fd_sc_hd__fa_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__fa_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__fa_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__fa_2.gds")


@gf.cell
def sky130_fd_sc_hd__fa_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__fa_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__fa_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__fa_4.gds")


@gf.cell
def sky130_fd_sc_hd__fah_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__fah_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__fah_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__fah_1.gds")


@gf.cell
def sky130_fd_sc_hd__fahcin_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__fahcin_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__fahcin_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__fahcin_1.gds")


@gf.cell
def sky130_fd_sc_hd__fahcon_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__fahcon_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__fahcon_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__fahcon_1.gds")


@gf.cell
def sky130_fd_sc_hd__fill_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__fill_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__fill_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__fill_1.gds")


@gf.cell
def sky130_fd_sc_hd__fill_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__fill_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__fill_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__fill_2.gds")


@gf.cell
def sky130_fd_sc_hd__fill_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__fill_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__fill_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__fill_4.gds")


@gf.cell
def sky130_fd_sc_hd__fill_8() -> gf.Component:
    """Returns sky130_fd_sc_hd__fill_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__fill_8()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__fill_8.gds")


@gf.cell
def sky130_fd_sc_hd__ha_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__ha_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__ha_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__ha_1.gds")


@gf.cell
def sky130_fd_sc_hd__ha_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__ha_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__ha_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__ha_2.gds")


@gf.cell
def sky130_fd_sc_hd__ha_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__ha_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__ha_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__ha_4.gds")


@gf.cell
def sky130_fd_sc_hd__inv_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__inv_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__inv_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__inv_1.gds")


@gf.cell
def sky130_fd_sc_hd__inv_12() -> gf.Component:
    """Returns sky130_fd_sc_hd__inv_12 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__inv_12()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__inv_12.gds")


@gf.cell
def sky130_fd_sc_hd__inv_16() -> gf.Component:
    """Returns sky130_fd_sc_hd__inv_16 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__inv_16()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__inv_16.gds")


@gf.cell
def sky130_fd_sc_hd__inv_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__inv_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__inv_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__inv_2.gds")


@gf.cell
def sky130_fd_sc_hd__inv_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__inv_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__inv_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__inv_4.gds")


@gf.cell
def sky130_fd_sc_hd__inv_6() -> gf.Component:
    """Returns sky130_fd_sc_hd__inv_6 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__inv_6()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__inv_6.gds")


@gf.cell
def sky130_fd_sc_hd__inv_8() -> gf.Component:
    """Returns sky130_fd_sc_hd__inv_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__inv_8()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__inv_8.gds")


@gf.cell
def sky130_fd_sc_hd__lpflow_bleeder_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_bleeder_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_bleeder_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__lpflow_bleeder_1.gds")


@gf.cell
def sky130_fd_sc_hd__lpflow_clkbufkapwr_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_clkbufkapwr_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_clkbufkapwr_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__lpflow_clkbufkapwr_1.gds")


@gf.cell
def sky130_fd_sc_hd__lpflow_clkbufkapwr_16() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_clkbufkapwr_16 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_clkbufkapwr_16()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__lpflow_clkbufkapwr_16.gds")


@gf.cell
def sky130_fd_sc_hd__lpflow_clkbufkapwr_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_clkbufkapwr_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_clkbufkapwr_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__lpflow_clkbufkapwr_2.gds")


@gf.cell
def sky130_fd_sc_hd__lpflow_clkbufkapwr_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_clkbufkapwr_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_clkbufkapwr_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__lpflow_clkbufkapwr_4.gds")


@gf.cell
def sky130_fd_sc_hd__lpflow_clkbufkapwr_8() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_clkbufkapwr_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_clkbufkapwr_8()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__lpflow_clkbufkapwr_8.gds")


@gf.cell
def sky130_fd_sc_hd__lpflow_clkinvkapwr_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_clkinvkapwr_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_clkinvkapwr_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__lpflow_clkinvkapwr_1.gds")


@gf.cell
def sky130_fd_sc_hd__lpflow_clkinvkapwr_16() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_clkinvkapwr_16 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_clkinvkapwr_16()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__lpflow_clkinvkapwr_16.gds")


@gf.cell
def sky130_fd_sc_hd__lpflow_clkinvkapwr_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_clkinvkapwr_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_clkinvkapwr_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__lpflow_clkinvkapwr_2.gds")


@gf.cell
def sky130_fd_sc_hd__lpflow_clkinvkapwr_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_clkinvkapwr_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_clkinvkapwr_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__lpflow_clkinvkapwr_4.gds")


@gf.cell
def sky130_fd_sc_hd__lpflow_clkinvkapwr_8() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_clkinvkapwr_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_clkinvkapwr_8()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__lpflow_clkinvkapwr_8.gds")


@gf.cell
def sky130_fd_sc_hd__lpflow_decapkapwr_12() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_decapkapwr_12 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_decapkapwr_12()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__lpflow_decapkapwr_12.gds")


@gf.cell
def sky130_fd_sc_hd__lpflow_decapkapwr_3() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_decapkapwr_3 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_decapkapwr_3()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__lpflow_decapkapwr_3.gds")


@gf.cell
def sky130_fd_sc_hd__lpflow_decapkapwr_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_decapkapwr_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_decapkapwr_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__lpflow_decapkapwr_4.gds")


@gf.cell
def sky130_fd_sc_hd__lpflow_decapkapwr_6() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_decapkapwr_6 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_decapkapwr_6()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__lpflow_decapkapwr_6.gds")


@gf.cell
def sky130_fd_sc_hd__lpflow_decapkapwr_8() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_decapkapwr_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_decapkapwr_8()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__lpflow_decapkapwr_8.gds")


@gf.cell
def sky130_fd_sc_hd__lpflow_inputiso0n_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_inputiso0n_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_inputiso0n_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__lpflow_inputiso0n_1.gds")


@gf.cell
def sky130_fd_sc_hd__lpflow_inputiso0p_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_inputiso0p_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_inputiso0p_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__lpflow_inputiso0p_1.gds")


@gf.cell
def sky130_fd_sc_hd__lpflow_inputiso1n_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_inputiso1n_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_inputiso1n_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__lpflow_inputiso1n_1.gds")


@gf.cell
def sky130_fd_sc_hd__lpflow_inputiso1p_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_inputiso1p_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_inputiso1p_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__lpflow_inputiso1p_1.gds")


@gf.cell
def sky130_fd_sc_hd__lpflow_inputisolatch_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_inputisolatch_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_inputisolatch_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__lpflow_inputisolatch_1.gds")


@gf.cell
def sky130_fd_sc_hd__lpflow_isobufsrc_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_isobufsrc_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_isobufsrc_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__lpflow_isobufsrc_1.gds")


@gf.cell
def sky130_fd_sc_hd__lpflow_isobufsrc_16() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_isobufsrc_16 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_isobufsrc_16()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__lpflow_isobufsrc_16.gds")


@gf.cell
def sky130_fd_sc_hd__lpflow_isobufsrc_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_isobufsrc_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_isobufsrc_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__lpflow_isobufsrc_2.gds")


@gf.cell
def sky130_fd_sc_hd__lpflow_isobufsrc_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_isobufsrc_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_isobufsrc_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__lpflow_isobufsrc_4.gds")


@gf.cell
def sky130_fd_sc_hd__lpflow_isobufsrc_8() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_isobufsrc_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_isobufsrc_8()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__lpflow_isobufsrc_8.gds")


@gf.cell
def sky130_fd_sc_hd__lpflow_isobufsrckapwr_16() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_isobufsrckapwr_16 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_isobufsrckapwr_16()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__lpflow_isobufsrckapwr_16.gds")


@gf.cell
def sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_1.gds")


@gf.cell
def sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_2.gds")


@gf.cell
def sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_4.gds")


@gf.cell
def sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_4.gds")


@gf.cell
def sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_1.gds")


@gf.cell
def sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_2.gds")


@gf.cell
def sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_4.gds")


@gf.cell
def sky130_fd_sc_hd__macro_sparecell() -> gf.Component:
    """Returns sky130_fd_sc_hd__macro_sparecell fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__macro_sparecell()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__macro_sparecell.gds")


@gf.cell
def sky130_fd_sc_hd__maj3_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__maj3_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__maj3_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__maj3_1.gds")


@gf.cell
def sky130_fd_sc_hd__maj3_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__maj3_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__maj3_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__maj3_2.gds")


@gf.cell
def sky130_fd_sc_hd__maj3_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__maj3_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__maj3_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__maj3_4.gds")


@gf.cell
def sky130_fd_sc_hd__mux2_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__mux2_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__mux2_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__mux2_1.gds")


@gf.cell
def sky130_fd_sc_hd__mux2_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__mux2_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__mux2_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__mux2_2.gds")


@gf.cell
def sky130_fd_sc_hd__mux2_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__mux2_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__mux2_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__mux2_4.gds")


@gf.cell
def sky130_fd_sc_hd__mux2_8() -> gf.Component:
    """Returns sky130_fd_sc_hd__mux2_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__mux2_8()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__mux2_8.gds")


@gf.cell
def sky130_fd_sc_hd__mux2i_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__mux2i_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__mux2i_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__mux2i_1.gds")


@gf.cell
def sky130_fd_sc_hd__mux2i_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__mux2i_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__mux2i_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__mux2i_2.gds")


@gf.cell
def sky130_fd_sc_hd__mux2i_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__mux2i_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__mux2i_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__mux2i_4.gds")


@gf.cell
def sky130_fd_sc_hd__mux4_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__mux4_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__mux4_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__mux4_1.gds")


@gf.cell
def sky130_fd_sc_hd__mux4_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__mux4_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__mux4_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__mux4_2.gds")


@gf.cell
def sky130_fd_sc_hd__mux4_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__mux4_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__mux4_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__mux4_4.gds")


@gf.cell
def sky130_fd_sc_hd__nand2_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__nand2_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nand2_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__nand2_1.gds")


@gf.cell
def sky130_fd_sc_hd__nand2_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__nand2_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nand2_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__nand2_2.gds")


@gf.cell
def sky130_fd_sc_hd__nand2_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__nand2_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nand2_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__nand2_4.gds")


@gf.cell
def sky130_fd_sc_hd__nand2_8() -> gf.Component:
    """Returns sky130_fd_sc_hd__nand2_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nand2_8()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__nand2_8.gds")


@gf.cell
def sky130_fd_sc_hd__nand2b_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__nand2b_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nand2b_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__nand2b_1.gds")


@gf.cell
def sky130_fd_sc_hd__nand2b_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__nand2b_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nand2b_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__nand2b_2.gds")


@gf.cell
def sky130_fd_sc_hd__nand2b_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__nand2b_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nand2b_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__nand2b_4.gds")


@gf.cell
def sky130_fd_sc_hd__nand3_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__nand3_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nand3_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__nand3_1.gds")


@gf.cell
def sky130_fd_sc_hd__nand3_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__nand3_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nand3_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__nand3_2.gds")


@gf.cell
def sky130_fd_sc_hd__nand3_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__nand3_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nand3_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__nand3_4.gds")


@gf.cell
def sky130_fd_sc_hd__nand3b_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__nand3b_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nand3b_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__nand3b_1.gds")


@gf.cell
def sky130_fd_sc_hd__nand3b_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__nand3b_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nand3b_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__nand3b_2.gds")


@gf.cell
def sky130_fd_sc_hd__nand3b_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__nand3b_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nand3b_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__nand3b_4.gds")


@gf.cell
def sky130_fd_sc_hd__nand4_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__nand4_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nand4_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__nand4_1.gds")


@gf.cell
def sky130_fd_sc_hd__nand4_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__nand4_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nand4_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__nand4_2.gds")


@gf.cell
def sky130_fd_sc_hd__nand4_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__nand4_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nand4_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__nand4_4.gds")


@gf.cell
def sky130_fd_sc_hd__nand4b_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__nand4b_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nand4b_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__nand4b_1.gds")


@gf.cell
def sky130_fd_sc_hd__nand4b_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__nand4b_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nand4b_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__nand4b_2.gds")


@gf.cell
def sky130_fd_sc_hd__nand4b_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__nand4b_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nand4b_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__nand4b_4.gds")


@gf.cell
def sky130_fd_sc_hd__nand4bb_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__nand4bb_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nand4bb_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__nand4bb_1.gds")


@gf.cell
def sky130_fd_sc_hd__nand4bb_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__nand4bb_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nand4bb_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__nand4bb_2.gds")


@gf.cell
def sky130_fd_sc_hd__nand4bb_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__nand4bb_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nand4bb_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__nand4bb_4.gds")


@gf.cell
def sky130_fd_sc_hd__nor2_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__nor2_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nor2_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__nor2_1.gds")


@gf.cell
def sky130_fd_sc_hd__nor2_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__nor2_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nor2_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__nor2_2.gds")


@gf.cell
def sky130_fd_sc_hd__nor2_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__nor2_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nor2_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__nor2_4.gds")


@gf.cell
def sky130_fd_sc_hd__nor2_8() -> gf.Component:
    """Returns sky130_fd_sc_hd__nor2_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nor2_8()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__nor2_8.gds")


@gf.cell
def sky130_fd_sc_hd__nor2b_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__nor2b_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nor2b_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__nor2b_1.gds")


@gf.cell
def sky130_fd_sc_hd__nor2b_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__nor2b_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nor2b_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__nor2b_2.gds")


@gf.cell
def sky130_fd_sc_hd__nor2b_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__nor2b_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nor2b_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__nor2b_4.gds")


@gf.cell
def sky130_fd_sc_hd__nor3_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__nor3_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nor3_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__nor3_1.gds")


@gf.cell
def sky130_fd_sc_hd__nor3_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__nor3_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nor3_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__nor3_2.gds")


@gf.cell
def sky130_fd_sc_hd__nor3_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__nor3_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nor3_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__nor3_4.gds")


@gf.cell
def sky130_fd_sc_hd__nor3b_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__nor3b_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nor3b_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__nor3b_1.gds")


@gf.cell
def sky130_fd_sc_hd__nor3b_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__nor3b_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nor3b_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__nor3b_2.gds")


@gf.cell
def sky130_fd_sc_hd__nor3b_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__nor3b_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nor3b_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__nor3b_4.gds")


@gf.cell
def sky130_fd_sc_hd__nor4_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__nor4_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nor4_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__nor4_1.gds")


@gf.cell
def sky130_fd_sc_hd__nor4_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__nor4_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nor4_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__nor4_2.gds")


@gf.cell
def sky130_fd_sc_hd__nor4_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__nor4_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nor4_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__nor4_4.gds")


@gf.cell
def sky130_fd_sc_hd__nor4b_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__nor4b_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nor4b_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__nor4b_1.gds")


@gf.cell
def sky130_fd_sc_hd__nor4b_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__nor4b_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nor4b_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__nor4b_2.gds")


@gf.cell
def sky130_fd_sc_hd__nor4b_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__nor4b_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nor4b_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__nor4b_4.gds")


@gf.cell
def sky130_fd_sc_hd__nor4bb_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__nor4bb_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nor4bb_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__nor4bb_1.gds")


@gf.cell
def sky130_fd_sc_hd__nor4bb_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__nor4bb_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nor4bb_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__nor4bb_2.gds")


@gf.cell
def sky130_fd_sc_hd__nor4bb_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__nor4bb_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__nor4bb_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__nor4bb_4.gds")


@gf.cell
def sky130_fd_sc_hd__o2111a_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__o2111a_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o2111a_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o2111a_1.gds")


@gf.cell
def sky130_fd_sc_hd__o2111a_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__o2111a_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o2111a_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o2111a_2.gds")


@gf.cell
def sky130_fd_sc_hd__o2111a_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__o2111a_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o2111a_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o2111a_4.gds")


@gf.cell
def sky130_fd_sc_hd__o2111ai_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__o2111ai_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o2111ai_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o2111ai_1.gds")


@gf.cell
def sky130_fd_sc_hd__o2111ai_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__o2111ai_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o2111ai_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o2111ai_2.gds")


@gf.cell
def sky130_fd_sc_hd__o2111ai_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__o2111ai_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o2111ai_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o2111ai_4.gds")


@gf.cell
def sky130_fd_sc_hd__o211a_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__o211a_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o211a_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o211a_1.gds")


@gf.cell
def sky130_fd_sc_hd__o211a_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__o211a_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o211a_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o211a_2.gds")


@gf.cell
def sky130_fd_sc_hd__o211a_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__o211a_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o211a_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o211a_4.gds")


@gf.cell
def sky130_fd_sc_hd__o211ai_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__o211ai_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o211ai_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o211ai_1.gds")


@gf.cell
def sky130_fd_sc_hd__o211ai_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__o211ai_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o211ai_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o211ai_2.gds")


@gf.cell
def sky130_fd_sc_hd__o211ai_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__o211ai_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o211ai_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o211ai_4.gds")


@gf.cell
def sky130_fd_sc_hd__o21a_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__o21a_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o21a_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o21a_1.gds")


@gf.cell
def sky130_fd_sc_hd__o21a_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__o21a_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o21a_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o21a_2.gds")


@gf.cell
def sky130_fd_sc_hd__o21a_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__o21a_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o21a_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o21a_4.gds")


@gf.cell
def sky130_fd_sc_hd__o21ai_0() -> gf.Component:
    """Returns sky130_fd_sc_hd__o21ai_0 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o21ai_0()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o21ai_0.gds")


@gf.cell
def sky130_fd_sc_hd__o21ai_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__o21ai_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o21ai_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o21ai_1.gds")


@gf.cell
def sky130_fd_sc_hd__o21ai_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__o21ai_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o21ai_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o21ai_2.gds")


@gf.cell
def sky130_fd_sc_hd__o21ai_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__o21ai_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o21ai_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o21ai_4.gds")


@gf.cell
def sky130_fd_sc_hd__o21ba_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__o21ba_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o21ba_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o21ba_1.gds")


@gf.cell
def sky130_fd_sc_hd__o21ba_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__o21ba_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o21ba_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o21ba_2.gds")


@gf.cell
def sky130_fd_sc_hd__o21ba_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__o21ba_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o21ba_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o21ba_4.gds")


@gf.cell
def sky130_fd_sc_hd__o21bai_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__o21bai_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o21bai_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o21bai_1.gds")


@gf.cell
def sky130_fd_sc_hd__o21bai_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__o21bai_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o21bai_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o21bai_2.gds")


@gf.cell
def sky130_fd_sc_hd__o21bai_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__o21bai_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o21bai_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o21bai_4.gds")


@gf.cell
def sky130_fd_sc_hd__o221a_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__o221a_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o221a_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o221a_1.gds")


@gf.cell
def sky130_fd_sc_hd__o221a_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__o221a_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o221a_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o221a_2.gds")


@gf.cell
def sky130_fd_sc_hd__o221a_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__o221a_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o221a_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o221a_4.gds")


@gf.cell
def sky130_fd_sc_hd__o221ai_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__o221ai_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o221ai_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o221ai_1.gds")


@gf.cell
def sky130_fd_sc_hd__o221ai_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__o221ai_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o221ai_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o221ai_2.gds")


@gf.cell
def sky130_fd_sc_hd__o221ai_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__o221ai_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o221ai_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o221ai_4.gds")


@gf.cell
def sky130_fd_sc_hd__o22a_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__o22a_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o22a_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o22a_1.gds")


@gf.cell
def sky130_fd_sc_hd__o22a_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__o22a_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o22a_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o22a_2.gds")


@gf.cell
def sky130_fd_sc_hd__o22a_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__o22a_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o22a_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o22a_4.gds")


@gf.cell
def sky130_fd_sc_hd__o22ai_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__o22ai_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o22ai_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o22ai_1.gds")


@gf.cell
def sky130_fd_sc_hd__o22ai_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__o22ai_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o22ai_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o22ai_2.gds")


@gf.cell
def sky130_fd_sc_hd__o22ai_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__o22ai_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o22ai_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o22ai_4.gds")


@gf.cell
def sky130_fd_sc_hd__o2bb2a_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__o2bb2a_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o2bb2a_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o2bb2a_1.gds")


@gf.cell
def sky130_fd_sc_hd__o2bb2a_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__o2bb2a_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o2bb2a_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o2bb2a_2.gds")


@gf.cell
def sky130_fd_sc_hd__o2bb2a_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__o2bb2a_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o2bb2a_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o2bb2a_4.gds")


@gf.cell
def sky130_fd_sc_hd__o2bb2ai_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__o2bb2ai_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o2bb2ai_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o2bb2ai_1.gds")


@gf.cell
def sky130_fd_sc_hd__o2bb2ai_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__o2bb2ai_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o2bb2ai_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o2bb2ai_2.gds")


@gf.cell
def sky130_fd_sc_hd__o2bb2ai_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__o2bb2ai_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o2bb2ai_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o2bb2ai_4.gds")


@gf.cell
def sky130_fd_sc_hd__o311a_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__o311a_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o311a_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o311a_1.gds")


@gf.cell
def sky130_fd_sc_hd__o311a_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__o311a_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o311a_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o311a_2.gds")


@gf.cell
def sky130_fd_sc_hd__o311a_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__o311a_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o311a_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o311a_4.gds")


@gf.cell
def sky130_fd_sc_hd__o311ai_0() -> gf.Component:
    """Returns sky130_fd_sc_hd__o311ai_0 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o311ai_0()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o311ai_0.gds")


@gf.cell
def sky130_fd_sc_hd__o311ai_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__o311ai_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o311ai_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o311ai_1.gds")


@gf.cell
def sky130_fd_sc_hd__o311ai_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__o311ai_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o311ai_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o311ai_2.gds")


@gf.cell
def sky130_fd_sc_hd__o311ai_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__o311ai_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o311ai_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o311ai_4.gds")


@gf.cell
def sky130_fd_sc_hd__o31a_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__o31a_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o31a_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o31a_1.gds")


@gf.cell
def sky130_fd_sc_hd__o31a_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__o31a_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o31a_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o31a_2.gds")


@gf.cell
def sky130_fd_sc_hd__o31a_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__o31a_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o31a_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o31a_4.gds")


@gf.cell
def sky130_fd_sc_hd__o31ai_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__o31ai_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o31ai_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o31ai_1.gds")


@gf.cell
def sky130_fd_sc_hd__o31ai_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__o31ai_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o31ai_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o31ai_2.gds")


@gf.cell
def sky130_fd_sc_hd__o31ai_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__o31ai_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o31ai_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o31ai_4.gds")


@gf.cell
def sky130_fd_sc_hd__o32a_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__o32a_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o32a_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o32a_1.gds")


@gf.cell
def sky130_fd_sc_hd__o32a_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__o32a_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o32a_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o32a_2.gds")


@gf.cell
def sky130_fd_sc_hd__o32a_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__o32a_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o32a_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o32a_4.gds")


@gf.cell
def sky130_fd_sc_hd__o32ai_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__o32ai_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o32ai_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o32ai_1.gds")


@gf.cell
def sky130_fd_sc_hd__o32ai_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__o32ai_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o32ai_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o32ai_2.gds")


@gf.cell
def sky130_fd_sc_hd__o32ai_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__o32ai_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o32ai_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o32ai_4.gds")


@gf.cell
def sky130_fd_sc_hd__o41a_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__o41a_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o41a_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o41a_1.gds")


@gf.cell
def sky130_fd_sc_hd__o41a_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__o41a_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o41a_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o41a_2.gds")


@gf.cell
def sky130_fd_sc_hd__o41a_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__o41a_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o41a_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o41a_4.gds")


@gf.cell
def sky130_fd_sc_hd__o41ai_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__o41ai_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o41ai_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o41ai_1.gds")


@gf.cell
def sky130_fd_sc_hd__o41ai_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__o41ai_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o41ai_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o41ai_2.gds")


@gf.cell
def sky130_fd_sc_hd__o41ai_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__o41ai_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__o41ai_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__o41ai_4.gds")


@gf.cell
def sky130_fd_sc_hd__or2_0() -> gf.Component:
    """Returns sky130_fd_sc_hd__or2_0 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__or2_0()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__or2_0.gds")


@gf.cell
def sky130_fd_sc_hd__or2_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__or2_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__or2_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__or2_1.gds")


@gf.cell
def sky130_fd_sc_hd__or2_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__or2_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__or2_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__or2_2.gds")


@gf.cell
def sky130_fd_sc_hd__or2_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__or2_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__or2_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__or2_4.gds")


@gf.cell
def sky130_fd_sc_hd__or2b_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__or2b_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__or2b_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__or2b_1.gds")


@gf.cell
def sky130_fd_sc_hd__or2b_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__or2b_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__or2b_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__or2b_2.gds")


@gf.cell
def sky130_fd_sc_hd__or2b_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__or2b_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__or2b_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__or2b_4.gds")


@gf.cell
def sky130_fd_sc_hd__or3_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__or3_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__or3_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__or3_1.gds")


@gf.cell
def sky130_fd_sc_hd__or3_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__or3_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__or3_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__or3_2.gds")


@gf.cell
def sky130_fd_sc_hd__or3_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__or3_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__or3_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__or3_4.gds")


@gf.cell
def sky130_fd_sc_hd__or3b_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__or3b_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__or3b_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__or3b_1.gds")


@gf.cell
def sky130_fd_sc_hd__or3b_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__or3b_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__or3b_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__or3b_2.gds")


@gf.cell
def sky130_fd_sc_hd__or3b_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__or3b_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__or3b_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__or3b_4.gds")


@gf.cell
def sky130_fd_sc_hd__or4_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__or4_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__or4_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__or4_1.gds")


@gf.cell
def sky130_fd_sc_hd__or4_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__or4_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__or4_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__or4_2.gds")


@gf.cell
def sky130_fd_sc_hd__or4_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__or4_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__or4_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__or4_4.gds")


@gf.cell
def sky130_fd_sc_hd__or4b_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__or4b_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__or4b_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__or4b_1.gds")


@gf.cell
def sky130_fd_sc_hd__or4b_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__or4b_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__or4b_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__or4b_2.gds")


@gf.cell
def sky130_fd_sc_hd__or4b_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__or4b_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__or4b_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__or4b_4.gds")


@gf.cell
def sky130_fd_sc_hd__or4bb_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__or4bb_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__or4bb_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__or4bb_1.gds")


@gf.cell
def sky130_fd_sc_hd__or4bb_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__or4bb_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__or4bb_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__or4bb_2.gds")


@gf.cell
def sky130_fd_sc_hd__or4bb_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__or4bb_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__or4bb_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__or4bb_4.gds")


@gf.cell
def sky130_fd_sc_hd__probe_p_8() -> gf.Component:
    """Returns sky130_fd_sc_hd__probe_p_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__probe_p_8()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__probe_p_8.gds")


@gf.cell
def sky130_fd_sc_hd__probec_p_8() -> gf.Component:
    """Returns sky130_fd_sc_hd__probec_p_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__probec_p_8()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__probec_p_8.gds")


@gf.cell
def sky130_fd_sc_hd__sdfbbn_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__sdfbbn_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sdfbbn_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__sdfbbn_1.gds")


@gf.cell
def sky130_fd_sc_hd__sdfbbn_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__sdfbbn_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sdfbbn_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__sdfbbn_2.gds")


@gf.cell
def sky130_fd_sc_hd__sdfbbp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__sdfbbp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sdfbbp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__sdfbbp_1.gds")


@gf.cell
def sky130_fd_sc_hd__sdfrbp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__sdfrbp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sdfrbp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__sdfrbp_1.gds")


@gf.cell
def sky130_fd_sc_hd__sdfrbp_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__sdfrbp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sdfrbp_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__sdfrbp_2.gds")


@gf.cell
def sky130_fd_sc_hd__sdfrtn_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__sdfrtn_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sdfrtn_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__sdfrtn_1.gds")


@gf.cell
def sky130_fd_sc_hd__sdfrtp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__sdfrtp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sdfrtp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__sdfrtp_1.gds")


@gf.cell
def sky130_fd_sc_hd__sdfrtp_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__sdfrtp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sdfrtp_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__sdfrtp_2.gds")


@gf.cell
def sky130_fd_sc_hd__sdfrtp_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__sdfrtp_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sdfrtp_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__sdfrtp_4.gds")


@gf.cell
def sky130_fd_sc_hd__sdfsbp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__sdfsbp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sdfsbp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__sdfsbp_1.gds")


@gf.cell
def sky130_fd_sc_hd__sdfsbp_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__sdfsbp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sdfsbp_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__sdfsbp_2.gds")


@gf.cell
def sky130_fd_sc_hd__sdfstp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__sdfstp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sdfstp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__sdfstp_1.gds")


@gf.cell
def sky130_fd_sc_hd__sdfstp_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__sdfstp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sdfstp_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__sdfstp_2.gds")


@gf.cell
def sky130_fd_sc_hd__sdfstp_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__sdfstp_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sdfstp_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__sdfstp_4.gds")


@gf.cell
def sky130_fd_sc_hd__sdfxbp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__sdfxbp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sdfxbp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__sdfxbp_1.gds")


@gf.cell
def sky130_fd_sc_hd__sdfxbp_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__sdfxbp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sdfxbp_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__sdfxbp_2.gds")


@gf.cell
def sky130_fd_sc_hd__sdfxtp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__sdfxtp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sdfxtp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__sdfxtp_1.gds")


@gf.cell
def sky130_fd_sc_hd__sdfxtp_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__sdfxtp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sdfxtp_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__sdfxtp_2.gds")


@gf.cell
def sky130_fd_sc_hd__sdfxtp_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__sdfxtp_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sdfxtp_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__sdfxtp_4.gds")


@gf.cell
def sky130_fd_sc_hd__sdlclkp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__sdlclkp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sdlclkp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__sdlclkp_1.gds")


@gf.cell
def sky130_fd_sc_hd__sdlclkp_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__sdlclkp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sdlclkp_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__sdlclkp_2.gds")


@gf.cell
def sky130_fd_sc_hd__sdlclkp_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__sdlclkp_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sdlclkp_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__sdlclkp_4.gds")


@gf.cell
def sky130_fd_sc_hd__sedfxbp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__sedfxbp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sedfxbp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__sedfxbp_1.gds")


@gf.cell
def sky130_fd_sc_hd__sedfxbp_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__sedfxbp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sedfxbp_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__sedfxbp_2.gds")


@gf.cell
def sky130_fd_sc_hd__sedfxtp_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__sedfxtp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sedfxtp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__sedfxtp_1.gds")


@gf.cell
def sky130_fd_sc_hd__sedfxtp_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__sedfxtp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sedfxtp_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__sedfxtp_2.gds")


@gf.cell
def sky130_fd_sc_hd__sedfxtp_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__sedfxtp_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__sedfxtp_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__sedfxtp_4.gds")


@gf.cell
def sky130_fd_sc_hd__tap_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__tap_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__tap_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__tap_1.gds")


@gf.cell
def sky130_fd_sc_hd__tap_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__tap_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__tap_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__tap_2.gds")


@gf.cell
def sky130_fd_sc_hd__tapvgnd2_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__tapvgnd2_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__tapvgnd2_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__tapvgnd2_1.gds")


@gf.cell
def sky130_fd_sc_hd__tapvgnd_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__tapvgnd_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__tapvgnd_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__tapvgnd_1.gds")


@gf.cell
def sky130_fd_sc_hd__tapvpwrvgnd_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__tapvpwrvgnd_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__tapvpwrvgnd_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__tapvpwrvgnd_1.gds")


@gf.cell
def sky130_fd_sc_hd__xnor2_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__xnor2_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__xnor2_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__xnor2_1.gds")


@gf.cell
def sky130_fd_sc_hd__xnor2_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__xnor2_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__xnor2_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__xnor2_2.gds")


@gf.cell
def sky130_fd_sc_hd__xnor2_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__xnor2_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__xnor2_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__xnor2_4.gds")


@gf.cell
def sky130_fd_sc_hd__xnor3_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__xnor3_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__xnor3_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__xnor3_1.gds")


@gf.cell
def sky130_fd_sc_hd__xnor3_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__xnor3_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__xnor3_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__xnor3_2.gds")


@gf.cell
def sky130_fd_sc_hd__xnor3_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__xnor3_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__xnor3_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__xnor3_4.gds")


@gf.cell
def sky130_fd_sc_hd__xor2_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__xor2_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__xor2_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__xor2_1.gds")


@gf.cell
def sky130_fd_sc_hd__xor2_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__xor2_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__xor2_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__xor2_2.gds")


@gf.cell
def sky130_fd_sc_hd__xor2_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__xor2_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__xor2_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__xor2_4.gds")


@gf.cell
def sky130_fd_sc_hd__xor3_1() -> gf.Component:
    """Returns sky130_fd_sc_hd__xor3_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__xor3_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__xor3_1.gds")


@gf.cell
def sky130_fd_sc_hd__xor3_2() -> gf.Component:
    """Returns sky130_fd_sc_hd__xor3_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__xor3_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__xor3_2.gds")


@gf.cell
def sky130_fd_sc_hd__xor3_4() -> gf.Component:
    """Returns sky130_fd_sc_hd__xor3_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hd__xor3_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hd__xor3_4.gds")


@gf.cell
def sky130_fd_sc_hs__a2111o_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__a2111o_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a2111o_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a2111o_1.gds")


@gf.cell
def sky130_fd_sc_hs__a2111o_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__a2111o_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a2111o_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a2111o_2.gds")


@gf.cell
def sky130_fd_sc_hs__a2111o_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__a2111o_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a2111o_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a2111o_4.gds")


@gf.cell
def sky130_fd_sc_hs__a2111oi_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__a2111oi_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a2111oi_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a2111oi_1.gds")


@gf.cell
def sky130_fd_sc_hs__a2111oi_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__a2111oi_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a2111oi_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a2111oi_2.gds")


@gf.cell
def sky130_fd_sc_hs__a2111oi_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__a2111oi_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a2111oi_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a2111oi_4.gds")


@gf.cell
def sky130_fd_sc_hs__a211o_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__a211o_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a211o_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a211o_1.gds")


@gf.cell
def sky130_fd_sc_hs__a211o_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__a211o_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a211o_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a211o_2.gds")


@gf.cell
def sky130_fd_sc_hs__a211o_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__a211o_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a211o_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a211o_4.gds")


@gf.cell
def sky130_fd_sc_hs__a211oi_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__a211oi_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a211oi_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a211oi_1.gds")


@gf.cell
def sky130_fd_sc_hs__a211oi_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__a211oi_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a211oi_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a211oi_2.gds")


@gf.cell
def sky130_fd_sc_hs__a211oi_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__a211oi_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a211oi_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a211oi_4.gds")


@gf.cell
def sky130_fd_sc_hs__a21bo_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__a21bo_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a21bo_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a21bo_1.gds")


@gf.cell
def sky130_fd_sc_hs__a21bo_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__a21bo_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a21bo_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a21bo_2.gds")


@gf.cell
def sky130_fd_sc_hs__a21bo_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__a21bo_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a21bo_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a21bo_4.gds")


@gf.cell
def sky130_fd_sc_hs__a21boi_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__a21boi_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a21boi_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a21boi_1.gds")


@gf.cell
def sky130_fd_sc_hs__a21boi_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__a21boi_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a21boi_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a21boi_2.gds")


@gf.cell
def sky130_fd_sc_hs__a21boi_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__a21boi_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a21boi_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a21boi_4.gds")


@gf.cell
def sky130_fd_sc_hs__a21o_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__a21o_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a21o_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a21o_1.gds")


@gf.cell
def sky130_fd_sc_hs__a21o_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__a21o_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a21o_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a21o_2.gds")


@gf.cell
def sky130_fd_sc_hs__a21o_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__a21o_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a21o_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a21o_4.gds")


@gf.cell
def sky130_fd_sc_hs__a21oi_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__a21oi_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a21oi_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a21oi_1.gds")


@gf.cell
def sky130_fd_sc_hs__a21oi_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__a21oi_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a21oi_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a21oi_2.gds")


@gf.cell
def sky130_fd_sc_hs__a21oi_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__a21oi_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a21oi_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a21oi_4.gds")


@gf.cell
def sky130_fd_sc_hs__a221o_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__a221o_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a221o_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a221o_1.gds")


@gf.cell
def sky130_fd_sc_hs__a221o_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__a221o_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a221o_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a221o_2.gds")


@gf.cell
def sky130_fd_sc_hs__a221o_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__a221o_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a221o_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a221o_4.gds")


@gf.cell
def sky130_fd_sc_hs__a221oi_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__a221oi_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a221oi_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a221oi_1.gds")


@gf.cell
def sky130_fd_sc_hs__a221oi_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__a221oi_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a221oi_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a221oi_2.gds")


@gf.cell
def sky130_fd_sc_hs__a221oi_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__a221oi_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a221oi_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a221oi_4.gds")


@gf.cell
def sky130_fd_sc_hs__a222o_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__a222o_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a222o_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a222o_1.gds")


@gf.cell
def sky130_fd_sc_hs__a222o_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__a222o_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a222o_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a222o_2.gds")


@gf.cell
def sky130_fd_sc_hs__a222oi_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__a222oi_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a222oi_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a222oi_1.gds")


@gf.cell
def sky130_fd_sc_hs__a222oi_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__a222oi_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a222oi_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a222oi_2.gds")


@gf.cell
def sky130_fd_sc_hs__a22o_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__a22o_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a22o_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a22o_1.gds")


@gf.cell
def sky130_fd_sc_hs__a22o_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__a22o_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a22o_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a22o_2.gds")


@gf.cell
def sky130_fd_sc_hs__a22o_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__a22o_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a22o_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a22o_4.gds")


@gf.cell
def sky130_fd_sc_hs__a22oi_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__a22oi_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a22oi_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a22oi_1.gds")


@gf.cell
def sky130_fd_sc_hs__a22oi_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__a22oi_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a22oi_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a22oi_2.gds")


@gf.cell
def sky130_fd_sc_hs__a22oi_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__a22oi_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a22oi_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a22oi_4.gds")


@gf.cell
def sky130_fd_sc_hs__a2bb2o_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__a2bb2o_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a2bb2o_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a2bb2o_1.gds")


@gf.cell
def sky130_fd_sc_hs__a2bb2o_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__a2bb2o_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a2bb2o_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a2bb2o_2.gds")


@gf.cell
def sky130_fd_sc_hs__a2bb2o_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__a2bb2o_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a2bb2o_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a2bb2o_4.gds")


@gf.cell
def sky130_fd_sc_hs__a2bb2oi_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__a2bb2oi_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a2bb2oi_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a2bb2oi_1.gds")


@gf.cell
def sky130_fd_sc_hs__a2bb2oi_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__a2bb2oi_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a2bb2oi_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a2bb2oi_2.gds")


@gf.cell
def sky130_fd_sc_hs__a2bb2oi_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__a2bb2oi_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a2bb2oi_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a2bb2oi_4.gds")


@gf.cell
def sky130_fd_sc_hs__a311o_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__a311o_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a311o_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a311o_1.gds")


@gf.cell
def sky130_fd_sc_hs__a311o_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__a311o_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a311o_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a311o_2.gds")


@gf.cell
def sky130_fd_sc_hs__a311o_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__a311o_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a311o_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a311o_4.gds")


@gf.cell
def sky130_fd_sc_hs__a311oi_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__a311oi_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a311oi_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a311oi_1.gds")


@gf.cell
def sky130_fd_sc_hs__a311oi_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__a311oi_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a311oi_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a311oi_2.gds")


@gf.cell
def sky130_fd_sc_hs__a311oi_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__a311oi_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a311oi_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a311oi_4.gds")


@gf.cell
def sky130_fd_sc_hs__a31o_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__a31o_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a31o_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a31o_1.gds")


@gf.cell
def sky130_fd_sc_hs__a31o_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__a31o_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a31o_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a31o_2.gds")


@gf.cell
def sky130_fd_sc_hs__a31o_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__a31o_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a31o_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a31o_4.gds")


@gf.cell
def sky130_fd_sc_hs__a31oi_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__a31oi_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a31oi_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a31oi_1.gds")


@gf.cell
def sky130_fd_sc_hs__a31oi_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__a31oi_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a31oi_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a31oi_2.gds")


@gf.cell
def sky130_fd_sc_hs__a31oi_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__a31oi_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a31oi_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a31oi_4.gds")


@gf.cell
def sky130_fd_sc_hs__a32o_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__a32o_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a32o_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a32o_1.gds")


@gf.cell
def sky130_fd_sc_hs__a32o_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__a32o_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a32o_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a32o_2.gds")


@gf.cell
def sky130_fd_sc_hs__a32o_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__a32o_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a32o_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a32o_4.gds")


@gf.cell
def sky130_fd_sc_hs__a32oi_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__a32oi_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a32oi_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a32oi_1.gds")


@gf.cell
def sky130_fd_sc_hs__a32oi_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__a32oi_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a32oi_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a32oi_2.gds")


@gf.cell
def sky130_fd_sc_hs__a32oi_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__a32oi_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a32oi_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a32oi_4.gds")


@gf.cell
def sky130_fd_sc_hs__a41o_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__a41o_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a41o_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a41o_1.gds")


@gf.cell
def sky130_fd_sc_hs__a41o_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__a41o_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a41o_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a41o_2.gds")


@gf.cell
def sky130_fd_sc_hs__a41o_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__a41o_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a41o_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a41o_4.gds")


@gf.cell
def sky130_fd_sc_hs__a41oi_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__a41oi_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a41oi_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a41oi_1.gds")


@gf.cell
def sky130_fd_sc_hs__a41oi_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__a41oi_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a41oi_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a41oi_2.gds")


@gf.cell
def sky130_fd_sc_hs__a41oi_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__a41oi_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__a41oi_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__a41oi_4.gds")


@gf.cell
def sky130_fd_sc_hs__and2_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__and2_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__and2_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__and2_1.gds")


@gf.cell
def sky130_fd_sc_hs__and2_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__and2_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__and2_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__and2_2.gds")


@gf.cell
def sky130_fd_sc_hs__and2_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__and2_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__and2_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__and2_4.gds")


@gf.cell
def sky130_fd_sc_hs__and2b_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__and2b_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__and2b_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__and2b_1.gds")


@gf.cell
def sky130_fd_sc_hs__and2b_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__and2b_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__and2b_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__and2b_2.gds")


@gf.cell
def sky130_fd_sc_hs__and2b_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__and2b_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__and2b_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__and2b_4.gds")


@gf.cell
def sky130_fd_sc_hs__and3_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__and3_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__and3_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__and3_1.gds")


@gf.cell
def sky130_fd_sc_hs__and3_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__and3_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__and3_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__and3_2.gds")


@gf.cell
def sky130_fd_sc_hs__and3_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__and3_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__and3_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__and3_4.gds")


@gf.cell
def sky130_fd_sc_hs__and3b_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__and3b_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__and3b_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__and3b_1.gds")


@gf.cell
def sky130_fd_sc_hs__and3b_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__and3b_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__and3b_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__and3b_2.gds")


@gf.cell
def sky130_fd_sc_hs__and3b_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__and3b_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__and3b_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__and3b_4.gds")


@gf.cell
def sky130_fd_sc_hs__and4_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__and4_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__and4_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__and4_1.gds")


@gf.cell
def sky130_fd_sc_hs__and4_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__and4_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__and4_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__and4_2.gds")


@gf.cell
def sky130_fd_sc_hs__and4_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__and4_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__and4_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__and4_4.gds")


@gf.cell
def sky130_fd_sc_hs__and4b_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__and4b_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__and4b_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__and4b_1.gds")


@gf.cell
def sky130_fd_sc_hs__and4b_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__and4b_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__and4b_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__and4b_2.gds")


@gf.cell
def sky130_fd_sc_hs__and4b_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__and4b_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__and4b_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__and4b_4.gds")


@gf.cell
def sky130_fd_sc_hs__and4bb_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__and4bb_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__and4bb_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__and4bb_1.gds")


@gf.cell
def sky130_fd_sc_hs__and4bb_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__and4bb_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__and4bb_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__and4bb_2.gds")


@gf.cell
def sky130_fd_sc_hs__and4bb_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__and4bb_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__and4bb_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__and4bb_4.gds")


@gf.cell
def sky130_fd_sc_hs__buf_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__buf_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__buf_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__buf_1.gds")


@gf.cell
def sky130_fd_sc_hs__buf_16() -> gf.Component:
    """Returns sky130_fd_sc_hs__buf_16 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__buf_16()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__buf_16.gds")


@gf.cell
def sky130_fd_sc_hs__buf_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__buf_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__buf_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__buf_2.gds")


@gf.cell
def sky130_fd_sc_hs__buf_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__buf_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__buf_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__buf_4.gds")


@gf.cell
def sky130_fd_sc_hs__buf_8() -> gf.Component:
    """Returns sky130_fd_sc_hs__buf_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__buf_8()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__buf_8.gds")


@gf.cell
def sky130_fd_sc_hs__bufbuf_16() -> gf.Component:
    """Returns sky130_fd_sc_hs__bufbuf_16 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__bufbuf_16()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__bufbuf_16.gds")


@gf.cell
def sky130_fd_sc_hs__bufbuf_8() -> gf.Component:
    """Returns sky130_fd_sc_hs__bufbuf_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__bufbuf_8()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__bufbuf_8.gds")


@gf.cell
def sky130_fd_sc_hs__bufinv_16() -> gf.Component:
    """Returns sky130_fd_sc_hs__bufinv_16 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__bufinv_16()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__bufinv_16.gds")


@gf.cell
def sky130_fd_sc_hs__bufinv_8() -> gf.Component:
    """Returns sky130_fd_sc_hs__bufinv_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__bufinv_8()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__bufinv_8.gds")


@gf.cell
def sky130_fd_sc_hs__clkbuf_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__clkbuf_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__clkbuf_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__clkbuf_1.gds")


@gf.cell
def sky130_fd_sc_hs__clkbuf_16() -> gf.Component:
    """Returns sky130_fd_sc_hs__clkbuf_16 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__clkbuf_16()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__clkbuf_16.gds")


@gf.cell
def sky130_fd_sc_hs__clkbuf_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__clkbuf_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__clkbuf_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__clkbuf_2.gds")


@gf.cell
def sky130_fd_sc_hs__clkbuf_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__clkbuf_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__clkbuf_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__clkbuf_4.gds")


@gf.cell
def sky130_fd_sc_hs__clkbuf_8() -> gf.Component:
    """Returns sky130_fd_sc_hs__clkbuf_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__clkbuf_8()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__clkbuf_8.gds")


@gf.cell
def sky130_fd_sc_hs__clkdlyinv3sd1_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__clkdlyinv3sd1_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__clkdlyinv3sd1_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__clkdlyinv3sd1_1.gds")


@gf.cell
def sky130_fd_sc_hs__clkdlyinv3sd2_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__clkdlyinv3sd2_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__clkdlyinv3sd2_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__clkdlyinv3sd2_1.gds")


@gf.cell
def sky130_fd_sc_hs__clkdlyinv3sd3_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__clkdlyinv3sd3_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__clkdlyinv3sd3_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__clkdlyinv3sd3_1.gds")


@gf.cell
def sky130_fd_sc_hs__clkdlyinv5sd1_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__clkdlyinv5sd1_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__clkdlyinv5sd1_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__clkdlyinv5sd1_1.gds")


@gf.cell
def sky130_fd_sc_hs__clkdlyinv5sd2_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__clkdlyinv5sd2_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__clkdlyinv5sd2_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__clkdlyinv5sd2_1.gds")


@gf.cell
def sky130_fd_sc_hs__clkdlyinv5sd3_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__clkdlyinv5sd3_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__clkdlyinv5sd3_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__clkdlyinv5sd3_1.gds")


@gf.cell
def sky130_fd_sc_hs__clkinv_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__clkinv_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__clkinv_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__clkinv_1.gds")


@gf.cell
def sky130_fd_sc_hs__clkinv_16() -> gf.Component:
    """Returns sky130_fd_sc_hs__clkinv_16 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__clkinv_16()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__clkinv_16.gds")


@gf.cell
def sky130_fd_sc_hs__clkinv_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__clkinv_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__clkinv_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__clkinv_2.gds")


@gf.cell
def sky130_fd_sc_hs__clkinv_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__clkinv_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__clkinv_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__clkinv_4.gds")


@gf.cell
def sky130_fd_sc_hs__clkinv_8() -> gf.Component:
    """Returns sky130_fd_sc_hs__clkinv_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__clkinv_8()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__clkinv_8.gds")


@gf.cell
def sky130_fd_sc_hs__conb_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__conb_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__conb_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__conb_1.gds")


@gf.cell
def sky130_fd_sc_hs__decap_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__decap_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__decap_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__decap_4.gds")


@gf.cell
def sky130_fd_sc_hs__decap_8() -> gf.Component:
    """Returns sky130_fd_sc_hs__decap_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__decap_8()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__decap_8.gds")


@gf.cell
def sky130_fd_sc_hs__dfbbn_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__dfbbn_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dfbbn_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dfbbn_1.gds")


@gf.cell
def sky130_fd_sc_hs__dfbbn_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__dfbbn_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dfbbn_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dfbbn_2.gds")


@gf.cell
def sky130_fd_sc_hs__dfbbp_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__dfbbp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dfbbp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dfbbp_1.gds")


@gf.cell
def sky130_fd_sc_hs__dfrbp_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__dfrbp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dfrbp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dfrbp_1.gds")


@gf.cell
def sky130_fd_sc_hs__dfrbp_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__dfrbp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dfrbp_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dfrbp_2.gds")


@gf.cell
def sky130_fd_sc_hs__dfrtn_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__dfrtn_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dfrtn_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dfrtn_1.gds")


@gf.cell
def sky130_fd_sc_hs__dfrtp_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__dfrtp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dfrtp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dfrtp_1.gds")


@gf.cell
def sky130_fd_sc_hs__dfrtp_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__dfrtp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dfrtp_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dfrtp_2.gds")


@gf.cell
def sky130_fd_sc_hs__dfrtp_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__dfrtp_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dfrtp_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dfrtp_4.gds")


@gf.cell
def sky130_fd_sc_hs__dfsbp_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__dfsbp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dfsbp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dfsbp_1.gds")


@gf.cell
def sky130_fd_sc_hs__dfsbp_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__dfsbp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dfsbp_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dfsbp_2.gds")


@gf.cell
def sky130_fd_sc_hs__dfstp_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__dfstp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dfstp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dfstp_1.gds")


@gf.cell
def sky130_fd_sc_hs__dfstp_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__dfstp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dfstp_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dfstp_2.gds")


@gf.cell
def sky130_fd_sc_hs__dfstp_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__dfstp_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dfstp_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dfstp_4.gds")


@gf.cell
def sky130_fd_sc_hs__dfxbp_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__dfxbp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dfxbp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dfxbp_1.gds")


@gf.cell
def sky130_fd_sc_hs__dfxbp_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__dfxbp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dfxbp_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dfxbp_2.gds")


@gf.cell
def sky130_fd_sc_hs__dfxtp_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__dfxtp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dfxtp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dfxtp_1.gds")


@gf.cell
def sky130_fd_sc_hs__dfxtp_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__dfxtp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dfxtp_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dfxtp_2.gds")


@gf.cell
def sky130_fd_sc_hs__dfxtp_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__dfxtp_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dfxtp_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dfxtp_4.gds")


@gf.cell
def sky130_fd_sc_hs__diode_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__diode_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__diode_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__diode_2.gds")


@gf.cell
def sky130_fd_sc_hs__dlclkp_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__dlclkp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dlclkp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dlclkp_1.gds")


@gf.cell
def sky130_fd_sc_hs__dlclkp_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__dlclkp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dlclkp_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dlclkp_2.gds")


@gf.cell
def sky130_fd_sc_hs__dlclkp_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__dlclkp_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dlclkp_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dlclkp_4.gds")


@gf.cell
def sky130_fd_sc_hs__dlrbn_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__dlrbn_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dlrbn_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dlrbn_1.gds")


@gf.cell
def sky130_fd_sc_hs__dlrbn_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__dlrbn_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dlrbn_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dlrbn_2.gds")


@gf.cell
def sky130_fd_sc_hs__dlrbp_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__dlrbp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dlrbp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dlrbp_1.gds")


@gf.cell
def sky130_fd_sc_hs__dlrbp_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__dlrbp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dlrbp_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dlrbp_2.gds")


@gf.cell
def sky130_fd_sc_hs__dlrtn_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__dlrtn_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dlrtn_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dlrtn_1.gds")


@gf.cell
def sky130_fd_sc_hs__dlrtn_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__dlrtn_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dlrtn_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dlrtn_2.gds")


@gf.cell
def sky130_fd_sc_hs__dlrtn_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__dlrtn_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dlrtn_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dlrtn_4.gds")


@gf.cell
def sky130_fd_sc_hs__dlrtp_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__dlrtp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dlrtp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dlrtp_1.gds")


@gf.cell
def sky130_fd_sc_hs__dlrtp_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__dlrtp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dlrtp_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dlrtp_2.gds")


@gf.cell
def sky130_fd_sc_hs__dlrtp_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__dlrtp_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dlrtp_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dlrtp_4.gds")


@gf.cell
def sky130_fd_sc_hs__dlxbn_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__dlxbn_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dlxbn_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dlxbn_1.gds")


@gf.cell
def sky130_fd_sc_hs__dlxbn_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__dlxbn_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dlxbn_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dlxbn_2.gds")


@gf.cell
def sky130_fd_sc_hs__dlxbp_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__dlxbp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dlxbp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dlxbp_1.gds")


@gf.cell
def sky130_fd_sc_hs__dlxtn_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__dlxtn_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dlxtn_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dlxtn_1.gds")


@gf.cell
def sky130_fd_sc_hs__dlxtn_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__dlxtn_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dlxtn_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dlxtn_2.gds")


@gf.cell
def sky130_fd_sc_hs__dlxtn_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__dlxtn_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dlxtn_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dlxtn_4.gds")


@gf.cell
def sky130_fd_sc_hs__dlxtp_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__dlxtp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dlxtp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dlxtp_1.gds")


@gf.cell
def sky130_fd_sc_hs__dlygate4sd1_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__dlygate4sd1_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dlygate4sd1_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dlygate4sd1_1.gds")


@gf.cell
def sky130_fd_sc_hs__dlygate4sd2_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__dlygate4sd2_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dlygate4sd2_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dlygate4sd2_1.gds")


@gf.cell
def sky130_fd_sc_hs__dlygate4sd3_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__dlygate4sd3_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dlygate4sd3_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dlygate4sd3_1.gds")


@gf.cell
def sky130_fd_sc_hs__dlymetal6s2s_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__dlymetal6s2s_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dlymetal6s2s_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dlymetal6s2s_1.gds")


@gf.cell
def sky130_fd_sc_hs__dlymetal6s4s_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__dlymetal6s4s_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dlymetal6s4s_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dlymetal6s4s_1.gds")


@gf.cell
def sky130_fd_sc_hs__dlymetal6s6s_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__dlymetal6s6s_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__dlymetal6s6s_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__dlymetal6s6s_1.gds")


@gf.cell
def sky130_fd_sc_hs__ebufn_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__ebufn_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__ebufn_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__ebufn_1.gds")


@gf.cell
def sky130_fd_sc_hs__ebufn_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__ebufn_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__ebufn_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__ebufn_2.gds")


@gf.cell
def sky130_fd_sc_hs__ebufn_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__ebufn_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__ebufn_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__ebufn_4.gds")


@gf.cell
def sky130_fd_sc_hs__ebufn_8() -> gf.Component:
    """Returns sky130_fd_sc_hs__ebufn_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__ebufn_8()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__ebufn_8.gds")


@gf.cell
def sky130_fd_sc_hs__edfxbp_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__edfxbp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__edfxbp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__edfxbp_1.gds")


@gf.cell
def sky130_fd_sc_hs__edfxtp_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__edfxtp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__edfxtp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__edfxtp_1.gds")


@gf.cell
def sky130_fd_sc_hs__einvn_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__einvn_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__einvn_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__einvn_1.gds")


@gf.cell
def sky130_fd_sc_hs__einvn_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__einvn_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__einvn_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__einvn_2.gds")


@gf.cell
def sky130_fd_sc_hs__einvn_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__einvn_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__einvn_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__einvn_4.gds")


@gf.cell
def sky130_fd_sc_hs__einvn_8() -> gf.Component:
    """Returns sky130_fd_sc_hs__einvn_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__einvn_8()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__einvn_8.gds")


@gf.cell
def sky130_fd_sc_hs__einvp_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__einvp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__einvp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__einvp_1.gds")


@gf.cell
def sky130_fd_sc_hs__einvp_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__einvp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__einvp_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__einvp_2.gds")


@gf.cell
def sky130_fd_sc_hs__einvp_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__einvp_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__einvp_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__einvp_4.gds")


@gf.cell
def sky130_fd_sc_hs__einvp_8() -> gf.Component:
    """Returns sky130_fd_sc_hs__einvp_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__einvp_8()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__einvp_8.gds")


@gf.cell
def sky130_fd_sc_hs__fa_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__fa_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__fa_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__fa_1.gds")


@gf.cell
def sky130_fd_sc_hs__fa_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__fa_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__fa_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__fa_2.gds")


@gf.cell
def sky130_fd_sc_hs__fa_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__fa_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__fa_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__fa_4.gds")


@gf.cell
def sky130_fd_sc_hs__fah_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__fah_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__fah_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__fah_1.gds")


@gf.cell
def sky130_fd_sc_hs__fah_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__fah_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__fah_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__fah_2.gds")


@gf.cell
def sky130_fd_sc_hs__fah_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__fah_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__fah_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__fah_4.gds")


@gf.cell
def sky130_fd_sc_hs__fahcin_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__fahcin_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__fahcin_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__fahcin_1.gds")


@gf.cell
def sky130_fd_sc_hs__fahcon_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__fahcon_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__fahcon_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__fahcon_1.gds")


@gf.cell
def sky130_fd_sc_hs__fill_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__fill_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__fill_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__fill_1.gds")


@gf.cell
def sky130_fd_sc_hs__fill_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__fill_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__fill_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__fill_2.gds")


@gf.cell
def sky130_fd_sc_hs__fill_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__fill_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__fill_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__fill_4.gds")


@gf.cell
def sky130_fd_sc_hs__fill_8() -> gf.Component:
    """Returns sky130_fd_sc_hs__fill_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__fill_8()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__fill_8.gds")


@gf.cell
def sky130_fd_sc_hs__fill_diode_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__fill_diode_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__fill_diode_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__fill_diode_2.gds")


@gf.cell
def sky130_fd_sc_hs__fill_diode_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__fill_diode_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__fill_diode_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__fill_diode_4.gds")


@gf.cell
def sky130_fd_sc_hs__fill_diode_8() -> gf.Component:
    """Returns sky130_fd_sc_hs__fill_diode_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__fill_diode_8()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__fill_diode_8.gds")


@gf.cell
def sky130_fd_sc_hs__ha_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__ha_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__ha_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__ha_1.gds")


@gf.cell
def sky130_fd_sc_hs__ha_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__ha_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__ha_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__ha_2.gds")


@gf.cell
def sky130_fd_sc_hs__ha_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__ha_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__ha_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__ha_4.gds")


@gf.cell
def sky130_fd_sc_hs__inv_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__inv_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__inv_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__inv_1.gds")


@gf.cell
def sky130_fd_sc_hs__inv_16() -> gf.Component:
    """Returns sky130_fd_sc_hs__inv_16 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__inv_16()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__inv_16.gds")


@gf.cell
def sky130_fd_sc_hs__inv_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__inv_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__inv_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__inv_2.gds")


@gf.cell
def sky130_fd_sc_hs__inv_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__inv_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__inv_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__inv_4.gds")


@gf.cell
def sky130_fd_sc_hs__inv_8() -> gf.Component:
    """Returns sky130_fd_sc_hs__inv_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__inv_8()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__inv_8.gds")


@gf.cell
def sky130_fd_sc_hs__maj3_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__maj3_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__maj3_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__maj3_1.gds")


@gf.cell
def sky130_fd_sc_hs__maj3_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__maj3_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__maj3_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__maj3_2.gds")


@gf.cell
def sky130_fd_sc_hs__maj3_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__maj3_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__maj3_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__maj3_4.gds")


@gf.cell
def sky130_fd_sc_hs__mux2_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__mux2_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__mux2_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__mux2_1.gds")


@gf.cell
def sky130_fd_sc_hs__mux2_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__mux2_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__mux2_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__mux2_2.gds")


@gf.cell
def sky130_fd_sc_hs__mux2_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__mux2_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__mux2_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__mux2_4.gds")


@gf.cell
def sky130_fd_sc_hs__mux2i_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__mux2i_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__mux2i_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__mux2i_1.gds")


@gf.cell
def sky130_fd_sc_hs__mux2i_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__mux2i_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__mux2i_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__mux2i_2.gds")


@gf.cell
def sky130_fd_sc_hs__mux2i_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__mux2i_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__mux2i_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__mux2i_4.gds")


@gf.cell
def sky130_fd_sc_hs__mux4_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__mux4_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__mux4_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__mux4_1.gds")


@gf.cell
def sky130_fd_sc_hs__mux4_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__mux4_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__mux4_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__mux4_2.gds")


@gf.cell
def sky130_fd_sc_hs__mux4_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__mux4_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__mux4_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__mux4_4.gds")


@gf.cell
def sky130_fd_sc_hs__nand2_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__nand2_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__nand2_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__nand2_1.gds")


@gf.cell
def sky130_fd_sc_hs__nand2_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__nand2_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__nand2_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__nand2_2.gds")


@gf.cell
def sky130_fd_sc_hs__nand2_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__nand2_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__nand2_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__nand2_4.gds")


@gf.cell
def sky130_fd_sc_hs__nand2_8() -> gf.Component:
    """Returns sky130_fd_sc_hs__nand2_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__nand2_8()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__nand2_8.gds")


@gf.cell
def sky130_fd_sc_hs__nand2b_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__nand2b_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__nand2b_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__nand2b_1.gds")


@gf.cell
def sky130_fd_sc_hs__nand2b_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__nand2b_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__nand2b_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__nand2b_2.gds")


@gf.cell
def sky130_fd_sc_hs__nand2b_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__nand2b_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__nand2b_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__nand2b_4.gds")


@gf.cell
def sky130_fd_sc_hs__nand3_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__nand3_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__nand3_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__nand3_1.gds")


@gf.cell
def sky130_fd_sc_hs__nand3_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__nand3_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__nand3_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__nand3_2.gds")


@gf.cell
def sky130_fd_sc_hs__nand3_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__nand3_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__nand3_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__nand3_4.gds")


@gf.cell
def sky130_fd_sc_hs__nand3b_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__nand3b_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__nand3b_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__nand3b_1.gds")


@gf.cell
def sky130_fd_sc_hs__nand3b_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__nand3b_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__nand3b_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__nand3b_2.gds")


@gf.cell
def sky130_fd_sc_hs__nand3b_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__nand3b_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__nand3b_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__nand3b_4.gds")


@gf.cell
def sky130_fd_sc_hs__nand4_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__nand4_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__nand4_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__nand4_1.gds")


@gf.cell
def sky130_fd_sc_hs__nand4_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__nand4_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__nand4_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__nand4_2.gds")


@gf.cell
def sky130_fd_sc_hs__nand4_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__nand4_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__nand4_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__nand4_4.gds")


@gf.cell
def sky130_fd_sc_hs__nand4b_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__nand4b_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__nand4b_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__nand4b_1.gds")


@gf.cell
def sky130_fd_sc_hs__nand4b_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__nand4b_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__nand4b_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__nand4b_2.gds")


@gf.cell
def sky130_fd_sc_hs__nand4b_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__nand4b_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__nand4b_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__nand4b_4.gds")


@gf.cell
def sky130_fd_sc_hs__nand4bb_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__nand4bb_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__nand4bb_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__nand4bb_1.gds")


@gf.cell
def sky130_fd_sc_hs__nand4bb_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__nand4bb_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__nand4bb_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__nand4bb_2.gds")


@gf.cell
def sky130_fd_sc_hs__nand4bb_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__nand4bb_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__nand4bb_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__nand4bb_4.gds")


@gf.cell
def sky130_fd_sc_hs__nor2_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__nor2_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__nor2_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__nor2_1.gds")


@gf.cell
def sky130_fd_sc_hs__nor2_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__nor2_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__nor2_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__nor2_2.gds")


@gf.cell
def sky130_fd_sc_hs__nor2_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__nor2_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__nor2_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__nor2_4.gds")


@gf.cell
def sky130_fd_sc_hs__nor2_8() -> gf.Component:
    """Returns sky130_fd_sc_hs__nor2_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__nor2_8()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__nor2_8.gds")


@gf.cell
def sky130_fd_sc_hs__nor2b_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__nor2b_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__nor2b_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__nor2b_1.gds")


@gf.cell
def sky130_fd_sc_hs__nor2b_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__nor2b_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__nor2b_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__nor2b_2.gds")


@gf.cell
def sky130_fd_sc_hs__nor2b_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__nor2b_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__nor2b_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__nor2b_4.gds")


@gf.cell
def sky130_fd_sc_hs__nor3_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__nor3_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__nor3_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__nor3_1.gds")


@gf.cell
def sky130_fd_sc_hs__nor3_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__nor3_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__nor3_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__nor3_2.gds")


@gf.cell
def sky130_fd_sc_hs__nor3_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__nor3_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__nor3_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__nor3_4.gds")


@gf.cell
def sky130_fd_sc_hs__nor3b_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__nor3b_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__nor3b_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__nor3b_1.gds")


@gf.cell
def sky130_fd_sc_hs__nor3b_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__nor3b_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__nor3b_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__nor3b_2.gds")


@gf.cell
def sky130_fd_sc_hs__nor3b_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__nor3b_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__nor3b_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__nor3b_4.gds")


@gf.cell
def sky130_fd_sc_hs__nor4_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__nor4_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__nor4_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__nor4_1.gds")


@gf.cell
def sky130_fd_sc_hs__nor4_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__nor4_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__nor4_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__nor4_2.gds")


@gf.cell
def sky130_fd_sc_hs__nor4_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__nor4_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__nor4_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__nor4_4.gds")


@gf.cell
def sky130_fd_sc_hs__nor4b_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__nor4b_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__nor4b_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__nor4b_1.gds")


@gf.cell
def sky130_fd_sc_hs__nor4b_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__nor4b_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__nor4b_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__nor4b_2.gds")


@gf.cell
def sky130_fd_sc_hs__nor4b_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__nor4b_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__nor4b_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__nor4b_4.gds")


@gf.cell
def sky130_fd_sc_hs__nor4bb_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__nor4bb_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__nor4bb_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__nor4bb_1.gds")


@gf.cell
def sky130_fd_sc_hs__nor4bb_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__nor4bb_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__nor4bb_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__nor4bb_2.gds")


@gf.cell
def sky130_fd_sc_hs__nor4bb_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__nor4bb_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__nor4bb_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__nor4bb_4.gds")


@gf.cell
def sky130_fd_sc_hs__o2111a_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__o2111a_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o2111a_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o2111a_1.gds")


@gf.cell
def sky130_fd_sc_hs__o2111a_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__o2111a_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o2111a_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o2111a_2.gds")


@gf.cell
def sky130_fd_sc_hs__o2111a_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__o2111a_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o2111a_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o2111a_4.gds")


@gf.cell
def sky130_fd_sc_hs__o2111ai_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__o2111ai_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o2111ai_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o2111ai_1.gds")


@gf.cell
def sky130_fd_sc_hs__o2111ai_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__o2111ai_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o2111ai_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o2111ai_2.gds")


@gf.cell
def sky130_fd_sc_hs__o2111ai_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__o2111ai_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o2111ai_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o2111ai_4.gds")


@gf.cell
def sky130_fd_sc_hs__o211a_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__o211a_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o211a_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o211a_1.gds")


@gf.cell
def sky130_fd_sc_hs__o211a_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__o211a_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o211a_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o211a_2.gds")


@gf.cell
def sky130_fd_sc_hs__o211a_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__o211a_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o211a_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o211a_4.gds")


@gf.cell
def sky130_fd_sc_hs__o211ai_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__o211ai_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o211ai_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o211ai_1.gds")


@gf.cell
def sky130_fd_sc_hs__o211ai_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__o211ai_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o211ai_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o211ai_2.gds")


@gf.cell
def sky130_fd_sc_hs__o211ai_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__o211ai_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o211ai_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o211ai_4.gds")


@gf.cell
def sky130_fd_sc_hs__o21a_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__o21a_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o21a_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o21a_1.gds")


@gf.cell
def sky130_fd_sc_hs__o21a_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__o21a_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o21a_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o21a_2.gds")


@gf.cell
def sky130_fd_sc_hs__o21a_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__o21a_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o21a_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o21a_4.gds")


@gf.cell
def sky130_fd_sc_hs__o21ai_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__o21ai_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o21ai_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o21ai_1.gds")


@gf.cell
def sky130_fd_sc_hs__o21ai_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__o21ai_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o21ai_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o21ai_2.gds")


@gf.cell
def sky130_fd_sc_hs__o21ai_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__o21ai_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o21ai_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o21ai_4.gds")


@gf.cell
def sky130_fd_sc_hs__o21ba_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__o21ba_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o21ba_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o21ba_1.gds")


@gf.cell
def sky130_fd_sc_hs__o21ba_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__o21ba_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o21ba_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o21ba_2.gds")


@gf.cell
def sky130_fd_sc_hs__o21ba_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__o21ba_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o21ba_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o21ba_4.gds")


@gf.cell
def sky130_fd_sc_hs__o21bai_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__o21bai_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o21bai_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o21bai_1.gds")


@gf.cell
def sky130_fd_sc_hs__o21bai_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__o21bai_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o21bai_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o21bai_2.gds")


@gf.cell
def sky130_fd_sc_hs__o21bai_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__o21bai_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o21bai_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o21bai_4.gds")


@gf.cell
def sky130_fd_sc_hs__o221a_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__o221a_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o221a_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o221a_1.gds")


@gf.cell
def sky130_fd_sc_hs__o221a_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__o221a_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o221a_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o221a_2.gds")


@gf.cell
def sky130_fd_sc_hs__o221a_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__o221a_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o221a_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o221a_4.gds")


@gf.cell
def sky130_fd_sc_hs__o221ai_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__o221ai_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o221ai_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o221ai_1.gds")


@gf.cell
def sky130_fd_sc_hs__o221ai_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__o221ai_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o221ai_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o221ai_2.gds")


@gf.cell
def sky130_fd_sc_hs__o221ai_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__o221ai_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o221ai_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o221ai_4.gds")


@gf.cell
def sky130_fd_sc_hs__o22a_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__o22a_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o22a_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o22a_1.gds")


@gf.cell
def sky130_fd_sc_hs__o22a_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__o22a_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o22a_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o22a_2.gds")


@gf.cell
def sky130_fd_sc_hs__o22a_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__o22a_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o22a_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o22a_4.gds")


@gf.cell
def sky130_fd_sc_hs__o22ai_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__o22ai_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o22ai_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o22ai_1.gds")


@gf.cell
def sky130_fd_sc_hs__o22ai_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__o22ai_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o22ai_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o22ai_2.gds")


@gf.cell
def sky130_fd_sc_hs__o22ai_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__o22ai_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o22ai_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o22ai_4.gds")


@gf.cell
def sky130_fd_sc_hs__o2bb2a_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__o2bb2a_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o2bb2a_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o2bb2a_1.gds")


@gf.cell
def sky130_fd_sc_hs__o2bb2a_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__o2bb2a_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o2bb2a_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o2bb2a_2.gds")


@gf.cell
def sky130_fd_sc_hs__o2bb2a_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__o2bb2a_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o2bb2a_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o2bb2a_4.gds")


@gf.cell
def sky130_fd_sc_hs__o2bb2ai_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__o2bb2ai_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o2bb2ai_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o2bb2ai_1.gds")


@gf.cell
def sky130_fd_sc_hs__o2bb2ai_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__o2bb2ai_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o2bb2ai_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o2bb2ai_2.gds")


@gf.cell
def sky130_fd_sc_hs__o2bb2ai_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__o2bb2ai_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o2bb2ai_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o2bb2ai_4.gds")


@gf.cell
def sky130_fd_sc_hs__o311a_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__o311a_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o311a_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o311a_1.gds")


@gf.cell
def sky130_fd_sc_hs__o311a_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__o311a_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o311a_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o311a_2.gds")


@gf.cell
def sky130_fd_sc_hs__o311a_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__o311a_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o311a_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o311a_4.gds")


@gf.cell
def sky130_fd_sc_hs__o311ai_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__o311ai_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o311ai_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o311ai_1.gds")


@gf.cell
def sky130_fd_sc_hs__o311ai_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__o311ai_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o311ai_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o311ai_2.gds")


@gf.cell
def sky130_fd_sc_hs__o311ai_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__o311ai_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o311ai_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o311ai_4.gds")


@gf.cell
def sky130_fd_sc_hs__o31a_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__o31a_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o31a_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o31a_1.gds")


@gf.cell
def sky130_fd_sc_hs__o31a_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__o31a_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o31a_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o31a_2.gds")


@gf.cell
def sky130_fd_sc_hs__o31a_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__o31a_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o31a_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o31a_4.gds")


@gf.cell
def sky130_fd_sc_hs__o31ai_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__o31ai_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o31ai_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o31ai_1.gds")


@gf.cell
def sky130_fd_sc_hs__o31ai_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__o31ai_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o31ai_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o31ai_2.gds")


@gf.cell
def sky130_fd_sc_hs__o31ai_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__o31ai_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o31ai_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o31ai_4.gds")


@gf.cell
def sky130_fd_sc_hs__o32a_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__o32a_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o32a_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o32a_1.gds")


@gf.cell
def sky130_fd_sc_hs__o32a_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__o32a_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o32a_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o32a_2.gds")


@gf.cell
def sky130_fd_sc_hs__o32a_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__o32a_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o32a_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o32a_4.gds")


@gf.cell
def sky130_fd_sc_hs__o32ai_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__o32ai_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o32ai_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o32ai_1.gds")


@gf.cell
def sky130_fd_sc_hs__o32ai_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__o32ai_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o32ai_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o32ai_2.gds")


@gf.cell
def sky130_fd_sc_hs__o32ai_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__o32ai_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o32ai_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o32ai_4.gds")


@gf.cell
def sky130_fd_sc_hs__o41a_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__o41a_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o41a_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o41a_1.gds")


@gf.cell
def sky130_fd_sc_hs__o41a_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__o41a_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o41a_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o41a_2.gds")


@gf.cell
def sky130_fd_sc_hs__o41a_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__o41a_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o41a_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o41a_4.gds")


@gf.cell
def sky130_fd_sc_hs__o41ai_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__o41ai_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o41ai_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o41ai_1.gds")


@gf.cell
def sky130_fd_sc_hs__o41ai_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__o41ai_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o41ai_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o41ai_2.gds")


@gf.cell
def sky130_fd_sc_hs__o41ai_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__o41ai_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__o41ai_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__o41ai_4.gds")


@gf.cell
def sky130_fd_sc_hs__or2_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__or2_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__or2_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__or2_1.gds")


@gf.cell
def sky130_fd_sc_hs__or2_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__or2_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__or2_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__or2_2.gds")


@gf.cell
def sky130_fd_sc_hs__or2_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__or2_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__or2_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__or2_4.gds")


@gf.cell
def sky130_fd_sc_hs__or2b_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__or2b_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__or2b_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__or2b_1.gds")


@gf.cell
def sky130_fd_sc_hs__or2b_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__or2b_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__or2b_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__or2b_2.gds")


@gf.cell
def sky130_fd_sc_hs__or2b_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__or2b_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__or2b_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__or2b_4.gds")


@gf.cell
def sky130_fd_sc_hs__or3_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__or3_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__or3_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__or3_1.gds")


@gf.cell
def sky130_fd_sc_hs__or3_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__or3_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__or3_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__or3_2.gds")


@gf.cell
def sky130_fd_sc_hs__or3_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__or3_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__or3_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__or3_4.gds")


@gf.cell
def sky130_fd_sc_hs__or3b_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__or3b_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__or3b_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__or3b_1.gds")


@gf.cell
def sky130_fd_sc_hs__or3b_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__or3b_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__or3b_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__or3b_2.gds")


@gf.cell
def sky130_fd_sc_hs__or3b_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__or3b_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__or3b_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__or3b_4.gds")


@gf.cell
def sky130_fd_sc_hs__or4_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__or4_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__or4_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__or4_1.gds")


@gf.cell
def sky130_fd_sc_hs__or4_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__or4_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__or4_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__or4_2.gds")


@gf.cell
def sky130_fd_sc_hs__or4_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__or4_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__or4_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__or4_4.gds")


@gf.cell
def sky130_fd_sc_hs__or4b_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__or4b_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__or4b_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__or4b_1.gds")


@gf.cell
def sky130_fd_sc_hs__or4b_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__or4b_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__or4b_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__or4b_2.gds")


@gf.cell
def sky130_fd_sc_hs__or4b_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__or4b_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__or4b_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__or4b_4.gds")


@gf.cell
def sky130_fd_sc_hs__or4bb_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__or4bb_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__or4bb_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__or4bb_1.gds")


@gf.cell
def sky130_fd_sc_hs__or4bb_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__or4bb_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__or4bb_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__or4bb_2.gds")


@gf.cell
def sky130_fd_sc_hs__or4bb_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__or4bb_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__or4bb_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__or4bb_4.gds")


@gf.cell
def sky130_fd_sc_hs__sdfbbn_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__sdfbbn_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__sdfbbn_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__sdfbbn_1.gds")


@gf.cell
def sky130_fd_sc_hs__sdfbbn_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__sdfbbn_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__sdfbbn_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__sdfbbn_2.gds")


@gf.cell
def sky130_fd_sc_hs__sdfbbp_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__sdfbbp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__sdfbbp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__sdfbbp_1.gds")


@gf.cell
def sky130_fd_sc_hs__sdfrbp_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__sdfrbp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__sdfrbp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__sdfrbp_1.gds")


@gf.cell
def sky130_fd_sc_hs__sdfrbp_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__sdfrbp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__sdfrbp_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__sdfrbp_2.gds")


@gf.cell
def sky130_fd_sc_hs__sdfrtn_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__sdfrtn_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__sdfrtn_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__sdfrtn_1.gds")


@gf.cell
def sky130_fd_sc_hs__sdfrtp_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__sdfrtp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__sdfrtp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__sdfrtp_1.gds")


@gf.cell
def sky130_fd_sc_hs__sdfrtp_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__sdfrtp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__sdfrtp_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__sdfrtp_2.gds")


@gf.cell
def sky130_fd_sc_hs__sdfrtp_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__sdfrtp_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__sdfrtp_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__sdfrtp_4.gds")


@gf.cell
def sky130_fd_sc_hs__sdfsbp_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__sdfsbp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__sdfsbp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__sdfsbp_1.gds")


@gf.cell
def sky130_fd_sc_hs__sdfsbp_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__sdfsbp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__sdfsbp_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__sdfsbp_2.gds")


@gf.cell
def sky130_fd_sc_hs__sdfstp_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__sdfstp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__sdfstp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__sdfstp_1.gds")


@gf.cell
def sky130_fd_sc_hs__sdfstp_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__sdfstp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__sdfstp_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__sdfstp_2.gds")


@gf.cell
def sky130_fd_sc_hs__sdfstp_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__sdfstp_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__sdfstp_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__sdfstp_4.gds")


@gf.cell
def sky130_fd_sc_hs__sdfxbp_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__sdfxbp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__sdfxbp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__sdfxbp_1.gds")


@gf.cell
def sky130_fd_sc_hs__sdfxbp_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__sdfxbp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__sdfxbp_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__sdfxbp_2.gds")


@gf.cell
def sky130_fd_sc_hs__sdfxtp_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__sdfxtp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__sdfxtp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__sdfxtp_1.gds")


@gf.cell
def sky130_fd_sc_hs__sdfxtp_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__sdfxtp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__sdfxtp_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__sdfxtp_2.gds")


@gf.cell
def sky130_fd_sc_hs__sdfxtp_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__sdfxtp_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__sdfxtp_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__sdfxtp_4.gds")


@gf.cell
def sky130_fd_sc_hs__sdlclkp_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__sdlclkp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__sdlclkp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__sdlclkp_1.gds")


@gf.cell
def sky130_fd_sc_hs__sdlclkp_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__sdlclkp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__sdlclkp_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__sdlclkp_2.gds")


@gf.cell
def sky130_fd_sc_hs__sdlclkp_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__sdlclkp_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__sdlclkp_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__sdlclkp_4.gds")


@gf.cell
def sky130_fd_sc_hs__sedfxbp_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__sedfxbp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__sedfxbp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__sedfxbp_1.gds")


@gf.cell
def sky130_fd_sc_hs__sedfxbp_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__sedfxbp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__sedfxbp_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__sedfxbp_2.gds")


@gf.cell
def sky130_fd_sc_hs__sedfxtp_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__sedfxtp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__sedfxtp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__sedfxtp_1.gds")


@gf.cell
def sky130_fd_sc_hs__sedfxtp_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__sedfxtp_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__sedfxtp_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__sedfxtp_2.gds")


@gf.cell
def sky130_fd_sc_hs__sedfxtp_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__sedfxtp_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__sedfxtp_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__sedfxtp_4.gds")


@gf.cell
def sky130_fd_sc_hs__tap_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__tap_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__tap_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__tap_1.gds")


@gf.cell
def sky130_fd_sc_hs__tap_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__tap_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__tap_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__tap_2.gds")


@gf.cell
def sky130_fd_sc_hs__tapmet1_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__tapmet1_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__tapmet1_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__tapmet1_2.gds")


@gf.cell
def sky130_fd_sc_hs__tapvgnd2_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__tapvgnd2_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__tapvgnd2_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__tapvgnd2_1.gds")


@gf.cell
def sky130_fd_sc_hs__tapvgnd_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__tapvgnd_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__tapvgnd_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__tapvgnd_1.gds")


@gf.cell
def sky130_fd_sc_hs__tapvpwrvgnd_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__tapvpwrvgnd_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__tapvpwrvgnd_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__tapvpwrvgnd_1.gds")


@gf.cell
def sky130_fd_sc_hs__xnor2_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__xnor2_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__xnor2_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__xnor2_1.gds")


@gf.cell
def sky130_fd_sc_hs__xnor2_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__xnor2_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__xnor2_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__xnor2_2.gds")


@gf.cell
def sky130_fd_sc_hs__xnor2_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__xnor2_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__xnor2_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__xnor2_4.gds")


@gf.cell
def sky130_fd_sc_hs__xnor3_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__xnor3_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__xnor3_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__xnor3_1.gds")


@gf.cell
def sky130_fd_sc_hs__xnor3_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__xnor3_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__xnor3_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__xnor3_2.gds")


@gf.cell
def sky130_fd_sc_hs__xnor3_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__xnor3_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__xnor3_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__xnor3_4.gds")


@gf.cell
def sky130_fd_sc_hs__xor2_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__xor2_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__xor2_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__xor2_1.gds")


@gf.cell
def sky130_fd_sc_hs__xor2_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__xor2_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__xor2_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__xor2_2.gds")


@gf.cell
def sky130_fd_sc_hs__xor2_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__xor2_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__xor2_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__xor2_4.gds")


@gf.cell
def sky130_fd_sc_hs__xor3_1() -> gf.Component:
    """Returns sky130_fd_sc_hs__xor3_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__xor3_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__xor3_1.gds")


@gf.cell
def sky130_fd_sc_hs__xor3_2() -> gf.Component:
    """Returns sky130_fd_sc_hs__xor3_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__xor3_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__xor3_2.gds")


@gf.cell
def sky130_fd_sc_hs__xor3_4() -> gf.Component:
    """Returns sky130_fd_sc_hs__xor3_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hs__xor3_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hs__xor3_4.gds")


@gf.cell
def sky130_fd_sc_hvl__a21o_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__a21o_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__a21o_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__a21o_1.gds")


@gf.cell
def sky130_fd_sc_hvl__a21oi_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__a21oi_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__a21oi_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__a21oi_1.gds")


@gf.cell
def sky130_fd_sc_hvl__a22o_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__a22o_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__a22o_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__a22o_1.gds")


@gf.cell
def sky130_fd_sc_hvl__a22oi_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__a22oi_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__a22oi_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__a22oi_1.gds")


@gf.cell
def sky130_fd_sc_hvl__and2_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__and2_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__and2_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__and2_1.gds")


@gf.cell
def sky130_fd_sc_hvl__and3_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__and3_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__and3_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__and3_1.gds")


@gf.cell
def sky130_fd_sc_hvl__buf_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__buf_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__buf_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__buf_1.gds")


@gf.cell
def sky130_fd_sc_hvl__buf_16() -> gf.Component:
    """Returns sky130_fd_sc_hvl__buf_16 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__buf_16()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__buf_16.gds")


@gf.cell
def sky130_fd_sc_hvl__buf_2() -> gf.Component:
    """Returns sky130_fd_sc_hvl__buf_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__buf_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__buf_2.gds")


@gf.cell
def sky130_fd_sc_hvl__buf_32() -> gf.Component:
    """Returns sky130_fd_sc_hvl__buf_32 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__buf_32()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__buf_32.gds")


@gf.cell
def sky130_fd_sc_hvl__buf_4() -> gf.Component:
    """Returns sky130_fd_sc_hvl__buf_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__buf_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__buf_4.gds")


@gf.cell
def sky130_fd_sc_hvl__buf_8() -> gf.Component:
    """Returns sky130_fd_sc_hvl__buf_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__buf_8()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__buf_8.gds")


@gf.cell
def sky130_fd_sc_hvl__conb_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__conb_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__conb_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__conb_1.gds")


@gf.cell
def sky130_fd_sc_hvl__decap_4() -> gf.Component:
    """Returns sky130_fd_sc_hvl__decap_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__decap_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__decap_4.gds")


@gf.cell
def sky130_fd_sc_hvl__decap_8() -> gf.Component:
    """Returns sky130_fd_sc_hvl__decap_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__decap_8()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__decap_8.gds")


@gf.cell
def sky130_fd_sc_hvl__dfrbp_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__dfrbp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__dfrbp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__dfrbp_1.gds")


@gf.cell
def sky130_fd_sc_hvl__dfrtp_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__dfrtp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__dfrtp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__dfrtp_1.gds")


@gf.cell
def sky130_fd_sc_hvl__dfsbp_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__dfsbp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__dfsbp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__dfsbp_1.gds")


@gf.cell
def sky130_fd_sc_hvl__dfstp_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__dfstp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__dfstp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__dfstp_1.gds")


@gf.cell
def sky130_fd_sc_hvl__dfxbp_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__dfxbp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__dfxbp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__dfxbp_1.gds")


@gf.cell
def sky130_fd_sc_hvl__dfxtp_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__dfxtp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__dfxtp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__dfxtp_1.gds")


@gf.cell
def sky130_fd_sc_hvl__diode_2() -> gf.Component:
    """Returns sky130_fd_sc_hvl__diode_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__diode_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__diode_2.gds")


@gf.cell
def sky130_fd_sc_hvl__dlclkp_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__dlclkp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__dlclkp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__dlclkp_1.gds")


@gf.cell
def sky130_fd_sc_hvl__dlrtp_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__dlrtp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__dlrtp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__dlrtp_1.gds")


@gf.cell
def sky130_fd_sc_hvl__dlxtp_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__dlxtp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__dlxtp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__dlxtp_1.gds")


@gf.cell
def sky130_fd_sc_hvl__einvn_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__einvn_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__einvn_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__einvn_1.gds")


@gf.cell
def sky130_fd_sc_hvl__einvp_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__einvp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__einvp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__einvp_1.gds")


@gf.cell
def sky130_fd_sc_hvl__fill_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__fill_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__fill_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__fill_1.gds")


@gf.cell
def sky130_fd_sc_hvl__fill_2() -> gf.Component:
    """Returns sky130_fd_sc_hvl__fill_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__fill_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__fill_2.gds")


@gf.cell
def sky130_fd_sc_hvl__fill_4() -> gf.Component:
    """Returns sky130_fd_sc_hvl__fill_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__fill_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__fill_4.gds")


@gf.cell
def sky130_fd_sc_hvl__fill_8() -> gf.Component:
    """Returns sky130_fd_sc_hvl__fill_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__fill_8()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__fill_8.gds")


@gf.cell
def sky130_fd_sc_hvl__inv_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__inv_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__inv_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__inv_1.gds")


@gf.cell
def sky130_fd_sc_hvl__inv_16() -> gf.Component:
    """Returns sky130_fd_sc_hvl__inv_16 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__inv_16()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__inv_16.gds")


@gf.cell
def sky130_fd_sc_hvl__inv_2() -> gf.Component:
    """Returns sky130_fd_sc_hvl__inv_2 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__inv_2()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__inv_2.gds")


@gf.cell
def sky130_fd_sc_hvl__inv_4() -> gf.Component:
    """Returns sky130_fd_sc_hvl__inv_4 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__inv_4()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__inv_4.gds")


@gf.cell
def sky130_fd_sc_hvl__inv_8() -> gf.Component:
    """Returns sky130_fd_sc_hvl__inv_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__inv_8()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__inv_8.gds")


@gf.cell
def sky130_fd_sc_hvl__lsbufhv2hv_hl_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__lsbufhv2hv_hl_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__lsbufhv2hv_hl_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__lsbufhv2hv_hl_1.gds")


@gf.cell
def sky130_fd_sc_hvl__lsbufhv2hv_lh_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__lsbufhv2hv_lh_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__lsbufhv2hv_lh_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__lsbufhv2hv_lh_1.gds")


@gf.cell
def sky130_fd_sc_hvl__lsbufhv2lv_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__lsbufhv2lv_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__lsbufhv2lv_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__lsbufhv2lv_1.gds")


@gf.cell
def sky130_fd_sc_hvl__lsbufhv2lv_simple_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__lsbufhv2lv_simple_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__lsbufhv2lv_simple_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__lsbufhv2lv_simple_1.gds")


@gf.cell
def sky130_fd_sc_hvl__lsbuflv2hv_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__lsbuflv2hv_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__lsbuflv2hv_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__lsbuflv2hv_1.gds")


@gf.cell
def sky130_fd_sc_hvl__lsbuflv2hv_clkiso_hlkg_3() -> gf.Component:
    """Returns sky130_fd_sc_hvl__lsbuflv2hv_clkiso_hlkg_3 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__lsbuflv2hv_clkiso_hlkg_3()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__lsbuflv2hv_clkiso_hlkg_3.gds")


@gf.cell
def sky130_fd_sc_hvl__lsbuflv2hv_isosrchvaon_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__lsbuflv2hv_isosrchvaon_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__lsbuflv2hv_isosrchvaon_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__lsbuflv2hv_isosrchvaon_1.gds")


@gf.cell
def sky130_fd_sc_hvl__lsbuflv2hv_symmetric_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__lsbuflv2hv_symmetric_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__lsbuflv2hv_symmetric_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__lsbuflv2hv_symmetric_1.gds")


@gf.cell
def sky130_fd_sc_hvl__mux2_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__mux2_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__mux2_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__mux2_1.gds")


@gf.cell
def sky130_fd_sc_hvl__mux4_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__mux4_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__mux4_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__mux4_1.gds")


@gf.cell
def sky130_fd_sc_hvl__nand2_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__nand2_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__nand2_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__nand2_1.gds")


@gf.cell
def sky130_fd_sc_hvl__nand3_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__nand3_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__nand3_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__nand3_1.gds")


@gf.cell
def sky130_fd_sc_hvl__nor2_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__nor2_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__nor2_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__nor2_1.gds")


@gf.cell
def sky130_fd_sc_hvl__nor3_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__nor3_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__nor3_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__nor3_1.gds")


@gf.cell
def sky130_fd_sc_hvl__o21a_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__o21a_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__o21a_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__o21a_1.gds")


@gf.cell
def sky130_fd_sc_hvl__o21ai_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__o21ai_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__o21ai_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__o21ai_1.gds")


@gf.cell
def sky130_fd_sc_hvl__o22a_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__o22a_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__o22a_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__o22a_1.gds")


@gf.cell
def sky130_fd_sc_hvl__o22ai_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__o22ai_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__o22ai_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__o22ai_1.gds")


@gf.cell
def sky130_fd_sc_hvl__or2_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__or2_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__or2_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__or2_1.gds")


@gf.cell
def sky130_fd_sc_hvl__or3_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__or3_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__or3_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__or3_1.gds")


@gf.cell
def sky130_fd_sc_hvl__probe_p_8() -> gf.Component:
    """Returns sky130_fd_sc_hvl__probe_p_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__probe_p_8()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__probe_p_8.gds")


@gf.cell
def sky130_fd_sc_hvl__probec_p_8() -> gf.Component:
    """Returns sky130_fd_sc_hvl__probec_p_8 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__probec_p_8()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__probec_p_8.gds")


@gf.cell
def sky130_fd_sc_hvl__schmittbuf_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__schmittbuf_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__schmittbuf_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__schmittbuf_1.gds")


@gf.cell
def sky130_fd_sc_hvl__sdfrbp_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__sdfrbp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__sdfrbp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__sdfrbp_1.gds")


@gf.cell
def sky130_fd_sc_hvl__sdfrtp_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__sdfrtp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__sdfrtp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__sdfrtp_1.gds")


@gf.cell
def sky130_fd_sc_hvl__sdfsbp_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__sdfsbp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__sdfsbp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__sdfsbp_1.gds")


@gf.cell
def sky130_fd_sc_hvl__sdfstp_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__sdfstp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__sdfstp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__sdfstp_1.gds")


@gf.cell
def sky130_fd_sc_hvl__sdfxbp_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__sdfxbp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__sdfxbp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__sdfxbp_1.gds")


@gf.cell
def sky130_fd_sc_hvl__sdfxtp_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__sdfxtp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__sdfxtp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__sdfxtp_1.gds")


@gf.cell
def sky130_fd_sc_hvl__sdlclkp_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__sdlclkp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__sdlclkp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__sdlclkp_1.gds")


@gf.cell
def sky130_fd_sc_hvl__sdlxtp_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__sdlxtp_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__sdlxtp_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__sdlxtp_1.gds")


@gf.cell
def sky130_fd_sc_hvl__xnor2_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__xnor2_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__xnor2_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__xnor2_1.gds")


@gf.cell
def sky130_fd_sc_hvl__xor2_1() -> gf.Component:
    """Returns sky130_fd_sc_hvl__xor2_1 fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.sky130_fd_sc_hvl__xor2_1()
      c.plot()
    """
    return import_gds("sky130_fd_sc_hvl__xor2_1.gds")


if __name__ == "__main__":
    # gf.write_cells.write_cells(gdspath=PATH.gdshd, dirpath="gds")
    # gf.write_cells.write_cells(gdspath=PATH.gdshs, dirpath="gds")
    # gf.write_cells.write_cells(gdspath=PATH.gdshvl, dirpath="gds")
    # print(gf.write_cells.get_import_gds_script(PATH.gds))
    # c = sky130_fd_sc_hvl__xor2_1()
    # c = sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_2()
    c = sky130_fd_sc_hd__conb_1()
    c.show()
