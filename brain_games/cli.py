import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May i have your name?")
    print(f"Hello, {name}!")