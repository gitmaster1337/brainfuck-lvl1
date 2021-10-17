"""Brainfuck Calc game logic."""


from random import choice, randint

from brainfuck_games import settings


def ask_question():
    """Return a question and a correct answer.

    Returns:
        question: String with arithmetic expression to calculate
        answer: Correct answer (result of the expression)
    """
    rand_num1 = randint(settings.MIN_NUM, settings.MAX_NUM)
    rand_num2 = randint(settings.MIN_NUM, settings.MAX_NUM)
    operation = choice(('+', '-', '*'))
    question = '{0} {1} {2}'.format(str(rand_num1), operation, str(rand_num2))
    if (operation == '+'):
        answer = str(rand_num1 + rand_num2)
    elif (operation == '-'):
        answer = str(rand_num1 - rand_num2)
    else:
        answer = str(rand_num1 * rand_num2)
    return question, answer
