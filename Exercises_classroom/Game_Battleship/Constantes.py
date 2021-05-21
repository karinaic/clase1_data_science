

## Here's where we will put all the variables we're going to use during the game: welcome messages, instructions, ship sizes, etc.
##4 boats 2x1, 3b 3x1, 2b 4x1, 1b 5x1.
#I also created the message dictionary in Json format.

MESSAGES = {
    "introduction": " **** Welcome to Battleship**** \
        \n Here's your fleet: \
        \n 1 carrier (5x1) \
        \n 2 Battleships (4x1) \
        \n 3 Frigates (3x1) \
        \n 2 Submarines (2x1) \
        \n 2 Destroyers (2x2)",

    "Rules":" Below we explain the rules of the game: \
        \n Place each ship in any horizontal or vertical position but not diagonally \
        \n Do not place the ships so that they overlap another ship or the edge of the grid \
        \n You cannot change the position of the ship once the game has started. ",

    "Hit": "You hit me, great shot!",
    "Miss": "Nice try, but you missed. Better luck next time!",
    "win" : "¡¡¡¡¡¡You WON!!!!! Great job!! CONGRATULATIONS",
    "lose": "You LOST, keep trying",
    "goodbye": "      GAME OVER\
        \n***See you soon***"
}

LIST_CHARACTERS = ['A','B','C','D','E','F','G','H','I','J'] #It is used to translate the position of the letter to the board index and draw the references on the interface

LIST_NUMBERS = [1,2,3,4,5,6,7,8,9,10] # It is used to translate the position of the number to the board index and draw the references on the interface

BOATS_TYPE = [(4, 2), (3, 3), (2, 4), (1, 5)] #saves a list of tuples with the length of the board and the number that has to be represented

BOAT_BOARD= "#"

WATER_BOARD = "~"

HIT_BOARD = "X"

MISS_BOARD = "Ø"
