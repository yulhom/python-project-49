import random

import prompt

MIN_GENERATOR_NUM = 1

MAX_GENERATOR_NUM = 100

ATTEMPTS = 3


def gcd_number(a, b):
    
    if b == 0:
        return a
    r = a % b
    while b != 0:
        r = a % b
        a, b = b, r   
    return a 


def run_gcd_game():
    
    print('Welcome to the Brain Games')
    name = prompt.string('May i have your name?')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    for i in range(ATTEMPTS):
        number1 = random.randint(MIN_GENERATOR_NUM, MAX_GENERATOR_NUM)
        number2 = random.randint(MIN_GENERATOR_NUM, MAX_GENERATOR_NUM)
        print(f'Question: {number1} {number2}')
        answer = prompt.string('Your answer: ')
        real_answer = gcd_number(number1, number2)
        
        if int(answer) == real_answer:
            print('Correct')
            
        else:
            print(f'{answer} is wrong answer ;(.', end=" ")
            print(f"Correct answer was '{real_answer}'.")
            print(f"Let's try again, {name}!")
            return
        
    print(f"Congratulations, {name}!")