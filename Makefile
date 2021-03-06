SHELL = /bin/bash

.PHONY: test
test:
	cloc bin
	flake8 bin/*

.PHONY: deploy
deploy:
	rm -fr dist/* || true
	python -c 'x = open("VERSION", "r").read().split("."); open("VERSION", "w").write(x[0] + "." + x[1] + "." + str(int(x[2])+1))'
	python3 -m build
	python3 -m twine upload dist/*
	rm -fr dist/* || true
	git commit -am'Version bump'
	git push
	bash -x version.sh