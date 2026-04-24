# sky130 gdsfactory PDK 0.15.2

<!-- BADGES:START -->
[![Docs](https://github.com/gdsfactory/skywater130/actions/workflows/pages.yml/badge.svg)](https://github.com/gdsfactory/skywater130/actions/workflows/pages.yml)
[![Tests](https://github.com/gdsfactory/skywater130/actions/workflows/test_code.yml/badge.svg)](https://github.com/gdsfactory/skywater130/actions/workflows/test_code.yml)
[![DRC](https://github.com/gdsfactory/skywater130/raw/badges/drc.svg)](https://github.com/gdsfactory/skywater130/actions/workflows/drc.yml)
[![Model Regression](https://github.com/gdsfactory/skywater130/actions/workflows/model_regression.yml/badge.svg)](https://github.com/gdsfactory/skywater130/actions/workflows/model_regression.yml)
[![Test Coverage](https://github.com/gdsfactory/skywater130/raw/badges/coverage.svg)](https://github.com/gdsfactory/skywater130/actions/workflows/test_coverage.yml)
[![Model Coverage](https://github.com/gdsfactory/skywater130/raw/badges/model_coverage.svg)](https://github.com/gdsfactory/skywater130/actions/workflows/model_coverage.yml)
[![Issues](https://github.com/gdsfactory/skywater130/raw/badges/issues.svg)](https://github.com/gdsfactory/skywater130/issues)
[![PRs](https://github.com/gdsfactory/skywater130/raw/badges/prs.svg)](https://github.com/gdsfactory/skywater130/pulls)
<!-- BADGES:END -->


[![pypi](https://img.shields.io/pypi/v/sky130)](https://pypi.org/project/sky130/)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

gdsfactory pdk based on [skywater130](https://github.com/google/skywater-pdk)

![logo](https://i.imgur.com/xvnfEtZ.png)


- [documentation](https://gdsfactory.github.io/skywater130/README.html)

## Installation

We recommend `uv`

```bash
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh
```

```bash
# On Windows.
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Installation for users

Use python 3.11, 3.12 or 3.13. We recommend [VSCode](https://code.visualstudio.com/) as an IDE.

```
uv pip install sky130 --upgrade
```

Then you need to restart Klayout to make sure the new technology installed appears.

### Installation for contributors


Then you can install with:

```bash
git clone https://github.com/gdsfactory/skywater130.git
cd sky130
make install
uv venv --python 3.12
uv sync --extra docs --extra dev
```

## Documentation

- [gdsfactory docs](https://gdsfactory.github.io/gdsfactory/)
