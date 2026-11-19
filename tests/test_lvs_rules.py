"""Smoke tests for sky130.lvs.rules (skipped unless gflvs is installed)."""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path
from typing import Any

import pytest

gflvs = pytest.importorskip("gflvs")

import gdstk  # noqa: E402  (ships with gflvs)
from gflvs.gflvs_refactor import ElectricalDeviceExtractionPolicy  # noqa: E402
from gflvs.gflvs_schema import LvsRunMode  # noqa: E402
from result import Err, Ok  # noqa: E402

from sky130 import PDK, pcells  # noqa: E402
from sky130.layers import LAYER  # noqa: E402
from sky130.lvs import rules  # noqa: E402

GROUP_FLAGS = {
    "ENABLE_MOSFET_TEMPLATES": rules.MOSFET_TEMPLATES,
    "ENABLE_RESISTOR_TEMPLATES": rules.RESISTOR_TEMPLATES,
    "ENABLE_CAPACITOR_TEMPLATES": rules.CAPACITOR_TEMPLATES,
    "ENABLE_DIODE_TEMPLATES": rules.DIODE_TEMPLATES,
    "ENABLE_BJT_TEMPLATES": rules.BJT_TEMPLATES,
}


def _names(templates: list[Any]) -> list[str]:
    return [t.device_name for t in templates]


def test_default_config_builds() -> None:
    assert isinstance(rules.DEFAULT_LVS_CONFIG, gflvs.LvsConfig)


def test_connectivity_symmetric() -> None:
    assert all(
        a in rules.LAYER_CONNECTIVITY[b]
        for a, bs in rules.LAYER_CONNECTIVITY.items()
        for b in bs
    )


def test_template_layers_in_pdk() -> None:
    pdk_layers = {(layer.layer, layer.datatype) for layer in LAYER}  # type: ignore[attr-defined]  # aenum LayerMap
    used = rules._template_layers(rules.DEVICE_TEMPLATES) | set(
        rules.LAYER_CONNECTIVITY
    )
    assert used <= pdk_layers


def test_terminals_use_markers() -> None:
    missing = [
        (t.device_name, term.terminal_name)
        for t in rules.DEVICE_TEMPLATES
        if t.device_name not in rules.NO_MARKER_TEMPLATES
        for term in t.device_terminal_template
        if not rules._leaf_layers(term.layer_composed_op) & rules.MARKER_LAYERS
    ]
    assert not missing


def test_flags_toggle(monkeypatch: pytest.MonkeyPatch) -> None:
    with monkeypatch.context() as m:
        m.setattr(rules, "ENABLE_ELECTRICAL_TRACING", False)
        assert (
            not rules.build_lvs_config().netlist_tracer_config.galvanic_drawing_layers
        )

    with monkeypatch.context() as m:
        m.setattr(rules, "ENABLE_DEVICE_EXTRACTION", False)
        assert rules.build_lvs_config().device_templates == []

    with monkeypatch.context() as m:
        m.setattr(rules, "ENABLE_PARAMETER_CHECK", False)
        templates = rules.build_lvs_config().device_templates
        assert templates
        assert all(t.properties["blackbox"] == "true" for t in templates)
        assert all("blackbox" not in t.properties for t in rules.DEVICE_TEMPLATES)

    full = _names(rules.build_lvs_config().device_templates)
    for flag, group in GROUP_FLAGS.items():
        with monkeypatch.context() as m:
            m.setattr(rules, flag, False)
            kept = _names(rules.build_lvs_config().device_templates)
            assert kept == [n for n in full if n not in _names(group)], flag

    with monkeypatch.context() as m:
        m.setattr(rules, "HIERARCHICAL_RUN", True)
        assert rules.build_lvs_config().run_mode == LvsRunMode.LVS_RUN_MODE_HIERARCHICAL


