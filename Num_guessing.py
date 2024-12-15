from random import randint
from art12 import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(user_guess, actual_answer,turns):
    if user_guess > actual_answer:
        print("Too high.")
        return turns -1
    elif user_guess <actual_answer:
        print("Too low.")
        return turns -1
    else:
        print(f"You got it! The answer was {actual_answer}")


def set_difficulty():
    level = input("Choose the difficulty level 'easy' or 'hard'. ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    
def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("Iam thinking a number between 1 and 100.")
    answer = randint(1,100)
    print(f"Pssst. The correct answer is {answer}")

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))

        turns = check_answer(guess,answer,turns)

        if turns == 0:
            print("You've run out of guesses. You Lose!")
            return
        elif guess != answer:
            print("Guess again.")
game()