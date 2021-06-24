from tictactoe_include import *
import time


def drawXO(row, col):
    global TTT, XO, posy, posx
    if row == 1:
        posx = 30
    if row == 2:
        posx = width / 3 + 30
    if row == 3:
        posx = width / 3 * 2 + 30

    if col == 1:
        posy = 30
    if col == 2:
        posy = height / 3 + 30
    if col == 3:
        posy = height / 3 * 2 + 30
    TTT[row - 1][col - 1] = XO
    if (XO == 'x'):
        screen.blit(x_img, (posy, posx))
        XO = 'o'
    else:
        screen.blit(o_img, (posy, posx))
        XO = 'x'
    pg.display.update()
    # print(posx,posy)
    # print(TTT)


def userClick():
    # get coordinates of mouse click
    x, y = pg.mouse.get_pos()

    # get column of mouse click (1-3)
    if (x < width / 3):
        col = 1
    elif (x < width / 3 * 2):
        col = 2
    elif (x < width):
        col = 3
    else:
        col = None

    # get row of mouse click (1-3)
    if (y < height / 3):
        row = 1
    elif (y < height / 3 * 2):
        row = 2
    elif (y < height):
        row = 3
    else:
        row = None
    # print(row,col)

    if (row and col and TTT[row - 1][col - 1] is None):
        global XO

        # draw the x or o on screen
        drawXO(row, col)
        check_win()


def reset_game():
    global TTT, winner, XO, draw
    time.sleep(3)
    XO = 'x'
    draw = False
    game_opening()
    winner = None
    TTT = [[None] * 3, [None] * 3, [None] * 3]


game_opening()

# run the game loop forever
while (True):
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            # the user clicked; place an X or O
            userClick()
            if (winner or draw):
                reset_game()

    pg.display.update()
    CLOCK.tick(fps)
