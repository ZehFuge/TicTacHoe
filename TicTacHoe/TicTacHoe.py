"""
Problem 1.1: Done
    Already set tileStates can be overwritten.

    ### Solution ###
    An if-statement in the changeState() function checks, if the chosen tile is blank.
    If not, the function does nothing. The player state also doesn't change.
    ###   End    ###

Problem 2.1: Done
    There is no win condition checker at the moment. Therefore, there is no end.

    ### Solution ###
    The function winChecker() was created. It checks for the right tiles[index]["state"] order and declares a winner.
    True = cross wins
    False = Circle wins

    If someone wins, the game closes because of missing restart conditions. Those are part of
    the Problem 2.2
    ###   End    ###

    Problem 2.2: Done
    The winner isn't displayed and you can't restart the game if wanted.

    The biggest problem at the moment is the wrong tiles[]["state"] handling. The 5 is seen as a "False" value.
    Therefore a new isWinning variable is needed in the tiles dictionary. So for showing the showWin image,
    another argument is needed in the drawTiles() function

    ### Solution ###
    The tiles[] dictonary got another statement named win (default = False). After checking a true
    winning condition, the winning tiles are set as win = True. Therefore they can be displayed by crowns.
    The system waits for 1 second, so the users can realize who won.

    After that, the main loops condition is False and another loop inside the main loop starts.
    The graphical output is "Press "Space" to play again". If the user presses the space bar,
    all the game values are resetted and the game starts from beginning. This is done in the
    resetTiles() function. This function also sets winner to None again, so the main loop will
    continue running. If the user presses the ESC button, the game will close.
    ###   End    ###

Problem 3.1: Work in progress
    The game isn't counting the amount of wins for cross and circle

Problem 4.1: Done
    If the games ends as draw, nothing happens. The games needs to check itself, if every tile is filled
    and there is no winner. If the case is True, all tiles need to be reseted

    ### Solution ###
    After the winChecker() checks the win condition, the drawChecker checks if the game is set draw.
    Therefore a for loop loops from range(0, 9 (index for tiles dictonary)) and raises the setTileCounter
    += 1.
    If a tile is blank (state = None), setTileCounter wont rise.
    If setTileCounter reaches 9 (all tiles are filled and not blank) and the winner is still None,
    all tiles are reseted and the game will continue, until there is a winner.
    ###   End    ###
"""

import pygame
import pygame.event as GAME_EVENTS
import pygame.time as GAME_TIME
import sys

# initialize pygame
pygame.init()

# set some screen info
windowWidth = 404
windowHeight = 537

window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("TicTacHoe")

# load pictures of tile states
blankTile = pygame.image.load("Images/blank.png")
crossTile = pygame.image.load("Images/cross.png")
circleTile = pygame.image.load("Images/circle.png")
winTile = pygame.image.load("Images/win.png")
replayTile = pygame.image.load("Images/replay.png")
winX = pygame.image.load("Images/winX.png")
winY = pygame.image.load("Images/winY.png")

# game info and variables
# set info for tiles
# tileStartingX, tileStartingY,
# tileState (None = blank, True = cross, False = circle)
# win is set, if a row/column/cross win condition is given
tiles = [{"x" : 5, "y" : 5, "state" : None, "win" : False},  # Tile 1 from row 1
         {"x": 138, "y": 5, "state": None, "win" : False},  # Tile 2 from row 1
         {"x": 271, "y": 5, "state": None, "win" : False},  # Tile 3 from row 1

         {"x": 5, "y": 138, "state": None, "win" : False},  # Tile 4 from row 2
         {"x": 138, "y": 138, "state": None, "win" : False},  # Tile 5 from row 2
         {"x": 271, "y": 138, "state": None, "win" : False},  # Tile 6 from row 2

         {"x": 5, "y": 271, "state": None, "win" : False},  # Tile 7 from row 3
         {"x": 138, "y": 271, "state": None, "win" : False},  # Tile 8 from row 3
         {"x": 271, "y": 271, "state": None, "win" : False}, ]  # Tile 9 from row 3

# the tile is an square, meaning all sides are even
tileSize = 128

# this value decides, if a tile is filled with a cross or a circle
# this value only changes, after the current state is set to a tile
# this happens through the function "changeState()"
mouseState = True  # True = cross / False = circle
winner = None

# pre declare variables for mouse position
mouseX = 0
mouseY = 0


def quitGame():
    pygame.quit()
    sys.exit()