# values from the swarm verification table (templates-sky130.md §3)
PCELL_ROWS = [
    (
        "nfet_01v8",
        dict(nf=3, gate_width=1, gate_length=0.5),
        4,
        dict(w=1.0, l=0.5, nf=3),
    ),
    ("nfet_01v8_lvt", dict(nf=5, gate_width=2), 4, dict(w=2.0, l=0.15, nf=5)),
    ("nfet_03v3_nvt", dict(nf=2), 4, dict(w=0.42, l=0.5, nf=2)),
    ("nfet_05v0_nvt", dict(nf=3), 4, dict(w=0.42, l=0.9, nf=3)),
    ("nfet_g5v0d10v5", dict(nf=2), 4, dict(w=0.42, l=0.5, nf=2)),
    ("esd_nfet_01v8", dict(nf=2, gate_width=5), 4, dict(w=5.0, l=0.15, nf=2)),
    (
        "pfet_01v8",
        dict(nf=2, gate_width=2, gate_length=0.25),
        4,
        dict(w=2.0, l=0.25, nf=2),
    ),
    ("pfet_01v8_lvt", dict(nf=3), 4, dict(w=0.42, l=0.35, nf=3)),
    (
        "pfet_01v8_hvt",
        dict(nf=2, gate_width=3, gate_length=1),
        4,
        dict(w=3.0, l=1.0, nf=2),
    ),
    ("pfet_g5v0d10v5", {}, 4, dict(w=0.42, l=0.5, nf=1)),
    ("res_generic_po", dict(res_width=1, res_length=5), 2, dict(w=1.0, l=5.0)),
    ("res_high_po_0p35", dict(res_length=2), 2, dict(w=0.35, l=2.0)),
    ("res_generic_nd", dict(res_width=0.5, res_length=4), 2, dict(w=0.5, l=4.0)),
    ("cap_mim_m3_1", dict(cap_width=5, cap_length=3), 2, dict(w=5.0, l=3.0)),
    # 3x5, not 4x6: TODO(https://github.com/gdsfactory/skywater130/issues/296) at 4x6 a via4 column ends on the cap2m edge and shorts the plates
    ("cap_mim_m3_2", dict(cap_width=3, cap_length=5), 2, dict(w=3.0, l=5.0)),
    ("diode_pw2nd_05v5", dict(diode_width=1, diode_length=2), 2, dict(w=1.0, l=2.0)),
    ("diode_pd2nw_05v5", dict(diode_width=2, diode_length=1), 2, dict(w=2.0, l=1.0)),
    pytest.param(
        "npn_05v5",
        dict(emitter_width=2, emitter_length=2),
        3,
        dict(w=2.0, l=2.0),
        # TODO(https://github.com/gdsfactory/skywater130/issues/296): the PCell npn has no collector tap, so COLLECTOR (the n+ tap) is empty
        marks=pytest.mark.xfail(
            strict=True, reason="PCell bug: npn collector has no tap"
        ),
    ),
    ("pnp_05v5", dict(emitter_width=3.4, emitter_length=3.4), 3, dict(w=3.4, l=3.4)),
]


@pytest.mark.parametrize("pcell, kwargs, n_terminals, params", PCELL_ROWS)
def test_pcell_extracts(
    pcell: str,
    kwargs: dict[str, float],
    n_terminals: int,
    params: dict[str, float],
    tmp_path: Path,
) -> None:
    device = f"sky130_fd_pr__{pcell}"
    PDK.activate()
    factory: Callable[..., Any] = getattr(pcells, device)
    component = factory(**kwargs)
    gds = component.write_gds(tmp_path / f"{pcell}.gds")
    # top_level() returns kfactory's $$$CONTEXT_INFO$$$ cell, so look the pcell up by name
    (top,) = [
        c
        for c in gdstk.read_gds(str(gds)).cells
        if isinstance(c, gdstk.Cell) and c.name == component.name
    ]

    results = ElectricalDeviceExtractionPolicy().execute(
        top,
        rules.DEVICE_TEMPLATES,
        rules.DEFAULT_LVS_CONFIG.electrical_device_extraction_config,
    )

    assert not [r for r in results if isinstance(r, Err)]
    devices = [r.ok_value for r in results if isinstance(r, Ok)]
    assert [d.class_name for d in devices] == [device]
    (extracted,) = devices
    assert len(extracted.terminals) == n_terminals
    values = {p.name: p.value for p in extracted.parameters}
    assert values == pytest.approx(params, rel=1e-3)
    # terminal names are the PCell's logical pins, its port names where it registers none
    pins = {p.name for p in component.pins} or {p.name for p in component.ports}
    assert {t.name for t in extracted.terminals} == pins


