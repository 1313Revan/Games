# A terminal-based number guessing game I made while learning basic Python

# Author: Revan
# Date: 3/6/24

from random import randint


def difficulty():
    print("\nSelect your difficulty:")
    print("\n1. Easy\n2. Medium\n3. Hard\n")
    diff = input(">> ").lower()
    if diff == "1" or diff == "easy":
        tries = 15
    elif diff == "2" or diff == "medium":
        tries = 10
    elif diff == "3" or diff == "hard":
        tries = 5
    else:
        print("\nInvalid option.\n")
        difficulty()
    return tries

def game(difficulty_level):
    answer = randint(1,100)
    lives = difficulty_level
    print("\nI'm thinking of a number between 1 and 100.\nCan you guess it?\n")
    end = False
    while not end:
        print(f"Lives remaining: {lives}\n")
        guess = int(input(">> "))
        if guess == answer:
            end = True
        elif guess > answer:
            print("\nToo high!\n")
            lives -= 1
        elif guess < answer:
            print("\nToo low!\n")
            lives -= 1
    if lives > 0:
        print(f"\nThe answer was {answer}, good job!\n")
    elif lives == 0:
        print(f"\nSorry, you ran out of lives. The answer was {answer}.\n")
    print("\nWould you like to play again?\n")
    play_again = input(">> ").lower()
    if play_again == "yes" or play_again == "y":
        game(difficulty())
    else:
        print("\nGoodbye!\n")
        exit()

def menu():
    print("\nWelcome to NUMBER GUESS!\n")
    print("\nPlease select an option:")
    print("\n1. Start\n2. Quit\n")
    choice = input(">> ").lower()
    if choice == "1" or choice == "start":
        game(difficulty())
    elif choice == "2" or choice == "quit":
        print("\nGoodbye!\n")
        exit()
    else:
        print("\nInvalid option.\n")
        menu()


menu()
