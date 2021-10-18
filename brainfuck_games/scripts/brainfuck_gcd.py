#!/usr/bin/env python
"""Brainfuck GCD game script."""


from brainfuck_games import engine, settings
from brainfuck_games.games import gcd


def main():
    """Run Brainfuck GCD game."""
    engine.run_game(settings.DESCR_GCD, gcd.ask_question)


if __name__ == '__main__':
    main()
