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
# Global parameters generation 
########################################################################################################################

import glob 
import os
# Listing device names 

fixed_dev_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"fixed_devices" )  # parent file path 

BJT_NPN_DEV = glob.glob (f"{fixed_dev_path}/bjt/npn/*") 

for i in range(len(BJT_NPN_DEV)):
    BJT_NPN_DEV[i] =  BJT_NPN_DEV[i].split("/")[-1]
    BJT_NPN_DEV[i] = BJT_NPN_DEV[i][:-4]


BJT_PNP_DEV = glob.glob (f"{fixed_dev_path}/bjt/pnp/*") 

for i in range(len(BJT_PNP_DEV)):
    BJT_PNP_DEV[i] =  BJT_PNP_DEV[i].split("/")[-1]
    BJT_PNP_DEV[i] = BJT_PNP_DEV[i][:-4]


VPP_CAP_DEV= glob.glob (f"{fixed_dev_path}/VPP/*") 

for i in range(len(VPP_CAP_DEV)):
    VPP_CAP_DEV[i] =  VPP_CAP_DEV[i].split("/")[-1]
    VPP_CAP_DEV[i] = VPP_CAP_DEV[i][:-4]


PHOTO_D_DEV = glob.glob (f"{fixed_dev_path}/photodiode/*") 
for i in range(len(PHOTO_D_DEV)):
    PHOTO_D_DEV[i] =  PHOTO_D_DEV[i].split("/")[-1]
    PHOTO_D_DEV[i] = PHOTO_D_DEV[i][:-4]

RF_MOSFET_DEV = glob.glob (f"{fixed_dev_path}/rf/rf_mosfet/*") 
for i in range(len(RF_MOSFET_DEV)):
    RF_MOSFET_DEV[i] =  RF_MOSFET_DEV[i].split("/")[-1]
    RF_MOSFET_DEV[i] = RF_MOSFET_DEV[i][:-4]

RF_BJT_DEV = glob.glob (f"{fixed_dev_path}/rf/rf_bjt/*") 
for i in range(len(RF_BJT_DEV)):
    RF_BJT_DEV[i] =  RF_BJT_DEV[i].split("/")[-1]
    RF_BJT_DEV[i] = RF_BJT_DEV[i][:-4]

RF_COILS_DEV = glob.glob (f"{fixed_dev_path}/rf/rf_coils/*") 
for i in range(len(RF_COILS_DEV)):
    RF_COILS_DEV[i] =  RF_COILS_DEV[i].split("/")[-1]
    RF_COILS_DEV[i] = RF_COILS_DEV[i][:-4]

#print (VPP_CAP_DEV)
