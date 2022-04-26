import pathlib
import inspect
import sky130


filepath = pathlib.Path(__file__).parent.absolute() / "components.rst"

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


with open(filepath, "w+") as f:
    f.write(
        """

Here are the components available in the PDK


Components
=============================
"""
    )

    for name in sorted(sky130.cells.keys()):
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
        if name in skip_plot:
            f.write(
                f"""

{name}
----------------------------------------------------

.. autofunction:: sky130.components.{name}

"""
            )
        else:
            f.write(
                f"""

{name}
----------------------------------------------------

.. autofunction:: sky130.components.{name}

.. plot::
  :include-source:

  import sky130

  c = sky130.components.{name}({kwargs})
  c.plot()

"""
            )
