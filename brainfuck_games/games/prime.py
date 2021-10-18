"""Brain Prime game logic."""


from random import randint

from brainfuck_games import settings


def is_prime(num):
    """Check if number is prime.

    Args:
        num: integer

    Returns:
        True: if number is prime
        False: if number is not prime
    """
    if num <=1:
        return False
    if num > 2:
        for i in range(2, num):
            if (num % i) == 0:
                return False
    return True


def ask_question():
    """Return a question and a correct answer.

    Returns:
        question: String with number to evaluate if it is a prime
        answer: String with correct answer ('yes' or 'no')
    """
    question = randint(settings.MIN_NUM, settings.MAX_NUM)
    answer = 'yes' if is_prime(question) else 'no'
    return str(question), answer
