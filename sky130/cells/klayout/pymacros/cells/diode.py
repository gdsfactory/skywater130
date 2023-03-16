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
# DIODE Generator for skywater130
########################################################################################################################


import pya

from .draw_diode import *
from .globals import *


class photo_diode(pya.PCellDeclarationHelper):
    """
    photo diode Generator for Skywater130
    """

    def __init__(self):

        # Important: initialize the super class
        super(photo_diode, self).__init__()
        self.Type_handle = self.param("Type", self.TypeList, "Type")
        
        for i in PHOTO_D_DEV :
            self.Type_handle.add_choice(i, i)
        
        
        self.param("Model", self.TypeString, "Model", default="sky130_fd_pr__photodiode",readonly=True)

    def display_text_impl(self):
        # Provide a descriptive text for the cell
        return str(self.Type)
    
    def produce_impl(self):

        # This is the main part of the implementation: create the layout

        self.percision = 1/self.layout.dbu
        ph_d_instance = draw_photodiode(layout=self.layout,device_name=self.Type)

        write_cells = pya.CellInstArray(ph_d_instance.cell_index(), pya.Trans(pya.Point(0, 0)),
                              pya.Vector(0, 0), pya.Vector(0, 0),1 , 1)
        self.cell.flatten(1)
        self.cell.insert(write_cells)
        
        self.layout.cleanup()

d_min = 0.45
grw_min = 0.17

class n_diode(pya.PCellDeclarationHelper):
    """
    N-Diode Generator for Skywater130
    """

    def __init__(self):
        # Initialize super class.
        super(n_diode, self).__init__()

        #===================== PARAMETERS DECLARATIONS =====================

        self.Type_handle  = self.param("type", self.TypeList, "Device Type")
        self.Type_handle.add_choice("sky130_fd_pr__diode_pw2nd_05v5", "sky130_fd_pr__diode_pw2nd_05v5")
        self.Type_handle.add_choice("sky130_fd_pr__diode_pw2nd_05v5_lvt", "sky130_fd_pr__diode_pw2nd_05v5_lvt")
        self.Type_handle.add_choice("sky130_fd_pr__diode_pw2nd_05v5_nvt", "sky130_fd_pr__diode_pw2nd_05v5_nvt")
        self.Type_handle.add_choice("sky130_fd_pr__diode_pw2nd_11v0", "sky130_fd_pr__diode_pw2nd_11v0")

        self.param("w", self.TypeDouble, "width", default=d_min, unit="um")
        self.param("l", self.TypeDouble, "length", default=d_min, unit="um")
        self.param("cath_w", self.TypeDouble, "Cathode Width", default=grw_min, unit="um")

        self.param("area", self.TypeDouble,"Area", readonly=True, unit="um^2")
        self.param("perim", self.TypeDouble,"Perimeter", readonly=True, unit="um")   

        #self.param("n", self.TypeInt, "n", default=1)

    def display_text_impl(self):
        # Provide a descriptive text for the cell
        return "n_diode(L=" + ('%.3f' % self.l) + ",W=" + ('%.3f' % self.w) + ")"
    
    def coerce_parameters_impl(self):
        # We employ coerce_parameters_impl to decide whether the handle or the
        # numeric parameter has changed (by comparing against the effective
        # radius ru) and set ru to the effective radius. We also update the
        # numerical value or the shape, depending on which on has not changed.
        self.area  = self.w * self.l
        self.perim = 2*(self.w + self.l)

        if self.l < d_min :
            self.l = d_min
        
        if self.w < d_min :
            self.w = d_min
        
        if self.cath_w < grw_min:
            self.cath_w = grw_min
    
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
        instance = draw_diode(layout= self.layout ,d_type="n", l=self.l, w=self.w, type=self.type,cath_w=self.cath_w)
        write_cells = pya.CellInstArray(instance.cell_index(), pya.Trans(pya.Point(0, 0)),
                      pya.Vector(0, 0), pya.Vector(0, 0), 1, 1)
        self.cell.insert(write_cells)
        self.cell.flatten(1)


class p_diode(pya.PCellDeclarationHelper):
    """
    N-Diode Generator for Skywater130
    """

    def __init__(self):
        # Initialize super class.
        super(p_diode, self).__init__()

        #===================== PARAMETERS DECLARATIONS =====================

        self.Type_handle  = self.param("type", self.TypeList, "Device Type")
        self.Type_handle.add_choice("sky130_fd_pr__diode_pd2nw_05v5", "sky130_fd_pr__diode_pd2nw_05v5")
        self.Type_handle.add_choice("sky130_fd_pr__diode_pd2nw_05v5_lvt", "sky130_fd_pr__diode_pd2nw_05v5_lvt")
        self.Type_handle.add_choice("sky130_fd_pr__diode_pd2nw_05v5_hvt", "sky130_fd_pr__diode_pd2nw_05v5_hvt")
        self.Type_handle.add_choice("sky130_fd_pr__diode_pd2nw_11v0", "sky130_fd_pr__diode_pd2nw_11v0")
        
        self.param("w", self.TypeDouble, "width", default=d_min, unit="um")
        self.param("l", self.TypeDouble, "length", default=d_min, unit="um")
        self.param("cath_w", self.TypeDouble, "Cathode width", default=grw_min, unit="um")
        self.param("grw", self.TypeDouble, "Gaurd Ring width", default=grw_min, unit="um")

        self.param("area", self.TypeDouble,"Area", readonly=True, unit="um^2")
        self.param("perim", self.TypeDouble,"Perimeter", readonly=True, unit="um")  

        #self.param("n", self.TypeInt, "n", default=1) 

    def display_text_impl(self):
        # Provide a descriptive text for the cell
        return "p_diode(L=" + ('%.3f' % self.l) + ",W=" + ('%.3f' % self.w) + ")"
    
    def coerce_parameters_impl(self):
        # We employ coerce_parameters_impl to decide whether the handle or the
        # numeric parameter has changed (by comparing against the effective
        # radius ru) and set ru to the effective radius. We also update the
        # numerical value or the shape, depending on which on has not changed.
        self.area  = self.w * self.l
        self.perim = 2*(self.w + self.l)

        if self.l < d_min :
            self.l = d_min
        
        if self.w < d_min :
            self.w = d_min
        
        if self.grw < grw_min:
            self.grw = grw_min

        if self.cath_w < grw_min:
            self.cath_w = grw_min
    
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
        instance = draw_diode(layout= self.layout ,d_type="p", l=self.l, w=self.w, type=self.type,grw=self.grw, cath_w=self.cath_w)
        write_cells = pya.CellInstArray(instance.cell_index(), pya.Trans(pya.Point(0, 0)),
                      pya.Vector(0, 0), pya.Vector(0, 0), 1, 1)
        self.cell.insert(write_cells)
        self.cell.flatten(1)
