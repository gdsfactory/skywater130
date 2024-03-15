########################################################################################################################
## RF Devices Pcells Generators for Klayout of skywater130
########################################################################################################################


import os

from .globals import RF_BJT_DEV, RF_COILS_DEV, RF_MOSFET_DEV

gds_p_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "fixed_devices/rf"
)  # parent file path


def draw_rf_mosfet(layout, device_name):
    """
    drawing rf mosfet devices
    """
    gds_path = f"{gds_p_path}/rf_mosfet"  # gds file path

    if device_name in RF_MOSFET_DEV:
        layout.read(f"{gds_path}/{device_name}.gds")
        cell_name = device_name
    else:
        cell_name = device_name

    return layout.cell(cell_name)


def draw_rf_bjt(layout, device_name):
    """
    drawing rf mosfet devices
    """

    gds_path = f"{gds_p_path}/rf_bjt"  # gds file path

    if device_name in RF_BJT_DEV:
        layout.read(f"{gds_path}/{device_name}.gds")
        cell_name = device_name
    else:
        cell_name = device_name

    return layout.cell(cell_name)


def draw_rf_coils(layout, device_name):
    """
    drawing rf coils devices
    """

    gds_path = f"{gds_p_path}/rf_coils"  # gds file path

    if device_name in RF_COILS_DEV:
        layout.read(f"{gds_path}/{device_name}.gds")
        cell_name = device_name
    else:
        cell_name = device_name

    return layout.cell(cell_name)
