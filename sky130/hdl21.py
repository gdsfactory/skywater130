"""
Configuration for the hdl21 PDK linking with our source files.
"""
import pathlib

import sky130_hdl21

pdk_path = pathlib.Path(__file__).parent / "src" / "sky130_fd_pr"
model_ref = pdk_path / "models" / "sky130.lib.spice"

sky130_hdl21.install = sky130_hdl21.Install(
    pdk_path=pdk_path,
    lib_path=model_ref,
    model_ref=model_ref,
)
