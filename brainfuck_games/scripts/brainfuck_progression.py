#!/usr/bin/env python
"""Brainfuck Progression game script."""


from brainfuck_games import engine, settings
from brainfuck_games.games import progression


def main():
    """Run Brainfuck Progression game."""
    engine.run_game(settings.DESCR_BRAIN_PROGRESSION, progression.ask_question)


if __name__ == '__main__':
    main()
