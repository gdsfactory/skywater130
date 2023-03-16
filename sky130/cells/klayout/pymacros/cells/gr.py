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
# Guard Ring Generator for skywater130
########################################################################################################################

import pya
from .draw_guard_ring import *

min_s = 0.27
min_w = 0.17
min_w_m1 = 0.23
min_s_m1 = 0.38

class guard_ring_gen(pya.PCellDeclarationHelper):
    """
    Guard Ring Generator for Skywater130
    """

    def __init__(self):
        # Initialize super class.
        super(guard_ring_gen, self).__init__()

        #===================== PARAMETERS DECLARATIONS =====================

        self.param("in_w", self.TypeDouble, "Inner Width", default=min_s, unit="um")
        self.param("in_l", self.TypeDouble, "Inner Length", default=min_s, unit="um")
        self.param("grw", self.TypeDouble, "Guard Ring Width", default=min_w, unit="um")

        
        self.Type_handle  = self.param("con_lev", self.TypeList, "Connection Level")
        self.Type_handle.add_choice("None", "None")
        self.Type_handle.add_choice("li", "li")
        self.Type_handle.add_choice("metal1", "metal1")

    def display_text_impl(self):
        # Provide a descriptive text for the cell
        return f"Guard Ring(Ring Width = {self.grw})"
    
    def coerce_parameters_impl(self):
        # We employ coerce_parameters_impl to decide whether the handle or the
        # numeric parameter has changed (by comparing against the effective
        # radius ru) and set ru to the effective radius. We also update the
        # numerical value or the shape, depending on which on has not changed.        
        # w,l must be larger or equal than min. values.
        

        if self.con_lev == "metal1":
            if self.grw < min_w_m1 :
                self.grw = min_w_m1

            if self.in_l < min_s_m1 :
                self.in_l = min_s_m1
        
            if self.in_w < min_s_m1 :
                self.in_w  = min_s_m1
        else : 
            if self.grw < min_w :
                self.grw = min_w

            if self.in_l < min_s :
                self.in_l = min_s
        
            if self.in_w < min_s :
                self.in_w  = min_s
    
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
        instance = draw_gr(layout=self.layout, in_l=self.in_l, in_w=self.in_w , grw= self.grw , con_lev=self.con_lev)
        write_cells = pya.CellInstArray(instance.cell_index(), pya.Trans(pya.Point(0, 0)),
                      pya.Vector(0, 0), pya.Vector(0, 0), 1, 1)
        self.cell.insert(write_cells)
        self.cell.flatten(1)
            