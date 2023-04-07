# This project will be a single-player, text-based adventure that's played in the terminal.
# It will be played by displaying a message in the terminal to the player and they'll respond with their input in the terminal.
# It will be a dungeon crawler adventure. You'll start by waking up in a random dark room with no knowledge of how you got there. From there, the adventure will begin.

from os import getloadavg


actions_start = ["pick up the stick", "go to the door", "look around"]
actions_lit = ["look around", "go to the door", "rest on a nearby box"]
actions_cross = ["continue ahead", "go through the left door", "go through the right door"]
actions_fight = ["fight", "flee"]

armor = False
old_knife = False
sword = False
cafe_explore = False


def return_start():
    user_input = ""
    print("What do you do?")
    while user_input not in actions_start:
        print("Actions: 'look around', 'go to the door', 'pick up the stick'")
        user_input = input("Enter action: ")
        if user_input == actions_start[0]:
            grab_stick()
        elif user_input == actions_start[1]:
            door_unlit()
        elif user_input == actions_start[2]:
            look_unlit()
        else:
            print("\nPlease input a valid action.\n")

def intro_scene():
    user_input = ""
    print("\nYou awaken in a dark, cold room. You can barely make anything out except what looks like a stick next to where you awoke, and the silhouette of a door ahead of you.\n")
    print("What do you do?")
    while user_input not in actions_start:
        print("Actions: 'look around', 'go to the door', 'pick up the stick'")
        user_input = input("Enter action: ")
        if user_input == actions_start[0]:
            grab_stick()
        elif user_input == actions_start[1]:
            door_unlit()
        elif user_input == actions_start[2]:
            look_unlit()
        else:
            print("\nPlease input a valid action.\n")

def continue_story():
    # STORY CONTINUE

def cross_roads_return():
    user_input = ""
    actions = ["continue ahead", "check other door"]
    print("What do you do?")
    while user_input not in actions:
        print("Actions: 'continue ahead', 'check other door'")
        user_input = input("Enter action: ")
        if user_input == actions[0]:
            continue_story()
        elif user_input == actions[1] and cafe_explore == False:
            actions_monster = ["fight", "flight"]
            input_answer = ""
            print("\nGrasping the handle, you hear a faint noise from behind the door. Taking a second to listen further yields no result. As you begin opening the door, a man slams through it, knocking you to the floor.")
            print("Directing your gaze to him you notice that is no man, but an emaciated husk of one, its skin dark and necrotic. Eyes burning like coals. You notice it's wielding a blade, bloodied and old.")
            print("The creature whips its gaze to you, lying on the floor. It rears its sword and lunges towards you...\n")
            while input_answer not in actions_monster:
                print("Quickly! 'fight' or 'flight'")
                input_answer = input("Enter choice: ")
                if input_answer == actions_monster[0] and old_knife == True:
                    print("\nRolling out of the way of the creature's attack and jumping to your feet, you rip that old knife from your belt. Looks like you'll have to use it already!")
                    print("The creature spins around to face you, swinging its sword at you. Stepping back out of the way, you bring the knife up and lunge at the creature, plunging the knife into its eye socket.")
                    print("As you pull on the knife to remove it, the handle breaks from the blade. The creature stumbles around for a moment before falling to the floor, motionless.")
                    print("It's time you were on your way.")
                    global old_knife
                    old_knife = False
                    continue_story()
                elif input_answer == actions_monster[0] and old_knife == False:
                    print("\nRolling out of the way, the creature misses you. You jump to your feet and throw a kick into its body, sending it stumbling into the wall. Regaining what 'balance' it has, it swipes its arm at you.")
                    print("You prepare another attack as the creature brings its blade into the air above it, forcing you to dodge instead.")
                    print("As you throw a punch into the left of its jaw, it stands unphased and slams its arm into the side of your head, connecting bone to skull and sending your face into the wall as well.")
                    print("Disoriented and head throbbing, a sharp pain begins radiating through your abdomen. Regaining focus, you notice the creatures sword embedded in your stomach just as it pulls it out.")
                    print("Blood flows out of the wound in a torrent. You slide down the wall in shock as the creature grips your head with its bony hand, ripping your head out of the way so it can plunge its sword through your neck and into your heart...\n")
                    exit()
                elif input_answer == actions_monster[1]:
                    print("\nYou spring to your feet and barely dodge the creature's sword. You try to take this moment to make a run for it down the hallway, but feel a sharp, stinging pain appear in your lower back.")
                    print("Falling to the floor once again, you panickedly scurry to get to your feet but notice you can barely move your legs. The creature moves closer, sword in hand, plunging it through your back and through your heart...\n")
                    exit()
                else:
                    print("\nPlease input a valid action.\n")
        elif user_input == actions[1] and cafe_explore == True:
            print("\nYou notice the door was left creaked open upon returning to it, but you could've sworn it was closed originally. Reaching for the handle, you pull it open slowly.")
            print("Peering behind the door, it appears to be a naught but a storage closet. Calling it a room would be generous. Seeing nothing of interest, you decide to carry on down the hall.\n")
            continue_story()
        else:
            print("\nPlease input a valid action.\n")

