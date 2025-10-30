import random

from brain_games.boolean import format_boolean

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

MIN_GENERATOR_NUM = 1

MAX_GENERATOR_NUM = 100


def is_even(number):
      
    return number % 2 == 0    


def generate_question_and_answer():
    
    number = random.randint(MIN_GENERATOR_NUM, MAX_GENERATOR_NUM)
    question = f'{number}'
    real_answer = is_even(number)   # True или False
    real_answer = format_boolean(real_answer)   # 'yes' или 'no'
        
    return question, real_answer
