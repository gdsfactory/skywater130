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

from .layers_def import (
    diff_layer,
    diff_res,
    nsdm_layer,
    tap_layer,
    psdm_layer,
    li_layer,
    licon_layer,
    m1_layer,
    mcon_layer,
    hvi_layer,
    hvntm_layer,
    nwell_layer,
)
from .parent_res import draw_res

# ##########constant#################
# [l,w]
# react
DIFF_RES = 0
DIFF_LAYER_ND = [0.515, 0]
NSDM_LAYER_ND = [0.64, 0.125]
# HVT
HVI_ND = [1.43, 0.915, 0.7, 0.21]
HVNTM_ND = [0.7, 0.185]
# [l,w,thickness]
# frame
TAP_ND_LVT = [1.125, 0.61, 0.17]
PSDM_ND_LVT = [1.25, 0.735, 0.42]
LI_ND_LVT = [1.125, 0.61, 0.17]
# HVT
TAP_ND_HVT = [1.245, 0.73, 0.29]
PSDM_ND_HVT = [1.37, 0.855, 0.54]
LI_ND_HVT = [1.185, 0.67, 0.17]
# [l,w,thickness_l,thickness_w,space]
# CONTACT H
LICON1_ND_LVT = [0.285, 0.17, 0.17, 0, 0.17]
LICON2_ND_LVT = [0.955, 0.17, 0.17, 0, 0.17]
MCON_ND_LVT = [0.185, 0.17, 0.17, 0, 0.19]
M1_ND_LVT = [0.025, 0.49, 0, 0, 0]
LI1_ND_LVT = [0.085, 0.2, 0, 0, 0]
LI2_ND_LVT = [0.285, 0.17, 0, 0, 0]
# HVT
LICON2_ND_HVT = 1.015

# CONTACT V
LICON3_ND_LVT = [0.44, 0.17, 0.17, 1.37, 0.17]
# HVT
LICON3_ND_HVT = 0.5

# #####PD
NWELL_PD = [1.305, 0.79]
# HVT
NWELL_PD_HVT = [1.575, 1.06]
HVI_PD_HVT = [1.575, 1.06]
# frame
TAP_PD_HVT = [1.245, 0.73, 0.29]
PSDM_PD_HVT = [1.37, 0.855, 0.54]
LI_PD_HVT = [1.185, 0.67, 0.17]


#################################


