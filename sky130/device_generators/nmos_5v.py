from math import ceil, floor
import gdsfactory as gf
import numpy as np
from gdsfactory.types import Float2, LayerSpec

@gf.cell
def nmos_5v(
    diffusion_layer: LayerSpec = (65, 20),
    poly_layer: LayerSpec = (66, 20),
    gate_width: float = 0.75,
    gate_length: float = 0.5,
    sd_width: float = 0.3,
    end_cap: float = 0.13,
    contact_size: Float2 = (0.17, 0.17),
    contact_spacing: Float2 = (0.17, 0.17),
    contact_layer: LayerSpec = (66, 44),
    contact_enclosure: float = (0.06,0.06),
    diff_spacing : float = 0.37 ,
    diff_enclosure : Float2 = (0.33,0.33) ,
    diffp_layer : LayerSpec = (65,44) ,
    pwell_layer : LayerSpec = (64,13),
    dnwell_enclosure: float = (0.4,0.4),
    dnwell_layer : LayerSpec = (64,18) ,
    nf : int =  1 ,
    sdm_enclosure : Float2 = (0.125,0.125) ,
    nsdm_layer : LayerSpec = (93,44),
    psdm_layer : LayerSpec = (94,20),
    sdm_spacing : float = 0.13,
    hvi_layer : LayerSpec= (75,20),
    hvntm_layer : LayerSpec = (125,20),
    hvntm_enclosure : Float2 = (0.185,0.185),
    li_width : float = 0.17 ,
    li_spacing : float = 0.17 ,
    li_layer : LayerSpec = (67,20),
    li_enclosure : float = 0.08,
    mcon_layer : LayerSpec = (67,44) ,
    mcon_enclosure : Float2 = (0.03,0.06),
    m1_layer : LayerSpec = (68,20),
    npc_layer : LayerSpec = (95,20),
    npc_spacing : float = 0.09

    

) -> gf.Component:
    """Return NMOS_5v.

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

    # generating poly and n+ diffusion 
    w_p = end_cap + gate_width + end_cap  # poly total width
    rect_p = gf.components.rectangle(size = (gate_length,w_p), layer= poly_layer)

    # adding fingers 
    #poly = c.add_ref(rect_p)
    poly = c.add_array(rect_p, rows= 1 , columns= nf , spacing= [sd_width+gate_length, 0 ])


    l_d = (nf + 1)*(sd_width + gate_length ) - gate_length # n diffution total length 
    rect_d = gf.components.rectangle(size = (l_d,gate_width), layer= diffusion_layer)  
    diff_n= c.add_ref(rect_d)

    poly.movex(sd_width)
    poly.movey(-end_cap)
    
     # generating n+ implant 
    rect_nm = gf.components.rectangle(size = (l_d+ 2*sdm_enclosure[0] ,gate_width+ 2*sdm_enclosure[1]), layer= nsdm_layer) 
    nsdm = c.add_ref(rect_nm)
    nsdm.movex(-sdm_enclosure[0])
    nsdm.movey(-sdm_enclosure[1])

     # generating contacts and local interconnects and mcon and m1 of  n+ diffusion 
    rect_c = gf.components.rectangle(size = contact_size, layer = contact_layer) 
    rect_mc = gf.components.rectangle(size = contact_size, layer = mcon_layer) 
    
   
    nr = ceil(gate_width / (contact_size[1]+contact_spacing[1]))
    if (gate_width - nr*contact_size[1] - (nr-1)*contact_spacing[1] )/2 <  contact_enclosure[1] :
        nr -= 1

    nc = ceil(sd_width / (contact_size[0]+contact_spacing[0]))
    if (sd_width - nc*contact_size[0] - (nc-1)*contact_spacing[0])/2 < contact_enclosure[0] :
        nc -= 1

    con_sp = (contact_size[0]+contact_spacing[0], contact_size[1]+contact_spacing[1])
    min_gate_len , min_gate_wid , sd_width_min = 0.15 , 0.42 , 0.3

    rect_con = [rect_c, rect_mc]
    for i in range(2):
        for j in range(2):
            cont_arr1 = c.add_array(rect_con[i], rows= nr , columns= nc , spacing= con_sp)
            cont_arr1.movex((sd_width - nc*contact_size[0] - (nc-1)*contact_spacing[0])/2)
            cont_arr1.movey((gate_width - nr*contact_size[1] - (nr-1)*contact_spacing[1])/2)
            cont_arr1.movex(j*nf*(sd_width + gate_length))
    
    if nr <= 1 :
        nr = 1
        li_w = li_width
    else: 
        li_w = nr*contact_size[1] + (nr-1)*contact_spacing[1] + 2* li_enclosure

    if nc<=1 :
        nc = 1
        li_l = li_width 
        li_en = 0 

    else :
        li_l = nc*contact_size[0] + (nc-1)*contact_spacing[0] + 2*li_enclosure
        li_en = li_enclosure

    rect_layer = [li_layer, m1_layer]

    for i in range(2):
        rect_lid_m1 = gf.components.rectangle(size= (li_l + 2*i*mcon_enclosure[0], gate_width+ (1-i)*li_enclosure ), layer= rect_layer[i])
        lid_m1_arr = c.add_array(rect_lid_m1, rows= 1 , columns= 2 , spacing= (nf*(sd_width + gate_length) , 0))
        lid_m1_arr.movex((sd_width - nc*contact_size[0]-(nc-1)*contact_spacing[0])/2 - li_en -i*mcon_enclosure[0])
        lid_m1_arr.movey(-(1-i)*li_enclosure/2)

    
    # generating contacts and local interconnects and mcon and m1 of poly
    
    pc_x = gate_length 
    nc_p = ceil (pc_x / (contact_size[0] + contact_spacing[0]))

    if (pc_x - nc_p*contact_size[0] - (nc_p-1)*contact_spacing[0])/2 < contact_enclosure[0]:
        nc_p -= 1
    
    for i in range(nf):
        for j in range (2): 
            cont_arr3 = c.add_array(rect_con[j], rows= 2 , columns= nc_p , spacing= [con_sp[0],contact_size[1]+ gate_width + 2*end_cap + 2*contact_enclosure[1]])
            cont_arr3.movex(sd_width +  ((gate_length - nc_p*contact_size[0] - (nc_p-1)*contact_spacing[0])/2)+ (i* (gate_length + sd_width)) )
            cont_arr3.movey(-contact_size[1] - end_cap - contact_enclosure[1] )



    pc_size = (gate_length, contact_enclosure[1] +contact_size[1]+contact_enclosure[1])  # poly size to contain contact
    rect_pc = gf.components.rectangle(size = pc_size, layer = poly_layer) 


    pc = c.add_array(rect_pc, rows= 2 , columns= nf , spacing= [sd_width + gate_length, pc_size[1]+ gate_width + 2*end_cap] )
    pc.movex(sd_width- ((pc_x - gate_length)/2))
    pc.movey(-pc_size[1] - end_cap)

    for i in range(2):
        rect_lip_m1 = gf.components.rectangle(size = (pc_x + (1-i)*li_enclosure - 2*i*(contact_enclosure[0]-mcon_enclosure[0]), li_width + 2*i*mcon_enclosure[1]), layer = rect_layer[i]) 
        lip_m1 = c.add_array(rect_lip_m1, rows= 2 , columns= nf , spacing= [sd_width + gate_length,pc_size[1]+gate_width+ 2*end_cap ] )
        lip_m1.movex(sd_width- ((pc_x - gate_length)/2) - (1-i)*li_enclosure/2 + i*(contact_enclosure[0]-mcon_enclosure[0]))
        lip_m1.movey(-pc_size[1]- end_cap + (1-i)*contact_enclosure[1] )

    # generating npc for poly contacts 

    npc_en = end_cap - npc_spacing 
    rect_npc = gf.components.rectangle(size = (pc_size[0] + npc_en, pc_size[1] + npc_en), layer = npc_layer) 

    npc = c.add_array(rect_npc, rows= 2 , columns= nf , spacing= [sd_width + gate_length,pc_size[1]+npc_en+gate_width + 2*(end_cap - npc_en/2)] )
    npc.movex(sd_width- ((pc_x - gate_length)/2) - npc_en/2)
    npc.movey(-pc_size[1] - npc_en - npc_spacing - npc_en/2)


    # generaing p+ bulk tie and its contact and mcon and m1 
    rect_dp = gf.components.rectangle(size = (sd_width,gate_width), layer= diffp_layer) 
    diff_p = c.add_ref(rect_dp)
    diff_p.connect("e1",destination= diff_n.ports["e3"])
    diff_p.movex(diff_spacing+sdm_spacing)

    for i in range(2):
        cont_arr2 = c.add_array(rect_con[i], rows= nr , columns= nc , spacing= con_sp)
        cont_arr2.movex((nf+1)*sd_width + nf*gate_length + diff_spacing + sdm_spacing)
        cont_arr2.movex((sd_width - nc*contact_size[0] - (nc-1)*contact_spacing[0])/2)
        cont_arr2.movey((gate_width - nr*contact_size[0] - (nr-1)*contact_spacing[0])/2)
    

    # generate its local interconnects 
     # generate its local interconnects and m1 
    for i in range(2):
        rect_li2_m1 = gf.components.rectangle(size= (li_l + 2*i*mcon_enclosure[0], gate_width+(1-i)*li_enclosure ), layer= rect_layer[i])
        li2_m1 = c.add_ref(rect_li2_m1)
        li2_m1.connect("e1",destination= diff_p.ports["e1"])
        li2_m1.movex(li_l + i*mcon_enclosure[0])
        li2_m1.movex((sd_width - nc*contact_size[0]-(nc-1)*contact_spacing[0])/2 - li_en )


    # generating p+ implant for bulk tie 
    rect_pm = gf.components.rectangle(size = (sd_width+ 2*sdm_enclosure[0],gate_width+ 2*sdm_enclosure[1]), layer= psdm_layer)
    psdm = c.add_ref(rect_pm)
    psdm.connect("e1",destination= diff_n.ports["e3"])
    psdm.movex(diff_spacing  + sdm_spacing - sdm_enclosure[0])



    # generating pwell 
    rect_pw = gf.components.rectangle(size = (2*diff_enclosure[0] + l_d + diff_spacing + sdm_spacing + sd_width , 2*diff_enclosure[1] + gate_width), layer= pwell_layer) 
    pwell = c.add_ref(rect_pw) 
    pwell.movex(-diff_enclosure[0])
    pwell.movey(-diff_enclosure[1])

    # generating deep nwell 
    rect_dnw =  gf.components.rectangle(size = (rect_pw.xmax - rect_pw.xmin + 2*dnwell_enclosure[0] , rect_pw.ymax - rect_pw.ymin + 2*dnwell_enclosure[1]), layer= dnwell_layer) 
    dnwell = c.add_ref(rect_dnw)
    dnwell.movex(-diff_enclosure[0]- dnwell_enclosure[0])
    dnwell.movey(-diff_enclosure[1]- dnwell_enclosure[1])

    # generating hvi 
    rect_hv =  gf.components.rectangle(size = (rect_pw.xmax - rect_pw.xmin + 2*dnwell_enclosure[0] , rect_pw.ymax - rect_pw.ymin + 2*dnwell_enclosure[1]), layer= hvi_layer) 
    dnwell = c.add_ref(rect_hv)
    dnwell.movex(-diff_enclosure[0]- dnwell_enclosure[0])
    dnwell.movey(-diff_enclosure[1]- dnwell_enclosure[1])


    # generating hvntm for n+ implants 
    rect_hvn = gf.components.rectangle(size = (l_d+ 2*sdm_enclosure[0] + 2*hvntm_enclosure[0],gate_width+ 2*sdm_enclosure[1]+ 2*hvntm_enclosure[1]), layer= hvntm_layer) 
    hvntm = c.add_ref(rect_hvn)
    hvntm.movex(-sdm_enclosure[0]- hvntm_enclosure[0])
    hvntm.movey(-sdm_enclosure[1]- hvntm_enclosure[1])

    return c

if __name__ == "__main__":
    #c = nmos_5v(gate_length= 2, gate_width=10, nf=3, sd_width=5) 
    c = nmos_5v(nf = 3)
    c.show()

