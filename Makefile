install:
	poetry install

lint:
	poetry run flake8 brainfuck_games

build:
	-@rm ./dist/*
	poetry build

publish:
	poetry publish --dry-run

package-install: install build
	python3 -m pip install --user dist/*.whl

brainfuck-games:
	poetry run brainfuck-games

brainfuck-even:
	poetry run brainfuck-even

.PHONY: install lint build publish