def drawTiles():
    global tiles

    for index in range(0, 9):
        # print(tiles[index]["state"], " ", tiles[index]["win"])

        # if tile got the cross state
        if tiles[index]["state"] \
                and tiles[index]["state"] is not None \
                and not tiles[index]["win"]:
            window.blit(crossTile, (tiles[index]["x"], tiles[index]["y"]))
            # print("Cross printed")

        # if tile got the circle state
        if not tiles[index]["state"] \
                and tiles[index]["state"] is not None \
                and not tiles[index]["win"]:
            window.blit(circleTile, (tiles[index]["x"], tiles[index]["y"]))
            # print("Circle printed")

        # if tile got whether cross nor circle state
        if tiles[index]["state"] is None \
                and tiles[index]["state"] is not True \
                and tiles[index]["state"] is not False \
                and not tiles[index]["win"]:
            window.blit(blankTile, (tiles[index]["x"], tiles[index]["y"]))
            # print("Blank printed")

        # if tile is set to show win
        if tiles[index]["win"] \
                and [tiles[index]["win"] is not None]:
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
                        # the print statement is just for checking events
                        # print("Something happened in Cross State")
                        # change the mouseState after a change is done
                        mouseState = False

                    # change tile to circle if current mouseState is circle
                    elif not mouseState:
                        tiles[index]["state"] = mouseState
                        # the print statement is just for checking events
                        # print("Something happened in Circle State")
                        # change the mouseState after a change is done
                        mouseState = True
    return


def winChecker():
    global tiles, winner

    # check for win conditions. Also set tileState to win condition if true
    # True = cross
    # False = circle
    # check rows for win condition
    if tiles[0]["state"] and tiles[1]["state"] and tiles[2]["state"]\
            and tiles[0]["state"] is not None \
            and tiles[1]["state"] is not None \
            and tiles[2]["state"] is not None:
        winner = True
        tiles[0]["win"] = True
        tiles[1]["win"] = True
        tiles[2]["win"] = True
    if not tiles[0]["state"] and not tiles[1]["state"] and not tiles[2]["state"] \
            and tiles[0]["state"] is not None \
            and tiles[1]["state"] is not None \
            and tiles[2]["state"] is not None:
        winner = False
        tiles[0]["win"] = True
        tiles[1]["win"] = True
        tiles[2]["win"] = True
    if tiles[3]["state"] and tiles[4]["state"] and tiles[5]["state"] \
            and tiles[3]["state"] is not None \
            and tiles[4]["state"] is not None \
            and tiles[5]["state"] is not None:
        winner = True
        tiles[3]["win"] = True
        tiles[4]["win"] = True
        tiles[5]["win"] = True
    if not tiles[3]["state"] and not tiles[4]["state"] and not tiles[5]["state"] \
            and tiles[3]["state"] is not None \
            and tiles[4]["state"] is not None \
            and tiles[5]["state"] is not None:
        winner = False
        tiles[3]["win"] = True
        tiles[4]["win"] = True
        tiles[5]["win"] = True
    if tiles[6]["state"] and tiles[7]["state"] and tiles[8]["state"] \
            and tiles[6]["state"] is not None \
            and tiles[7]["state"] is not None \
            and tiles[8]["state"] is not None:
        winner = True
        tiles[6]["win"] = True
        tiles[7]["win"] = True
        tiles[8]["win"] = True
    if not tiles[6]["state"] and not tiles[7]["state"] and not tiles[8]["state"] \
            and tiles[6]["state"] is not None \
            and tiles[7]["state"] is not None \
            and tiles[8]["state"] is not None:
        winner = False
        tiles[6]["win"] = True
        tiles[7]["win"] = True
        tiles[8]["win"] = True

    # check columns for win condition
    if tiles[0]["state"] and tiles[3]["state"] and tiles[6]["state"] \
            and tiles[0]["state"] is not None \
            and tiles[3]["state"] is not None \
            and tiles[6]["state"] is not None:
        winner = True
        tiles[0]["win"] = True
        tiles[3]["win"] = True
        tiles[6]["win"] = True
    if not tiles[0]["state"] and not tiles[3]["state"] and not tiles[6]["state"] \
            and tiles[0]["state"] is not None \
            and tiles[3]["state"] is not None \
            and tiles[6]["state"] is not None:
        winner = False
        tiles[0]["win"] = True
        tiles[3]["win"] = True
        tiles[6]["win"] = True
    if tiles[1]["state"] and tiles[4]["state"] and tiles[7]["state"] \
            and tiles[1]["state"] is not None \
            and tiles[4]["state"] is not None \
            and tiles[7]["state"] is not None:
        winner = True
        tiles[1]["win"] = True
        tiles[4]["win"] = True
        tiles[7]["win"] = True
    if not tiles[1]["state"] and not tiles[4]["state"] and not tiles[7]["state"] \
            and tiles[1]["state"] is not None \
            and tiles[4]["state"] is not None \
            and tiles[7]["state"] is not None:
        winner = False
        tiles[1]["win"] = True
        tiles[4]["win"] = True
        tiles[7]["win"] = True
    if tiles[2]["state"] and tiles[5]["state"] and tiles[8]["state"] \
            and tiles[2]["state"] is not None \
            and tiles[5]["state"] is not None \
            and tiles[8]["state"] is not None:
        winner = True
        tiles[2]["win"] = True
        tiles[5]["win"] = True
        tiles[8]["win"] = True
    if not tiles[2]["state"] and not tiles[5]["state"] and not tiles[8]["state"] \
            and tiles[2]["state"] is not None \
            and tiles[5]["state"] is not None \
            and tiles[8]["state"] is not None:
        winner = False
        tiles[2]["win"] = True
        tiles[5]["win"] = True
        tiles[8]["win"] = True

    # check cross for win condition
    if tiles[0]["state"] and tiles[4]["state"] and tiles[8]["state"] \
            and tiles[0]["state"] is not None \
            and tiles[4]["state"] is not None \
            and tiles[8]["state"] is not None:
        winner = True
        tiles[0]["win"] = True
        tiles[4]["win"] = True
        tiles[8]["win"] = True
    if not tiles[0]["state"] and not tiles[4]["state"] and not tiles[8]["state"] \
            and tiles[0]["state"] is not None \
            and tiles[4]["state"] is not None \
            and tiles[8]["state"] is not None:
        winner = False
        tiles[0]["win"] = True
        tiles[4]["win"] = True
        tiles[8]["win"] = True
    if tiles[6]["state"] and tiles[4]["state"] and tiles[2]["state"] \
            and tiles[6]["state"] is not None \
            and tiles[4]["state"] is not None \
            and tiles[2]["state"] is not None:
        winner = True
        tiles[6]["win"] = True
        tiles[4]["win"] = True
        tiles[2]["win"] = True
    if not tiles[6]["state"] and not tiles[4]["state"] and not tiles[2]["state"] \
            and tiles[6]["state"] is not None \
            and tiles[4]["state"] is not None \
            and tiles[2]["state"] is not None:
        winner = False
        tiles[6]["win"] = True
        tiles[4]["win"] = True
        tiles[2]["win"] = True


