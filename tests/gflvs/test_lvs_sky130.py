"""Integration test for SkyWater130 gflvs LVS config."""

from __future__ import annotations

import pytest

gflvs = pytest.importorskip("gflvs")

from sky130.lvs import DEFAULT_LVS_CONFIG  # noqa: E402


def test_lvs_config_importable() -> None:
    assert DEFAULT_LVS_CONFIG is not None


def test_gds_table_nonempty() -> None:
    from sky130.lvs.lvs import GDS_TABLE

    assert len(GDS_TABLE) > 0


def test_inverter_lvs_smoke() -> None:
    """Smoke: inverter schematic + empty layout, run LVS, assert result returned."""
    import gdsfactory as gf
    from gflvs.gflvs_schema.circuit import TerminalReference
    from gflvs.schematic import (
        build_circuit,
        build_connection,
        build_external_module,
        build_module,
        build_module_reference,
        build_terminal,
    )

    from sky130.lvs import run_lvs_sky130

    nfet = build_external_module("sky130_fd_pr__nfet_01v8", terminals=[
        build_terminal("D"), build_terminal("G"), build_terminal("S"), build_terminal("B"),
    ])
    pfet = build_external_module("sky130_fd_pr__pfet_01v8", terminals=[
        build_terminal("D"), build_terminal("G"), build_terminal("S"), build_terminal("B"),
    ])
    top = build_module(
        name="inverter",
        module_references=[build_module_reference("mn", "sky130_fd_pr__nfet_01v8"), build_module_reference("mp", "sky130_fd_pr__pfet_01v8")],
        connections=[
            build_connection(
                "drain_net",
                source=TerminalReference(instance_name="mn", terminal_name="D"),
                target=TerminalReference(instance_name="mp", terminal_name="D"),
            ),
        ],
    )
    circuit = build_circuit("inverter", top_module="inverter", modules=[top], ext_modules=[nfet, pfet])
    layout = gf.Component("inverter")
    result = run_lvs_sky130(layout, circuit)
    assert result is not None
