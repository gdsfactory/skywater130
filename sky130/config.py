"""Store paths."""

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
    lyp = module_path / "klayout" / "layers.lyp"
    lyp_yaml = module_path / "klayout" / "layers.yaml"
    libs = module_path / "sky130A"
    sparameters = module_path / "sparameters"
    klayout = module_path / "klayout"
    spice = module_path / "spice"
    src = module_path / "src"


PATH = Path()

if __name__ == "__main__":
    print(PATH)
