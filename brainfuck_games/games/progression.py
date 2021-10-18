"""Brain Progression game logic."""


from random import randint

from brainfuck_games import settings


def ask_question():
    """Return a question and a correct answer.

    Returns:
        question: Arithmetic progression string with a missing number
        answer: Correct answer (number missing from progression)
    """
    progr_len = randint(settings.MIN_LEN, settings.MAX_LEN)
    step = randint(1, settings.MAX_STEP)
    first = randint(settings.MIN_NUM, settings.MAX_NUM)
    missed_num_i = randint(0, progr_len)
    question = ''
    answer = str(first)
    for i in range(0, progr_len):
        if (i == missed_num_i):
            current_num = '..'
            answer = str(first + (i * step))
        else:
            current_num = first + (i * step)
        question = question + str(current_num) + ' '
    return question, answer
