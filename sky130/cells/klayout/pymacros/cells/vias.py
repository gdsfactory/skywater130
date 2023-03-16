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
# Vias Generator for skywater130
########################################################################################################################

import pya
from .via_generator import * 

licon_size = (0.17,0.17)
        
licon_spacing = (0.17,0.17)

mcon_size = (0.17,0.17)
mcon_enc = (0.06,0.03)
mcon_spacing = (0.19,0.19)

via1_size = (0.15,0.15)
via1_enc = (0.085,0.055)
via1_spacing = (0.17,0.17)

via2_size = (0.2,0.2)
via2_enc = (0.085,0.065)
via2_spacing = (0.2,0.2)

via3_size = (0.2,0.2)
via3_enc = (0.09,0.065)
via3_spacing = (0.2,0.2)

via4_size = (0.8,0.8)
via4_enc = (0.31,0.31)
via4_spacing = (0.8,0.8)


class vias_gen(pya.PCellDeclarationHelper):
    """
    Vias Generator for Skywater130
    """
    def __init__(self):
        # Initialize super class.
        super(vias_gen, self).__init__()

        #===================== PARAMETERS DECLARATIONS =====================

        self.param("l", self.TypeDouble, "length", default=1, unit="um")
        self.param("w", self.TypeDouble, "width", default=1, unit="um")
        
        self.Type_handle  = self.param("start_layer", self.TypeList, "Start Layer")
        self.Type_handle.add_choice("poly","poly")
        self.Type_handle.add_choice("p_tap","p_tap")
        self.Type_handle.add_choice("n_tap","n_tap")
        self.Type_handle.add_choice("p_diff","p_diff")
        self.Type_handle.add_choice("n_diff","n_diff")
        self.Type_handle.add_choice("li","li")
        self.Type_handle.add_choice("metal1","metal1")
        self.Type_handle.add_choice("metal2","metal2")
        self.Type_handle.add_choice("metal3","metal3")
        self.Type_handle.add_choice("metal4","metal4")
        
        self.Type_handle  = self.param("end_layer", self.TypeList, "End Layer")
        self.Type_handle.add_choice("li","li")
        self.Type_handle.add_choice("metal1","metal1")
        self.Type_handle.add_choice("metal2","metal2")
        self.Type_handle.add_choice("metal3","metal3")
        self.Type_handle.add_choice("metal4","metal4")
        self.Type_handle.add_choice("metal5","metal5")
        
        

    def display_text_impl(self):
        # Provide a descriptive text for the cell
        return "via (L=" + ('%.3f' % self.l) + ",W=" + ('%.3f' % self.w) + ")"
    
    def coerce_parameters_impl(self):
        # We employ coerce_parameters_impl to decide whether the handle or the
        # numeric parameter has changed (by comparing against the effective
        # radius ru) and set ru to the effective radius. We also update the
        # numerical value or the shape, depending on which on has not changed.
        
        base_layers = ["poly","n_diff","p_diff","n_tap","p_tap"]
        metal_layers = ["li","metal1","metal2","metal3","metal4","metal5"]

        if self.start_layer in base_layers : 
            level_1 = -1 
        else :
            for i in range(len(metal_layers)):
                if self.start_layer == metal_layers[i]:
                    level_1 = i
    
        if self.end_layer in base_layers :
            level_2 = -1
        else :
            for i in range(len(metal_layers)):
                if self.end_layer == metal_layers[i]:
                    level_2 = i
        
        #if level_1 < level_2 :
        #    temp_layer = self.start_layer
        #    self.start_layer = self.end_layer
        #    self.end_layer = temp_layer
        
        if level_1 <= -1 and level_2 > -1 :

            if self.start_layer == "poly":
                licon_enc = (0.08,0.05)
            elif "diff" in self.start_layer :
                licon_enc = (0.12,0.06) #(0.06,0.04)
            elif "tap" in self.start_layer :
                licon_enc = (0.12,0.06)
            else : 
                licon_enc = (0.12,0.12)
            
            if self.l < (licon_size[0]+2*licon_enc[0]):
                self.l = licon_size[0]+2*licon_enc[0]
            
        
            if self.w < (licon_size[1]+2*licon_enc[1]):
                self.w = licon_size[1]+2*licon_enc[1]
        
        if level_1 <= 0 and level_2 > 0 :

            if self.l < (mcon_size[0]+2*mcon_enc[0]):
                self.l = mcon_size[0]+2*mcon_enc[0]
            
        
            if self.w < (mcon_size[1]+2*mcon_enc[1]):
                self.w = mcon_size[1]+2*mcon_enc[1]
        
        if level_1 <= 1 and level_2 > 1 :

            if self.l < (via1_size[0]+2*via1_enc[0]):
                self.l = via1_size[0]+2*via1_enc[0]
            
        
            if self.w < (via1_size[1]+2*via1_enc[1]):
                self.w = via1_size[1]+2*via1_enc[1]

        if level_1 <= 2 and level_2 > 2 :      

            if self.l < (via2_size[0]+2*via2_enc[0]):
                self.l = via2_size[0]+2*via2_enc[0]
            
        
            if self.w < (via2_size[1]+2*via2_enc[1]):
                self.w = via2_size[1]+2*via2_enc[1]

        if level_1 <= 3 and level_2 > 3 :

            if self.l < (via3_size[0]+2*via3_enc[0]):
                self.l = (via3_size[0]+2*via3_enc[0])
            
        
            if self.w < (via3_size[1]+2*via3_enc[1]):
                self.w = via3_size[1]+2*via3_enc[1]
        
        if level_1 <= 4 and level_2 > 4 :

            if self.l < (via4_size[0]+2*via4_enc[0]):
                self.l = via4_size[0]+2*via4_enc[0]
            
        
            if self.w < (via4_size[1]+2*via4_enc[1]):
                self.w = via4_size[1]+2*via4_enc[1]
            
              



    def can_create_from_shape_impl(self):
        # Implement the "Create PCell from shape" protocol: we can use any shape which
        # has a finite bounding box
        return self.shape.is_box() or self.shape.is_polygon() or self.shape.is_path()

    def parameters_from_shape_impl(self):
        # Implement the "Create PCell from shape" protocol: we set r and l from the shape's
        # bounding box width and layer
        self.r = self.shape.bbox().width() * self.layout.dbu / 2
        self.l = self.layout.get_info(self.layer)
    
    def transformation_from_shape_impl(self):
        # Implement the "Create PCell from shape" protocol: we use the center of the shape's
        # bounding box to determine the transformation
        return pya.Trans(self.shape.bbox().center())

    def produce_impl(self):
        instance = vias_gen_draw(layout= self.layout , l=self.l, w=self.w, start_layer=self.start_layer, end_layer=self.end_layer)
        write_cells = pya.CellInstArray(instance.cell_index(), pya.Trans(pya.Point(0, 0)),
                      pya.Vector(0, 0), pya.Vector(0, 0), 1, 1)
        self.cell.insert(write_cells)
        self.cell.flatten(1)

        

        
        