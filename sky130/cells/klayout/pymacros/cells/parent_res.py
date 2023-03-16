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

import gdsfactory as gf
import math

from abc import ABC, abstractmethod

# ##############CONSTANT############3


CONTACT_SPACE=0.19
CONTACT_S=0.18
CONTACT_N=10
############################3
class draw_res(ABC):
    """parent abstracted class for the backend of the res
    Args:
        type (str): type of the res
    """

    def __init__(self, type):
        self.type_ = type
        self.c = gf.Component(self.type_)

    def set_l_w(self, len, wid):
        """set the length and width of the res
        Args:
            len(float):  length of the resistor
            wid(float):  width of the resistor
        """
        self.l_res = len
        self.w_res = wid

    def draw_rect_layer(self, layer_names, l_space, w_space):
        """draw the rect layers of the res
        Args:
            layer_names(list[layers]):
                list of the layer names
            l_space(list[float]):
                [0.5*length of the layers - 0.5*length of the marked layer]
            w_space(list[float]):
                [0.5*width of the layers - 0.5*width of the marked layer]

        """
        for layer_, l, w in zip(layer_names, l_space, w_space):
            self.c.add_ref(
                gf.components.rectangle(
                    size=(self.w_res + 2 * w, self.l_res + 2 * l),
                    layer=layer_,
                    centered=True,
                )
            )

    def draw_frame_layer(self, lay_nm, l_sp, w_sp, thi):
        """draw the frame layers of the res
        Args:
            lay_nm(list[layers]):
                list of the layer names
            l_sp(list[float]):
                [0.5*length of the layers - 0.5*length of the marked layer]
            w_sp(list[float]):
                [0.5*width of the layers - 0.5*width of the marked layer]
            thi(list[float]):
                list of the thickness of the frame

        """
        for layer_, l, w, thick in zip(lay_nm, l_sp, w_sp, thi):
            l_h = thick
            w_h = self.w_res + 2 * w

            l_v = self.l_res + 2 * l - 2 * thick
            w_v = thick

            res1 = self.c.add_ref(
                gf.components.rectangle(
                    size=(w_h, l_h), layer=layer_, centered=True
                )
            )
            res2 = self.c.add_ref(
                gf.components.rectangle(
                    size=(w_h, l_h), layer=layer_, centered=True
                )
            )

            res1.movey(0.5 * l_v + 0.5 * l_h)
            res2.movey(-1 * (0.5 * l_v + 0.5 * l_h))

            res1 = self.c.add_ref(
                gf.components.rectangle(
                    size=(w_v, l_v), layer=layer_, centered=True
                )
            )
            res2 = self.c.add_ref(
                gf.components.rectangle(
                    size=(w_v, l_v), layer=layer_, centered=True
                )
            )

            res1.movex(0.5 * w_h - 0.5 * w_v)
            res2.movex(-1 * (0.5 * w_h - 0.5 * w_v))

    def draw_contact_layer_h(
        self, layer_names, l_space, sizes_w, sizes_l, s_fit_in, s_btw
    ):
        """draw the horizontal contact layers of the res
        Args:
            layer_names(list[layers]):
                list of the layer names
            l_space(list[float]):
                [0.5*length of the layers - 0.5*length of the marked layer]
            sizes_w(list[float]):
                list of contacts width
            sizes_l(list[float]):
                list of contacts length
            s_fit_in(list[float]):
                list of total length to fit contacts in
            s_btw(list[float]):
                list of the spaces btw the contacts

        """
        for layer_, l, size_l, size_w, space_fit, space_btw in zip(
            layer_names, l_space, sizes_l, sizes_w, s_fit_in, s_btw
        ):

            counts = math.floor((space_fit) / (size_w + space_btw))
            if counts < 1:
                counts = 1
            res = gf.components.rectangle(
                size=(size_w, size_l), layer=layer_, centered=True
            )
            res_ar1 = self.c.add_array(
                res,
                rows=1,
                columns=counts,
                spacing=(size_w + space_btw, size_w + space_btw),
            )
            res_ar2 = self.c.add_array(
                res,
                rows=1,
                columns=counts,
                spacing=(size_w + space_btw, size_w + space_btw),
            )

            res_ar1.movey(size_l * 0.5 + l + self.l_res * 0.5)
            res_ar2.movey(-1 * (size_l * 0.5 + l + self.l_res * 0.5))

            res_ar1.movex(-(counts - 1) * (size_w + space_btw) * 0.5)
            res_ar2.movex(-(counts - 1) * (size_w + space_btw) * 0.5)

    def draw_contact_layer_v(
        self,
        layer_names,
        l_space,
        sizes_w,
        sizes_l,
        space_fit_in,
        spaces_btw=None,
    ):
        """draw the vertical contact layers of the res
        Args:
            layer_names(list[layers]):
                list of the layer names
            l_space(list[float]):
                [0.5*length of the layers - 0.5*length of the marked layer]
            sizes_w(list[float]):
                list of contacts width
            sizes_l(list[float]):
                list of contacts length
            space_fit_in(list[float]):
                list of total length to fit contacts in
            spaces_btw(list[float]):
                list of the spaces btw the contacts
        """
        if spaces_btw is None:
            spaces_btw = sizes_w
        for layer_, l, size_l, size_w, space_fit, space_btw in zip(
            layer_names,
            l_space,
            sizes_l,
            sizes_w,
            space_fit_in,
            spaces_btw,
        ):

            counts = math.floor((space_fit) / (size_w + space_btw))
            res = gf.components.rectangle(
                size=(size_w, size_l), layer=layer_, centered=True
            )
            res_ar1 = self.c.add_array(
                res,
                rows=counts,
                columns=1,
                spacing=(size_l + space_btw, size_l + space_btw),
            )
            res_ar2 = self.c.add_array(
                res,
                rows=counts,
                columns=1,
                spacing=(size_l + space_btw, size_l + space_btw),
            )

            res_ar1.movey(-(counts - 1) * size_l)
            res_ar2.movey(-(counts - 1) * size_l)

            res_ar1.movex(0.5 * self.w_res + l + 0.5 * size_w)
            res_ar2.movex(-(0.5 * self.w_res + l + 0.5 * size_w))

    def draw_2dArr_layer(self, layer_names, mcon_d, l_up=0, l_down=0, n=0):
        """draw the 2d contact layers of the res
        Args:
            layer_names(list[layers]):  list of the layer names
            mcon_d(list[float]):  list of contacts thickness
            l_up(list[float]):  upper contacts array space from marked layer
            l_down(list[float]):  down contacts array space from marked layer
            n(list[float]):  list of the 1 for 2d arr and 0 for 1d arr
        """
        res = gf.components.rectangle(
            size=(mcon_d, mcon_d), layer=layer_names, centered=True
        )

        counts_arr = math.floor(self.w_res / (2*CONTACT_S))
        if counts_arr <= 0:
            counts_arr = 1
        if counts_arr % 2 == 0 and counts_arr > CONTACT_N:
            counts_arr = counts_arr - 1
        res_ar1 = self.c.add_array(
            res,
            rows=6,
            columns=counts_arr + n,
            spacing=(mcon_d + CONTACT_SPACE, mcon_d + CONTACT_SPACE),
        )
        res_ar2 = self.c.add_array(
            res,
            rows=6,
            columns=counts_arr + n,
            spacing=(mcon_d + CONTACT_SPACE, mcon_d + CONTACT_SPACE),
        )

        res_ar1.movey(mcon_d * 0.5 + l_up + (self.l_res) * 0.5)
        res_ar2.movey(-1 * (mcon_d * 0.5 + l_down + (self.l_res) * 0.5))
        if (counts_arr + n) != 1:
            # res_ar1.movex(-1*(mcon_d * 0.5 + 0.5*self.w_res))
            # res_ar2.movex(-1 * (mcon_d * 0.5 +0.5*self.w_res))
            res_ar1.movex(-(counts_arr + n - 1) * CONTACT_S)
            res_ar2.movex(-(counts_arr + n - 1) * CONTACT_S)

    def get_c(self):
        """get component

        Returns:
            c(gf.component): layout creates
        """
        return self.c

    @abstractmethod
    def your_res():
        """must override in the child class"""
        pass