def cross_roads():
    user_input = ""
    print("\nYou move through the doorway and see a dark hallway ahead of you. Moving through it with nothing but your torch to light the way, you eventually come to an intersection.")
    print("Ahead of you, the hallway continues. To the left and right, doors.\n")
    print("What do you do?")
    while user_input not in actions_cross:
        print("Actions: 'continue ahead', 'go through the left door', 'go through the right door'")
        user_input = input("Enter action: ")
        if user_input == actions_cross[0]:
            continue_story()
        elif user_input == actions_cross[1]:
            user_input_left = ""
            actions_left = ["explore the room", "inspect the bodies", "leave"]
            print("\nYou open the door to find a small cafeteria full of corpses, each within a pool of blood. Maybe it's best if you don't stay here too long.\n")
            print("What do you do?")
            while user_input_left not in actions_left:
                print("Actions: 'exlore the room', 'inspect the bodies', 'leave'")
                user_input_left = input("Enter action: ")
                if user_input_left == actions_left[0]:
                    user_input_sword = ""
                    sword_answer = ["yes", "no"]
                    print("\nYou begin moving through the room, stepping over bodies. You notice these corpses haven't been here very long. Moving your way towards the main counter, you step behind and search around.")
                    print("There appears to be a small sword set on one of the shelves below.\n")
                    print("Do you take it?")
                    while user_input_sword not in sword_answer:
                        print("'yes' or 'no'")
                        user_input_sword = input("Enter choice: ")
                        if user_input_sword == sword_answer[0]:
                            print("\nYou grab the sword and slide it into your belt. This could come in handy.")
                            print("You move your way back to the front of the room and into the hallway, no longer wishing to be around all those corpses.\n")
                            global sword
                            sword = True
                            cross_roads_return()
                        elif user_input_sword == sword_answer[1]:
                            print("\nYou leave the sword and move back into the hallway, not finding anything else of interest.\n")
                            cross_roads_return()
                        else:
                            print("\nPlease input a valid action.\n")
                    global cafe_explore
                    cafe_explore = True
                elif user_input_left == actions_left[1]:
                    user_input_left2 = ""
                    print("\nMoving to one of the corpses, you kneel beside it. Inspecting the body reveals large slashes diagonally along the chest.")
                    print("Moving to another corpse reveals stab wounds through the abdomen. Another, a large, splitting gash along the face.\n")
                    print("As you wonder who could've done this, a gutteral shriek rips your attention to the room's entrance.")
                    print("Standing in the doorway...an emaciated husk of a man, its skin dark and necrotic. Eyes burning like coals. In its hand drips a bloodied blade.")
                    print("Lunging at you, sword in hand, it smashes the it down toward you. Quickly you throw yourself aside before you end up like the rest.")
                    print("Clumsily, the creature regains its ever-wavering balance and whips its gaze to you lying on the floor...\n")
                    while user_input_left2 not in actions_fight:
                        print("Quickly! 'fight' or 'flight'")
                        user_input_left2 = input("Enter choice: ")
                        if user_input_left2 == actions_fight[0] and old_knife == True:
                            print("\nSpringing to your feet, you scan for a weapon. Remembering the old knife you found, you pull it out and prepare yourself.")
                            print("The creature shambles toward you with sword in hand, rearing for an attack. Dodging to the side, you jam the old knife into the creature's throat!")
                            print("Pulling back, the knife breaks from the handle. Black fluid leaks from the creature's wound and mouth. As it stumbles for a minute, it finally crashes through a table, unmoving.\n")
                            print("You walk out of the room, noticing the other door now sits open. Perhaps it's best to move out of this area.\n")
                            global old_knife
                            old_knife = False
                            continue_story()
                        elif user_input_left2 == actions_fight[0] and old_knife == False:
                            print("\nThrowing yourself to your feet, you anxiously scan around for a weapon. With no better options and the creature right on you, you throw yourself to a table with a dinner knife.")
                            print("Upon grabbing the knife, the creature's dulled blade finds its way down upon your forearm, too old and blunt to cut completely through.")
                            print("As the blade retreats, blood pouring from your near-severed arm, pain floods into focus almost instantly. The creature rears its blade once more, striking your neck...\n")
                            exit()
                        elif user_input_left2 == actions_fight[1]:
                            print("\nScrambling to your feet, you sprint for the room's entrance hoping the creature isn't close behind. Reaching the door you kick a few chairs into the creature's path, tripping it.")
                            print("Slamming the door shut, you sprint down the hallway with no desire to wait around for the creature.\n")
                            continue_story()
                        else:
                            print("\nPlease input a valid action.\n")
                elif user_input_left == actions_left[2]:
                    cross_roads_return()
                else:
                    print("\nPlease input a valid action.\n")
        elif user_input == actions_cross[2]:
            # Right Door option. Copy & Paste the crossroad return function output to this.
        else:
            print("\nPlease input a valid action.\n")

