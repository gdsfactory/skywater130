########################################################################################################################
# VPP CAP Generator for skywater130
########################################################################################################################


import pya

from .draw_vpp import draw_vpp
from .globals import VPP_CAP_DEV


class cap_vpp(pya.PCellDeclarationHelper):
    """
    VPP Cap Generator for Skywater130
    """

    def __init__(self):
        # Important: initialize the super class
        super().__init__()
        self.Type_handle = self.param("Type", self.TypeList, "Type")

        for i in range(len(VPP_CAP_DEV)):
            self.Type_handle.add_choice(VPP_CAP_DEV[i], VPP_CAP_DEV[i])

        self.param(
            "Model",
            self.TypeString,
            "Model",
            default="sky130_fd_pr__cap_vpp",
            readonly=True,
        )

    def display_text_impl(self):
        # Provide a descriptive text for the cell
        return str(self.Type)

    def produce_impl(self):
        # This is the main part of the implementation: create the layout

        self.percision = 1 / self.layout.dbu
        vpp_instance = draw_vpp(layout=self.layout, device_name=self.Type)
        write_cells = pya.CellInstArray(
            vpp_instance.cell_index(),
            pya.Trans(pya.Point(0, 0)),
            pya.Vector(0, 0),
            pya.Vector(0, 0),
            1,
            1,
        )
        self.cell.flatten(1)
        self.cell.insert(write_cells)
        self.layout.cleanup()
