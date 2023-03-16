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
# via Generator for skywater130
########################################################################################################################


from math import ceil, floor
from tracemalloc import start
import gdsfactory as gf
from gdsfactory.types import Float2 , LayerSpec
from .layers_def import *

@gf.cell
def via_generator(
    x_range : Float2 = (0,1) ,
    y_range : Float2 = (0,1) ,
    via_size : Float2 = (0.17,0.17),
    via_layer : LayerSpec = (66,44),
    via_enclosure : Float2 = (0.06,0.06),
    via_spacing : Float2 = (0.17,0.17)
    

) -> gf.Component():
    
    """
    return only vias withen the range xrange and yrange while enclosing by via_enclosure 
    and set number of rows and number of coloumns according to ranges and via size and spacing  

    """
 
    c = gf.Component()

    width = x_range[1] - x_range[0]
    length = y_range[1] - y_range[0]
    nr = floor(length / (via_size[1] + via_spacing[1]))
    if (length - nr*via_size[1] - (nr-1)*via_spacing[1])/2 < via_enclosure[1]:
        nr -= 1

    if nr <1 :
        nr = 1
    
    nc = ceil(width / (via_size[0]+via_spacing[0]))
    

    if (round(width - nc*via_size[0] - (nc-1)*via_spacing[0],2))/2 < via_enclosure[0]:
        nc -= 1
    
    if nc<1 :
        nc =1 
    

    via_sp = (via_size[0]+via_spacing[0],via_size[1]+via_spacing[1])

    rect_via = gf.components.rectangle(size = via_size , layer= via_layer)

    via_arr = c.add_array(rect_via, rows= nr, columns= nc , spacing=via_sp)

    via_arr.move((x_range[0],y_range[0]))

    via_arr.movex((width - nc*via_size[0] - (nc-1)*via_spacing[0])/2)
    via_arr.movey((length - nr*via_size[1] - (nr-1)*via_spacing[1])/2)

    return c

