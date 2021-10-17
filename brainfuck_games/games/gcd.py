"""Brainfuck GCD game logic."""


from random import randint

from brainfuck_games import settings


def calculate_gcd(num1, num2):
    """Calculate GCD of num1 and num2 using Euclidian algorithm.

    Args:
        num1: Integer
        num2: Integer

    Returns:
        gcd: Greatest common divisor of num1 and num2
    """
    while (num2):
        num1, num2 = num2, num1 % num2
    return num1


def ask_question():
    """Return a question and a correct answer.

    Returns:
        question: String with two numbers to find greatest common divisor
        answer: Correct answer (greatest common divisor)
    """
    rand_num1 = randint(settings.MIN_NUM, settings.MAX_NUM)
    rand_num2 = randint(settings.MIN_NUM, settings.MAX_NUM)
    question = '{0} {1}'.format(str(rand_num1), str(rand_num2))
    answer = str(calculate_gcd(rand_num1, rand_num2))
    return question, answer
