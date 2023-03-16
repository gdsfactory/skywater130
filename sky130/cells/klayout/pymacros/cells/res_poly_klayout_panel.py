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
from .res_klayout_panel import res
from .res_poly_child import res_poly_draw
# ################constants################
L_MIN = 1.65
W_MIN = 0.33
L_MIN_ISO=26.5
W_MIN_ISO=2.65
L_MIN_PO = 0.5
W_MIN_0P35 = 0.35
W_MIN_0P69 = 0.69
W_MIN_1P41 = 1.41
W_MIN_2P85 = 2.85
W_MIN_5P73 = 5.73

# ##############sheet resistances
RES_GEN = 442.6  # sheet res for sky130_fd_pr__res_generic_po

RES_ISO = 153.3  # sheet res for sky130_fd_pr__res_iso_pw

RES_0P35 = 8971.42  # sheet res for sky130_fd_pr__res_high_po_0p35
RES_0P69 = 2308.5  # sheet res for sky130_fd_pr__res_high_po_0p69
RES_1P41 = 552.76  # sheet res for sky130_fd_pr__res_high_po_1p41
RES_2P85 = 135.3  # sheet res for sky130_fd_pr__res_high_po_2p85
RES_5P73 = 33.47  # sheet res for sky130_fd_pr__res_high_po_5p73
# XHIGH
RES_XH_0P35 = 22468.57  # sheet res for sky130_fd_pr__res_xhigh_po_0p35
RES_XH_0P69 = 5779.7  # sheet res for sky130_fd_pr__res_xhigh_po_0p69
RES_XH_1P41 = 1384.63  # sheet res for sky130_fd_pr__res_xhigh_po_1p41
RES_XH_2P85 = 338.87  # sheet res for sky130_fd_pr__res_xhigh_po_2p85
RES_XH_5P73 = 83.8  # sheet res for sky130_fd_pr__res_xhigh_po_5p73
##########################################


class res_poly(res):
    """child class for the front end of the poly res (klayout panel)
    Args:
        res(class): parent class for all types of resistors
        l_min(float): minimum length of the resistor
        w_min(float): minimum width of the resistor

    """

    def __init__(self):
        super().__init__(L_MIN_PO, W_MIN)  # (l_min,w_min)

        # types of resistor you need to add
        # it goes in var self.type

        self.Type_handle.add_choice(
            "sky130_fd_pr__res_generic_po", "sky130_fd_pr__res_generic_po"
        )
        self.Type_handle.add_choice(
            "sky130_fd_pr__res_iso_pw", "sky130_fd_pr__res_iso_pw"
        )        
        self.Type_handle.add_choice(
            "sky130_fd_pr__res_high_po_0p35", "sky130_fd_pr__res_high_po_0p35"
        )
        self.Type_handle.add_choice(
            "sky130_fd_pr__res_high_po_0p69", "sky130_fd_pr__res_high_po_0p69"
        )

        self.Type_handle.add_choice(
            "sky130_fd_pr__res_high_po_1p41", "sky130_fd_pr__res_high_po_1p41"
        )
        self.Type_handle.add_choice(
            "sky130_fd_pr__res_high_po_2p85", "sky130_fd_pr__res_high_po_2p85"
        )
        self.Type_handle.add_choice(
            "sky130_fd_pr__res_high_po_5p73", "sky130_fd_pr__res_high_po_5p73"
        )

        self.Type_handle.add_choice(
            "sky130_fd_pr__res_xhigh_po_0p35",
            "sky130_fd_pr__res_xhigh_po_0p35",
        )
        self.Type_handle.add_choice(
            "sky130_fd_pr__res_xhigh_po_0p69",
            "sky130_fd_pr__res_xhigh_po_0p69",
        )
        self.Type_handle.add_choice(
            "sky130_fd_pr__res_xhigh_po_1p41",
            "sky130_fd_pr__res_xhigh_po_1p41",
        )
        self.Type_handle.add_choice(
            "sky130_fd_pr__res_xhigh_po_2p85",
            "sky130_fd_pr__res_xhigh_po_2p85",
        )
        self.Type_handle.add_choice(
            "sky130_fd_pr__res_xhigh_po_5p73",
            "sky130_fd_pr__res_xhigh_po_5p73",
        )

    def coerce_parameters_impl(self):
        """(override func) check the minimum values of l and w

        decide whether the handle or the numeric parameter has
        changed (by comparing against the effective
        radius ru) and set ru to the effective radius. We also update the
        numerical value or the shape, depending on which on has not changed


        """

        # res_value = sheet res * area
        if self.type == "sky130_fd_pr__res_generic_po":
            super().coerce_parameters_impl(L_MIN, W_MIN)  # (l_min,w_min)
            self.res_value = RES_GEN * self.area
        
        elif self.type == "sky130_fd_pr__res_iso_pw":
            super().coerce_parameters_impl(L_MIN_ISO, W_MIN_ISO)
            self.res_value = RES_ISO * self.area

        elif self.type == "sky130_fd_pr__res_high_po_0p35":
            super().coerce_parameters_impl(L_MIN_PO, W_MIN_0P35)
            self.res_value = RES_0P35 * self.area

        elif self.type == "sky130_fd_pr__res_high_po_0p69":
            super().coerce_parameters_impl(L_MIN_PO, W_MIN_0P69)
            self.res_value = RES_0P69 * self.area
        elif self.type == "sky130_fd_pr__res_high_po_1p41":
            super().coerce_parameters_impl(L_MIN_PO, W_MIN_1P41)
            self.res_value = RES_1P41 * self.area
        elif self.type == "sky130_fd_pr__res_high_po_2p85":
            super().coerce_parameters_impl(L_MIN_PO, W_MIN_2P85)
            self.res_value = RES_2P85 * self.area

        elif self.type == "sky130_fd_pr__res_high_po_5p73":
            super().coerce_parameters_impl(L_MIN_PO, W_MIN_5P73)
            self.res_value = RES_5P73 * self.area

        elif self.type == "sky130_fd_pr__res_xhigh_po_0p35":
            super().coerce_parameters_impl(L_MIN_PO, W_MIN_0P35)
            self.res_value = RES_XH_0P35 * self.area
        elif self.type == "sky130_fd_pr__res_xhigh_po_0p69":
            super().coerce_parameters_impl(L_MIN_PO, W_MIN_0P69)
            self.res_value = RES_XH_0P69 * self.area
        elif self.type == "sky130_fd_pr__res_xhigh_po_1p41":
            super().coerce_parameters_impl(L_MIN_PO, W_MIN_1P41)
            self.res_value = RES_XH_1P41 * self.area
        elif self.type == "sky130_fd_pr__res_xhigh_po_2p85":
            super().coerce_parameters_impl(L_MIN_PO, W_MIN_2P85)
            self.res_value = RES_XH_2P85 * self.area
        elif self.type == "sky130_fd_pr__res_xhigh_po_5p73":
            super().coerce_parameters_impl(L_MIN_PO, W_MIN_5P73)
            self.res_value = RES_XH_5P73 * self.area

    def produce_impl(self):
        """(override func)call the implementation backend code
        create instance and pass it to the parent func

        instance(layout): the result layout to show

        """
        drw = res_poly_draw(self.type)
        instance = drw.your_res(
            self.layout, l=self.len, w=self.w, type=self.type, gr=self.gr
        )
        super().produce_impl(instance)
