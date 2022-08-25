"""Store configuration."""

__all__ = ["PATH"]

import pathlib

home = pathlib.Path.home()
cwd = pathlib.Path.cwd()
cwd_config = cwd / "config.yml"

home_config = home / ".config" / "sky130.yml"
config_dir = home / ".config"
config_dir.mkdir(exist_ok=True)
module_path = pathlib.Path(__file__).parent.absolute()
repo_path = module_path.parent


class Path:
    module = module_path
    repo = repo_path
    lyp = module_path / "klayout" / "sky130" / "layers.lyp"
    libs = module_path / "sky130A"
    sparameters = module_path / "sparameters"

    libs_tech = libs / "libs.tech"
    libs_ref = libs / "libs.ref"
    libs_ngspice = libs_tech / "ngspice"
    spice = module_path / "spice"

    libhd = libs / "sky130hd"
    libhs = libs / "sky130hs"
    libhvl = libs / "sky130hvl"

    gds = module_path / "gds"
    gdshd = libhd / "gds" / "sky130_fd_sc_hd.gds"
    gdshs = libhs / "gds" / "sky130_fd_sc_hs.gds"
    gdshvl = libhvl / "gds" / "sky130_fd_sc_hvl.gds"


PATH = Path()

if __name__ == "__main__":
    print(PATH)
