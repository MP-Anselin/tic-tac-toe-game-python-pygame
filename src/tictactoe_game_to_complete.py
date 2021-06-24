from pygame.locals import *
from algorithm.tictactoeAlgorithm import *

# initialize global variables
XO = 'x'  # <-- Variable to know which player are playing
winner = None  # <-- Variable to know who is the winner 
draw = False  # <-- Variable to know if the game is a draw
width = 400  # <-- Variable to know set the width of the map
height = 400  # <-- Variable to know set the height of the map


# TTT ==> map
# posy and posx are the position on x and y of the cursor

def drawXO(row, col):
    global TTT, XO, posy, posx

    # __________________________________________________________________________________
    # Figure out the position in the axe of row.
    # Complete the three point below. If the "row" is equal to the number "1" so "posx = 30".
    # if ...
    # ...
    # Complete the three point below. Else if "row" is equal to the number "2" so "posx = width / 3 + 30".
    # elif ...
    # ...
    # Complete the three point below. Else if "row" is equal to the number "3" so "posx = width / 3 * 2 + 30".
    # elif ...
    # ...

    # __________________________________________________________________________________
    # Figure out the position in the axe of col.
    # Complete the three point below. If the "col" is equal to the number "1" so "posy = 30".
    # if ...
    # ...
    # Complete the three point below. Else if "col" is equal to the number "2" so "posy = height / 3 + 30".
    # elif ...
    # ...
    # Complete the three point below. Else if "col" is equal to the number "3" so "posy = height / 3 * 2 + 30".
    # elif ...
    # ...

    TTT[row - 1][col - 1] = XO  # We put the varaible at the place coordinates "row" and "col" on the map
    # if the player "X" or "O" finish to play we change the content of the variable XO by the value "x" or "o"
    if XO == 'x':
        screen.blit(x_img, (posy, posx))
        XO = 'o'
    else:
        screen.blit(o_img, (posy, posx))
        XO = 'x'
    pg.display.update()  # we update the posting


def userClick(winner, draw):
    # get coordinates of mouse click, through pygame
    x, y = pg.mouse.get_pos()

    # get column of mouse click (1-3) (3 number the case on the axe x them number the axe y )
    # __________________________________________________________________________________
    # Figure out the position of the mouse on the map, axe of x (col).
    # Complete the three point below. If the variable "x" is inferior to the number "width / 3" so "col = 1".
    # if ...
    # ...
    # Complete the three point below. Else if the variable "x" is inferior to the number "width / 3 * 2" so "col = 2"..
    # elif ...
    # ...
    # Complete the three point below. Else if the variable "x" is inferior to the variable "width" so "col = 3".
    # elif ...
    # ...
    # Complete the three point below. Else "x" is not matching with previous check, so "col" variable will get the value "none".
    # else:
    # ...

    # __________________________________________________________________________________
    # Figure out the position of the mouse on the map, axe of y (row).
    # Complete the three point below. If the variable "y" is inferior to the number "height / 3" so "row = 1".
    # if ...
    # ...
    # Complete the three point below. Else if the variable "y" is inferior to the number "height / 3 * 2" so "row = 2"..
    # elif ...
    # ...
    # Complete the three point below. Else if the variable "y" is inferior to the variable "height" so "row = 3".
    # elif ...
    # ...
    # Complete the three point below. Else "y" is not matching with previous check, so "row" variable will get the value "none".
    # else:
    # ...
    # get row of mouse click (1-3)

    if row and col and TTT[row - 1][col - 1] is None:
        global XO
        # draw the x or o on screen
        drawXO(row, col)
        return check_win(TTT, winner, draw, XO)


def reset_game():
    global winner, XO, draw
    time.sleep(2)  # sleep to make the program in pause, for 2 seconds

    # Complete the three point below. If we reset the game what should be the value of XO variable ?
    # XO = ..

    # Complete the three point below. If we reset the game what should be the value of XO draw ?
    # draw = ...

    game_opening(draw, winner, XO)

    # Complete the three point below. If we reset the game what should be the value of XO variable ?
    # winner = ...

    return [[None] * 3, [None] * 3, [None] * 3]  # We reset the map as the beginning.


game_opening(draw, winner, XO)

# run the game loop forever
while True:
    for event in pg.event.get():
        # We check if the type of the event is equal to QUIT, if the user want to close the windows
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        # We check ig the type of the event is equal to MOUSEBUTTONDOWN, means the user has presse on the mouse, and
        # we check what we have to do in function of the position of the mouse.
        elif event.type == MOUSEBUTTONDOWN:
            # the user clicked; place an X or O
            res = userClick(winner, draw)
            winner = res[0]
            draw = res[1]
            TTT = res[2]
            # In the case the variable draw or winner is not undefine, means theg game end up in this case we reset the game
            if winner or draw:
                TTT = reset_game()
    pg.display.update()
    CLOCK.tick(fps)
