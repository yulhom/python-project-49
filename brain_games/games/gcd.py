import random

MIN_GENERATOR_NUM = 1

MAX_GENERATOR_NUM = 100

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd_number(a, b):
    
    if b == 0:
        return a
    r = a % b
    while b != 0:
        r = a % b
        a, b = b, r   
    return a 


def generate_question_and_answer():
    
    number1 = random.randint(MIN_GENERATOR_NUM, MAX_GENERATOR_NUM)
    number2 = random.randint(MIN_GENERATOR_NUM, MAX_GENERATOR_NUM)
    question = f'{number1} {number2}'
    real_answer = gcd_number(number1, number2)
        
    return question, str(real_answer)