build: clean 
	python -m venv build_venv
	./build_venv/bin/pip install setuptools
	./build_venv/bin/python ./setup.py sdist

clean:
	@rm -rf build_venv
	@rm -rf SpotifyLinuxOpen.egg-info

install:
	pip install dist/*
