########################################################################################################################
## BJT Pcells Generators for Klayout of skywater130
########################################################################################################################


import os

from .globals import BJT_NPN_DEV, BJT_PNP_DEV

gds_p_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "fixed_devices/bjt"
)  #  parent file path


def draw_npn(layout, device_name):
    """
    drawing NPN devices
    """
    gds_path = f"{gds_p_path}/npn"

    if device_name in BJT_NPN_DEV:
        layout.read(f"{gds_path}/{device_name}.gds")
        cell_name = device_name
    else:
        cell_name = device_name

    return layout.cell(cell_name)


def draw_pnp(layout, device_name):
    """
    drawing PNP devices
    """
    gds_path = f"{gds_p_path}/pnp"

    if device_name in BJT_PNP_DEV:
        layout.read(f"{gds_path}/{device_name}.gds")
        cell_name = device_name
    else:
        cell_name = device_name

    return layout.cell(cell_name)
