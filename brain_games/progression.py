import random

import prompt

ATTEMPTS = 3


def run_progression():
    
    print('Welcome to the Brain Games')
    name = prompt.string('May i have your name?')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    for _ in range(ATTEMPTS):
        d = random.randint(-10, 10)
        progression_len = random.randint(5, 10)
        a1 = random.randint(1, 10)
        numbers = []
        for i in range(progression_len): 
            an = a1 + i * d
            numbers.append(an)
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