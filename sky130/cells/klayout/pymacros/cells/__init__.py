
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

#============================================================================
# ---------------- Pcells Generators for Klayout of sky ----------------
#============================================================================

import pya
from cells.vias import vias_gen

from .fet     import *
from .diode   import *
from .bjt     import *
from .vpp     import *
from .rf      import *
from .cap import * 
from .gr import *
from .res_poly_klayout_panel import res_poly
from .res_diff_klayout_panel import res_diff
from .res_metal_klayout_panel import res_metal




# It's a Python class that inherits from the pya.Library class
class sky130(pya.Library):
    """
    The library where we will put the PCell into
    """

    def __init__(self):
        # Set the description
        self.description = "sky130 Pcells"

    # Create the PCell declarations
        # MOS DEVICES
        self.layout().register_pcell("pfet", pfet())
        self.layout().register_pcell("nfet", nfet())

        # BJT
        self.layout().register_pcell("npn_bjt", npn_bjt())  # npn_05v5_1p00x1p00, npn_05v5_1p00x2p00 , npn_11v0_1p00x1p00  
        self.layout().register_pcell("pnp_bjt", pnp_bjt())  # pnp_05v5_0p68x0p68 , pnp_05v5_3p40x3p40


        # CAP Devices 
        self.layout().register_pcell("cap_vpp", cap_vpp()) # VPP devices
        self.layout().register_pcell("cap_var", cap_var()) # varactor devices 
        self.layout().register_pcell("mim_cap", mim_cap()) # mim cap devices
    

        # DIODE DEVICES

        self.layout().register_pcell("photodiode", photo_diode())
        self.layout().register_pcell("n_diode", n_diode())
        self.layout().register_pcell("p_diode", p_diode())
        

        # RF Devices 
        self.layout().register_pcell("rf_mosfet", rf_mosfet())   # rf mosfets 
        self.layout().register_pcell("rf_bjt", rf_bjt())   # rf bjt 
        self.layout().register_pcell("rf_coils", rf_coils())   # rf coils 

        
        # vias 
        self.layout().register_pcell("vias_gen", vias_gen())   # vias generator 
        self.layout().register_pcell("guard_ring_gen", guard_ring_gen())   # vias generator 

        # Resistor 
        self.layout().register_pcell("res_diff", res_diff())   # Res diff generator 
        self.layout().register_pcell("res_poly", res_poly())   # Res poly generator 
        self.layout().register_pcell("res_metal", res_metal())   # Res metal generator 

        # Register us with the name "skywater130".
        self.register("skywater130")