@gf.cell
def via_stack (
    x_range : Float2 = (0,1),
    y_range : Float2 = (0,1),
    base_layer : LayerSpec = diff_layer,
    slotted_licon : int = 0,
    metal_level : int = 1,
    li_enc_dir = "V"

) -> gf.Component :

    """
    return via stack till the metal level indicated where :
    metal_level 0 : till li
    metal_level 1 : till m1
    metal_level 2 : till m2
    metal_level 3 : till m3
    metal_level 4 : till m4
    metal_level 5 : till m5
    withen the range xrange and yrange and expecting the base_layer to be drawen 

    """

    c = gf.Component()

    # vias dimensions 

    if slotted_licon == 1 :
        licon_size = (0.19,2)

    else :
        licon_size = (0.17,0.17)
    
    mcon_size = (0.17,0.17)
    

    if base_layer == diff_layer or base_layer == tap_layer :
        con_enc = (0.06,0.06)
    
    #elif  base_layer == tap_layer:
    #    con_enc = (0.1,0.06)
        

    elif base_layer == poly_layer :
        con_enc = (0.05,0.08)
        npc_enc = 0.01 
        npc = c.add_ref(gf.components.rectangle(size=(x_range[1]-x_range[0]+2*npc_enc, y_range[1]-y_range[0]+2*npc_enc),layer=npc_layer))
        npc.move((x_range[0]-npc_enc, y_range[0]-npc_enc))
        
    else : 
        pass 

    if li_enc_dir == "H":
        li_enc = (0.08,0)
        m1_enc = (0.06,0.03)
    elif li_enc_dir == "V" : 
        li_enc = (0,0.08)
        m1_enc = (0.03,0.06)

    con_spacing = (0.19,0.19)

    via1_size = (0.15,0.15)
    via1_spacing = (0.17,0.17)
    via1_enc = (0.055,0.085)

    via2_size = (0.2,0.2)
    via2_enc = (0.04,0.085)
    via2_spacing = (0.2,0.2)

    via3_size = (0.2,0.2)
    via3_enc = (0.06,0.09)
    via3_spacing = (0.2,0.2)

    via4_size = (0.8,0.8)
    via4_enc = (0.19,0.19)
    via4_spacing = (0.8,0.8)


    if metal_level >= 0 :
        licon_gen = via_generator(x_range=x_range,y_range=y_range,via_size=licon_size,via_enclosure=con_enc,via_layer=licon_layer,via_spacing=con_spacing)
        licon = c.add_ref(licon_gen)
                

        li = c.add_ref(gf.components.rectangle(size=(licon.xmax-licon.xmin+(2*li_enc[0]),licon.ymax-licon.ymin+(2*li_enc[1])),layer=li_layer))
        li.move((licon.xmin-li_enc[0], licon.ymin-li_enc[1]))

    if metal_level >= 1 :
        mcon_gen = via_generator(x_range=x_range,y_range=y_range,via_size=mcon_size,via_enclosure=con_enc,via_layer=mcon_layer,via_spacing=con_spacing)
        mcon = c.add_ref(mcon_gen)    
        
        

        if (mcon.xmax-mcon.xmin + 2*m1_enc[0]) < (via1_size[0] + 2*via1_enc[0]) and metal_level >=2:
            m1_x = via1_size[0] + 2*via1_enc[0]
            

        else :
            m1_x = mcon.xmax-mcon.xmin + 2*m1_enc[0]
            

        if (mcon.ymax-mcon.ymin + 2*m1_enc[1]) < (via1_size[1] + 2*via1_enc[1]) and metal_level >=2 :
            m1_y = via1_size[1] + 2*via1_enc[1]
            
        else :
            m1_y = mcon.ymax-mcon.ymin + 2*m1_enc[1]
        
        m1_a = 0.084
        
        if (m1_x*m1_y)< m1_a :
            m1_x = m1_a/m1_y
            
            
        
        m1_mx = (m1_x - (mcon.xmax - mcon.xmin))/2
        m1_my = (m1_y - (mcon.ymax - mcon.ymin))/2


        m1 = c.add_ref(gf.components.rectangle(size=(m1_x,m1_y),layer=m1_layer))
        m1.move((mcon.xmin - m1_mx, mcon.ymin - m1_my))

    if metal_level >=2 :
        via1_gen = via_generator(x_range= (m1.xmin, m1.xmax), y_range=(m1.ymin,m1.ymax),via_size=via1_size,via_enclosure=via1_enc
        ,via_layer=via1_layer,via_spacing=via1_spacing)
        via1 = c.add_ref(via1_gen)

        if (via1.xmax-via1.xmin) > (via1.ymax - via1.ymin):
            m2_enc = (0.055,0.085)
        else : 
            m2_enc = (0.085,0.055)
        
        if (via1.xmax-via1.xmin + 2*m2_enc[0]) < (via2_size[0] + 2*via2_enc[0]) and metal_level >=3:
            m2_x = via2_size[0] + 2*via2_enc[0]
            

        else :
            m2_x = via1.xmax-via1.xmin + 2*m2_enc[0]
            

        if (via1.ymax-via1.ymin + 2*m2_enc[1]) < (via2_size[1] + 2*via2_enc[1]) and metal_level >=3:
            m2_y = via2_size[1] + 2*via2_enc[1]
            

        else :
            m2_y = via1.ymax-via1.ymin + 2*m2_enc[1]
            
        m2_mx = (m2_x - (via1.xmax - via1.xmin))/2
        m2_my = (m2_y - (via1.ymax - via1.ymin))/2

        m2 = c.add_ref(gf.components.rectangle(size=(m2_x,m2_y),layer=m2_layer))
        m2.move((via1.xmin - m2_mx, via1.ymin -m2_my))
    
    if metal_level >= 3 : 
        via2_gen = via_generator(x_range= (m2.xmin, m2.xmax), y_range=(m2.ymin,m2.ymax),via_size=via2_size,via_enclosure=via2_enc
        ,via_layer=via2_layer,via_spacing=via2_spacing)
        via2 = c.add_ref(via2_gen)

        m3_enc = (0.065,0.065)

        if (via2.xmax-via2.xmin + 2*m3_enc[0]) < (via3_size[0] + 2*via3_enc[0]) and metal_level >= 4:
            m3_x = via3_size[0] + 2*via3_enc[0]
            
        else :
            m3_x = via2.xmax-via2.xmin + 2*m3_enc[0]
            

        if (via2.ymax-via2.ymin + 2*m3_enc[1]) < (via3_size[1] + 2*via3_enc[1]) and metal_level >=4:
            m3_y = via3_size[1] + 2*via3_enc[1]
            
        else :
            m3_y = via2.ymax-via2.ymin + 2*m3_enc[1]
            
        m3_mx = (m3_x - (via2.xmax - via2.xmin))/2
        m3_my = (m3_y - (via2.ymax - via2.ymin))/2
        

        m3 = c.add_ref(gf.components.rectangle(size=(m3_x,m3_y),layer=m3_layer))
        m3.move((via2.xmin - m3_mx, via2.ymin - m3_my))

    if metal_level >= 4 : 
        via3_gen = via_generator(x_range= (m3.xmin, m3.xmax), y_range=(m3.ymin,m3.ymax),via_size=via3_size,via_enclosure=via3_enc
        ,via_layer=via3_layer,via_spacing=via3_spacing)
        via3 = c.add_ref(via3_gen)

        m4_enc = (0.065,0.065)

        if (via3.xmax-via3.xmin + 2*m4_enc[0]) < (via4_size[0] + 2*via4_enc[0]) and metal_level >=5:
            m4_x = via4_size[0] + 2*via4_enc[0]
            
        else :
            m4_x = via3.xmax-via3.xmin + 2*m4_enc[0]
            

        if (via3.ymax-via3.ymin + 2*m4_enc[1]) < (via4_size[1] + 2*via4_enc[1]) and metal_level >=5:
            m4_y = via4_size[1] + 2*via4_enc[1]
            
            
        else :
            m4_y = via3.ymax-via3.ymin + 2*m4_enc[1]
            
        m4_mx =  (m4_x- (via3.xmax - via3.xmin))/2
        m4_my =  (m4_y- (via3.ymax - via3.ymin))/2
        
        m4 = c.add_ref(gf.components.rectangle(size=(m4_x,m4_y),layer=m4_layer))
        m4.move(( via3.xmin-m4_mx , via3.ymin- m4_my ))

    if metal_level >= 5 : 
        via4_gen = via_generator(x_range= (m4.xmin, m4.xmax), y_range=(m4.ymin,m4.ymax),via_size=via4_size,via_enclosure=via4_enc
        ,via_layer=via4_layer,via_spacing=via4_spacing)
        via4 = c.add_ref(via4_gen)

        m5_enc = (0.31,0.31)
        m5_min_w = 1.6 
        if (via4.xmax-via4.xmin + 2*m5_enc[0]) < m5_min_w:
            m5_x = m5_min_w
            
        else :
            m5_x = via4.xmax-via4.xmin + 2*m5_enc[0]
            

        if (via4.ymax-via4.ymin + 2*m5_enc[1]) < m5_min_w:
            m5_y = m5_min_w
            
            
        else :
            m5_y = via4.ymax-via4.ymin + 2*m5_enc[1]
            

        
        m5_a = 4 
        if (m5_x*m5_y)< m5_a :
            m5_x = m5_a/m5_y
        
        m5_mx = (m5_x - (via4.xmax - via4.xmin))/2
        m5_my =  (m5_y - (via4.ymax - via4.ymin))/2

        m5 = c.add_ref(gf.components.rectangle(size=(m5_x,m5_y),layer=m5_layer))
        m5.move((via4.xmin - m5_mx, via4.ymin - m5_my))

    return c

