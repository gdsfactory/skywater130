# res Generator for skywater130

from gdsfactory.types import LayerSpec

from .layers_def import (
    li1_res,
    li_layer,
    m1_layer,
    m2_layer,
    m3_layer,
    m4_layer,
    m5_layer,
    met1_res,
    met2_res,
    met3_res,
    met4_res,
    met5_res,
)
from .parent_res import draw_res

# ########constants##########
# ONLY FOR GENERIC RES
L_MIN_G = 0.17
W_MIN_G = 0.17
# REACT
LI_LYAER_G = [0.285, 0]


# ##########################
class res_metal_draw(draw_res):
    """child class for the backend of the metal res
    Args:
        type_ (str): type of the res
    """

    def __init__(self, type_):
        super().__init__(type_)
        # self.l=l
        # self.w=w
        # self.your_res()

    def gen_res(self, ly1: LayerSpec, ly2: LayerSpec):
        """draw the different metal res

        Args:
            ly1(LayerSpec):  marked layer
            ly2(LayerSpec):  overlapping layer

        """
        layer_names = [ly1, ly2]
        l1 = [0, LI_LYAER_G[0]]
        w1 = [0, LI_LYAER_G[1]]
        self.draw_rect_layer(layer_names, l1, w1)

    def your_res(
        self,
        layout,
        type="sky130_fd_pr__res_generic_l1",
        l_res: float = L_MIN_G,
        w: float = W_MIN_G,
    ):
        """draw the res with calling the parent func with right data

        Args:
            layout(layout):  drawing layout
            type(str):  type of the resistor
            l(float):  length of the resistor
            w(float):  width of the resistor

        """
        self.set_l_w(l_res, w)

        if type == "sky130_fd_pr__res_generic_l1":
            self.gen_res(li1_res, li_layer)

        elif type == "sky130_fd_pr__res_generic_m1":
            self.gen_res(met1_res, m1_layer)

        elif type == "sky130_fd_pr__res_generic_m2":
            self.gen_res(met2_res, m2_layer)

        elif type == "sky130_fd_pr__res_generic_m3":
            self.gen_res(met3_res, m3_layer)

        elif type == "sky130_fd_pr__res_generic_m4":
            self.gen_res(met4_res, m4_layer)

        elif type == "sky130_fd_pr__res_generic_m5":
            self.gen_res(met5_res, m5_layer)
        c = self.get_c()
        c.write_gds("res_temp.gds")
        layout.read("res_temp.gds")
        cell_name = type
        return layout.cell(cell_name)
