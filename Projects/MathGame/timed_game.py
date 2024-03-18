import time
from random import randint

def timed_math_game(num_of_questions):
    """A simple game to time the user by asking a number of math questions.

    Args:
        num_of_questions (int): The number of questions to be asked.
    """

    number_of_questions = num_of_questions

    # the operands the question may use.
    operands = ["*", "+", "-", "//", "%"]

    start_time = time.time()

    # format of the question
    question = f'{randint(1, 20)} {operands[randint(0, len(operands) - 1)]} {randint(1, 20)}'

    correct = 0

    # loops until all questions are answered correctly.
    while correct < number_of_questions:
        print(question)
        
        try:
            answer = int(input('Enter answer: '))
        except ValueError:
            print("Answer should be an integer!")
            continue
        
        if answer == eval(question):
            print("Correct!")
            correct += 1
            question = f'{randint(1, 20)} {operands[randint(0, len(operands) - 1)]} {randint(1, 20)}'
        else:
            print("Incorrect! Please try again: ")

    end_time = f'{time.time() - start_time:.2f}'

    print(f'You completed {number_of_questions} in {end_time}s!')

timed_math_game(3)