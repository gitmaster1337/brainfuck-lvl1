"""Brainfuck Games game engine."""


import prompt
from brainfuck_games import cli, settings


def run_game(game_descr, ask_question):
    """Run a specific Brainfuck Game.

    Args:
        game_descr:
            Game description string
        ask_question:
            Function returning question and correct
            answer for a specific game

    Returns:
        1: If player won the game
        0: If player lost the game
    """
    user_name = cli.welcome_user()
    print(game_descr)
    rounds_won = 0
    while (rounds_won < settings.ROUNDS_TO_WIN):
        question, answer = ask_question()
        if run_round(user_name, question, answer):
            rounds_won += 1
        else:
            return 0
    print('Congratulations, {0}!'.format(user_name))
    return 1


def run_round(user_name, question, answer):
    """Run one round of a game.

    Args:
        user_name: User name string
        question: Game question to answer by user
        answer: Correct answer

    Returns:
        1: If user_answer entered by user matches correct answer
        0: If user_answer is different from correct answer
    """
    print('Question: {0}'.format(question))
    user_answer = prompt.string('Your answer: ')
    if user_answer == answer:
        print('Correct!')
        return 1
    print("'{0}' is the wrong answer ;(. Correct answer was '{1}'".format(
        user_answer, answer,
    ))
    print("Let's try again, {0}!".format(user_name))
    return 0
