import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

MIN_GENERATOR_NUM = 1

MAX_GENERATOR_NUM = 100


def prime(num):
    
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def format_boolean(val):
    if val:
        return 'yes'
    else:
        return 'no'


def generate_question_and_answer():
    
    number = random.randint(MIN_GENERATOR_NUM, MAX_GENERATOR_NUM)
    question = f'{number}'
    real_answer = format_boolean(prime(number))

    return question, real_answer