#!/usr/bin/env python
"""Brainfuck Calc game script."""


from brainfuck_games import engine, settings
from brainfuck_games.games import calc


def main():
    """Run Brainfuck Calc game."""
    engine.run_game(settings.DESCR_BRAIN_CALC, calc.ask_question)


if __name__ == '__main__':
    main()
