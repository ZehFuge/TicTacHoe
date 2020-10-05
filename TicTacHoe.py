"""
Problem 1:
    Tiles are only changed, if the mouse is moving and getting pressed.
    Otherwise it won't change anything

Problem 2: Done
    Already set tileStates can be overwritten.

    ### Solution ###
    An if-statement in the changeState() function checks, if the chosen tile is blank.
    If not, the function does nothing. The player state also doesn't change.
    ###   End    ###

Problem 3: Work in progress
    There is no win condition checker at the moment. Therefore, there is no end.

    ### Solution ###
    The function winChecker() was created. It checks for the right tiles[index]["state"] order and declares a winner.
    True = cross wins
    False = Circle wins

    If someone wins, the game closes because of missing restart conditions. Those are part of
    the Problem 3.2
    ###   End    ###

    Problem 3.2:
    The winner isn't displayed and you can't restart the game if wanted.

    The biggest problem at the moment is the wrong tiles[]["state"] handling. The 5 is seen as a "False" value.
    Therefore a new isWinning variable is needed in the tiles dictionary. So for showing the showWin image,
    another argument is needed in the drawTiles() function
"""

import pygame
import pygame.event as GAME_EVENTS
import sys

# initialize pygame
pygame.init()

# set some screen info
windowWidth = 404
windowHeight = 404

window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("TicTacHoe")

# load pictures of tile states
blankTile = pygame.image.load("Images/blank.png")
crossTile = pygame.image.load("Images/cross.png")
circleTile = pygame.image.load("Images/circle.png")
winTile = pygame.image.load("Images/win.png")

# game info and variables
# set info for tiles
# tileStartingX, tileStartingY, tileState (None = blank, True = cross, False = circle, "win" = show win)
tiles = [{"x": 5, "y": 5, "state": None},  # Tile 1 from row 1
         {"x": 138, "y": 5, "state": None},  # Tile 2 from row 1
         {"x": 271, "y": 5, "state": None},  # Tile 3 from row 1

         {"x": 5, "y": 138, "state": None},  # Tile 4 from row 2
         {"x": 138, "y": 138, "state": None},  # Tile 5 from row 2
         {"x": 271, "y": 138, "state": None},  # Tile 6 from row 2

         {"x": 5, "y": 271, "state": None},  # Tile 7 from row 3
         {"x": 138, "y": 271, "state": None},  # Tile 8 from row 3
         {"x": 271, "y": 271, "state": None}, ]  # Tile 9 from row 3

# the tile is an square, meaning all sides are even
tileSize = 128

# this value decides, if a tile is filled with a cross or a circle
# this value only changes, after the current state is set to a tile
# this happens through the function "changeState()"
mouseState = True  # True = cross / False = circle
winner = None


def quitGame():
    pygame.quit()
    sys.exit()


def drawTiles():
    global tiles

    for index in range(0, 9):
        # if tile got the cross state
        if tiles[index]["state"]:
            window.blit(crossTile, (tiles[index]["x"], tiles[index]["y"]))

        # if tile got the circle state
        elif not tiles[index]["state"]:
            window.blit(circleTile, (tiles[index]["x"], tiles[index]["y"]))

        # if tile got whether cross nor circle state
        elif tiles[index]["state"] is None:
            window.blit(blankTile, (tiles[index]["x"], tiles[index]["y"]))

        # if tile is set to show win
        elif tiles[index]["state"] == "win":
            window.blit(winTile, (tiles[index]["x"], tiles[index]["y"]))

    pygame.display.update()
    return


def changeState():
    global tiles, mousePosition, mouseState, mouseX, mouseY

    # check if mouse collides with a tile
    # if it does and the mouse is pressed, change the state of the "collided" tile
    for index in range(0, 9):
        # mousePosition[0] = x axis
        # mousePosition[1] = y axis
        # check for mouse collision with every tile
        if tiles[index]["x"] <= mouseX < tiles[index]["x"] + tileSize:
            if tiles[index]["y"] <= mouseY < tiles[index]["y"] + tileSize:

                # check if tile is already filled
                if tiles[index]["state"] is None:
                    # change the state of a tile
                    # change tile to cross if current mouseState is cross
                    if mouseState:
                        tiles[index]["state"] = mouseState
                        print("Something happened in Cross State")
                        # change the mouseState after a change is done
                        mouseState = False

                    # change tile to circle if current mouseState is circle
                    elif not mouseState:
                        tiles[index]["state"] = mouseState
                        print("Something happened in Circle State")
                        # change the mouseState after a change is done
                        mouseState = True
    return


