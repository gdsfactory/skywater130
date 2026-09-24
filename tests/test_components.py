import pathlib

import gdsfactory as gf
import numpy as np
import pytest
from gdsfactory.component import Component
from pytest_regressions.data_regression import DataRegressionFixture

from sky130 import cells

skip = [
    "add_ports",
    "add_ports_m1",
    "add_ports_m2",
    "import_gds",
    "sky130_fd_sc_hd__conb_1",
    "sky130_fd_sc_hd__macro_sparecell",
    "compile_components",
    # Utility cells — tested separately in test_contact.py / test_guard_ring.py
    "contact_array",
    "licon_array",
    "mcon_array",
    "pwell_guard_ring",
    "nwell_guard_ring",
]

cell_names = set(cells.keys()) - set(skip)
dirpath = pathlib.Path(__file__).absolute().parent / "gds_ref"


@pytest.fixture(params=cell_names, scope="function")
def component(request) -> Component:
    return cells[request.param]()


def test_pdk_settings(
    component: Component, data_regression: DataRegressionFixture
) -> None:
    """Avoid regressions when exporting settings."""
    data_regression.check(component.to_dict())


MANHATTAN_ORIENTATIONS = (0.0, 90.0, 180.0, 270.0)

skip_test_manhattan_ports: set[str] = set()


@pytest.mark.parametrize("component_name", sorted(cell_names))
def test_port_orientations_manhattan(component_name: str) -> None:
    """Ensure that all ports have a manhattan orientation (0, 90, 180 or 270 deg)."""
    if component_name in skip_test_manhattan_ports:
        pytest.skip(f"Skipping manhattan port orientation test for {component_name}")
    component = cells[component_name]()
    if isinstance(component, gf.ComponentAllAngle):
        pytest.skip(f"{component_name} is an all-angle component")
    for port in component.ports:
        orientation = port.orientation % 360
        if not np.any(np.isclose(orientation, MANHATTAN_ORIENTATIONS, atol=1e-3)):
            raise AssertionError(
                f"Port {port.name} of {component_name} has non-manhattan "
                f"orientation {port.orientation} degrees."
            )
