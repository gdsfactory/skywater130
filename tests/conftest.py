import gdsfactory as gf
import pytest


@pytest.fixture(autouse=True)
def _clear_gds_cache():
    """Clear gdsfactory cell cache before each test.

    When _top variants are loaded first, base cells get cached as sub-cells
    without post_process (port extraction) applied. Clearing the cache ensures
    each test starts fresh.
    """
    gf.clear_cache()