def winChecker():
    global tiles, winner

    # check for win conditions. Also set tileState to win condition if true
    # True = cross
    # False = circle
    # check rows for win condition
    if tiles[0]["state"] and tiles[1]["state"] and tiles[2]["state"]:
        winner = True
        tiles[0]["state"] = "win"
        tiles[1]["state"] = "win"
        tiles[2]["state"] = "win"
    elif not tiles[0]["state"] and tiles[1]["state"] and tiles[2]["state"]:
        winner = False
        tiles[0]["state"] = "win"
        tiles[1]["state"] = "win"
        tiles[2]["state"] = "win"
    if tiles[3]["state"] and tiles[4]["state"] and tiles[5]["state"]:
        winner = True
        tiles[3]["state"] = "win"
        tiles[4]["state"] = "win"
        tiles[5]["state"] = "win"
    elif not tiles[3]["state"] and tiles[4]["state"] and tiles[5]["state"]:
        winner = False
        tiles[3]["state"] = "win"
        tiles[4]["state"] = "win"
        tiles[5]["state"] = "win"
    if tiles[6]["state"] and tiles[7]["state"] and tiles[8]["state"]:
        winner = True
        tiles[6]["state"] = "win"
        tiles[7]["state"] = "win"
        tiles[8]["state"] = "win"
    elif not tiles[6]["state"] and tiles[7]["state"] and tiles[8]["state"]:
        winner = False
        tiles[6]["state"] = "win"
        tiles[7]["state"] = "win"
        tiles[8]["state"] = "win"

    # check columns for win condition
    if tiles[0]["state"] and tiles[3]["state"] and tiles[6]["state"]:
        winner = True
        tiles[0]["state"] = "win"
        tiles[3]["state"] = "win"
        tiles[6]["state"] = "win"
    elif not tiles[0]["state"] and tiles[3]["state"] and tiles[6]["state"]:
        winner = False
        tiles[0]["state"] = "win"
        tiles[3]["state"] = "win"
        tiles[6]["state"] = "win"
    if tiles[1]["state"] and tiles[4]["state"] and tiles[7]["state"]:
        winner = True
        tiles[1]["state"] = "win"
        tiles[4]["state"] = "win"
        tiles[7]["state"] = "win"
    elif not tiles[1]["state"] and tiles[4]["state"] and tiles[7]["state"]:
        winner = False
        tiles[1]["state"] = "win"
        tiles[4]["state"] = "win"
        tiles[7]["state"] = "win"
    if tiles[2]["state"] and tiles[5]["state"] and tiles[8]["state"]:
        winner = True
        tiles[2]["state"] = "win"
        tiles[5]["state"] = "win"
        tiles[8]["state"] = "win"
    elif not tiles[2]["state"] and tiles[5]["state"] and tiles[8]["state"]:
        winner = False
        tiles[2]["state"] = "win"
        tiles[5]["state"] = "win"
        tiles[8]["state"] = "win"

    # check cross for win condition
    if tiles[0]["state"] and tiles[4]["state"] and tiles[8]["state"]:
        winner = True
        tiles[0]["state"] = "win"
        tiles[4]["state"] = "win"
        tiles[8]["state"] = "win"
    elif not tiles[0]["state"] and tiles[4]["state"] and tiles[8]["state"]:
        winner = False
        tiles[0]["state"] = "win"
        tiles[4]["state"] = "win"
        tiles[8]["state"] = "win"
    if tiles[6]["state"] and tiles[4]["state"] and tiles[2]["state"]:
        winner = True
        tiles[6]["state"] = "win"
        tiles[4]["state"] = "win"
        tiles[2]["state"] = "win"
    elif not tiles[6]["state"] and tiles[4]["state"] and tiles[2]["state"]:
        winner = False
        tiles[6]["state"] = "win"
        tiles[4]["state"] = "win"
        tiles[2]["state"] = "win"


# pre declare variables for mouse position
mouseX = 0
mouseY = 0

# main loop
while winner is None:
    # draws the tiles by their state
    # (0=blank, 1=cross, 2=circle)
    drawTiles()

    # mousePosition[0] = x axis
    # mousePosition[1] = y axis
    mousePosition = pygame.mouse.get_pos()

    for event in GAME_EVENTS.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quitGame()

        # check if left mouse button got pressed
        # the event of change happens, if the user let go of the mouse button
        # otherwise it can cause problems, if the user keeps the mouse button pressed
        if pygame.mouse.get_pressed()[0]:
            # save the mouse position in the moment of press
            mouseX = pygame.mouse.get_pos()[0]
            mouseY = pygame.mouse.get_pos()[1]
            # change the state of the chosen tile
            changeState()

    winChecker()
    if winner or not winner:
        drawTiles()

    # updates the change on "window"
    pygame.display.update()
