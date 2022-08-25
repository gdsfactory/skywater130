from math import ceil, floor
import gdsfactory as gf
import numpy as np
from gdsfactory.types import Float2, LayerSpec

@gf.cell
def pmos_5v(
    diffusion_layer: LayerSpec = (65, 20),
    poly_layer: LayerSpec = (66, 20),
    gate_width: float = 0.75,
    gate_length: float = 0.5,
    sd_width: float = 0.3,
    end_cap: float = 0.13,
    contact_size: Float2 = (0.17, 0.17),
    contact_spacing: Float2 = (0.17, 0.17),
    contact_layer: LayerSpec = (66, 44),
    contact_enclosure: float = (0.04,0.06),
    diff_spacing : float = 0.37 ,
    diff_enclosure : Float2 = (0.33,0.33) ,
    diffn_layer : LayerSpec = (65,44) ,
    nwell_layer : LayerSpec = (64,22),
    dnwell_enclosure: float = (0.4,0.4),
    dnwell_layer : LayerSpec = (64,18) ,
    nf : int =  1 ,
    sdm_enclosure : Float2 = (0.125,0.125) ,
    nsdm_layer : LayerSpec = (93,44),
    psdm_layer : LayerSpec = (94,20),
    sdm_spacing : float = 0.13,
    hvi_layer : LayerSpec= (75,20),
    li_width : float = 0.17 ,
    li_spacing : float = 0.17 ,
    li_layer : LayerSpec = (67,20),
    li_enclosure : float = 0.08

) -> gf.Component:
    """Return NMOS.

    Args:
        diffusion_layer: spec.
        poly_layer: spec.
        gate_width: for poly.
        gate_length: for poly.
        sd_width: source drain length.
        end_cap : end cap length.
        contact_size : contact dimension (length and width)
        contact_layer : for contacts 
        contact_enclosure : for contacts within diffusion or poly 
        diff_spacing : for two adjacent diffusions
        diff_enclosure : for diffusion within well 
        diffp_layer : for bulk tie 
        dnwell layer : for deep nwell 
        nf : for finger option 
    """

    c = gf.Component() 

    # generating poly and p+ diffusion 
    w_p = end_cap + gate_width + end_cap  # poly total width
    rect_p = gf.components.rectangle(size = (gate_length,w_p), layer= poly_layer)

    # adding fingers 
    #poly = c.add_ref(rect_p)
    poly = c.add_array(rect_p, rows= 1 , columns= nf , spacing= [sd_width+gate_length, 0 ])


    l_d = (nf + 1)*(sd_width + gate_length ) - gate_length # n diffution total length 
    rect_d = gf.components.rectangle(size = (l_d,gate_width), layer= diffusion_layer)  
    diff_p= c.add_ref(rect_d)

    poly.movex(sd_width)
    poly.movey(-end_cap)

     # generating p+ implant 
    rect_pm = gf.components.rectangle(size = (l_d+ 2*sdm_enclosure[0] ,gate_width+ 2*sdm_enclosure[1]), layer= psdm_layer) 
    psdm = c.add_ref(rect_pm)
    psdm.movex(-sdm_enclosure[0])
    psdm.movey(-sdm_enclosure[1])

     # generating contacts and interconnects of p+ diffusion 
    rect_c = gf.components.rectangle(size = contact_size, layer = contact_layer) 
    
   
    nr =  floor (gate_width / (2* contact_size[1])) 
    nc = floor (sd_width / (2* contact_size[0])) 
    
    con_sp = list(contact_spacing)
    con_sp[0] = con_sp[1] = contact_spacing[0] + contact_size[0]

    min_gate_len , min_gate_wid , sd_width_min = 0.15 , 0.42 , 0.3

    cont_arr1 = c.add_array(rect_c, rows= nr , columns= nc , spacing= con_sp)
    cont_arr2 = c.add_array(rect_c, rows= nr , columns= nc , spacing= con_sp)

    cont_arr1.movey((min_gate_wid - contact_size[1])/2)
    cont_arr2.movey((min_gate_wid - contact_size[1])/2)

    rect_lid = gf.components.rectangle(size= (li_width , gate_width+ li_enclosure), layer= li_layer)
    li1 = c.add_array(rect_lid, rows= 1 , columns= nc , spacing= con_sp)
    li2 = c.add_array(rect_lid, rows= 1 , columns= nc , spacing= con_sp)

    if nc > 1 : 
        cont_arr1.movex ((sd_width  - (cont_arr1.xmax - cont_arr1.xmin))/2)
        cont_arr2.movex((nf*(sd_width+ gate_length) )+  ((sd_width  - (cont_arr2.xmax - cont_arr2.xmin))/2)) 
        li1.movex ((sd_width  - (cont_arr1.xmax - cont_arr1.xmin))/2)
        li2.movex((nf*(sd_width+ gate_length) )+  ((sd_width  - (cont_arr2.xmax - cont_arr2.xmin))/2)) 
    else : 
        cont_arr1.movex ((sd_width  - contact_size[0])/2)
        cont_arr2.movex((nf*(sd_width+ gate_length) )+  ((sd_width  - contact_size[0])/2) )
        li1.movex ((sd_width  - contact_size[0])/2)
        li2.movex((nf*(sd_width+ gate_length) )+  ((sd_width  - contact_size[0])/2) )

    li1.movey(-li_enclosure/2)
    li2.movey(-li_enclosure/2)


    # generating contacts and local interconnects of poly
    
    nc_p = floor (gate_length / (2* contact_size[0])) 
    for i in range(nf):
        cont_arr3 = c.add_array(rect_c, rows= 1 , columns= nc_p , spacing= con_sp)
        cont_arr3.movex(sd_width +  ((gate_length - (cont_arr3.xmax - cont_arr3.xmin))/2)+ (i* (gate_length + sd_width)) )
        cont_arr3.movey(gate_width + end_cap + contact_enclosure[1] )
        cont_arr5 = c.add_array(rect_c, rows= 1 , columns= nc_p , spacing= con_sp)
        cont_arr5.movex(sd_width +  ((gate_length - (cont_arr5.xmax - cont_arr5.xmin))/2)+ (i* (gate_length + sd_width))  )
        cont_arr5.movey(-contact_size[1] - end_cap - contact_enclosure[1] )


    pc_size = (gate_length, contact_enclosure[1] +contact_size[1]+contact_enclosure[1])  # poly size to contain contact
    rect_pc = gf.components.rectangle(size = pc_size, layer = poly_layer) 
    pc_u = c.add_array(rect_pc, rows= 1 , columns= nf , spacing= [sd_width + gate_length, 0] )
    pc_u.movex(sd_width- ((gate_length - gate_length)/2))
    pc_u.movey(gate_width + end_cap)

    pc_d = c.add_array(rect_pc, rows= 1 , columns= nf , spacing= [sd_width + gate_length, 0] )
    pc_d.movex(sd_width)
    pc_d.movey(-pc_size[1]- end_cap)

    rect_lip = gf.components.rectangle(size = (pc_size[0]+ li_enclosure, li_width), layer = li_layer) 
    lip_u = c.add_array(rect_lip, rows= 1 , columns= nf , spacing= [sd_width + gate_length, 0] )
    lip_u.movex(sd_width - li_enclosure/2)
    lip_u.movey(gate_width + end_cap + contact_enclosure[1] )

    lip_d = c.add_array(rect_lip, rows= 1 , columns= nf , spacing= [sd_width + gate_length, 0] )
    lip_d.movex(sd_width - li_enclosure/2)
    lip_d.movey(-contact_size[1] - end_cap - contact_enclosure[1] )


    # generaing n+ bulk tie and its contact 
    rect_dn = gf.components.rectangle(size = (sd_width,gate_width), layer= diffn_layer) 
    diff_n = c.add_ref(rect_dn)
    diff_n.connect("e1",destination= diff_p.ports["e3"])
    diff_n.movex(diff_spacing + sdm_spacing)

    cont_arr4 = c.add_array(rect_c, rows= nr , columns= nc , spacing= con_sp)
    cont_arr4.movey((min_gate_wid - contact_size[1])/2 ) 

    # generate its local interconnects 
    li4 = c.add_array(rect_lid, rows= 1 , columns= nc , spacing= con_sp)

    if nc > 1 : 
        cont_arr4.movex(l_d + diff_spacing + sdm_spacing +  ((sd_width  - (cont_arr4.xmax - cont_arr4.xmin))/2)) 
        li4.movex(l_d + diff_spacing + sdm_spacing +  ((sd_width  - (cont_arr4.xmax - cont_arr4.xmin))/2)) 
    else :
        cont_arr4.movex(l_d + diff_spacing + sdm_spacing + ((sd_width  - contact_size[0])/2)) 
        li4.movex(l_d + diff_spacing + sdm_spacing + ((sd_width  - contact_size[0])/2)) 
    
    li4.movey(-li_enclosure/2)

    # generating n+ implant for bulk tie 
    rect_nm = gf.components.rectangle(size = (sd_width+ 2*sdm_enclosure[0],gate_width+ 2*sdm_enclosure[1]), layer= nsdm_layer)
    nsdm = c.add_ref(rect_nm)
    nsdm.connect("e1",destination= diff_p.ports["e3"])
    nsdm.movex(diff_spacing + sdm_spacing - sdm_enclosure[0])

    # generating nwell 
    rect_nw = gf.components.rectangle(size = (2*diff_enclosure[0] + l_d + diff_spacing + sdm_spacing + sd_width , 2*diff_enclosure[1] + gate_width), layer= nwell_layer) 
    nwell = c.add_ref(rect_nw) 
    nwell.movex(-diff_enclosure[0])
    nwell.movey(-diff_enclosure[1])
    
    # generating deep nwell 
    rect_dnw =  gf.components.rectangle(size = (rect_nw.xmax - rect_nw.xmin + 2*dnwell_enclosure[0] , rect_nw.ymax - rect_nw.ymin + 2*dnwell_enclosure[1]), layer= dnwell_layer) 
    dnwell = c.add_ref(rect_dnw)
    dnwell.movex(-diff_enclosure[0]- dnwell_enclosure[0])
    dnwell.movey(-diff_enclosure[1]- dnwell_enclosure[1])

    # generating hvi 
    rect_hv =  gf.components.rectangle(size = (rect_nw.xmax - rect_nw.xmin + 2*dnwell_enclosure[0] , rect_nw.ymax - rect_nw.ymin + 2*dnwell_enclosure[1]), layer= hvi_layer) 
    dnwell = c.add_ref(rect_hv)
    dnwell.movex(-diff_enclosure[0]- dnwell_enclosure[0])
    dnwell.movey(-diff_enclosure[1]- dnwell_enclosure[1])

    return c

if __name__ == "__main__":
    #c = pmos_5v(gate_length= 2, gate_width=10,nf = 3 )
    c = pmos_5v()
    c.show()