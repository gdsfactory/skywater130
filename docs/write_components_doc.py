"""Generate sectioned ``components.rst`` and ``pcells.rst`` for the docs.

Cells are grouped by function so that the docs are easier to navigate than a
single flat list:

* ``components.rst`` splits the fixed (GDS-backed) cells into the digital
  standard-cell library (``sky130_fd_sc_hd``) and the analog primitive
  library (``sky130_fd_pr``).  Each library is further split into
  sub-sections (e.g. inverters/buffers, flip-flops, MOSFETs, capacitors,
  ESD, ...).
* ``pcells.rst`` splits the parametric cells into analog devices, vias and
  routing primitives.
"""

from __future__ import annotations

import pathlib
import re
from collections.abc import Iterable

import sky130

HERE = pathlib.Path(__file__).parent.absolute()
COMPONENTS_RST = HERE / "components.rst"
PCELLS_RST = HERE / "pcells.rst"

SKIP = {
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


# ---------------------------------------------------------------------------
# Categorisation
# ---------------------------------------------------------------------------

SC_PREFIX = "sky130_fd_sc_hd__"
PR_PREFIX = "sky130_fd_pr__"


def _sc_category(name: str) -> str:
    """Bucket a ``sky130_fd_sc_hd__*`` standard cell by function."""
    base = name[len(SC_PREFIX) :]
    base = re.sub(r"_\d+$", "", base)  # drop drive-strength suffix

    if base in {
        "decap",
        "diode",
        "fill",
        "fillcap",
        "tap",
        "tapvgnd",
        "tapvgnd2",
        "tapvpwrvgnd",
        "conb",
        "macro_sparecell",
        "probe_p",
        "probec_p",
    } or base.startswith(("fill", "tap", "decap", "probe")):
        return "Physical / fill / tap"

    if base.startswith(("clkbuf", "clkinv", "clkdly", "clkdlybuf", "clk")):
        return "Clock"
    if base.startswith(("buf", "bufinv", "bufbuf", "ebuf")):
        return "Buffers"
    if base.startswith(("inv", "einv")):
        return "Inverters"
    if base.startswith("mux"):
        return "Multiplexers"
    if base.startswith(("xnor", "xor")):
        return "XOR / XNOR"
    if base.startswith(("nand", "and")):
        return "AND / NAND"
    if base.startswith(("nor", "or")):
        return "OR / NOR"
    if base.startswith(("ha", "fa", "maj")):
        return "Arithmetic (adders / majority)"
    if base.startswith(("a2", "a3", "a4", "o2", "o3", "o4")):
        return "Complex AOI / OAI gates"
    if base.startswith(("df", "sdf", "sed", "edf")):
        return "Flip-flops"
    if base.startswith(("dl", "sdl")):
        return "Latches & delay cells"
    if base.startswith(("lpflow", "sleep", "iso")):
        return "Low-power"
    return "Other"


def _pr_category(name: str) -> str:
    """Bucket a ``sky130_fd_pr__*`` analog primitive cell by function."""
    base = name[len(PR_PREFIX) :]

    if base.startswith("cap_"):
        return "Capacitors (MIM / VPP)"
    if base.startswith("esd_"):
        return "ESD devices"
    if base.startswith("rf_nfet"):
        return "RF NFETs"
    if base.startswith("rf_pfet"):
        return "RF PFETs"
    if base.startswith("rf_npn"):
        return "RF NPN BJTs"
    if base.startswith("rf_pnp"):
        return "RF PNP BJTs"
    if base.startswith("rf_test"):
        return "RF test structures"
    if base.startswith("rf_aura"):
        return "RF aura test structures"
    if base.startswith("rf_"):
        return "RF other"
    return "Analog other"


def _pcell_category(name: str) -> str:
    """Bucket a parametric cell by function."""
    if name in {"nmos", "nmos_5v", "pmos", "pmos_5v"}:
        return "MOSFETs"
    if name in {"npn_W1L1", "npn_W1L2", "pnp"}:
        return "Bipolar transistors"
    if name in {"mimcap_1", "mimcap_2", "p_n_poly", "p_p_poly"}:
        return "Capacitors & poly resistors"
    if name in {"via_generator"} or name.startswith("via"):
        return "Vias"
    if name.startswith(("bend_", "straight_", "wire_")) or name == "waypoint":
        return "Routing primitives"
    return "Other"


# Order in which categories are rendered.
SC_ORDER: list[str] = [
    "Inverters",
    "Buffers",
    "Clock",
    "AND / NAND",
    "OR / NOR",
    "XOR / XNOR",
    "Multiplexers",
    "Arithmetic (adders / majority)",
    "Complex AOI / OAI gates",
    "Flip-flops",
    "Latches & delay cells",
    "Low-power",
    "Physical / fill / tap",
    "Other",
]

PR_ORDER: list[str] = [
    "Capacitors (MIM / VPP)",
    "RF NFETs",
    "RF PFETs",
    "RF NPN BJTs",
    "RF PNP BJTs",
    "ESD devices",
    "RF test structures",
    "RF aura test structures",
    "RF other",
    "Analog other",
]

PCELL_ORDER: list[str] = [
    "MOSFETs",
    "Bipolar transistors",
    "Capacitors & poly resistors",
    "Vias",
    "Routing primitives",
    "Other",
]


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------


def _heading(text: str, char: str) -> str:
    return f"{text}\n{char * len(text)}\n"


def _autosummary(module: str, names: Iterable[str]) -> str:
    body = [
        f".. currentmodule:: {module}",
        "",
        ".. autosummary::",
        "   :toctree: _autosummary/",
        "",
    ]
    body += [f"   {n}" for n in names]
    body.append("")
    return "\n".join(body)


def _grouped(
    names: Iterable[str], categorize, order: list[str]
) -> dict[str, list[str]]:
    groups: dict[str, list[str]] = {k: [] for k in order}
    for n in sorted(names):
        if n in SKIP or n.startswith("_"):
            continue
        cat = categorize(n)
        groups.setdefault(cat, []).append(n)
    return {k: v for k, v in groups.items() if v}


def write_components() -> None:
    all_names = set(sky130.cells.keys())
    pcell_names = set(sky130.pcells.__all__)
    fixed_names = all_names - pcell_names

    sc_names = [n for n in fixed_names if n.startswith(SC_PREFIX)]
    pr_names = [n for n in fixed_names if n.startswith(PR_PREFIX)]

    sc_groups = _grouped(sc_names, _sc_category, SC_ORDER)
    pr_groups = _grouped(pr_names, _pr_category, PR_ORDER)

    out: list[str] = []
    out.append(_heading("Cells", "="))
    out.append("Fixed (GDS-backed) cells available in the PDK, grouped by function.\n")

    out.append(_heading("Digital standard cells (sky130_fd_sc_hd)", "-"))
    out.append(
        "High-density digital standard-cell library.  Cells are grouped by\n"
        "logical function.  The trailing ``_N`` in each name encodes the\n"
        "drive strength.\n"
    )
    for cat in SC_ORDER:
        names = sc_groups.get(cat)
        if not names:
            continue
        out.append(_heading(cat, "^"))
        out.append(_autosummary("sky130.components", names))

    out.append(_heading("Analog / RF primitives (sky130_fd_pr)", "-"))
    out.append(
        "Analog primitive devices: MOSFETs, BJTs, capacitors, ESD devices\n"
        "and RF test structures.\n"
    )
    for cat in PR_ORDER:
        names = pr_groups.get(cat)
        if not names:
            continue
        out.append(_heading(cat, "^"))
        out.append(_autosummary("sky130.components", names))

    # Anything that didn't match either prefix
    leftover = sorted(
        n
        for n in fixed_names
        if not n.startswith((SC_PREFIX, PR_PREFIX))
        and n not in SKIP
        and not n.startswith("_")
    )
    if leftover:
        out.append(_heading("Other fixed cells", "-"))
        out.append(_autosummary("sky130.components", leftover))

    COMPONENTS_RST.write_text("\n".join(out).rstrip() + "\n")


def write_pcells() -> None:
    pcell_names = list(sky130.pcells.__all__)
    groups = _grouped(pcell_names, _pcell_category, PCELL_ORDER)

    out: list[str] = []
    out.append(_heading("PCells", "="))
    out.append("Parametric cells available in the PDK, grouped by device family.\n")
    for cat in PCELL_ORDER:
        names = groups.get(cat)
        if not names:
            continue
        out.append(_heading(cat, "-"))
        out.append(_autosummary("sky130.pcells", names))

    PCELLS_RST.write_text("\n".join(out).rstrip() + "\n")


if __name__ == "__main__":
    write_components()
    write_pcells()
    print(f"wrote {COMPONENTS_RST}")
    print(f"wrote {PCELLS_RST}")
