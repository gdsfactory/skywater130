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
## RF Devices Pcells Generators for Klayout of skywater130
########################################################################################################################


import pya
import os
from .globals import *
import gdsfactory as gf

 

gds_p_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"fixed_devices/rf" )  # parent file path 



def draw_rf_mosfet(layout, device_name):

    '''
    drawing rf mosfet devices 
    '''
    gds_path = f"{gds_p_path}/rf_mosfet"   # gds file path 

    
    if device_name in RF_MOSFET_DEV :
        layout.read(f"{gds_path}/{device_name}.gds")
        cell_name = device_name
    else : 
        cell_name = device_name    


    return layout.cell(cell_name)

def draw_rf_bjt(layout, device_name):
    '''
    drawing rf mosfet devices 
    '''

    gds_path = f"{gds_p_path}/rf_bjt"   # gds file path 


    
    if device_name in RF_BJT_DEV :
        layout.read(f"{gds_path}/{device_name}.gds")
        cell_name = device_name
    else : 
        cell_name = device_name      


    return layout.cell(cell_name)


def draw_rf_coils(layout, device_name):
    '''
    drawing rf coils devices 
    '''

    gds_path = f"{gds_p_path}/rf_coils"   # gds file path 

    
    
    if device_name in RF_COILS_DEV :
        layout.read(f"{gds_path}/{device_name}.gds")
        cell_name = device_name
    else : 
        cell_name = device_name   

    return layout.cell(cell_name)
