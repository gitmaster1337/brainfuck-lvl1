"""Brain Even game logic."""


from random import randint

from brainfuck_games import settings


def ask_question():
    """Return a question and a correct answer.

    Returns:
        question: Number to evaluate if it is odd or even
        answer: Correct answer ('yes' or 'no')
    """
    question = randint(settings.MIN_NUM, settings.MAX_NUM)
    if question % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
