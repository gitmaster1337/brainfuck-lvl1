install:
	poetry install

lint:
	poetry run flake8 brainfuck_games

build:
	-@rm ./dist/* 2> /dev/null
	poetry build

publish:
	poetry publish --dry-run

package-install: install build
	python3 -m pip install --user dist/*.whl

brainfuck-games:
	poetry run brainfuck-games

brainfuck-even:
	poetry run brainfuck-even

brainfuck-calc:
	poetry run brainfuck-calc

brainfuck-gcd:
	poetry run brainfuck-gcd

brainfuck-progression:
	poetry run brainfuck-progression

brainfuck-prime:
	poetry run brainfuck-prime

.PHONY: install lint build publish
