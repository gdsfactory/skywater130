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
from .res_metal_child import res_metal_draw

# ################constants################
L_MIN = 0.17
W_MIN = 0.17

L_MIN_M1 = 0.14
L_MIN_M2 = 0.14
L_MIN_M3 = 0.3
L_MIN_M4 = 0.3
L_MIN_M5 = 1.6

# ##############sheet resistances
RES_GEN = 442.9  # sheet res for sky130_fd_pr__res_generic_l1


RES_M1 = 6.377  # sheet res for sky130_fd_pr__res_generic_m1
RES_M2 = 6.377  # sheet res for sky130_fd_pr__res_generic_m2
RES_M3 = 0.522  # sheet res for sky130_fd_pr__res_generic_m3
RES_M4 = 0.522  # sheet res for sky130_fd_pr__res_generic_m4
RES_M5 = 0.0113  # sheet res for sky130_fd_pr__res_generic_m5

##########################################


class res_metal(res):
    """child class for the front end of the poly res (klayout panel)
    Args:
        res(class): parent class for all types of resistors
        l_min(float): minimum length of the resistor
        w_min(float): minimum width of the resistor

    """

    def __init__(self):
        super().__init__(L_MIN, W_MIN)  # (l_min,w_min)

        # types of resistor you need to add
        # it goes in var self.type

        self.Type_handle.add_choice(
            "sky130_fd_pr__res_generic_l1", "sky130_fd_pr__res_generic_l1"
        )
        self.Type_handle.add_choice(
            "sky130_fd_pr__res_generic_m1", "sky130_fd_pr__res_generic_m1"
        )
        self.Type_handle.add_choice(
            "sky130_fd_pr__res_generic_m2", "sky130_fd_pr__res_generic_m2"
        )

        self.Type_handle.add_choice(
            "sky130_fd_pr__res_generic_m3", "sky130_fd_pr__res_generic_m3"
        )
        self.Type_handle.add_choice(
            "sky130_fd_pr__res_generic_m4", "sky130_fd_pr__res_generic_m4"
        )
        self.Type_handle.add_choice(
            "sky130_fd_pr__res_generic_m5", "sky130_fd_pr__res_generic_m5"
        )

    def coerce_parameters_impl(self):
        """(override func) check the minimum values of l and w

        decide whether the handle or the numeric parameter has
        changed (by comparing against the effective
        radius ru) and set ru to the effective radius. We also update the
        numerical value or the shape, depending on which on has not changed


        """

        # res_value = sheet res * area
        if self.type == "sky130_fd_pr__res_generic_l1":
            super().coerce_parameters_impl(L_MIN, W_MIN)  # (l_min,w_min)
            self.res_value = RES_GEN * self.area

        elif self.type == "sky130_fd_pr__res_generic_m1":
            super().coerce_parameters_impl(L_MIN_M1, L_MIN_M1)
            self.res_value = RES_M1 * self.area
        elif self.type == "sky130_fd_pr__res_generic_m2":
            super().coerce_parameters_impl(L_MIN_M2, L_MIN_M2)
            self.res_value = RES_M2 * self.area
        elif self.type == "sky130_fd_pr__res_generic_m3":
            super().coerce_parameters_impl(L_MIN_M3, L_MIN_M3)
            self.res_value = RES_M3 * self.area
        elif self.type == "sky130_fd_pr__res_generic_m4":
            super().coerce_parameters_impl(L_MIN_M4, L_MIN_M4)
            self.res_value = RES_M4 * self.area
        elif self.type == "sky130_fd_pr__res_generic_m5":
            super().coerce_parameters_impl(L_MIN_M5, L_MIN_M5)
            self.res_value = RES_M5 * self.area

    def produce_impl(self):
        """(override func)call the implementation backend code
        create instance and pass it to the parent func

        instance(layout): the result layout to show

        """
        drw = res_metal_draw(self.type)
        instance = drw.your_res(
            self.layout, l=self.len, w=self.w, type=self.type
        )
        super().produce_impl(instance)
