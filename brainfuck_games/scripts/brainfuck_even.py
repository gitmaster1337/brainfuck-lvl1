#!/usr/bin/env python
"""Brainfuck Even game script."""


from random import randint

import prompt
from brainfuck_games import cli

MIN_NUM = 1
MAX_NUM = 100
ROUNDS_TO_WIN = 3


def make_round(user_name):
    """Run a round of Brainfuck Even game.

    Args:
        user_name: Name of the player

    Returns:
        1: If player won the round
        0: If player lost the round
    """
    rand_num = randint(MIN_NUM, MAX_NUM)
    print('Question: {0}'.format(rand_num))
    if rand_num % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    user_answer = prompt.string('Your answer: ')
    if user_answer == answer:
        print('Correct!')
        return 1
    print("'{0}' is the wrong answer ;(. Correct answer was '{1}'".format(
        user_answer, answer,
    ))
    print("Let's try again, {0}!".format(user_name))
    return 0


def main():
    """Run Brainfuck Even game.

    Returns:
        1: If player won ROUNDS_TO_WIN rounds
        0: If player lost
    """
    user_name = cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    rounds_won = 0
    while (rounds_won < ROUNDS_TO_WIN):
        if make_round(user_name):
            rounds_won += 1
        else:
            return 0
    print('Congratulations, {0}!'.format(user_name))
    return 1


if __name__ == '__main__':
    main()
