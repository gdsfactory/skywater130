# Copyright 2022 Skywater 130nm pdk development
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


# res Generator for skywater130

import math
from .layers_def import (

    tap_layer,
    psdm_layer,
    nsdm_layer,
    li_layer,
    licon_layer,
    m1_layer,
    mcon_layer,
    rpm_drawing,
    rpm_high_drawing,
    npc_layer,
    poly_layer,
    poly_res,
    pwell_res,
    dnwell_layer,
    nwell_layer,


)
from .parent_res import draw_res

# ########constants##########
# ONLY FOR GENERIC RES
L_MIN_G = 1.65
W_MIN_G = 0.42

# react
POLY_LAYER_G = [2.15, 0]
# FRAME
TAP_LI_LAYER_G = [2.8, 0.65, 0.17]
PSDM_LAYER_G = [2.925, 0.775, 0.42]

# CONTACTS H
LICON1_LAYER_G = [1.9, 0.17, 0.17, 0, 0.17]
LICON2_LAYER_G = [2.63, 0.17, 0.17, 0, 0.17]
NPC_LAYER_G = [1.8, 0.37, 0, 0, 0]
LI1_LAYER_G = [0.085, 1.815, 0, 0, 0]
LI2_LAYER_G = [1.9, 0.17, 0, 0, 0]
M1_LAYER_G = [0.025, 2.105, 0, 0, 0]
# CONTACT V
LICON_LAYER_G = [0.48, 0.17, 0.17, 4.98, 0.17]
# 2D ARRAY
MCON_LAYER_G = [0.17, 0.09, 1.89]
# ###################################


# ONLY FOR ISO RES
L_MIN_ISO = 26.5
W_MIN_ISO = 2.65

# react
DNWELL=[1.82,1.03]
# FRAME
NWELL=[2.22,1.43,1.43]
TAP_LI_LAYER_ISO = [1.59, 0.8, 0.17]
NSDM_LAYER_ISO = [1.715, 0.925, 0.42]
# CONTACTS H
TAP_ISO=[0,0.53,0,0,0]
PSDM_ISO=[-0.125,0.78,0,0,0]
LI_ISO=[0,0.53,0,0,0]
M1_ISO=[0.055,0.325,0,0,0]
LICON_ISO=[0.01,0.17,0.17,0,0.17]
LICON_ISO2=0.35
LICON_ISO3=1.42
MCON_ISO=[0.13,0.17,0.17,0,0.19]
# CONTACTS H
LICON_ISO_H=[0.63,0.17,0.17,2.1,0.17]
# ###############################
# THE REST OF THE RES
L_MIN = 0.5
W_MIN = 0.35
W_MIN_0P35 = 0.35
W_MIN_0P69 = 0.69
W_MIN_1P41 = 1.41
W_MIN_2P85 = 2.85
W_MIN_5P73 = 5.73
GR = 1
RPM_LAYER = 0.29
EXTRA_LEN = 0.12

# REACT
POLY_RES = [0, 0]
POLY_LAYER = [2.1, 0]
PSDM_LAYER = [2.875, 0.775]
PSDM_LAYER_NO_GR = [2.21, 0.11]
NPC_LAYER = [2.195, 0.095]
RPM_LAUER = [2.3, 0]
RPM_FOR_LAYERS = [0.46, 0.29, 0.2, 0.2, 0.2]
# FRAME
TAP_LI_LAYER = [2.75, 0.65, 0.17]
# CONTACTS H
LICON1_LAYER = [0.02, 2, 0.19, 0, 0.52]
LICON2_LAYER = [2.58, 0.17, 0.17, 0, 0.17]
LI_LAYER = [-0.06, 2.16, 0, 0, 0]
M1_LAYER = [-0.035, 2.105, 0, 0, 0]
LICON1_LAYER_NO_GR = 2

# CONTACT V
LICON_LAYER = [0.48, 0.17, 0.17, 4.31, 0.17]
# 2D ARRAY
MCON_LAYER = [0.17, 0.035, 1.83]


