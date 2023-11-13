#!/usr/bin/python3
import dice



# The class that moves the game forward (it helped me stay organized and not get overwhelmed)
class Script:

    # This will kick off the game after instancing each player variable.
    def Intro(self):
        print("Welcome to Tyler's Terminal Tussle!")
        print("Two players will fight to see who is the last one standing!\n")
        input("Press ENTER to begin\n")
        name1 = input("Player 1, please enter your name:\n").title()
        name2 = input("Player 2, please enter your name:\n").title()
        player_one.name = name1
        player_two.name = name2


# The player class and methods
class Player:
    stamina = 100
    inventory = [] # item dictionaries will be appended to this list
    block_chance = [] # this is a list so multiple "dice" can be applied to this stat

    def __init__(self):
        self.name = ""

    # This will assign the class-based stats to each player. This will run after the intro text.
    def ChooseClass(self):
        print(self.name + ", please choose your class:")
        print("Tank\nPaladin\nSorcerer\n")
        choice = input().lower()

        if choice == "tank":
            self.job = "tank"
            self.health = 100
            self.armor = 5
            self.moveset = [{"norm_atk": {}}] # CREATE MOVESET !!!

        elif choice == "paladin":
            self.job = "paladin"
            self.health = 100
            self.armor = 4
            self.moveset = [] # CREATE MOVESET !!!

        elif choice == "sorcerer":
            self.job = "sorcerer"
            self.health = 120
            self.armor = 3
            self.moveset = [] # CREATE MOVESET !!!
        else:
            print("Please choose one of the listed options.")
            self.ChooseClass()
        
        print("{name} has chosen the {job} class. Their stats are {health} health and {armor} armor!".format(name=self.name,job=self.job,health=self.health,armor=self.armor))

    # This prints your character's remaining health, remaining stamina and armor stat.
    def Stats(self):
        print("Health: " + self.health)
        print("Stamina: " + self.stamina + "\n")
        print("Armor: " + self.armor)

    # This will print the names, descriptions and stats of a class' attacks/abilities
    def MovesetInfo(self): # FINISH AFTER MOVESETS ARE MADE !!!
        pass



# SCRIPT #
###############################
# Instancing the variables
script = Script()
player_one = Player()
player_two = Player()

# Intro text and prompts
script.Intro()

# Players choose their classes
player_one.ChooseClass()
player_two.ChooseClass()

# The match begins


###############################


# NOTES #
#########
# - Movesets need to be devised next,
#   then finish the 'MovesetInfo' class method,
#   after that, moving the script forward should bring the next task up.
