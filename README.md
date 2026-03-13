# sky130 gdsfactory PDK 0.15.2

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

## Pre-commit

```bash
make pre-commit
```

## Release

Releases are automated via GitHub Actions.

1. Merge your changes to `main`.
2. A draft release is automatically created/updated by the release drafter.
3. When ready, publish the draft release with a tag (e.g. `v1.0.0`). This triggers the release workflow that builds wheels and uploads them.
