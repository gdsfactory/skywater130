from math import ceil, floor
import gdsfactory as gf
import numpy as np
from gdsfactory.types import Float2, LayerSpec

@gf.cell
def nmos(
    diffusion_layer: LayerSpec = (65, 20),
    poly_layer: LayerSpec = (66, 22),
    gate_width: float = 0.42,
    gate_length: float = 0.15,
    sd_width: float = 0.3,
    end_cap: float = 0.13,
    contact_size: Float2 = (0.17, 0.17),
    contact_spacing: Float2 = (0.17, 0.17),
    contact_layer: LayerSpec = (66, 44),
    contact_enclosure: float = (0.04,0.06)
) -> gf.Component:

    """Return NMOS.

    Args:
        diffusion_layer: spec.
        poly_layer: spec.
        gate_width: for poly.
        gate_length: for poly.
        sd_width: source drain length.
        end_cap : end cap length.
        

    .. code::
                    _______
                    | poly |
           _________|      |_________  _
          | sd_width|      | sd_width| |
          |<------->|      |<------->| |gate_width
          |_________|      |_________| |
                    |  Lg  |
                    |<---->|
                    |______|

    """
    c = gf.Component()

    
    w_p = end_cap + gate_width + end_cap  # poly total width
    rect_p = gf.components.rectangle(size = (gate_length,w_p), layer= poly_layer)
    poly = c.add_ref(rect_p)


    l_d = sd_width + gate_length + sd_width  # n diffution total length 
    rect_d = gf.components.rectangle(size = (l_d,gate_width), layer= diffusion_layer)  
    diff_n= c.add_ref(rect_d)

    poly.movex(sd_width)
    poly.movey(-end_cap)


    rect_c = gf.components.rectangle(size = contact_size, layer = contact_layer) 
    
   
    nr =  floor (gate_width / (2* contact_size[1])) 
    nc = floor (sd_width / (2* contact_size[0])) 
    
    con_sp = list(contact_spacing)
    con_sp[0] = con_sp[1] = contact_spacing[0] + contact_size[0]

    cont_arr1 = c.add_array(rect_c, rows= nr , columns= nc , spacing= con_sp)
    cont_arr2 = c.add_array(rect_c, rows= nr , columns= nc , spacing= con_sp)

    cont_arr1.move(contact_enclosure)
    cont_arr2.movex(l_d- cont_arr2.xmax + cont_arr2.xmin- contact_size[0] - contact_enclosure[0])
    cont_arr2.movey(contact_enclosure[1])
    


    if (gate_length <= contact_size[0]) :
        pc_x = contact_enclosure[0] +contact_size[0] + contact_enclosure[1]
        cont_p = c.add_ref(rect_c)
        cont_p.connect("e2", destination= poly.ports["e2"])
        cont_p.movey(contact_enclosure[1])
    else :
        pc_x = gate_length 
        nc_p = floor (pc_x / (2* contact_size[0])) +1 
        cont_arr3 = c.add_array(rect_c, rows= 1 , columns= nc_p , spacing= con_sp)
        cont_arr3.movex(sd_width + contact_enclosure[0] )
        cont_arr3.movey(gate_width + end_cap + contact_enclosure[1] )


    pc_size = (pc_x, contact_enclosure[1] +contact_size[1]+contact_enclosure[1])  # poly size to contain contact
    rect_pc = gf.components.rectangle(size = pc_size, layer = poly_layer) 
    pc = c.add_ref(rect_pc)
    pc.connect("e2", destination= poly.ports["e2"])

    return c


if __name__ == "__main__":
    #c = nmos(gate_length= 2, gate_width=10) # , sd_width= 5)
    c = nmos()
    c.show()