class res_diff_draw(draw_res):
    """child class for the backend of the diff res
    Args:
        type_ (str): type of the res
    """

    def __init__(self, type_):
        super().__init__(type_)

    def your_res(
        self,
        layout,
        type="sky130_fd_pr__res_nd_lvt",
        l: float = 2.1,
        w: float = 0.42,
        gr: int = 1,
    ):
        """draw the res with calling the parent func with right data

        Args:
            layout(layout):  drawing layout
            type(float):  type of the resistor
            l(float):  length of the resistor
            w(float):  width of the resistor
            gr(int):  guard ring of the resistor

        """
        self.set_l_w(l, w)
        if type == "sky130_fd_pr__res_nd_lvt":

            # rects
            layer_names = [diff_res, diff_layer, nsdm_layer]
            l1 = [DIFF_RES, DIFF_LAYER_ND[0], NSDM_LAYER_ND[0]]
            w1 = [DIFF_RES, DIFF_LAYER_ND[1], NSDM_LAYER_ND[1]]

            self.draw_rect_layer(layer_names, l1, w1)

            # frams
            layer_names = [tap_layer, psdm_layer, li_layer]
            l1 = [TAP_ND_LVT[0], PSDM_ND_LVT[0], LI_ND_LVT[0]]
            w1 = [TAP_ND_LVT[1], PSDM_ND_LVT[1], LI_ND_LVT[1]]
            thick = [TAP_ND_LVT[2], PSDM_ND_LVT[2], LI_ND_LVT[2]]

            if gr == 1:
                self.draw_frame_layer(layer_names, l1, w1, thick)

            # countacts

            layer_names = [
                licon_layer,
                licon_layer,
                mcon_layer,
                m1_layer,
                li_layer,
                li_layer,
            ]
            l1 = [
                LICON1_ND_LVT[0],
                LICON2_ND_LVT[0],
                MCON_ND_LVT[0],
                M1_ND_LVT[0],
                LI1_ND_LVT[0],
                LI2_ND_LVT[0],
            ]
            sizes_l = [
                LICON1_ND_LVT[1],
                LICON2_ND_LVT[1],
                MCON_ND_LVT[1],
                M1_ND_LVT[1],
                LI1_ND_LVT[1],
                LI2_ND_LVT[1],
            ]
            sizes_w = [
                LICON1_ND_LVT[2],
                LICON2_ND_LVT[2],
                MCON_ND_LVT[2],
                w - 0.05,
                w - 0.12,
                w + 0.04,
            ]
            space_fit_in = [
                w,
                w + 0.34,
                w - 0.12,
                M1_ND_LVT[3],
                LI1_ND_LVT[3],
                LI2_ND_LVT[3],
            ]
            spaces = [
                LICON1_ND_LVT[4],
                LICON2_ND_LVT[4],
                MCON_ND_LVT[4],
                M1_ND_LVT[4],
                LI1_ND_LVT[4],
                LI2_ND_LVT[4],
            ]

            if gr == 0:
                layer_names = [
                    licon_layer,
                    mcon_layer,
                    m1_layer,
                    li_layer,
                    li_layer,
                ]
                l1 = [
                    LICON1_ND_LVT[0],
                    MCON_ND_LVT[0],
                    M1_ND_LVT[0],
                    LI1_ND_LVT[0],
                    LI2_ND_LVT[0],
                ]
                sizes_l = [
                    LICON1_ND_LVT[1],
                    MCON_ND_LVT[1],
                    M1_ND_LVT[1],
                    LI1_ND_LVT[1],
                    LI2_ND_LVT[1],
                ]
                sizes_w = [
                    LICON1_ND_LVT[2],
                    MCON_ND_LVT[2],
                    w - 0.05,
                    w - 0.12,
                    w + 0.04,
                ]
                space_fit_in = [
                    w,
                    w - 0.12,
                    M1_ND_LVT[3],
                    LI1_ND_LVT[3],
                    LI2_ND_LVT[3],
                ]
                spaces = [
                    LICON1_ND_LVT[4],
                    MCON_ND_LVT[4],
                    M1_ND_LVT[4],
                    LI1_ND_LVT[4],
                    LI2_ND_LVT[4],
                ]

            self.draw_contact_layer_h(
                layer_names, l1, sizes_w, sizes_l, space_fit_in, spaces
            )
            if gr:
                layer_names = [licon_layer]
                l1 = [LICON3_ND_LVT[0]]
                sizes_l = [LICON3_ND_LVT[1]]
                sizes_w = [LICON3_ND_LVT[2]]
                space_fit_in = [l + LICON3_ND_LVT[3]]
                spaces = [LICON3_ND_LVT[4]]
                self.draw_contact_layer_v(
                    layer_names, l1, sizes_w, sizes_l, space_fit_in, spaces
                )

            c = self.get_c()
            c.write_gds("res_temp.gds")
            layout.read("res_temp.gds")
            cell_name = type
            return layout.cell(cell_name)
        elif type == "sky130_fd_pr__res_nd_hvt":
            # rects
            layer_names = [
                diff_res,
                diff_layer,
                nsdm_layer,
                hvi_layer,
                hvntm_layer,
            ]
            l1 = [
                DIFF_RES,
                DIFF_LAYER_ND[0],
                NSDM_LAYER_ND[0],
                HVI_ND[0],
                HVNTM_ND[0],
            ]
            w1 = [
                DIFF_RES,
                DIFF_LAYER_ND[1],
                NSDM_LAYER_ND[1],
                HVI_ND[1],
                HVNTM_ND[1],
            ]

            if gr == 0:
                layer_names = [
                    diff_res,
                    diff_layer,
                    nsdm_layer,
                    hvi_layer,
                    hvntm_layer,
                ]
                l1 = [
                    DIFF_RES,
                    DIFF_LAYER_ND[0],
                    NSDM_LAYER_ND[0],
                    HVI_ND[2],
                    HVNTM_ND[0],
                ]
                w1 = [
                    DIFF_RES,
                    DIFF_LAYER_ND[1],
                    NSDM_LAYER_ND[1],
                    HVI_ND[3],
                    HVNTM_ND[1],
                ]

            self.draw_rect_layer(layer_names, l1, w1)

            # frams
            layer_names = [tap_layer, psdm_layer, li_layer]

            l1 = [TAP_ND_HVT[0], PSDM_ND_HVT[0], LI_ND_HVT[0]]
            w1 = [TAP_ND_HVT[1], PSDM_ND_HVT[1], LI_ND_HVT[1]]
            thick = [TAP_ND_HVT[2], PSDM_ND_HVT[2], LI_ND_HVT[2]]

            if gr:
                self.draw_frame_layer(layer_names, l1, w1, thick)

            # countacts

            layer_names = [
                licon_layer,
                licon_layer,
                mcon_layer,
                m1_layer,
                li_layer,
                li_layer,
            ]

            l1 = [
                LICON1_ND_LVT[0],
                LICON2_ND_HVT,
                MCON_ND_LVT[0],
                M1_ND_LVT[0],
                LI1_ND_LVT[0],
                LI2_ND_LVT[0],
            ]
            sizes_l = [
                LICON1_ND_LVT[1],
                LICON2_ND_LVT[1],
                MCON_ND_LVT[1],
                M1_ND_LVT[1],
                LI1_ND_LVT[1],
                LI2_ND_LVT[1],
            ]
            sizes_w = [
                LICON1_ND_LVT[2],
                LICON2_ND_LVT[2],
                MCON_ND_LVT[2],
                w - 0.05,
                w - 0.12,
                w + 0.04,
            ]
            space_fit_in = [
                w,
                w + 0.34,
                w - 0.12,
                M1_ND_LVT[3],
                LI1_ND_LVT[3],
                LI2_ND_LVT[3],
            ]
            spaces = [
                LICON1_ND_LVT[4],
                LICON2_ND_LVT[4],
                MCON_ND_LVT[4],
                M1_ND_LVT[4],
                LI1_ND_LVT[4],
                LI2_ND_LVT[4],
            ]

            if gr == 0:
                layer_names = [
                    licon_layer,
                    mcon_layer,
                    m1_layer,
                    li_layer,
                    li_layer,
                ]

                l1 = [
                    LICON1_ND_LVT[0],
                    MCON_ND_LVT[0],
                    M1_ND_LVT[0],
                    LI1_ND_LVT[0],
                    LI2_ND_LVT[0],
                ]
                sizes_l = [
                    LICON1_ND_LVT[1],
                    MCON_ND_LVT[1],
                    M1_ND_LVT[1],
                    LI1_ND_LVT[1],
                    LI2_ND_LVT[1],
                ]
                sizes_w = [
                    LICON1_ND_LVT[2],
                    MCON_ND_LVT[2],
                    w - 0.05,
                    w - 0.12,
                    w + 0.04,
                ]
                space_fit_in = [
                    w,
                    w - 0.12,
                    M1_ND_LVT[3],
                    LI1_ND_LVT[3],
                    LI2_ND_LVT[3],
                ]
                spaces = [
                    LICON1_ND_LVT[4],
                    MCON_ND_LVT[4],
                    M1_ND_LVT[4],
                    LI1_ND_LVT[4],
                    LI2_ND_LVT[4],
                ]

            self.draw_contact_layer_h(
                layer_names, l1, sizes_w, sizes_l, space_fit_in, spaces
            )

            layer_names = [licon_layer]
            l1 = [LICON3_ND_HVT]
            sizes_l = [LICON3_ND_LVT[1]]
            sizes_w = [LICON3_ND_LVT[2]]
            space_fit_in = [l + LICON3_ND_LVT[3]]
            spaces = [LICON3_ND_LVT[4]]

            if gr:
                self.draw_contact_layer_v(
                    layer_names, l1, sizes_w, sizes_l, space_fit_in, spaces
                )

            c = self.get_c()
            c.write_gds("res_temp.gds")
            layout.read("res_temp.gds")
            cell_name = type
            return layout.cell(cell_name)
        elif type == "sky130_fd_pr__res_pd_lvt":

            # rects
            layer_names = [
                diff_res,
                diff_layer,
                psdm_layer,
                nwell_layer,
            ]

            l1 = [DIFF_RES, DIFF_LAYER_ND[0], NSDM_LAYER_ND[0], NWELL_PD[0]]
            w1 = [DIFF_RES, DIFF_LAYER_ND[1], NSDM_LAYER_ND[1], NWELL_PD[1]]

            if gr == 0:
                layer_names = [
                    diff_res,
                    diff_layer,
                    psdm_layer,
                ]
                l1 = [DIFF_RES, DIFF_LAYER_ND[0], NSDM_LAYER_ND[0]]
                w1 = [DIFF_RES, DIFF_LAYER_ND[1], NSDM_LAYER_ND[1]]

            self.draw_rect_layer(layer_names, l1, w1)

            # frams
            layer_names = [tap_layer, nsdm_layer, li_layer]
            l1 = [TAP_ND_LVT[0], PSDM_ND_LVT[0], LI_ND_LVT[0]]
            w1 = [TAP_ND_LVT[1], PSDM_ND_LVT[1], LI_ND_LVT[1]]
            thick = [TAP_ND_LVT[2], PSDM_ND_LVT[2], LI_ND_LVT[2]]

            if gr:

                self.draw_frame_layer(layer_names, l1, w1, thick)

            # countacts

            layer_names = [
                licon_layer,
                licon_layer,
                mcon_layer,
                m1_layer,
                li_layer,
                li_layer,
            ]
            l1 = [
                LICON1_ND_LVT[0],
                LICON2_ND_LVT[0],
                MCON_ND_LVT[0],
                M1_ND_LVT[0],
                LI1_ND_LVT[0],
                LI2_ND_LVT[0],
            ]
            sizes_l = [
                LICON1_ND_LVT[1],
                LICON2_ND_LVT[1],
                MCON_ND_LVT[1],
                M1_ND_LVT[1],
                LI1_ND_LVT[1],
                LI2_ND_LVT[1],
            ]
            sizes_w = [
                LICON1_ND_LVT[2],
                LICON2_ND_LVT[2],
                MCON_ND_LVT[2],
                w - 0.05,
                w - 0.12,
                w + 0.04,
            ]
            space_fit_in = [
                w,
                w + 0.34,
                w - 0.12,
                M1_ND_LVT[3],
                LI1_ND_LVT[3],
                LI2_ND_LVT[3],
            ]
            spaces = [
                LICON1_ND_LVT[4],
                LICON2_ND_LVT[4],
                MCON_ND_LVT[4],
                M1_ND_LVT[4],
                LI1_ND_LVT[4],
                LI2_ND_LVT[4],
            ]

            if gr == 0:

                layer_names = [
                    licon_layer,
                    mcon_layer,
                    m1_layer,
                    li_layer,
                    li_layer,
                ]
                l1 = [
                    LICON1_ND_LVT[0],
                    MCON_ND_LVT[0],
                    M1_ND_LVT[0],
                    LI1_ND_LVT[0],
                    LI2_ND_LVT[0],
                ]
                sizes_l = [
                    LICON1_ND_LVT[1],
                    MCON_ND_LVT[1],
                    M1_ND_LVT[1],
                    LI1_ND_LVT[1],
                    LI2_ND_LVT[1],
                ]
                sizes_w = [
                    LICON1_ND_LVT[2],
                    MCON_ND_LVT[2],
                    w - 0.05,
                    w - 0.12,
                    w + 0.04,
                ]
                space_fit_in = [
                    w,
                    w - 0.12,
                    M1_ND_LVT[3],
                    LI1_ND_LVT[3],
                    LI2_ND_LVT[3],
                ]
                spaces = [
                    LICON1_ND_LVT[4],
                    MCON_ND_LVT[4],
                    M1_ND_LVT[4],
                    LI1_ND_LVT[4],
                    LI2_ND_LVT[4],
                ]

            self.draw_contact_layer_h(
                layer_names, l1, sizes_w, sizes_l, space_fit_in, spaces
            )

            layer_names = [licon_layer]
            l1 = [LICON3_ND_LVT[0]]
            sizes_l = [LICON3_ND_LVT[1]]
            sizes_w = [LICON3_ND_LVT[2]]
            space_fit_in = [l + LICON3_ND_LVT[3]]
            spaces = [LICON3_ND_LVT[4]]
            if gr:

                self.draw_contact_layer_v(
                    layer_names, l1, sizes_w, sizes_l, space_fit_in, spaces
                )

            c = self.get_c()
            c.write_gds("res_temp.gds")
            layout.read("res_temp.gds")
            cell_name = type
            return layout.cell(cell_name)
        elif type == "sky130_fd_pr__res_pd_hvt":

            # rects
            layer_names = [
                diff_res,
                diff_layer,
                psdm_layer,
                hvi_layer,
                nwell_layer,
            ]
            l1 = [
                DIFF_RES,
                DIFF_LAYER_ND[0],
                NSDM_LAYER_ND[0],
                HVI_PD_HVT[0],
                NWELL_PD_HVT[0],
            ]
            w1 = [
                DIFF_RES,
                DIFF_LAYER_ND[1],
                NSDM_LAYER_ND[1],
                HVI_PD_HVT[1],
                NWELL_PD_HVT[1],
            ]

            if gr == 0:
                layer_names = [
                    diff_res,
                    diff_layer,
                    psdm_layer,
                    hvi_layer,
                ]
                l1 = [DIFF_RES, DIFF_LAYER_ND[0], NSDM_LAYER_ND[0], HVI_ND[2]]
                w1 = [DIFF_RES, DIFF_LAYER_ND[1], NSDM_LAYER_ND[1], HVI_ND[3]]
            self.draw_rect_layer(layer_names, l1, w1)

            # frams
            layer_names = [tap_layer, nsdm_layer, li_layer]
            l1 = [TAP_PD_HVT[0], PSDM_PD_HVT[0], LI_PD_HVT[0]]
            w1 = [TAP_PD_HVT[1], PSDM_PD_HVT[1], LI_PD_HVT[1]]
            thick = [TAP_PD_HVT[2], PSDM_PD_HVT[2], LI_PD_HVT[2]]

            if gr:

                self.draw_frame_layer(layer_names, l1, w1, thick)

            # countacts

            layer_names = [
                licon_layer,
                licon_layer,
                mcon_layer,
                m1_layer,
                li_layer,
                li_layer,
            ]
            l1 = [
                LICON1_ND_LVT[0],
                LICON2_ND_HVT,
                MCON_ND_LVT[0],
                M1_ND_LVT[0],
                LI1_ND_LVT[0],
                LI2_ND_LVT[0],
            ]
            sizes_l = [
                LICON1_ND_LVT[1],
                LICON2_ND_LVT[1],
                MCON_ND_LVT[1],
                M1_ND_LVT[1],
                LI1_ND_LVT[1],
                LI2_ND_LVT[1],
            ]
            sizes_w = [
                LICON1_ND_LVT[2],
                LICON2_ND_LVT[2],
                MCON_ND_LVT[2],
                w - 0.05,
                w - 0.12,
                w + 0.04,
            ]
            space_fit_in = [
                w,
                w + 0.34,
                w - 0.12,
                M1_ND_LVT[3],
                LI1_ND_LVT[3],
                LI2_ND_LVT[3],
            ]
            spaces = [
                LICON1_ND_LVT[4],
                LICON2_ND_LVT[4],
                MCON_ND_LVT[4],
                M1_ND_LVT[4],
                LI1_ND_LVT[4],
                LI2_ND_LVT[4],
            ]

            if gr == 0:
                layer_names = [
                    licon_layer,
                    mcon_layer,
                    m1_layer,
                    li_layer,
                    li_layer,
                ]
                l1 = [
                    LICON1_ND_LVT[0],
                    MCON_ND_LVT[0],
                    M1_ND_LVT[0],
                    LI1_ND_LVT[0],
                    LI2_ND_LVT[0],
                ]
                sizes_l = [
                    LICON1_ND_LVT[1],
                    MCON_ND_LVT[1],
                    M1_ND_LVT[1],
                    LI1_ND_LVT[1],
                    LI2_ND_LVT[1],
                ]
                sizes_w = [
                    LICON1_ND_LVT[2],
                    MCON_ND_LVT[2],
                    w - 0.05,
                    w - 0.12,
                    w + 0.04,
                ]
                space_fit_in = [
                    w,
                    w - 0.12,
                    M1_ND_LVT[3],
                    LI1_ND_LVT[3],
                    LI2_ND_LVT[3],
                ]
                spaces = [
                    LICON1_ND_LVT[4],
                    MCON_ND_LVT[4],
                    M1_ND_LVT[4],
                    LI1_ND_LVT[4],
                    LI2_ND_LVT[4],
                ]

            self.draw_contact_layer_h(
                layer_names, l1, sizes_w, sizes_l, space_fit_in, spaces
            )
            layer_names = [licon_layer]
            l1 = [LICON3_ND_HVT]
            sizes_l = [LICON3_ND_LVT[1]]
            sizes_w = [LICON3_ND_LVT[2]]
            space_fit_in = [l + LICON3_ND_LVT[3]]
            spaces = [LICON3_ND_LVT[4]]
            if gr:

                self.draw_contact_layer_v(
                    layer_names, l1, sizes_w, sizes_l, space_fit_in, spaces
                )

            c = self.get_c()
            c.write_gds("res_temp.gds")
            layout.read("res_temp.gds")
            cell_name = type
            return layout.cell(cell_name)
