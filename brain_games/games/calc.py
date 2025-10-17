import random

MIN_GENERATOR_NUM = 1

MAX_GENERATOR_NUM = 100

DESCRIPTION = 'What is the result of the expression?'

OPTIONS = ('+', '-', '*')   
    
        
def generate_question_and_answer():
       
    number1 = random.randint(MIN_GENERATOR_NUM, MAX_GENERATOR_NUM)
    number2 = random.randint(MIN_GENERATOR_NUM, MAX_GENERATOR_NUM)
    operation = random.choice(OPTIONS)
    question = (f'Question: {number1} {operation} {number2}')
    if operation == '+': 
        real_answer = number1 + number2
    elif operation == '-':
        real_answer = number1 - number2
    elif operation == '*':
        real_answer = number1 * number2
    return question, str(real_answer)      