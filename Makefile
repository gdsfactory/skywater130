install: modules
	uv venv --python 3.12
	uv sync --extra docs --extra dev

rm-samples:
	rm -rf samples

dev:
	uv sync --all-extras
	uv pip install -e .
	uv run pre-commit install

modules:
	git config --global --add safe.directory sky130
	git config --global --add safe.directory sky130/src
	git config --global --add safe.directory /__w/skywater130/skywater130
	git submodule
	git submodule update --init --recursive

ngspice:
	sudo apt-get update
	sudo apt-get install -y ngspice

test:
	uv run pytest -s -n logical

cov:
	uv run pytest --cov=sky130

mypy:
	mypy . --ignore-missing-imports

doc:
	python docs/write_components_doc.py

update-pre:
	pre-commit autoupdate

git-rm-merged:
	git branch -D `git branch --merged | grep -v \* | xargs`

release:
	git push
	git push --tags

build:
	rm -rf sky130/src/sky130_fd_sc_hd/timing
	find . -type d -name "tests" -exec rm -rf {} +
	rm -rf dist
	pip install build
	python -m build

tech:
	python3 install_tech.py

docs:
	uv run jb build docs

.PHONY: gdsdiff build conda docs modules
