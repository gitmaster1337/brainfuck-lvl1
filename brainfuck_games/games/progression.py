"""Brain Progression game logic."""


from random import randint

from brainfuck_games.settings import (
    MAX_LEN,
    MAX_NUM,
    MAX_STEP,
    MIN_LEN,
    MIN_NUM,
)


def ask_question():
    """Return a question and a correct answer.

    Returns:
        question: Arithmetic progression string with a missing number
        answer: Correct answer (number missing from progression)
    """
    progr_len = randint(MIN_LEN, MAX_LEN)
    step = randint(1, MAX_STEP)
    first = randint(MIN_NUM, MAX_NUM)
    answer_index = randint(0, progr_len)
    question = ''
    answer = str(first)
    for index in range(0, progr_len + 1):
        if (index == answer_index):
            question += '{0} '.format('..')
            answer = str(first + (index * step))
        else:
            question += '{0} '.format(str(first + (index * step)))
    return question, answer
