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
from .res_diff_child import res_diff_draw

# ################constants################
L_MIN = 2.1
W_MIN = 0.42
# ##############sheet resistances
RES_ND_LVT = 772.2  # sheet res for sky130_fd_pr__res_nd_lvt
RES_ND_HVT = 714.28  # sheet res for sky130_fd_pr__res_nd_hvt
RES_PD = 1172.33  # sheet res for sky130_fd_pr__res_pd_lvt,hvt
##########################################


class res_diff(res):
    """child class for the front end of the diff res (klayout panel)
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
            "sky130_fd_pr__res_nd_lvt", "sky130_fd_pr__res_nd_lvt"
        )
        self.Type_handle.add_choice(
            "sky130_fd_pr__res_nd_hvt", "sky130_fd_pr__res_nd_hvt"
        )

        self.Type_handle.add_choice(
            "sky130_fd_pr__res_pd_lvt", "sky130_fd_pr__res_pd_lvt"
        )
        self.Type_handle.add_choice(
            "sky130_fd_pr__res_pd_hvt", "sky130_fd_pr__res_pd_hvt"
        )

    def coerce_parameters_impl(self):
        """(override func) check the minimum values of l and w

        decide whether the handle or the numeric parameter has
        changed (by comparing against the effective
        radius ru) and set ru to the effective radius. We also update the
        numerical value or the shape, depending on which on has not changed


        """
        super().coerce_parameters_impl(L_MIN, W_MIN)  # (l_min,w_min)
        # res_value = sheet res * area
        if self.type == "sky130_fd_pr__res_nd_lvt":
            self.res_value = RES_ND_LVT * self.area
        elif self.type == "sky130_fd_pr__res_nd_hvt":
            self.res_value = RES_ND_HVT * self.area
        else:
            self.res_value = RES_PD * self.area

    def produce_impl(self):
        """(override func)call the implementation backend code
        create instance and pass it to the parent func

        instance(layout): the result layout to show

        """
        drw = res_diff_draw(self.type)
        instance = drw.your_res(
            self.layout, l=self.len, w=self.w, type=self.type, gr=self.gr
        )
        super().produce_impl(instance)