# ##########################
class res_poly_draw(draw_res):
    """child class for the backend of the poly res
    Args:
        type_ (str): type of the res
    """

    def __init__(self, type_):
        super().__init__(type_)
        # self.l=l
        # self.w=w
        # self.your_res()

    def poly_res(
        self,
        l: float = L_MIN,
        w: float = W_MIN,
        gr: int = GR,
        n_mcon: int = 0,
        rpm: float = RPM_LAYER,
        xhigh: int = 0,
    ):
        """draw the res the specific res with right data

        Args:
            l(float):  length of the resistor
            w(float):  width of the resistor
            gr(int):  guard ring of the resistor
            n_mcon(float):  mcon_layer number of columns
            rpm(float):  rpm layer width
            xhigh(int):  select high or xhigh poly res

        """
        # rects
        self.set_l_w(l + EXTRA_LEN, w)
        rpm_layer = rpm_drawing
        if xhigh:
            rpm_layer = rpm_high_drawing
        layer_names = [poly_res, poly_layer, psdm_layer, npc_layer, rpm_layer]
        l1 = [POLY_RES[0], POLY_LAYER[0], PSDM_LAYER[0], NPC_LAYER[0], RPM_LAUER[0]]
        w1 = [POLY_RES[1], POLY_LAYER[1], PSDM_LAYER[1], NPC_LAYER[1], rpm]
        if gr == 0:
            layer_names = [poly_res, poly_layer, psdm_layer, npc_layer, rpm_layer]
            l1 = [
                POLY_RES[0],
                POLY_LAYER[0],
                PSDM_LAYER_NO_GR[0],
                NPC_LAYER[0],
                RPM_LAUER[0],
            ]
            w1 = [POLY_RES[1], POLY_LAYER[1], PSDM_LAYER_NO_GR[1], NPC_LAYER[1], rpm]
        self.draw_rect_layer(layer_names, l1, w1)

        # frams
        layer_names = [tap_layer, li_layer]
        l1 = [TAP_LI_LAYER[0], TAP_LI_LAYER[0]]
        w1 = [TAP_LI_LAYER[1], TAP_LI_LAYER[1]]
        thick = [TAP_LI_LAYER[2], TAP_LI_LAYER[2]]
        if gr:

            self.draw_frame_layer(layer_names, l1, w1, thick)

        # countacts

        layer_names = [licon_layer, licon_layer, li_layer, m1_layer]
        l1 = [LICON1_LAYER[0], LICON2_LAYER[0], LI_LAYER[0], M1_LAYER[0]]
        sizes_l = [LICON1_LAYER[1], LICON2_LAYER[1], LI_LAYER[1], M1_LAYER[1]]
        sizes_w = [LICON1_LAYER[2], LICON2_LAYER[2], w, w - 0.1]
        space_fit_in = [w + 0.1, w + 0.34, LI_LAYER[3], M1_LAYER[3]]
        spaces = [LICON1_LAYER[4], LICON2_LAYER[4], LI_LAYER[4], M1_LAYER[4]]

        if gr == 0:
            layer_names = [licon_layer, li_layer, m1_layer]
            l1 = [LICON1_LAYER[0], LI_LAYER[0], M1_LAYER[0]]
            sizes_l = [LICON1_LAYER_NO_GR, LI_LAYER[1], M1_LAYER[1]]
            sizes_w = [LICON1_LAYER[2], w, w - 0.1]
            space_fit_in = [w + 0.1, LI_LAYER[3], M1_LAYER[3]]
            spaces = [LICON1_LAYER[4], LI_LAYER[4], M1_LAYER[4]]

        self.draw_contact_layer_h(
            layer_names, l1, sizes_w, sizes_l, space_fit_in, spaces
        )

        # vertical contacts

        layer_names = [licon_layer]
        l1 = [LICON_LAYER[0]]
        sizes_l = [LICON_LAYER[1]]
        sizes_w = [LICON_LAYER[2]]
        space_fit_in = [l + LICON_LAYER[3]]
        spaces = [LICON_LAYER[4]]

        if gr:

            self.draw_contact_layer_v(
                layer_names, l1, sizes_w, sizes_l, space_fit_in, spaces
            )

        # 2d arr
        self.draw_2dArr_layer(
            mcon_layer, MCON_LAYER[0], MCON_LAYER[1], MCON_LAYER[2], n_mcon
        )

    def your_res(
        self,
        layout,
        type="sky130_fd_pr__res_generic_po",
        l: float = L_MIN_G,
        w: float = W_MIN_G,
        gr: int = GR,
    ):
        """draw the res with calling the parent func with right data

        Args:
            layout(layout):  drawing layout
            type(str):  type of the resistor
            l(float):  length of the resistor
            w(float):  width of the resistor
            gr(int):  guard ring of the resistor

        """
        self.set_l_w(l, w)

        if type == "sky130_fd_pr__res_generic_po":
            # rects
            layer_names = [poly_res, poly_layer]
            l1 = [POLY_RES[0], POLY_LAYER_G[0]]
            w1 = [POLY_RES[1], POLY_LAYER_G[1]]

            self.draw_rect_layer(layer_names, l1, w1)

            # frams
            layer_names = [tap_layer, psdm_layer, li_layer]
            l1 = [TAP_LI_LAYER_G[0], PSDM_LAYER_G[0], TAP_LI_LAYER_G[0]]
            w1 = [TAP_LI_LAYER_G[1], PSDM_LAYER_G[1], TAP_LI_LAYER_G[1]]
            thick = [TAP_LI_LAYER_G[2], PSDM_LAYER_G[2], TAP_LI_LAYER_G[2]]
            if gr:

                self.draw_frame_layer(layer_names, l1, w1, thick)

            # countacts

            layer_names = [
                licon_layer,
                licon_layer,
                npc_layer,
                li_layer,
                li_layer,
                m1_layer,
            ]
            # npc
            counts_arr = math.floor(w / 0.36)
            if counts_arr <= 0:
                counts_arr = 1
            w_met = w - 0.21
            if counts_arr == 1:
                w_met = 0.37
            ##
            l1 = [
                LICON1_LAYER_G[0],
                LICON2_LAYER_G[0],
                NPC_LAYER_G[0],
                LI1_LAYER_G[0],
                LI2_LAYER_G[0],
                M1_LAYER_G[0],
            ]
            sizes_l = [
                LICON1_LAYER_G[1],
                LICON2_LAYER_G[1],
                NPC_LAYER_G[1],
                LI1_LAYER_G[1],
                LI2_LAYER_G[1],
                M1_LAYER_G[1],
            ]
            sizes_w = [LICON1_LAYER_G[2], LICON2_LAYER_G[2], w_met, w - 0.16, w, w]
            space_fit_in = [
                w,
                w + 0.68,
                NPC_LAYER_G[3],
                LI1_LAYER_G[3],
                LI2_LAYER_G[3],
                M1_LAYER_G[3],
            ]
            spaces = [
                LICON1_LAYER_G[4],
                LICON2_LAYER_G[4],
                NPC_LAYER_G[4],
                LI1_LAYER_G[4],
                LI2_LAYER_G[4],
                M1_LAYER_G[4],
            ]

            if gr == 0:
                layer_names = [
                    licon_layer,
                    npc_layer,
                    li_layer,
                    li_layer,
                    m1_layer,
                ]
                l1 = [
                    LICON1_LAYER_G[0],
                    NPC_LAYER_G[0],
                    LI1_LAYER_G[0],
                    LI2_LAYER_G[0],
                    M1_LAYER_G[0],
                ]
                sizes_l = [
                    LICON1_LAYER_G[1],
                    NPC_LAYER_G[1],
                    LI1_LAYER_G[1],
                    LI2_LAYER_G[1],
                    M1_LAYER_G[1],
                ]
                sizes_w = [LICON1_LAYER_G[2], w_met, w - 0.16, w, w]
                space_fit_in = [
                    w,
                    w + 0.68,
                    LI1_LAYER_G[3],
                    LI2_LAYER_G[3],
                    M1_LAYER_G[3],
                ]
                spaces = [
                    LICON1_LAYER_G[4],
                    NPC_LAYER_G[4],
                    LI1_LAYER_G[4],
                    LI2_LAYER_G[4],
                    M1_LAYER_G[4],
                ]

            self.draw_contact_layer_h(
                layer_names, l1, sizes_w, sizes_l, space_fit_in, spaces
            )

            layer_names = [licon_layer]
            l1 = [LICON_LAYER_G[0]]
            sizes_l = [LICON_LAYER_G[1]]
            sizes_w = [LICON_LAYER_G[2]]
            space_fit_in = [l + LICON_LAYER_G[3]]
            spaces = [LICON_LAYER_G[4]]

            if gr:

                self.draw_contact_layer_v(
                    layer_names, l1, sizes_w, sizes_l, space_fit_in, spaces
                )

            # 2d arr
            self.draw_2dArr_layer(
                mcon_layer, MCON_LAYER_G[0], MCON_LAYER_G[1], MCON_LAYER_G[2]
            )  # 0.09,1.9
            c = self.get_c()
            c.write_gds("res_temp.gds")
            layout.read("res_temp.gds")
            cell_name = type
            return layout.cell(cell_name)
 
        elif type == "sky130_fd_pr__res_iso_pw":
            # rects
            layer_names = [pwell_res, dnwell_layer]
            l1 = [0, DNWELL[0]]
            w1 = [0, DNWELL[1]]
            if gr==0:
                layer_names = [pwell_res]
                l1 = [0]
                w1 = [0]

            self.draw_rect_layer(layer_names, l1, w1)

            # frams
            layer_names = [nwell_layer, tap_layer,nsdm_layer ,li_layer]
            l1 = [NWELL[0], TAP_LI_LAYER_ISO[0], NSDM_LAYER_ISO[0],TAP_LI_LAYER_ISO[0]]
            w1 = [NWELL[1], TAP_LI_LAYER_ISO[1], NSDM_LAYER_ISO[1],TAP_LI_LAYER_ISO[1]]
            thick = [NWELL[2], TAP_LI_LAYER_ISO[2], NSDM_LAYER_ISO[2],TAP_LI_LAYER_ISO[2]]
           
            if gr:

                self.draw_frame_layer(layer_names, l1, w1, thick)

            # countacts

            layer_names = [
                tap_layer,
                psdm_layer,
                li_layer,
                m1_layer,
                licon_layer,
                licon_layer,
                licon_layer,
                mcon_layer
            ]

            l1 = [
                TAP_ISO[0],
                PSDM_ISO[0],
                LI_ISO[0],
                M1_ISO[0],
                LICON_ISO[0],
                LICON_ISO2,
                LICON_ISO3,
                MCON_ISO[0]
            ]
            sizes_l = [
                TAP_ISO[1],
                PSDM_ISO[1],
                LI_ISO[1],
                M1_ISO[1],
                LICON_ISO[1],
                LICON_ISO[1],
                LICON_ISO[1],
                MCON_ISO[1]
            ]
            sizes_w = [w-0.4, w-0.15, w-0.48, w - 0.4, LICON_ISO[2],LICON_ISO[2],LICON_ISO[2],MCON_ISO[2]]
            space_fit_in = [
                TAP_ISO[3],
                PSDM_ISO[3],
                LI_ISO[3],
                M1_ISO[3],
                w-0.6,
                w-0.6,
                w+0.76,
                w-0.49
            ]
            spaces = [
                TAP_ISO[4],
                PSDM_ISO[4],
                LI_ISO[4],
                M1_ISO[4],
                LICON_ISO[4],
                LICON_ISO[4],
                LICON_ISO[4],
                MCON_ISO[4]
            ]

            if gr == 0:
                layer_names = [
                    tap_layer,
                    psdm_layer,
                    li_layer,
                    m1_layer,
                    licon_layer,
                    licon_layer,
                    mcon_layer
                ]

                l1 = [
                    TAP_ISO[0],
                    PSDM_ISO[0],
                    LI_ISO[0],
                    M1_ISO[0],
                    LICON_ISO[0],
                    LICON_ISO2,
                    MCON_ISO[0]
                ]
                sizes_l = [
                    TAP_ISO[1],
                    PSDM_ISO[1],
                    LI_ISO[1],
                    M1_ISO[1],
                    LICON_ISO[1],
                    LICON_ISO[1],
                    MCON_ISO[1]
                ]
                sizes_w = [w-0.4, w-0.15, w-0.48, w - 0.4, LICON_ISO[2],LICON_ISO[2],MCON_ISO[2]]
                space_fit_in = [
                    TAP_ISO[3],
                    PSDM_ISO[3],
                    LI_ISO[3],
                    M1_ISO[3],
                    w-0.6,
                    w-0.6,
                    w-0.49
                ]
                spaces = [
                    TAP_ISO[4],
                    PSDM_ISO[4],
                    LI_ISO[4],
                    M1_ISO[4],
                    LICON_ISO[4],
                    LICON_ISO[4],
                    MCON_ISO[4]
                ]    

            self.draw_contact_layer_h(
                layer_names, l1, sizes_w, sizes_l, space_fit_in, spaces
            )

            layer_names = [licon_layer]
            l1 = [LICON_ISO_H[0]]
            sizes_l = [LICON_ISO_H[1]]
            sizes_w = [LICON_ISO_H[2]]
            space_fit_in = [l + LICON_ISO_H[3]]
            spaces = [LICON_ISO_H[4]]

            if gr:

                self.draw_contact_layer_v(
                    layer_names, l1, sizes_w, sizes_l, space_fit_in, spaces
                )


            c = self.get_c()
            c.write_gds("res_temp.gds")
            layout.read("res_temp.gds")
            cell_name = type
            return layout.cell(cell_name)

 
        elif type == "sky130_fd_pr__res_high_po_0p35":
            self.poly_res(l, W_MIN_0P35, gr, 0, RPM_FOR_LAYERS[0])
        elif type == "sky130_fd_pr__res_high_po_0p69":
            self.poly_res(l, W_MIN_0P69, gr, 1, RPM_FOR_LAYERS[1])
        elif type == "sky130_fd_pr__res_high_po_1p41":
            self.poly_res(l, W_MIN_1P41, gr, 1, RPM_FOR_LAYERS[2])
        elif type == "sky130_fd_pr__res_high_po_2p85":
            self.poly_res(l, W_MIN_2P85, gr, 1, RPM_FOR_LAYERS[3])
        elif type == "sky130_fd_pr__res_high_po_5p73":
            self.poly_res(l, W_MIN_5P73, gr, 1, RPM_FOR_LAYERS[4])
        # high

        elif type == "sky130_fd_pr__res_xhigh_po_0p35":
            self.poly_res(l, W_MIN_0P35, gr, 0, RPM_FOR_LAYERS[0], 1)
        elif type == "sky130_fd_pr__res_xhigh_po_0p69":
            self.poly_res(l, W_MIN_0P69, gr, 1, RPM_FOR_LAYERS[1], 1)
        elif type == "sky130_fd_pr__res_xhigh_po_1p41":
            self.poly_res(l, W_MIN_1P41, gr, 1, RPM_FOR_LAYERS[2], 1)
        elif type == "sky130_fd_pr__res_xhigh_po_2p85":
            self.poly_res(l, W_MIN_2P85, gr, 1, RPM_FOR_LAYERS[3], 1)
        elif type == "sky130_fd_pr__res_xhigh_po_5p73":
            self.poly_res(l, W_MIN_5P73, gr, 1, RPM_FOR_LAYERS[4], 1)

        c = self.get_c()
        c.write_gds("res_temp.gds")
        layout.read("res_temp.gds")
        cell_name = type
        return layout.cell(cell_name)
