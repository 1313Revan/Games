# This is a project from Angela Wu's 100 Days of Code Python bootcamp

import random
import art_vars


print('\nWelcome to the ROCK PAPER SCISSORS terminal game!\nYou\'ll be placed against the computer to see which of you comes out on top.\n')
print('\nMake your choice!\n')
print('1. Rock\n2. Paper\n3. Scissors\n')

player = input('>> ').lower()
if player == 'rock' or player == '1':
    p_choice = art_vars.rock
elif player == 'paper' or player == '2':
    p_choice = art_vars.paper
else:
    p_choice = art_vars.scissors

computer = random.randint(1,3)
if computer == 1:
    c_choice = art_vars.rock
elif computer == 2:
    c_choice = art_vars.paper
else:
    c_choice = art_vars.scissors

print('\n********************')
print('\nYou chose:\n',p_choice,'\n')
print('\nComputer chose:\n',c_choice)
print('\n********************')

if p_choice == art_vars.rock:
    if c_choice == art_vars.rock:
        print('\nDRAW\n')
    elif c_choice == art_vars.paper:
        print('\nYOU LOSE\n')
    else:
        print('\nYOU WIN\n')
elif p_choice == art_vars.paper:
    if c_choice == art_vars.rock:
        print('\nYOU WIN\n')
    elif c_choice == art_vars.paper:
        print('\nDRAW\n')
    else:
        print('\nYOU LOSE')
else:
    if c_choice == art_vars.rock:
        print('\nYOU LOSE')
    elif c_choice == art_vars.paper:
        print('\nYOU WIN\n')
    else:
        print('\nDRAW\n')