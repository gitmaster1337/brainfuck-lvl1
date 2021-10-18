#!/usr/bin/env python
"""Brainfuck Even game script."""


from brainfuck_games import engine, settings
from brainfuck_games.games import even


def main():
    """Run Brainfuck Even game."""
    engine.run_game(settings.DESCR_EVEN, even.ask_question)


if __name__ == '__main__':
    main()
