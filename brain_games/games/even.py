import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

MIN_GENERATOR_NUM = 1

MAX_GENERATOR_NUM = 100


def is_even(number):
      
    return number % 2 == 0


def format_boolean(val):
    
    if val:
        return 'yes'   
    return 'no'     


def generate_question_and_answer():
    
    number = random.randint(MIN_GENERATOR_NUM, MAX_GENERATOR_NUM)
    question = f'{number}'
    real_answer = is_even(number)   # True или False
    real_answer = format_boolean(real_answer)   # 'yes' или 'no'
        
    return question, real_answer
