install:
	poetry install

lint:
	poetry run flake8 brainfuck_games

build:
	-rm ./dist/*
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl
brainfuck-games:
	poetry run brainfuck-games

.PHONY: install
