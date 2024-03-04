# A terminal-based Hangman game I made while taking a Python course
# Author: Revan

import random
import hm_art as art
from hm_list import wordlist
from os import system


# intro text
print('\n****************************************')
print(art.logo)
print('\nWelcome to the HANGMAN terminal game!\n')
print('\n****************************************\n')
print('What would you like to do?')
print('\n1. Start\n2. Exit\n')

# menu options
menu_choice = input('>> ').lower()
if menu_choice == 'exit' or menu_choice == '2':
    print('\nGoodbye!')
    exit()
elif menu_choice == 'start' or menu_choice == '1':
    system('clear')
    pass
else:
    print('Input error!')

# word is chosen
word = random.choice(wordlist)
display = ['_' for letter in word]

# game variables
game_end = False
won = False
lives = 6
# game loop
while not game_end:
    print('\n****************************************\n')
    print(art.stages[lives])
    print('\n',display,'\n')
    print('\n****************************************\n')
    # user guesses
    print('\nWhat letter would you like to guess?\n')
    guess = input('>> ').lower()
    system('clear')
    # check if guess already made
    if guess in display:
        print('\nYou\'ve already revealed this letter.\n')
    # check if guess is correct
    for position in range(len(word)):
        letter = word[position]
        if guess == letter:
            # update display
            display[position] = letter
    # if guess is wrong, reduce lives
    if guess not in word:
        lives -= 1
    # exit loop if all letters guessed or all lives lost
    if '_' not in display or lives == 0:
        game_end = True
        # determine if player won
        if lives > 0:
            won = True

if won:
    print('\n****************************************')
    print(f'\nYou guessed {word}!')
    print('\nYou win!\n')
    print('****************************************\n')
else:
    print('\n****************************************')
    print(art.stages[lives])
    print('You lost.\n')
    print(f'The word was {word}.\n')
    print('****************************************\n')
