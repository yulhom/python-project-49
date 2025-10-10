import random

import prompt

MIN_GENERATOR_NUM = 1

MAX_GENERATOR_NUM = 100

ATTEMPTS = 3


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


def run_prime_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for _ in range(ATTEMPTS):
        number = random.randint(MIN_GENERATOR_NUM, MAX_GENERATOR_NUM)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        real_answer = format_boolean(prime(number))

        if answer == real_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(.", end=' ')
            print(f"Correct answer was '{real_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')