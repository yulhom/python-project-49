#!/usr/bin/env python3

from brain_games.engine import run
from brain_games.games.calc import DESCRIPTION, generate_question_and_answer


def main():
    run(DESCRIPTION, generate_question_and_answer)
    
    
if __name__ == "__main__":
    main()