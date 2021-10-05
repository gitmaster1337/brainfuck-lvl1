"""CLI functions."""


import prompt


def welcome_user():
    """Prompt user name, print welcome message."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
