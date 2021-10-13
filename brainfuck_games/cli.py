"""CLI functions."""


import prompt


def welcome_user():
    """Prompt user name, print welcome message.

    Returns:
        name: Name entered by user
    """
    print('Welcome to Brainfuck Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name
