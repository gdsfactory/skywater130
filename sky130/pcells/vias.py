
import gdsfactory as gf
from gdsfactory.typings import LayerSpec
from sky130.pcells.via_generator import via_generator

@gf.cell
def via_m1_m2(
    width: float = 0.5,
    length: float = 0.5,
) -> gf.Component:
    """Return a via transition between Metal1 and Metal2.
    
    Acts as a 'bend' component for routing, with one port on Metal1 and one on Metal2.
    """
    c = gf.Component()
    
    # Metal 1 and Metal 2 layers (Sky130)
    layer_m1 = (68, 20)
    layer_m2 = (69, 20)
    layer_via1 = (68, 44)
    
    # Via parameters for m1-m2 transition (via1)
    via_size = (0.15, 0.15)
    via_spacing = (0.17, 0.17)
    via_enclosure = (0.07, 0.07)
    
    # Generate the via array
    # Note: via_generator creates the via layer and the top/bottom metal enclosures?
    # Let's check via_generator impl: it seems to only draw the via layer rectangles.
    # We need to manually add the metal landing pads if via_generator doesn't.
    # Checking via_generator source again... 
    # It draws "rect_via = gf.components.rectangle(size=via_size, layer=via_layer)"
    # It does NOT draw the metal enclosures. We must add them.
    
    # Add Metal 1 landing pad
    m1_rect = c.add_ref(gf.components.rectangle(size=(width+via_enclosure[0], length+via_enclosure[1]), layer=layer_m1))
    m1_rect.dcenter = (0, 0)
    
    # Add Metal 2 landing pad
    m2_rect = c.add_ref(gf.components.rectangle(size=(width+via_enclosure[0], length+via_enclosure[1]), layer=layer_m2))
    m2_rect.dcenter = (0, 0)
    
    # Add Via 1 array
    # We want the vias centered.
    # Recalculate best fit for vias inside width/length
    v = via_generator(
        width=width,
        length=length,
        via_size=via_size,
        via_spacing=via_spacing,
        via_layer=layer_via1,
        via_enclosure=via_enclosure
    )
    via_ref = c.add_ref(v)
    # via_generator output is centered at (width/2, length/2) relative to its origin?
    # Actually via_generator demo moves it. Let's Center it.
    via_ref.dcenter = (0, 0)
    
    # Add Ports
    # Port 1: Metal 1 (Horizontal - West/East)
    # Move to Left edge (-width/2)
    c.add_port(
        name="e1",
        center=(-width/2, 0),
        width=width,
        orientation=180,
        layer=layer_m1,
        port_type="electrical"
    )
    
    # Port 2: Metal 2 (Vertical - North/South)
    # Move to Top edge (+width/2)
    c.add_port(
        name="e2",
        center=(0, width/2),
        width=width,
        orientation=90,
        layer=layer_m2,
        port_type="electrical"
    )
    
    return c
