"""Generate Markdown docs for skywater130 cells and pcells with kwasm viewers."""

import inspect
import pathlib
import traceback

import kwasm.embed
import matplotlib as mpl
import matplotlib.pyplot as plt

import sky130

mpl.use("Agg")

docs_dir = pathlib.Path(__file__).parent.absolute()
cells_md = docs_dir / "components.md"
pcells_md = docs_dir / "pcells.md"
kwasm_dir = docs_dir / "kwasm"
gds_dir = kwasm_dir / "gds"

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

skip_plot: set[str] = set()
skip_settings = {"flatten", "safe_cell_names"}

pcell_names = set(sky130.pcells.__all__)
cell_names = set(sky130.cells.keys()) - pcell_names


def _setup_kwasm_viewer() -> None:
    """Create the kwasm viewer HTML template for interactive GDS viewing."""
    gds_dir.mkdir(parents=True, exist_ok=True)
    viewer_path = kwasm_dir / "viewer.html"
    if viewer_path.exists():
        return
    template = kwasm.embed._read_artifacts()
    template = template.replace("KWASM_GDS_B64", "")
    template = template.replace("KWASM_LYP_B64", "")
    template = template.replace("KWASM_LYRDB_B64", "")
    template = template.replace("KWASM_NETLIST_B64", "")
    viewer_path.write_text(template)


def _write_gds(name: str) -> bool:
    """Instantiate a pcell with defaults and write GDS + PNG. Returns True on success."""
    try:
        sig = inspect.signature(sky130.PDK.cells[name])
        kwargs = {
            p: sig.parameters[p].default
            for p in sig.parameters
            if isinstance(sig.parameters[p].default, int | float | str | tuple)
            and p not in skip_settings
        }
        c = sky130.PDK.cells[name](**kwargs)

        # Write GDS
        gds_path = gds_dir / f"{name}.gds"
        c.write_gds(gds_path)

        # Write PNG
        fig, ax = plt.subplots()
        c.plot(ax=ax)
        png_path = gds_dir / f"{name}.png"
        fig.savefig(png_path, dpi=150, bbox_inches="tight")
        plt.close(fig)

        return True
    except Exception:
        traceback.print_exc()
        return False


# --- Main ---

_setup_kwasm_viewer()

# Write pcells.md with kwasm viewers
with open(pcells_md, "w") as f:
    f.write("# PCells\n\n")
    f.write("Parametric PCells available in the PDK.\n\n")

    for name in sorted(pcell_names):
        if name in skip or name.startswith("_"):
            continue
        print(name)
        sig = inspect.signature(sky130.PDK.cells[name])
        kwargs = ", ".join(
            [
                f"{p}={repr(sig.parameters[p].default)}"
                for p in sig.parameters
                if isinstance(sig.parameters[p].default, int | float | str | tuple)
                and p not in skip_settings
            ]
        )

        f.write(f"## {name}\n\n")
        f.write(f"::: sky130.pcells.{name}\n\n")

        if name not in skip_plot:
            has_gds = _write_gds(name)
            if has_gds:
                f.write('=== "Static"\n\n')
                f.write(f"    ![{name}](kwasm/gds/{name}.png)\n\n")
                f.write('=== "Dynamic"\n\n')
                f.write(
                    f'    <iframe src="kwasm/viewer.html?url=gds/{name}.gds"'
                    f' loading="lazy" width="100%" height="400"'
                    f' style="border:none"></iframe>\n\n'
                )

        f.write("```python\n")
        f.write("import sky130\n\n")
        f.write("sky130.PDK.activate()\n")
        f.write(f'c = sky130.PDK.cells["{name}"]({kwargs})\n')
        f.write("c.draw_ports()\n")
        f.write("c.plot()\n")
        f.write("```\n\n")

# Write components.md (listing only, no viewers)
with open(cells_md, "w") as f:
    f.write("# Cells\n\n")
    f.write("Fixed cells available in the PDK.\n\n")

    for name in sorted(cell_names):
        if name in skip or name.startswith("_"):
            continue
        print(name)
        sig = inspect.signature(sky130.cells[name])
        kwargs = ", ".join(
            [
                f"{p}={repr(sig.parameters[p].default)}"
                for p in sig.parameters
                if isinstance(sig.parameters[p].default, int | float | str | tuple)
                and p not in skip_settings
            ]
        )
        f.write(f"::: sky130.components.{name}\n\n")
