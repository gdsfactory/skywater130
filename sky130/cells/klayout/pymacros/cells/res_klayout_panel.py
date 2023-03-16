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

# res Generator for skywater130

import pya


class res(pya.PCellDeclarationHelper):
    """parent class for the front end of the res (klayout panel)
    Args:
        l_min(float): minimum length of the resistor
        w_min(float): minimum width of the resistor
    """

    def __init__(self, l_min, w_min):
        # Initialize super class.
        super(res, self).__init__()

        # ===================== PARAMETERS DECLARATIONS =====================

        self.Type_handle = self.param("type", self.TypeList, "Device Type")

        self.param("len", self.TypeDouble, "length", default=l_min, unit="um")
        self.param("w", self.TypeDouble, "width", default=w_min, unit="um")

        self.param("gr", self.TypeBoolean, "Gaurd Ring", default=1)
        self.param(
            "area", self.TypeDouble, "Area", readonly=True, unit="um^2"
        )
        self.param(
            "res_value",
            self.TypeDouble,
            "Res Value",
            readonly=True,
            unit="ohms",
        )

    def display_text_impl(self):
        """Provide a descriptive text for the cell
        Return:
            (str):the res name with len and w
        """

        # Provide a descriptive text for the cell
        return (
            "Resistor_"
            + str(self.type)
            + "(L="
            + ("%.3f" % self.len)
            + ",W="
            + ("%.3f" % self.w)
            + ")"
        )

    def coerce_parameters_impl(self, l_min, w_min):
        """check the minimum values of l and w

            decide whether the handle or the numeric parameter has
            changed (by comparing against the effective
            radius ru) and set ru to the effective radius. We also update the
            numerical value or the shape, depending on which on has not changed
        Args:
            l_min(float): minimum length of the resistor
            w_min(float): minimum width of the resistor

        """

        self.area = self.w * self.len

        if self.len < l_min:
            self.len = l_min

        if self.w < w_min:
            self.w = w_min

    def can_create_from_shape_impl(self):
        """Implement the Create PCell

        we can use any shape which has a finite bounding box
        """

        return (
            self.shape.is_box()
            or self.shape.is_polygon()
            or self.shape.is_path()
        )

    def parameters_from_shape_impl(self):
        """Implement the "Create PCell from shape" protocol:

        we set r and l from the shape's bounding box width and layer
        """
        self.r = self.shape.bbox().width() * self.layout.dbu / 2
        self.len = self.layout.get_info(self.layer)

    def transformation_from_shape_impl(self):
        """Implement the "Create PCell from shape" protocol:

        we use the center of the shape's bounding box
        to determine the transformation
        """
        return pya.Trans(self.shape.bbox().center())

    def produce_impl(self, instance):
        """call the implementation backend code
        Args:
            instance(layout): the result layout to show

        """
        write_cells = pya.CellInstArray(
            instance.cell_index(),
            pya.Trans(pya.Point(0, 0)),
            pya.Vector(0, 0),
            pya.Vector(0, 0),
            1,
            1,
        )
        self.cell.insert(write_cells)
        self.cell.flatten(1)
