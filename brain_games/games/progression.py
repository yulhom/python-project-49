import random

DESCRIPTION = 'What number is missing in the progression?'

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


def generate_question_and_answer():
           
    d = random.randint(MIN_GENERATION_INDEX, MAX_GENERATION_INDEX)
    progression_len = random.randint(MIN_GENERATION_LEN, MAX_GENERATION_LEN)
    a1 = random.randint(MIN_GENERATION_NUM, MAX_GENERATION_NUM)
    numbers = progression_numbers(a1, d, progression_len)
    skip_idx = random.randint(0, progression_len - 1)
    real_answer = numbers[skip_idx]
    numbers[skip_idx] = '..'
    result = " ".join(map(str, numbers))
    question = f'{result}'
    return question, str(real_answer)