def grab_stick():
    user_input = ""
    print("\nYou pick up the stick and realize it's an unlit torch. You faintly remember having some matches in your back pocket.")
    print("Taking the matches out, you light one, pressing it to the end of the torch. The torch lights the room in an orange glow.\n")
    print("What do you do?")
    while user_input not in actions_lit:
        print("Actions: 'look around', 'go to the door', 'rest on a nearby box'")
        user_input = input("Enter action: ")
        if user_input == actions_lit[0]:
            look_lit()
        elif user_input == actions_lit[1]:
            door_lit()
        elif user_input == actions_lit[2]:
            rest_box()
        else:
            print("\nPlease input a valid action.\n")
            
def return_lit():
    user_input = ""
    print("What do you do?")
    while user_input not in actions_lit:
        print("Actions: 'look around', 'go to the door', 'rest on a nearby box'")
        user_input = input("Enter action: ")
        if user_input == actions_lit[0]:
            look_lit()
        elif user_input == actions_lit[1]:
            door_lit()
        elif user_input == actions_lit[2]:
            rest_box()
        else:
            print("\nPlease input a valid action.\n")

def found_key():
    actions = ["go to the door", "look around some more"]
    user_input = ""
    print("What do you do?")
    while user_input not in actions:
        print("Actions: 'go to the door', 'look around some more'")
        user_input = input("Enter Action: ")
        if user_input == actions[0]:
            print("\nYou move to the door and try the key you found on it.")
            print("The key unlocked the door!\n")
            cross_roads()
        elif user_input == actions[1]:
            print("\nYou look around some more but you find nothing of interest.\n")
            found_key()
        else:
            print("\nPlease input a valid action.\n")



def look_lit():
    print("\nYou start searching around the room. Looking through one of the crates, you find a key. What could you use it for?\n")
    found_key()

def door_lit():
    print("\nYou make your way to the door and try to open it, but it's locked.\n")
    return_lit()
    
def rest_box():
    knife_answer = ["take it", "leave it"]
    user_answer = ""
    knife_actions = ["take the knife", "leave the knife", "kill yourself"]
    knife_input = ""
    print("\nYou move to a nearby box and take a seat. There's an old, rusty knife next to you.\n")
    while user_answer not in knife_answer:
        print("Take it or leave it?")
        user_answer = input("Enter answer: ")
        if user_answer == knife_answer[0]:
            print("\nYou grab the knife.")
            print("You can feel how old it is, like it's ready to fall apart at any moment.\n")
            print("What do you do with it?")
            while knife_input not in knife_actions:
                print("Actions: 'take the knife', 'leave the knife'")
                knife_input = input("Enter action: ")
                if knife_input == knife_actions[0]:
                    print("\nYou slot the knife under your belt and return to finding a way out of here.\n")
                    global old_knife
                    old_knife = True
                    return_lit()
                elif knife_input == knife_actions[1]:
                    print("\nYou set the knife down and get back to finding a way out of here.")
                    return_lit()
                elif knife_input == knife_actions[2]:
                    print("\nYou raise the rusty knife to your throat, unable to handle the situation you found yourself in. God forgive you...\n")
                    exit()
        elif user_answer == knife_answer[1]:
            print("\nYou sit on the crate and ponder your situation for a bit. Eventually you get back up and return to finding a way out.\n")
            return_lit()
        else:
            print("\nPlease input a valid action.\n")


def door_unlit():
    print("\nYou shuffle your way through the dark room, unable to see where your foot falls each time. Slowly you make it to the other side of the room and see the door more clearly.")
    print("Trying to open it however, you realize it's locked. Maybe you could find a key or something to pry the door open but, not in this darkness.\n")
    return_start()
    
def look_unlit():
    print("\nYou try looking around the room a bit but it's too dark to see anything other than shapes and darkness.\n")
    return_start()


if __name__ == "__main__":
    while True:
        print("Welcome to Tyler's Text Adventure!")
        print("In this adventure you will explore a dungeon and search for a way to escape it.")
        print("Before we begin, let's start with naming your character: \n")
        name = input("Name: ")
        print("\nGood luck " + name.title() + ".")
        intro_scene()