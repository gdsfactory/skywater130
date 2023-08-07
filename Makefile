install:
	pip install -e .[dev,docs]
	pre-commit install

dev: install

test:
	pytest -s

cov:
	pytest --cov=sky130

mypy:
	mypy . --ignore-missing-imports

doc:
	python docs/write_components_doc.py

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

docs:
	jb build docs

.PHONY: gdsdiff build conda docs
