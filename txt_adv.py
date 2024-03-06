# A short text adventure made as practice while I was taking a Python course
# Author: Revan

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print('Welcome to TREASURE ISLAND, a short, choice-based terminal game!\n')
print('Can you survive the adventure that awaits you?\n')
print('-------------------------------------------------------------------------------\n')

print('Let\'s begin with your name. What is it adventurer?\n')
p_name = input('\n>> ').title()
print(f'\nWelcome {p_name}! Please type your choice!\n')

print('1. Begin Story\n2. Exit Game\n')
menu_op = input('\n>> ').lower()
if menu_op == '1' or menu_op == 'begin story':
    print('\nYou\'ve awoken on a tropical island with no memory of how you arrived here. After some trekking along a path through the trees, you come across a split in the road.\nThe path to the left is dense with brush, and naught but leaves cover the right path.\n')
    print('\nWhich way do you go?\n1. Left\n2. Right\n')
    l_or_r = input('\n>> ').lower()

    if l_or_r == '1' or l_or_r == 'left':
        print('\nYou move through the path, pushing branch and bush alike out of your way for a while.\nFinally, you reach a river cutting through your path with no way around it.\n')
        print('\nWhat do you do?\n1. Swim across\n2. Wait')
        swim_wait = input('\n>> ').lower()
        if swim_wait == '2' or swim_wait == 'wait':
            print('\nTaking a seat on the dirt path, you wait for a couple hours, finding ways to occupy your time while you wait out the tide.\nOnce the water level has receded enough to walk through, you reach the other side of the river bank.')
            print('Continuing along the path, you eventually come to a temple with three doors presented to you.\n')
            print('Which do you go through?\n1. Red\n2. Yellow\n3. Blue')
            door_choice = input('\n>> ').lower()
            if door_choice == '2' or door_choice == 'yellow':
                print('\nThe doors open and you are presented with a glowing room of gold and other treasures.\n')
                print('\nYOU WON!\n')
                exit()
            elif door_choice == '1' or door_choice == 'red':
                print('\nYou move through the doors to a room with torches lining the walls and a large cylindrical spire in the middle, a dragon\'s face engraved on it staring at you.')
                print('The eyes suddenly light up red as the mouth opens with a stream of flames that engulf you\nGAME OVER\n')
                exit()
            else:
                print('\nThe doors open to a dark room, damp and cold. The doors slam behind you as you enter, leaving you in total darkness.')
                print('A shriek echoes through the room from an unknown creature, unlike any you\'ve heard before. It pounces onto you with no way to defend yourself.\nGAME OVER\n')
                exit()
        else:
            print('\nYou jump into the water blocking your path and attempt to swim to the other side, but the current is too strong! You can\'t get out.\nGAME OVER\n')
            exit()
    else:
        print('\nAs you walk along the path to the right, the ground below you gives way. You fall into a hole with no way out!\nGAME OVER')
        exit()
else:
    exit()
