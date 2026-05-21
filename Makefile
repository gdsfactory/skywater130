install: modules
	uv venv --python 3.12
	uv sync --extra docs --extra dev

rm-samples:
	rm -rf samples

dev: modules
	uv sync --all-extras
	uv pip install -e .
	curl -sf https://raw.githubusercontent.com/doplaydo/pdk-ci-workflow/main/templates/.pre-commit-config.yaml -o .pre-commit-config.yaml
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

test-force: install
	uv run pytest -s -n logical --force-regen

cov:
	uv run pytest --cov=sky130

mypy:
	mypy . --ignore-missing-imports

doc:
	uv run python docs/write_components_doc.py

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

nbdocs:
	rm -rf docs/notebooks/*.md
	find notebooks -maxdepth 1 -mindepth 1 -name "*.ipynb" | sort | \
		xargs -P4 -I{} uv run --extra docs jupyter nbconvert \
			--execute --to markdown --embed-images {} --output-dir docs/notebooks
	uv run python docs/hooks.py docs/notebooks/*.md

docs-pdf: nbdocs
	uv run python -c "import re; from pathlib import Path; t=Path('CHANGELOG.md').read_text(); Path('docs/changelog.md').write_text(re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', t))"
	uv run mkdocs build -f mkdocs-pdf.yml

docs: nbdocs
	uv run python -c "import re; from pathlib import Path; t=Path('CHANGELOG.md').read_text(); Path('docs/changelog.md').write_text(re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', t))"
	uv run --extra docs zensical build

docs-serve: nbdocs
	uv run python -c "import re; from pathlib import Path; t=Path('CHANGELOG.md').read_text(); Path('docs/changelog.md').write_text(re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', t))"
	uv run --extra docs zensical serve -a localhost:8080

.PHONY: drc drc-sample doc docs docs-pdf build
