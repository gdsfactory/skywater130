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
## Diode Pcells Generators for Klayout of skywater130
########################################################################################################################


import os

from .via_generator import *
from .globals import *
from .layers_def import *
import gdsfactory as gf

 
gds_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"fixed_devices/photodiode" )  # parent file path 


def draw_photodiode(layout, device_name):

    '''
    drawing photo diode device 
    '''
    
    if device_name in PHOTO_D_DEV :
        layout.read(f"{gds_path}/{device_name}.gds")
        cell_name = device_name
    else :
        cell_name = device_name  

    return layout.cell(cell_name)

def draw_diode (
    layout ,
    d_type = "n",
    w : float = 0.45,
    l: float = 0.45,
    type = "sky130_fd_pr__diode_pw2nd_05v5",
    cath_w : float = 0.17,
    grw : float = 0.17,
) :

    '''
    Retern diode 

    Args: 
        layout : layout object 
        d_type : string of the diode type [n,p]
        w : float of the diode width
        l: float of the diode length
        type : string of the device type
        cath_w : float of cathode width in case of p_diode
        grw : float of the gaurd ring width 

    '''

    c = gf.Component("sky_diode_dev")

    c_inst = gf.Component("dev inst")
    

    # used dimensions and layers 

    npsd_enc = 0.125
    diff_tap_spacing : float = 0.37

    

    con_size = (0.17,0.17)
    con_spacing = (0.19,0.19)
    d_con_enc = (0.06,0.06)
    t_con_enc = (0.12,0.12)


    li_enc = 0.08
    m1_enc = 0.03

    con_layer = [licon_layer, mcon_layer]

    lvt_enc : float = 0.18

    hv_enc = 0.185 

    nwell_enc = 0.185 

    

    if d_type == "n":
        d_npsd_layer = nsdm_layer
        t_npsd_layer = psdm_layer
    elif d_type == "p":
        d_npsd_layer = psdm_layer
        t_npsd_layer = nsdm_layer
    
    # generating diff and areaid_diode and its contacts 
    diff = c_inst.add_ref(gf.components.rectangle(size=(w,l),layer=diff_layer))
    diode = c_inst.add_ref(gf.components.rectangle(size=(w,l),layer=areaid_dio_layer))


    d_npsd = c_inst.add_ref(gf.components.rectangle(size=(w+ 2*npsd_enc, l+ 2*npsd_enc),layer=d_npsd_layer))
    d_npsd.move((-npsd_enc,-npsd_enc))

    
    for i in range(2):
        d_con = c_inst.add_ref(via_generator(x_range=(0,w),y_range=(0,l),via_enclosure=d_con_enc,via_layer=con_layer[i],via_size=con_size,via_spacing=con_spacing))

    d_li = c_inst.add_ref(gf.components.rectangle(size=(diode.xmax - diode.xmin + 2*(li_enc-d_con_enc[0]),d_con.ymax - d_con.ymin + 2*li_enc),layer=li_layer))
    d_li.move((-(li_enc-d_con_enc[0]) , d_con.ymin -li_enc))
    d_m1 = c_inst.add_ref(gf.components.rectangle(size=(w,d_li.ymax - d_li.ymin + 2*m1_enc),layer=m1_layer))
    d_m1.movey(d_li.ymin - m1_enc)

    # generating gaurd ring and its contacts 
    c_temp = gf.Component("temp store")
    tap_in = c_temp.add_ref(gf.components.rectangle(size=(w +2*diff_tap_spacing,l +2*diff_tap_spacing)
    ,layer=tap_layer))
    tap_in.move((-diff_tap_spacing,-diff_tap_spacing))
    tap_out = c_temp.add_ref(gf.components.rectangle(size=(tap_in.xmax - tap_in.xmin + 2*cath_w, tap_in.ymax - tap_in.ymin + 2*cath_w),layer=tap_layer))
    tap_out.move((tap_in.xmin - cath_w, tap_in.ymin-cath_w))
    tap = c_inst.add_ref(gf.geometry.boolean(A=tap_out, B = tap_in, operation="A-B",layer=tap_layer))


    t_npsd_in = c_temp.add_ref(gf.components.rectangle(size=(tap_in.xmax - tap_in.xmin - 2*npsd_enc, tap_in.ymax - tap_in.ymin - 2*npsd_enc)
    ,layer=t_npsd_layer))
    t_npsd_in.move((tap_in.xmin + npsd_enc, tap_in.ymin + npsd_enc))
    t_npsd_out = c_temp.add_ref(gf.components.rectangle(size=(tap_out.xmax - tap_out.xmin + 2*npsd_enc, tap_out.ymax - tap_out.ymin + 2*npsd_enc)
    ,layer=t_npsd_layer))
    t_npsd_out.move((tap_out.xmin - npsd_enc, tap_out.ymin - npsd_enc))
    t_npsd = c_inst.add_ref(gf.geometry.boolean(A=t_npsd_out, B=t_npsd_in, operation="A-B",layer=t_npsd_layer))
    
    if cath_w < con_size[0] + 2*t_con_enc[0]:
        t_con_range = (tap_in.xmin, tap_in.xmax)
    else :
        t_con_range = (tap_out.xmin, tap_out.xmax)

    t_licon_u = c_inst.add_ref(via_generator(x_range=t_con_range,y_range=(tap_in.ymax,tap_out.ymax),via_enclosure=t_con_enc
    , via_layer=licon_layer,via_size=con_size,via_spacing=con_spacing))

    t_licon_d = c_inst.add_ref(via_generator(x_range=t_con_range,y_range=(tap_out.ymin,tap_in.ymin),via_enclosure=t_con_enc
    , via_layer=licon_layer,via_size=con_size,via_spacing=con_spacing))

    t_licon_l = c_inst.add_ref(via_generator(x_range=(tap_out.xmin, tap_in.xmin),y_range=(tap_in.ymin +0.17,tap_in.ymax-0.17),via_enclosure=t_con_enc
    , via_layer=licon_layer,via_size=con_size,via_spacing=con_spacing))

    t_licon_r = c_inst.add_ref(via_generator(x_range=(tap_in.xmax, tap_out.xmax),y_range=(tap_in.ymin +0.17,tap_in.ymax-0.17),via_enclosure=t_con_enc
    , via_layer=licon_layer,via_size=con_size,via_spacing=con_spacing))

    tap_li_in = c_temp.add_ref(gf.components.rectangle(size=(w+2*diff_tap_spacing,l+2*diff_tap_spacing),layer=li_layer))
    tap_li_in.move((-diff_tap_spacing,-diff_tap_spacing))
    tap_li_out = c_temp.add_ref(gf.components.rectangle(size=(tap_in.xmax - tap_in.xmin + 2*cath_w, tap_in.ymax - tap_in.ymin + 2*cath_w),layer=li_layer))
    tap_li_out.move((tap_in.xmin - cath_w, tap_in.ymin-cath_w))
    tap_li = c_inst.add_ref(gf.geometry.boolean(A=tap_li_out, B = tap_li_in, operation="A-B",layer=li_layer))

    if type ==  "sky130_fd_pr__diode_pw2nd_05v5_lvt" or type == "sky130_fd_pr__diode_pw2nd_05v5_nvt" or type == "sky130_fd_pr__diode_pd2nw_05v5_lvt": 
        lvt = c_inst.add_ref(gf.components.rectangle(size=(w+2*lvt_enc,l+2*lvt_enc),layer=lvtn_layer))
        lvt.move((-lvt_enc,-lvt_enc))
    
    if type == "sky130_fd_pr__diode_pw2nd_05v5_nvt" or type == "sky130_fd_pr__diode_pw2nd_11v0" : 
        hvntm = c_inst.add_ref(gf.components.rectangle(size=(w+2*hv_enc,l+2*hv_enc),layer=hvntm_layer))
        hvntm.move((diode.xmin - hv_enc, diode.ymin - hv_enc)) 

    if type == "sky130_fd_pr__diode_pd2nw_05v5_hvt"  :
        hvt = c_inst.add_ref(gf.components.rectangle(size=(w+2*lvt_enc,l+2*lvt_enc),layer=hvtp_layer))
        hvt.move((-lvt_enc,-lvt_enc))

    if type == "sky130_fd_pr__diode_pw2nd_05v5_nvt" or type == "sky130_fd_pr__diode_pw2nd_11v0" :
        hvi = c_inst.add_ref(gf.components.rectangle(size=(tap_out.xmax - tap_out.xmin + 2*hv_enc, tap_out.ymax - tap_out.ymin + 2*hv_enc),layer=hvi_layer))
        hvi.move((tap_out.xmin - hv_enc, tap_out.ymin - hv_enc))

    # drawing nwell and outer gaurd ring  in case of p-diode 
    if d_type == "p":

        if type == "sky130_fd_pr__diode_pd2nw_11v0":
            nwell_enc = 0.34 

        nwell = c_inst.add_ref(gf.components.rectangle(size=(tap_out.xmax - tap_out.xmin + 2*nwell_enc, tap_out.ymax - tap_out.ymin + 2*nwell_enc),layer=nwell_layer))
        nwell.move((tap_out.xmin - nwell_enc, tap_out.ymin - nwell_enc))

        gr_in = c_temp.add_ref(gf.components.rectangle(size = (c_inst.xmax-c_inst.xmin + 2*diff_tap_spacing,c_inst.ymax - c_inst.ymin + 2*diff_tap_spacing )
        , layer= tap_layer))
        gr_in.move((c_inst.xmin - diff_tap_spacing, c_inst.ymin - diff_tap_spacing))
        gr_out = c_temp.add_ref(gf.components.rectangle(size=(gr_in.xmax - gr_in.xmin + 2*grw, gr_in.ymax - gr_in.ymin + 2*grw),layer=tap_layer))
        gr_out.move((gr_in.xmin - grw, gr_in.ymin - grw))
        gr = c.add_ref(gf.geometry.boolean(A=gr_out, B=gr_in , operation= "A-B", layer=tap_layer))

        gr_li = c.add_ref(gf.geometry.boolean(A=gr_out, B=gr_in , operation= "A-B", layer=li_layer))

        g_psdm_in = c.add_ref(gf.components.rectangle(size=(gr_in.xmax - gr_in.xmin - 2*npsd_enc, gr_in.ymax - gr_in.ymin - 2*npsd_enc),layer=psdm_layer))
        g_psdm_in.move((gr_in.xmin + npsd_enc, gr_in.ymin + npsd_enc))
        g_psdm_out = c.add_ref(gf.components.rectangle(size=(gr_out.xmax - gr_out.xmin + 2*npsd_enc, gr_out.ymax - gr_out.ymin + 2*npsd_enc),layer=psdm_layer))
        g_psdm_out.move((gr_out.xmin - npsd_enc, gr_out.ymin - npsd_enc))


        if grw < con_size[0] + 2*t_con_enc[0] : 
            g_con_range = (gr_in.ymin , gr_in.ymax )
        else : 
            g_con_range = (gr_out.ymin , gr_out.ymax )
        
        g_licon_u = c.add_ref(via_generator(x_range=(gr_in.xmin + 0.17, gr_in.xmax-0.17),y_range=(gr_in.ymax,gr_out.ymax),via_enclosure=t_con_enc
        , via_layer=licon_layer,via_size=con_size,via_spacing=con_spacing))

        g_licon_d = c.add_ref(via_generator(x_range=(gr_in.xmin + 0.17, gr_in.xmax-0.17),y_range=(gr_out.ymin,gr_in.ymin),via_enclosure=t_con_enc
        , via_layer=licon_layer,via_size=con_size,via_spacing=con_spacing))

        g_licon_l = c.add_ref(via_generator(x_range=(gr_out.xmin, gr_in.xmin),y_range=g_con_range,via_enclosure=t_con_enc
        , via_layer=licon_layer,via_size=con_size,via_spacing=con_spacing))

        g_licon_r = c.add_ref(via_generator(x_range=(gr_in.xmax, gr_out.xmax),y_range=g_con_range,via_enclosure=t_con_enc
        , via_layer=licon_layer,via_size=con_size,via_spacing=con_spacing))


        if type == "sky130_fd_pr__diode_pd2nw_11v0":
            hvi = c.add_ref(gf.components.rectangle(size=(gr_out.xmax - gr_out.xmin + 2*hv_enc, gr_out.ymax - gr_out.ymin + 2*hv_enc),layer=hvi_layer))
            hvi.move((gr_out.xmin - hv_enc, gr_out.ymin - hv_enc))




    c.add_ref(c_inst)

    c.write_gds("diode_temp.gds")
    layout.read("diode_temp.gds")
    cell_name = "sky_diode_dev"


    return layout.cell(cell_name)
     
