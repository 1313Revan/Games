# Tyler's Terminal Tussle Notes:
###### *(subject to updates, not final)*<br></br>

### Player Attributes
1. Health
2. Stamina
3. Armor
4. Block Chance
5. Moveset
6. Inventory<br></br>

## Game Cycle
1. Match begins
    * Players follow prompts
2. Round 1 starts
    1. Item phase
        * occurs only at round start
    2. Action phase
        * roll for turn
        * each attacks and defends to count a cycle
        * repeat x3
3. Round 2 starts
    * see round 1
4. Round 3 starts
    * see round 1
5. Match ends
    * If no player was defeated by match end, the player with the most health wins.<br></br>

## Round Cycle
### Item Phase
1. Players get to choose one item presented to them (at random) to add to their inventory.
2. Once both players have chosen, the round moves to the 'Action Phase'.
### Action Phase
1. Players roll for first turn.
2. Starting player selects a choice:
    * Attack
    * Use Item
    * Regen
* If 'attack':
    1. The attacking player chooses an available attack from their moveset.
        * Available attacks depend on player stamina and the attacks' stamina cost.
    2. A block roll is made to see if the attack lands against the defender.
        * Dice are rolled and the larger sum wins for the respective side.
        * If the defender wins, the block succeeds and the attack ends and continues to step three.
        * If the attacker wins, the attack hits and continues to the armor phase.
    3. An armor penetration roll is made to see how much damage the defender receives.
        * Each attack has an individual armor penetration stat. It's compared against the defender's armor stat and based on the table that will be presented in the rule book, that determines how many dice and what type of dice are rolled to determine the amount of damage inflicted to the defender.
    4. The turn ends and moves to the next player.
* If 'use item':
    1. Player chooses what item to use.
    2. The item's effect is applied to the player.
    3. The turn ends and moves to the next player.
* If 'regen':
    1. Player's block chance is increased to 2D6 from the standard 1D6.
    2. A chunk of stamina is regenerated instantly.
3. Next player begins their turn and makes the same choices.
4. Repeat three times.<br></br>

## Match End
Once a player wins by reducing the other's health to zero, or by more remaining health at match's end, the game will congratulate the winner and prompt the players to vote for a choice of rematching or exiting the game.
* Any votes for 'exit' will exit the script completely and force the players to execute the game script again, losing player names & win count.