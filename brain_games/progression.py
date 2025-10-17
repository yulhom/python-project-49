import random

import prompt

ATTEMPTS = 3

MIN_GENERATION_INDEX = -10

MAX_GENERATION_INDEX = 10

MIN_GENERATION_LEN = 5

MAX_GENERATION_LEN = 10

MIN_GENERATION_NUM = 1

MAX_GENERATION_NUM = 10


def progression_numbers(a1, d, progression_len):
    
    numbers = []
    for i in range(progression_len):
        an = a1 + i * d
        numbers.append(an)
    return numbers


def run_progression():
    
    print('Welcome to the Brain Games')
    name = prompt.string('May i have your name?')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    for _ in range(ATTEMPTS):
        
        d = random.randint(MIN_GENERATION_INDEX, MAX_GENERATION_INDEX)
        progression_len = random.randint(MIN_GENERATION_LEN, MAX_GENERATION_LEN)
        a1 = random.randint(MIN_GENERATION_NUM, MAX_GENERATION_NUM)
        numbers = progression_numbers(a1, d, progression_len)
        skip_idx = random.randint(0, progression_len - 1)
        real_answer = numbers[skip_idx]
        numbers[skip_idx] = '..'
        result = " ".join(map(str, numbers))
        print(f'Question: {result}')
        answer = prompt.string('Your answer: ')
        
        if int(answer) == real_answer:
            print('Correct')
            
        else:
            print(f'{answer} is wrong answer ;(.', end=" ")
            print(f"Correct answer was '{real_answer}'.")
            print(f"Let's try again, {name}!")
            return
        
    print(f"Congratulations, {name}!")