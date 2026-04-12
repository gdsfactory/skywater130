"""Build a cell and write it to build/gds/<cell_name>.gds."""

import sys
from pathlib import Path

from gdsfactoryplus.core.pdk import get_pdk, register_cells

cell_name = sys.argv[1]
Path("build/gds").mkdir(parents=True, exist_ok=True)
register_cells()
c = get_pdk().cells[cell_name]()
c.write_gds(f"build/gds/{cell_name}.gds")