def test_terminals_bind_to_routes(tmp_path: Path) -> None:
    """li1 straps drawn in a parent on the S/D ports land the DRAIN/SOURCE terminals on traced nets."""
    PDK.activate()
    component = pcells.sky130_fd_pr__nfet_01v8()
    gds = component.write_gds(tmp_path / "nfet.gds")
    (device,) = [
        c
        for c in gdstk.read_gds(str(gds)).cells
        if isinstance(c, gdstk.Cell) and c.name == component.name
    ]
    top = gdstk.Cell("TOP")
    top.add(gdstk.Reference(device))
    li1 = LAYER.li1drawing
    for port in ("SOURCE", "DRAIN"):
        x, y = component.ports[port].center
        top.add(
            gdstk.rectangle(
                (x - 0.05, y - 0.05),
                (x + 0.05, y + 0.05),
                layer=li1[0],
                datatype=li1[1],
            )
        )
    library = gdstk.Library()
    library.add(top, device)

    cfg = rules.DEFAULT_LVS_CONFIG
    _, layout_to_netlist, _ = gflvs.layout_to_netlist(
        library,
        "TOP",
        device_templates=cfg.device_templates,
        nettracer_config=cfg.netlist_tracer_config,
        electrical_device_extraction_config=cfg.electrical_device_extraction_config,
    )

    nets = {net.name: net for net in layout_to_netlist.nets}
    (mos,) = [d for d in layout_to_netlist.devices if d.class_name]
    net_of = {t.name: nets[t.parent_net.net_name] for t in mos.terminals}
    assert net_of["DRAIN"].connected_shapes and net_of["SOURCE"].connected_shapes
    assert net_of["DRAIN"].name != net_of["SOURCE"].name


# deck testcases from efabless/sky130_klayout_pdk@dace518 (Apache-2.0), expected values from its KLayout LVS
LVS_GDS = Path(__file__).parent / "lvs_gds"


def _extract(gds: Path) -> list[Any]:
    library = gdstk.read_gds(str(gds))
    (top,) = library.top_level()
    cfg = rules.DEFAULT_LVS_CONFIG
    _, layout_to_netlist, _ = gflvs.layout_to_netlist(
        library,
        top.name,
        device_templates=cfg.device_templates,
        nettracer_config=cfg.netlist_tracer_config,
        electrical_device_extraction_config=cfg.electrical_device_extraction_config,
    )
    return [d for d in layout_to_netlist.devices if d.class_name]


def _nets(device: Any) -> dict[str, str]:
    return {t.name: t.parent_net.net_name for t in device.terminals}


def test_hd_inv_1_matches_klayout() -> None:
    """Dense std cell: per-finger W/L as KLayout, and A, Y, VGND, VPWR stay separate."""
    devices = {
        d.class_name: d for d in _extract(LVS_GDS / "sky130_fd_sc_hd__inv_1.gds")
    }
    n, p = devices["sky130_fd_pr__nfet_01v8"], devices["sky130_fd_pr__pfet_01v8_hvt"]
    assert {x.name: x.value for x in n.parameters} == pytest.approx(
        dict(l=0.15, w=0.65, nf=1)
    )
    assert {x.name: x.value for x in p.parameters} == pytest.approx(
        dict(l=0.15, w=1.0, nf=1)
    )
    n_nets, p_nets = _nets(n), _nets(p)
    assert n_nets["GATE"] == p_nets["GATE"]  # A
    n_sd = {n_nets["DRAIN"], n_nets["SOURCE"]}
    p_sd = {p_nets["DRAIN"], p_nets["SOURCE"]}
    assert len(n_sd) == len(p_sd) == 2
    assert len(n_sd & p_sd) == 1  # Y; VGND and VPWR stay apart
    assert n_nets["GATE"] not in n_sd | p_sd


def test_deck_npn_terminals_distinct() -> None:
    """The collector anchors on its n+ tap ring, not on the emitter li1."""
    (npn,) = _extract(LVS_GDS / "sky130_fd_pr__npn_05v5_W1p00L1p00.gds")
    nets = _nets(npn)
    assert sorted(nets) == ["BASE", "COLLECTOR", "EMITTER"]
    assert len(set(nets.values())) == 3
