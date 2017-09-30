install-dependencies:
	pip install twine pytest pylint yapf

test: 
	pytest

build:
	python setup.py sdist
	python setup.py bdist_wheel

clean:
	rm -rf dist
	rm -rf build
	rm -rf src/susan.egg-info/

quality:
	yapf --recursive --in-place src/susan
	pylint src/susan

deploy: install-dependencies clean build
	twine upload dist/

