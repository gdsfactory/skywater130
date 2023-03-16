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
# cap(Varactor-MIM) Generator for skywater130
########################################################################################################################


import pya

from .draw_cap import *
from .globals import *


l_min = 0.18 
w_min = 1
grw_min = 0.17 

l_mim = 2 
l_mim2 = 2.16 

class cap_var(pya.PCellDeclarationHelper):
    """
    Cap(Varactor) Generator for Skywater130
    """

    def __init__(self):
        # Initialize super class.
        super(cap_var, self).__init__()

        #===================== PARAMETERS DECLARATIONS =====================

        self.Type_handle  = self.param("type", self.TypeList, "Device Type")
        self.Type_handle.add_choice("sky130_fd_pr__cap_var_lvt","sky130_fd_pr__cap_var_lvt")
        self.Type_handle.add_choice("sky130_fd_pr__cap_var_hvt","sky130_fd_pr__cap_var_hvt")
        

        self.param("l", self.TypeDouble, "length", default=l_min, unit="um")
        self.param("w", self.TypeDouble, "width", default=w_min, unit="um")
        self.param("tap_con_col", self.TypeInt, "tap Contacts Columns", default=1)

        self.param("gr", self.TypeBoolean, "Gaurd Ring", default=0)
        self.param("grw", self.TypeDouble, "Gaurd Ring Width", default=grw_min, unit="um")

        self.param("nf", self.TypeDouble, "Number of Fingers", default=1)
        #self.param("n", self.TypeDouble, "instance number", default=1)

        self.param("area", self.TypeDouble,"Area", readonly=True, unit="um^2")
        self.param("perim", self.TypeDouble,"Perimeter", readonly=True, unit="um")  
        self.param("cap_value", self.TypeDouble,"Cap Value", readonly=True, unit="fF") 

    
    def display_text_impl(self):
        # Provide a descriptive text for the cell
        return "Varactor(L=" + ('%.3f' % self.l) + ",W=" + ('%.3f' % self.w) + ")"
    
    def coerce_parameters_impl(self):
        # We employ coerce_parameters_impl to decide whether the handle or the
        # numeric parameter has changed (by comparing against the effective
        # radius ru) and set ru to the effective radius. We also update the
        # numerical value or the shape, depending on which on has not changed.
        self.area  = self.w * self.l
        self.perim = 2*(self.w + self.l)
        self.cap_value = 4.4* self.area

        if self.l < l_min : 
            self.l = l_min 
        
        if self.w < w_min:
            self.w = w_min
        
        if self.grw < grw_min:
            self.grw = grw_min
    
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
        instance = draw_cap_var(layout= self.layout , l=self.l, w=self.w, type=self.type,tap_con_col=self.tap_con_col, gr= self.gr , grw= self.grw, nf=self.nf)
        write_cells = pya.CellInstArray(instance.cell_index(), pya.Trans(pya.Point(0, 0)),
                      pya.Vector(0, 0), pya.Vector(0, 0), 1, 1)
        self.cell.insert(write_cells)
        self.cell.flatten(1)


class mim_cap(pya.PCellDeclarationHelper):
    """
    Cap(mim) Generator for Skywater130
    """

    def __init__(self):
        # Initialize super class.
        super(mim_cap, self).__init__()

        #===================== PARAMETERS DECLARATIONS =====================

        self.Type_handle  = self.param("type", self.TypeList, "Device Type")
        self.Type_handle.add_choice("sky130_fd_pr__model__cap_mim","sky130_fd_pr__model__cap_mim")
        self.Type_handle.add_choice("sky130_fd_pr__model__cap_mim_m4","sky130_fd_pr__model__cap_mim_m4")
        

        self.param("l", self.TypeDouble, "length", default=l_mim, unit="um")
        self.param("w", self.TypeDouble, "width", default=l_mim, unit="um")
        
        #self.param("n", self.TypeInt, "instance number", default=1)

        self.param("area", self.TypeDouble,"Area", readonly=True, unit="um^2")
        self.param("perim", self.TypeDouble,"Perimeter", readonly=True, unit="um")  
        self.param("cap_value", self.TypeDouble,"Cap Value", readonly=True, unit="fF")  

    def display_text_impl(self):
        # Provide a descriptive text for the cell
        return "mimcap(L=" + ('%.3f' % self.l) + ",W=" + ('%.3f' % self.w) + ")"

    def coerce_parameters_impl(self):
        # We employ coerce_parameters_impl to decide whether the handle or the
        # numeric parameter has changed (by comparing against the effective
        # radius ru) and set ru to the effective radius. We also update the
        # numerical value or the shape, depending on which on has not changed.
        self.area  = self.w * self.l
        self.perim = 2*(self.w + self.l)
        self.cap_value = 2*self.area 

        if self.type == "sky130_fd_pr__model__cap_mim_m4":
            if self.l < l_mim2 : 
                self.l = l_mim2 
            
            if self.w < l_mim2:
                self.w = l_mim2
        else : 
            if self.l < l_mim : 
                self.l = l_mim 
            
            if self.w < l_mim:
                self.w = l_mim
        
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
        instance = draw_mim_cap(layout= self.layout , l=self.l, w=self.w, type=self.type)
        write_cells = pya.CellInstArray(instance.cell_index(), pya.Trans(pya.Point(0, 0)),
                      pya.Vector(0, 0), pya.Vector(0, 0), 1, 1)
        self.cell.insert(write_cells)
        self.cell.flatten(1)
