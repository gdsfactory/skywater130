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
# BJT Generator for skywater130
########################################################################################################################


import pya
from .draw_bjt import *
from .globals import *



class npn_bjt(pya.PCellDeclarationHelper):
    """
    NPN BJT Generator for Skywater130
    """

    def __init__(self):

        # Important: initialize the super class
        super(npn_bjt, self).__init__()
        self.Type_handle = self.param("type", self.TypeList, "type")
        
        for i in BJT_NPN_DEV :
            self.Type_handle.add_choice(i, i)

        
        
        self.param("Model", self.TypeString, "Model", default="sky130_fd_pr__npn",readonly=True)

    def display_text_impl(self):
        # Provide a descriptive text for the cell
        return str(self.type)
    
    def produce_impl(self):

        # This is the main part of the implementation: create the layout

        self.percision = 1/self.layout.dbu
        #self.cell.flatten(1)
        npn_instance = draw_npn(layout=self.layout,device_name=self.type)
        write_cells = pya.CellInstArray(npn_instance.cell_index(), pya.Trans(pya.Point(0, 0)),
                              pya.Vector(0, 0), pya.Vector(0, 0),1 , 1)
        self.cell.flatten(1)
        self.cell.insert(write_cells)
        self.layout.cleanup()
     
class pnp_bjt(pya.PCellDeclarationHelper):
    """
    PNP BJT Generator for Skywater130
    """

    def __init__(self):

        # Important: initialize the super class
        super(pnp_bjt, self).__init__()
        self.Type_handle = self.param("Type", self.TypeList, "Type")

        for i in BJT_PNP_DEV : 
            self.Type_handle.add_choice(i, i)


        self.param("Model", self.TypeString, "Model", default="sky130_fd_pr__pnp",readonly=True)

    def display_text_impl(self):
        # Provide a descriptive text for the cell
        return str(self.Type)
    
    def produce_impl(self):

        # This is the main part of the implementation: create the layout

        self.percision = 1/self.layout.dbu
        pnp_instance = draw_pnp(layout=self.layout,device_name=self.Type)
        write_cells = pya.CellInstArray(pnp_instance.cell_index(), pya.Trans(pya.Point(0, 0)),
                              pya.Vector(0, 0), pya.Vector(0, 0),1 , 1)
        self.cell.flatten(1)
        self.cell.insert(write_cells)

        self.layout.cleanup()
