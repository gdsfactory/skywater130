########################################################################################################################
## VPP CAP Pcells Generators for Klayout of skywater130
########################################################################################################################


import os

from .globals import VPP_CAP_DEV

gds_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixed_devices/VPP")


def draw_vpp(layout, device_name):
    """
    drawing VPP Capacitors devices
    """

    if device_name in VPP_CAP_DEV:
        layout.read(f"{gds_path}/{device_name}.gds")
        cell_name = device_name
    else:
        cell_name = device_name
    return layout.cell(cell_name)
