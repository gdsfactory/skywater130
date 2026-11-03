"""Pack."""

import gdsfactory as gf


@gf.cell
def sample3_grid():
    t1 = gf.components.text("1", layer="met1drawing")
    t2 = gf.components.text("2", layer="met1drawing")
    t3 = gf.components.text("3", layer="met1drawing")
    t4 = gf.components.text("4", layer="met1drawing")
    t5 = gf.components.text("5", layer="met1drawing")
    t6 = gf.components.text("6", layer="met1drawing")

    return gf.grid([t1, t2, t3, t4, t5, t6], shape=(2, 3), spacing=(10, 10))
