from brain_games.engine import run
from brain_games.games.prime import DESCRIPTION, generate_question_and_answer


def main():  
    run(DESCRIPTION, generate_question_and_answer)
    
    
if __name__ == "__main__":
    main()