#@gf.cell
def vias_gen_draw(
    layout,
    l : float = 1.0,
    w : float = 1.0,
    start_layer = "poly",
    end_layer = "metal5"
    

) : #-> gf.Component :
    '''
    draws a vias stack from the start_layer to the end_layer and also draws the start and end layers where :
    l : float of the length that vias will be drawn in 
    w : float of the width that vias will drawn in 
    start_layer : string of the first layer to be drawn that takes input of (poly,p_tap,n_tap,p_diff,n_diff,li,metal1:5)
    end_layer : string of the last layer to be drawn that takes input of (poly,p_tap,n_tap,p_diff,n_diff,li,metal1:5)

    '''
    c = gf.Component("via")

    base_layers = ["poly","n_diff","p_diff","n_tap","p_tap"]
    metal_layers = ["li","metal1","metal2","metal3","metal4","metal5"]


    if start_layer in base_layers : 
        level_1 = -1 
    else :
        for i in range(len(metal_layers)):
            if start_layer == metal_layers[i]:
                level_1 = i
    
    if end_layer in base_layers :
        level_2 = -1
    else :
        for i in range(len(metal_layers)):
            if end_layer == metal_layers[i]:
                level_2 = i
    
    
    if level_1 <= -1 and level_2 >= -1 :
        if start_layer == "poly" or end_layer == "poly":
            npc_enc = 0.05
            poly = c.add_ref(gf.components.rectangle(size=(l,w),layer = poly_layer))
            npc = c.add_ref(gf.components.rectangle(size=(l+2*npc_enc,w+2*npc_enc),layer=npc_layer)).move((-npc_enc, -npc_enc))
        if "diff" in start_layer or "diff" in end_layer:
            n_p_enc = 0.125
            nwell_enc = 0.18
            diff = c.add_ref(gf.components.rectangle(size=(l,w),layer = diff_layer))
            if "n_" in start_layer or "n_" in end_layer :
                nsdm = c.add_ref(gf.components.rectangle(size=(l+2*n_p_enc,w+2*n_p_enc),layer=nsdm_layer)).move((-n_p_enc,-n_p_enc))
            else :
                psdm = c.add_ref(gf.components.rectangle(size=(l+2*n_p_enc,w+2*n_p_enc),layer=psdm_layer)).move((-n_p_enc,-n_p_enc))
                nwell = c.add_ref(gf.components.rectangle(size=(l+2*nwell_enc,w+2*nwell_enc),layer=nwell_layer)).move((-nwell_enc,-nwell_enc))
        if "tap" in start_layer or "tap" in end_layer:
            n_p_enc = 0.125
            nwell_enc = 0.18
            tap = c.add_ref(gf.components.rectangle(size=(l,w),layer = tap_layer))
            if "n_" in start_layer or "n_" in end_layer:
                nsdm = c.add_ref(gf.components.rectangle(size=(l+2*n_p_enc,w+2*n_p_enc),layer=nsdm_layer)).move((-n_p_enc,-n_p_enc))
                nwell = c.add_ref(gf.components.rectangle(size=(l+2*nwell_enc,w+2*nwell_enc),layer=nwell_layer)).move((-nwell_enc,-nwell_enc))
            else :
                psdm = c.add_ref(gf.components.rectangle(size=(l+2*n_p_enc,w+2*n_p_enc),layer=psdm_layer)).move((-n_p_enc,-n_p_enc))

    if level_1 <= 0 and level_2 >= 0:
        li =  c.add_ref(gf.components.rectangle(size=(l,w),layer = li_layer))    

    if level_1 <= 1 and level_2 >= 1:
        m1 =  c.add_ref(gf.components.rectangle(size=(l,w),layer = m1_layer))  

    if level_1 <= 2 and level_2 >= 2:
        m2 =  c.add_ref(gf.components.rectangle(size=(l,w),layer = m2_layer))  

    if level_1 <= 3 and level_2 >= 3:
        m3 =  c.add_ref(gf.components.rectangle(size=(l,w),layer = m3_layer))  

    if level_1 <= 4 and level_2 >= 4:
        m4 =  c.add_ref(gf.components.rectangle(size=(l,w),layer = m4_layer))  

    if level_1 <= 5 and level_2 >= 5:
        m5 =  c.add_ref(gf.components.rectangle(size=(l,w),layer = m5_layer))    

    if level_1 <= -1 and level_2 > -1 :

        
        licon_size = (0.17,0.17)
        
        licon_spacing = (0.17,0.17)
        
        if start_layer == "poly":
            licon_enc = (0.08,0.05)
        elif "diff" in start_layer :
            licon_enc = (0.12,0.06) #(0.06,0.04)
        elif "tap" in start_layer :
            licon_enc = (0.12,0.06)

            
        
        licon = via_generator(x_range=(0,l),y_range=(0,w),via_size=licon_size,via_layer=licon_layer,via_enclosure=licon_enc,via_spacing=licon_spacing)
        c.add_ref(licon)
 
    if level_1 <= 0 and level_2 > 0 :
        mcon_size = (0.17,0.17)
        mcon_enc = (0.06,0.03)
        mcon_spacing = (0.19,0.19)
            

        mcon = via_generator(x_range=(0,l),y_range=(0,w),via_size=mcon_size,via_layer=mcon_layer,via_enclosure=mcon_enc,via_spacing=mcon_spacing)
        c.add_ref(mcon)

    if level_1 <= 1 and level_2 > 1 :
        via1_size = (0.15,0.15)
        via1_enc = (0.085,0.055)
        via1_spacing = (0.17,0.17)

            

        via1 = via_generator(x_range=(0,l),y_range=(0,w),via_size=via1_size,via_layer=via1_layer,via_enclosure=via1_enc,via_spacing=via1_spacing)
        c.add_ref(via1)

    if level_1 <= 2 and level_2 > 2 :
        via2_size = (0.2,0.2)
        via2_enc = (0.085,0.065)
        via2_spacing = (0.2,0.2)


        via2 = via_generator(x_range=(0,l),y_range=(0,w),via_size=via2_size,via_layer=via2_layer,via_enclosure=via2_enc,via_spacing=via2_spacing)
        c.add_ref(via2)

    if level_1 <= 3 and level_2 > 3 :
        via3_size = (0.2,0.2)
        via3_enc = (0.09,0.065)
        via3_spacing = (0.2,0.2)
            

        via3 = via_generator(x_range=(0,l),y_range=(0,w),via_size=via3_size,via_layer=via3_layer,via_enclosure=via3_enc,via_spacing=via3_spacing)
        c.add_ref(via3)

    if level_1 <= 4 and level_2 > 4 :
        via4_size = (0.8,0.8)
        via4_enc = (0.31,0.31)
        via4_spacing = (0.8,0.8)

        via4 = via_generator(x_range=(0,l),y_range=(0,w),via_size=via4_size,via_layer=via4_layer,via_enclosure=via4_enc,via_spacing=via4_spacing)
        c.add_ref(via4)
    
    # creating layout and cell in klayout 
    c.write_gds("vias_temp.gds")
    layout.read("vias_temp.gds")
    cell_name = "via"
    
    return layout.cell(cell_name)
    #return c

# testing the generated methods 
if __name__ == "__main__":
    c = vias_gen_draw(start_layer="li",end_layer="poly")
    c.show()
    