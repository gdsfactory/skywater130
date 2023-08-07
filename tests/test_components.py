import pathlib

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
]

cell_names = set(cells.keys()) - set(skip)
dirpath = pathlib.Path(__file__).absolute().with_suffix(".gds")


@pytest.fixture(params=cell_names, scope="function")
def component(request) -> Component:
    return cells[request.param]()


# def test_pdk_gds(component: Component) -> None:
#     """Avoid regressions in GDS geometry shapes and layers."""
#     difftest(component, dirpath=dirpath)


def test_pdk_settings(
    component: Component, data_regression: DataRegressionFixture
) -> None:
    """Avoid regressions when exporting settings."""
    data_regression.check(component.to_dict())


def test_assert_ports_on_grid(component: Component):
    component.assert_ports_on_grid()