def replayScreen():
    # this screen shows the player the event key to play again
    global tiles
    window.blit(replayTile, (tiles[3]["x"], tiles[3]["y"]))

    pygame.display.update()


def resetTiles():
    # reset every value to its starting value
    global  tiles
    tiles = [{"x": 5, "y": 5, "state": None, "win": False},  # Tile 1 from row 1
             {"x": 138, "y": 5, "state": None, "win": False},  # Tile 2 from row 1
             {"x": 271, "y": 5, "state": None, "win": False},  # Tile 3 from row 1

             {"x": 5, "y": 138, "state": None, "win": False},  # Tile 4 from row 2
             {"x": 138, "y": 138, "state": None, "win": False},  # Tile 5 from row 2
             {"x": 271, "y": 138, "state": None, "win": False},  # Tile 6 from row 2

             {"x": 5, "y": 271, "state": None, "win": False},  # Tile 7 from row 3
             {"x": 138, "y": 271, "state": None, "win": False},  # Tile 8 from row 3
             {"x": 271, "y": 271, "state": None, "win": False}, ]  # Tile 9 from row 3


def resetValues():
    global winner, mouseState

    winner = None
    mouseState = True

    # set the background to black again
    pygame.draw.rect(window, (0, 0, 0), (0, 0, 404, 404), 0)


def drawChecker():
    # if every tile is not blank and there is no winner, reset the tiles
    global tiles
    setTileCounter = 0

    for index in range(0, 9):
        if tiles[index]["state"] is not None:
            setTileCounter += 1

    # check if setTileCounter works
    # print(setTileCounter)

    if setTileCounter == 9 \
        and winner is None:
        resetTiles()


# main loop
while winner is None:
    # draws the tiles by their state
    # (0=blank, 1=cross, 2=circle)
    drawTiles()

    # mousePosition[0] = x axis
    # mousePosition[1] = y axis
    mousePosition = pygame.mouse.get_pos()

    for event in GAME_EVENTS.get():
        if event.type == pygame.QUIT:
            quitGame()

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
    drawChecker()
    if winner or not winner and winner is not None:
        # show winning line and wait bevor asking to play again
        # ask player to play again
        drawTiles()
        GAME_TIME.wait(1000)
        replayScreen()
        while winner is not None:
            for event in GAME_EVENTS.get():
                if event.type == pygame.QUIT:
                    quitGame()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        # reset values to start values
                        # also changes winner to None
                        # so this loop will end, and the main loop starts running again
                        resetTiles()
                        resetValues()
                    if event.key == pygame.K_ESCAPE:
                        quitGame()

    # updates the change on "window"
    pygame.display.update()
