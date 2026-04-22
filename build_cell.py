"""Build a cell and write it to build/gds/<cell_name>.gds.

When cell_name is "all_cells", builds every PDK-owned cell that can be
instantiated with default arguments and packs them into a single GDS.
Cells from installed packages (site-packages / .venv) and cells that
require positional arguments are skipped automatically.
"""

import inspect
import sys
from pathlib import Path

from gdsfactoryplus.core.pdk import get_pdk, register_cells

cell_name = sys.argv[1]
Path("build/gds").mkdir(parents=True, exist_ok=True)
register_cells()
pdk = get_pdk()

if cell_name == "all_cells":
    import gdsfactory as gf

    c = gf.Component("all_cells")
    for name, func in sorted(pdk.cells.items()):
        # Skip cells from installed packages (not PDK-owned)
        try:
            src = inspect.getfile(func)
        except TypeError:
            continue
        if ".venv" in src or "site-packages" in src:
            continue

        # Skip cells that require positional arguments
        sig = inspect.signature(func)
        required = [
            p
            for p in sig.parameters.values()
            if p.default is inspect.Parameter.empty
            and p.kind not in (p.VAR_POSITIONAL, p.VAR_KEYWORD)
        ]
        if required:
            print(f"Skipping {name}: requires arguments {[p.name for p in required]}")
            continue

        try:
            c.add_ref(func())
        except Exception as e:  # noqa: BLE001
            print(f"Error instantiating cell {name}: {e}")
    c.write_gds(f"build/gds/{cell_name}.gds")
else:
    c = pdk.cells[cell_name]()
    c.write_gds(f"build/gds/{cell_name}.gds")
