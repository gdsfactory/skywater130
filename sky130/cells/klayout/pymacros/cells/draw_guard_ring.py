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

########################################################################################################################
## Guard Ring Pcells Generators for Klayout of skywater130
########################################################################################################################


from .via_generator import *
from .globals import *
from .layers_def import *
import gdsfactory as gf

def draw_gr (
    layout ,
    in_l : float = 1,
    in_w : float = 1,
    grw : float = 0.17,
    con_lev = "li"
) :

    '''
    layout : layout object 
    in_l : float of the inner length of the ring
    in_w : float of the inner width of the ring 
    grw : float of the guard ring width 
    con_lev : connection level of (li, metal1)

    '''

    con_size = (0.17,0.17)
    con_spacing = (0.19, 0.19)
    con_enc = (0.12, 0.12)

    c = gf.Component("sky_ring_gen")
    c_temp = gf.Component("temp_store")

    inner = c_temp.add_ref(gf.components.rectangle(size=(in_w, in_l), layer=tap_layer))
    outer = c_temp.add_ref(gf.components.rectangle(size=(inner.xmax - inner.xmin + 2*grw , inner.ymax - inner.ymin + 2*grw), layer=tap_layer))
    outer.move((-grw, -grw))

    gr = c.add_ref(gf.geometry.boolean(A=outer, B=inner , operation="A-B", layer=tap_layer))

    if con_lev == "li" or con_lev == "metal1":
        li = c.add_ref(gf.geometry.boolean(A=outer, B=inner, operation="A-B", layer=li_layer))

        if grw < con_size[0] + 2*con_enc[0]:
            con_range = (inner.xmin, inner.xmax)
        else : 
            con_range = (outer.xmin, outer.xmax)

        licon_l = c.add_ref(via_generator(x_range=(outer.xmin, inner.xmin), y_range=(inner.ymin + 0.17 , inner.ymax - 0.17), via_enclosure=con_enc, via_layer=licon_layer
        , via_size=con_size, via_spacing=con_spacing))
        licon_r = c.add_ref(via_generator(x_range=(inner.xmax, outer.xmax), y_range=(inner.ymin + 0.17 , inner.ymax - 0.17), via_enclosure=con_enc, via_layer=licon_layer
        , via_size=con_size, via_spacing=con_spacing))
        licon_t = c.add_ref(via_generator(x_range=con_range, y_range=(inner.ymax, outer.ymax), via_enclosure=con_enc, via_layer=licon_layer
        , via_size=con_size, via_spacing=con_spacing))
        licon_b = c.add_ref(via_generator(x_range=con_range, y_range=(outer.ymin, inner.ymin), via_enclosure=con_enc, via_layer=licon_layer
        , via_size=con_size, via_spacing=con_spacing))



    if con_lev == "metal1" :
        m1 = c.add_ref(gf.geometry.boolean(A=outer, B=inner, operation="A-B", layer=m1_layer))

        mcon_l = c.add_ref(via_generator(x_range=(outer.xmin, inner.xmin), y_range=(inner.ymin + 0.17 , inner.ymax - 0.17), via_enclosure=con_enc, via_layer=mcon_layer
        , via_size=con_size, via_spacing=con_spacing))
        mcon_r = c.add_ref(via_generator(x_range=(inner.xmax, outer.xmax), y_range=(inner.ymin + 0.17 , inner.ymax - 0.17), via_enclosure=con_enc, via_layer=mcon_layer
        , via_size=con_size, via_spacing=con_spacing))
        mcon_t = c.add_ref(via_generator(x_range=con_range, y_range=(inner.ymax, outer.ymax), via_enclosure=con_enc, via_layer=mcon_layer
        , via_size=con_size, via_spacing=con_spacing))
        mcon_b = c.add_ref(via_generator(x_range=con_range, y_range=(outer.ymin, inner.ymin), via_enclosure=con_enc, via_layer=mcon_layer
        , via_size=con_size, via_spacing=con_spacing))



    c.write_gds("ring_temp.gds")
    layout.read("ring_temp.gds")
    cell_name = "sky_ring_gen"

   

    return layout.cell(cell_name)
