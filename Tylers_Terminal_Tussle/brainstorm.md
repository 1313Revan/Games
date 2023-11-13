# TTT Brainstorming
<br></br>

### The Player Class
1. Health
2. Armor
    - A stat to compare an attack's Armor Pierce against
3. Stamina
    - Determines what actions you can take on your turn
4. Moveset
    - Your set of attacks and abilities
5. Block Chance
    - The dice roll to see if you negate an attack
6. Inventory<br></br>

### The Gameplay
- Two local players are pitted against each other and fight to see who can defeat the other first. They will manage their stamina in order to use attacks against the other player to inflict damage, or to use abilities that will heal themselves, stun the other player, increase a stat, etc.
- Each player will choose a class for themselves that will determine their health, armor and moveset.
- The players will also choose an item at the start of each round from a list of three randomly picked items. Items can heal, increase stats or effects of an attack, etc.
- Each match will consist of three rounds in which the players go through the item phase and then move to the action phase, where they will perform their turns against each other.
- Once a player has reduced their opponent's health to zero, the match ends and the remaining player is the winner.<br></br>

## The Code
#### How will I code all of this?
The gameplay will be done within the **player class**. It will have each line of code needed to make the gameplay function properly.

The scripting will be organized with a dedicated **"script" class** for non-gameplay moments such as the intro text and match ending.

Comments will also be pasted everywhere to give me a quick reference for each method or part of the script. This is just to *keep me sane*.<br></br>

## Brainstorming and Notes
#### The Action Phase
- placeholder