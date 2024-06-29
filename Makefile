install:
	pip install -e .[dev,docs]

dev: install
	pre-commit install

modules:
	git submodule
	git submodule update --init --recursive

test:
	pytest -s

cov:
	pytest --cov=sky130

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
	jb build docs

.PHONY: gdsdiff build conda docs
