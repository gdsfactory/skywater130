import pathlib
import inspect
import sky130


cells = pathlib.Path(__file__).parent.absolute() / "components.rst"
pcells = pathlib.Path(__file__).parent.absolute() / "pcells.rst"

skip = {
    "LIBRARY",
    "circuit_names",
    "cells",
    "component_names",
    "container_names",
    "component_names_test_ports",
    "component_names_skip_test",
    "component_names_skip_test_ports",
    "dataclasses",
    "library",
    "waveguide_template",
    "add_ports_m1",
    "add_ports_m2",
    "add_ports",
    "import_gds",
}

skip_plot = {}
skip_settings = {"flatten", "safe_cell_names"}

pcell_names = set(sky130.pcells.__all__)
cell_names = set(sky130.cells.keys()) - pcell_names


with open(pcells, "w+") as f:
    f.write(
        """

Here are the Parametric Pcells available in the PDK

PCells
=============================

.. currentmodule:: sky130.pcells

.. autosummary::
   :toctree: _autosummary/

"""
    )

    for name in sorted(pcell_names):
        if name in skip or name.startswith("_"):
            continue
        print(name)
        sig = inspect.signature(sky130.PDK.cells[name])
        kwargs = ", ".join(
            [
                f"{p}={repr(sig.parameters[p].default)}"
                for p in sig.parameters
                if isinstance(sig.parameters[p].default, (int, float, str, tuple))
                and p not in skip_settings
            ]
        )
        f.write(f"   {name}\n")

with open(cells, "w+") as f:

    f.write(
        """

Cells
=============================

.. currentmodule:: sky130.components

.. autosummary::
   :toctree: _autosummary/

"""
    )

    for name in sorted(cell_names):
        if name in skip or name.startswith("_"):
            continue
        print(name)
        sig = inspect.signature(sky130.cells[name])
        kwargs = ", ".join(
            [
                f"{p}={repr(sig.parameters[p].default)}"
                for p in sig.parameters
                if isinstance(sig.parameters[p].default, (int, float, str, tuple))
                and p not in skip_settings
            ]
        )
        f.write(f"   {name}\n")
