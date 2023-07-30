install:
	pip install -e .[dev]
	pre-commit install
	gf tool install

watch:
	gf yaml watch sky130

test:
	pytest -s

cov:
	pytest --cov=sky130

mypy:
	mypy . --ignore-missing-imports

pylint:
	pylint sky130

lintd:
	pydocstyle sky130

doc:
	python docs/write_components_doc.py

doc8:
	doc8 docs/

update:
	pur

update-pre:
	pre-commit autoupdate --bleeding-edge

git-rm-merged:
	git branch -D `git branch --merged | grep -v \* | xargs`

release:
	git push
	git push --tags

build:
	rm -rf dist
	pip install build
	python -m build

tech:
	python3 install_tech.py

notebooks:
	nbstripout --drop-empty-cells docs/notebooks/intro.ipynb

link:
	ln -sf ${PWD}/sky130/klayout/sky130 ${HOME}/.klayout/tech/sky130

plugins:
	pip install -e .[docs]
	sudo apt install magic

docs:
	jb build docs

.PHONY: gdsdiff build conda docs
