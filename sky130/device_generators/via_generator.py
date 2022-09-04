from math import ceil
import gdsfactory as gf
import numpy as np
from gdsfactory.types import Float2 , LayerSpec

@gf.cell
def via_generator(
    x_range : Float2 = [0,1] ,
    y_range : Float2 = [0,1] ,
    via_size : Float2 = (0.17,0.17),
    via_layer : LayerSpec = (66,44),
    via_enclosure : Float2 = (0.06,0.06),
    via_spacing : Float2 = (0.17,0.17)

) -> gf.Component():
    
    """
    return vias withen the area of width x length 
    and set number of rows and number of coloumns as a global variable to be used outside the function 

    """
    c = gf.Component()

    width = x_range[1] - x_range[0]
    length = y_range[1] - y_range[0]
    nr = ceil(length / (via_size[1] + via_spacing[1]))
    if (length - nr*via_size[1] - (nr-1)*via_spacing[1])/2 < via_enclosure[1]:
        nr -= 1

    if nr <1 :
        nr = 1
    
    nc = ceil(width / (via_size[0]+via_spacing[0]))
    if (width - nc*via_size[0] - (nc-1)*via_spacing[0])/2 < via_enclosure[0]:
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


if __name__ == "__main__":
    
    width =1.5
    length = 1.5
    via_size = (0.15,0.15) # via4:(0.8,0.8),via3,via2 : (0.2,0.2) ,via1 : (0.15,0.15),licon: (0.17,0.17) 
    via_spacing =(0.17,0.17) # via4:(0.8,0.8) via2 :(0.2,0.2), via1,licon :(0.17,0.17)
    via_layer =(68,44) # via4:(71,44),via3 :(70,44)via2 : (69,44) ,via1 : (68,44),licon: (66,44)
    via_enclosure =(0.055,0.055) # via4: (0.19,0.19)via2 : (0.04,0.04) via1 : (0.055,0.055),via3,licon: (0.06,0.06)
    bottom_layer : LayerSpec =(68,20)# m4 :(71,20),m3:(70:20) , m2 :(69,20),  m1 :(68,20),tap: (65,44) 

    rect = gf.components.rectangle(size= (width,length), layer= bottom_layer) 
    
    c1 = gf.Component("via test for rectangle")
    c1.add_label(f"test for via1 over met1 withen {width} x {length} area" , position= (width/2, length + via_enclosure[1]))
    c1.add_ref(rect)
  
    #c = via_generator(width= width , length= length , via_size= via_size , via_spacing= via_spacing , via_layer= via_layer)
    c = via_generator(x_range= (c1.xmin, c1.xmax) , y_range=(c1.ymin,c1.ymax))
    v = c1.add_ref(c)

    c2 = gf.Component("via test for bending structure")
    rect_out = gf.components.rectangle(size= (2*width, 2*length))
    d = gf.Component()
    x1 = d.add_ref(rect)
    x2 = d.add_ref(rect_out)
    x1.move((0.5*width,0.5*length))
    c2.add_ref(gf.geometry.boolean(A= x2, B= x1,operation="A-B", layer= bottom_layer))
    #c2.add_label(f"test for via4 over met4 withe a bending area" , position= (width, 4*length + via_enclosure[1]))
    v1 = via_generator (x_range=(x2.xmin , x1.xmin), y_range=(x1.ymin, x1.ymax))
    c2.add_array(v1, rows=1 , columns=2 , spacing=[x2.xmax-x1.xmin,0])
    v2 = via_generator (x_range=(x1.xmin , x1.xmax), y_range=(x2.ymin, x1.ymin))
    c2.add_array(v2, rows=2 , columns= 1 , spacing= [0,x2.ymax - x1.ymin])
    v3 = via_generator (x_range=(x2.xmin , x1.xmin), y_range=(x2.ymin, x1.ymin))
    c2.add_array(v3, rows=2 , columns=2 , spacing= [x2.xmax-x1.xmin,x2.ymax - x1.ymin])


 

  
c1.show() 
#c2.show()



