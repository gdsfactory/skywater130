from math import ceil, floor
import gdsfactory as gf
import numpy as np
from gdsfactory.types import Float2, LayerSpec

@gf.cell
def mimcap_1(
    m3_layer : LayerSpec = (70,20),
    via3_size : float = (0.2,0.2),
    via3_layer : LayerSpec = (70,44),
    via3_enclosure : Float2 = (0.09,0.09),
    via3_spacing : Float2 = (0.2,0.35),
    m4_spacing : float = 0.3,
    m4_length : float = 0.3,
    m4_layer : LayerSpec = (71,20),
    capm_length : float = 1,
    capm_width : float = 1,
    capm_layer : LayerSpec = (89,44),
    capm_enclosure : float = 0.14




) -> gf.Component:

    """Return mimcap_1

    mim cap between metal 3 and 4 

   
    """
    c = gf.Component()

    en = (0.02,0.05)  # for enclosure 
    #generating m3 plate 
    m3_length = capm_enclosure +  capm_length + m4_spacing - capm_enclosure + m4_length + en[0]
    m3_width = 2*capm_enclosure + capm_width + en[1]
    rect_m3 = gf.components.rectangle(size= (m3_length,m3_width) , layer= m3_layer)
    m3 = c.add_ref(rect_m3)

    # generate m4 plates 

    rect_m4_1 = gf.components.rectangle(size= (m4_length,m3_width- en[1] ), layer= m4_layer) 
    m4_1 = c.add_ref(rect_m4_1) 
    m4_1.movex (m3_length - m4_length - en[0]/2)
    m4_1.movey (en[1]/2)

    rect_m4_2 = gf.components.rectangle(size= (capm_length - 2*capm_enclosure ,capm_width - 2*capm_enclosure ), layer= m4_layer) 
    m4_1 = c.add_ref(rect_m4_2)
    m4_1.connect("e3", destination= m3.ports["e3"]) 
    m4_1.movex(- capm_length + 2*capm_enclosure - en[0]/2 - m4_length - m4_spacing)

    # generate capm 
    rect_capm = gf.components.rectangle(size= (capm_length,capm_width) , layer= capm_layer)
    capm = c.add_ref(rect_capm)
    capm.connect("e3", destination= m4_1.ports["e3"])
    capm.movex(capm_length - capm_enclosure)    


    # generat3 via3 
    #rect_via3 = gf.components.rectangle(size= via3_size, layer= via3_layer)
    #via3_arr1 = c.add_ref(rect_via3)

    

    return c

if __name__ == "__main__":
    
    c = mimcap_1()
    #c = mimcap_1 (capm_length= 5 , capm_width= 3, m4_length=1)
    c.show()
