import random

import prompt

MIN_GENERATOR_NUM = 1

MAX_GENERATOR_NUM = 100

ATTEMPTS = 3


def is_even(number):
      
    return number % 2 == 0


def format_boolean(val):
    
    if val:
        return 'yes'   
    return 'no'     


def run_even_game():
    
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(ATTEMPTS): 
        number = random.randint(MIN_GENERATOR_NUM, MAX_GENERATOR_NUM)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')  # 'yes'
        real_answer = is_even(number)   # True или False
        real_answer = format_boolean(real_answer)   # 'yes' или 'no'
        
        if answer == real_answer:
            print('Correct!')
          
        else:
            print(f"'{answer}' is wrong answer ;(. ", end=" ")
            print(f"Correct answer was '{real_answer}'.")
            print(f"Let's try again, {name}")
            return
                 
    print(f'Congratulations, {name}') 
