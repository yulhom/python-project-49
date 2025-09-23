import random

import prompt

MIN_GENERATOR_NUM = 1

MAX_GENERATOR_NUM = 100

ATTEMPTS = 3

OPTIONS = ('+', '-', '*')


def calc_number(number1, number2, operation):
    
    if operation == '+': 
        result = number1 + number2
    elif operation == '-':
        result = number1 - number2
    elif operation == '*':
        result = number1 * number2
    return result   
    
        
def run_calc_game():
    
    print('Welcome to the Brain Games')
    name = prompt.string('May i have your name?')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    for i in range(ATTEMPTS):
        number1 = random.randint(MIN_GENERATOR_NUM, MAX_GENERATOR_NUM)
        number2 = random.randint(MIN_GENERATOR_NUM, MAX_GENERATOR_NUM)
        operation = random.choice(OPTIONS)
        print(f'Question: {number1} {operation} {number2}')
        answer = prompt.string('Your answer: ')
        real_answer = calc_number(number1, number2, operation) 
        
        if int(answer) == real_answer:
            print('Correct')
            
        else:
            print(f'{answer} is wrong answer ;(.', end=" ")
            print(f"Correct answer was '{real_answer}'.")
            print(f"Let's try again, {name}!")
            return
        
    print(f"Congratulations, {name}!")        