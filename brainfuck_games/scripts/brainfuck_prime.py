#!/usr/bin/env python
"""Brainfuck Prime game script."""


from brainfuck_games import engine, settings
from brainfuck_games.games import prime


def main():
    """Run Brainfuck Prime game."""
    engine.run_game(settings.DESCR_PRIME, prime.ask_question)


if __name__ == '__main__':
    main()
