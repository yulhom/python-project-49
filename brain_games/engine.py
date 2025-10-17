import prompt

ATTEMPTS = 3   
   
        
def run(description, generate_question_and_answer):
    
    print('Welcome to the Brain Games')
    name = prompt.string('May i have your name? ')
    print(f'Hello, {name}!')
    print(description)
    for _ in range(ATTEMPTS):
        question, real_answer = generate_question_and_answer(
        )
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == real_answer:
            print('Correct')   
        else:
            print(f'{answer} is wrong answer ;(.', end=" ")
            print(f"Correct answer was '{real_answer}'.")
            print(f"Let's try again, {name}!")
            return
        
    print(f"Congratulations, {name}!")