install-dependencies:
	pip install twine pytest

test: 
	pytest

build:
	python setup.py sdist
	python setup.py bdist_wheel

clean:
	rm -rf dist
	rm -rf build
	rm -rf src/susan.egg-info/

deploy: install-dependencies clean build
	twine upload dist/

