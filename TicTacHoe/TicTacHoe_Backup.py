# Backup date 2020-10-06 19:28
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

Problem 3.1: Done
    The game isn't counting the amount of wins for cross and circle

    ### Solution ###
    Every players dictonary got another statement named "wins". By default it starts at 0.
    Everytime a player wins, the raiseWin() function is started and raises the winners win counter by 1.
    Meanwhile the scores are drawn all the time.
    ###   End    ###

    Problem 3.2: Done
    Drawing the scores all the time lets the displayed scores flash/blink all the time.
    This is pretty annoying.

    ### Solution ###
    Before the player win tiles and its score are displayed, its been checked for change.
    If there is no change, there is no need for a pygame.display.update. Otherwise
    the player win tiles are blitted again to clear the old blit, and then the new score
    is displayed
    ###   End    ###

Problem 4.1: Done
    If the games ends as draw, nothing happens. The games needs to check itself, if every tile is filled
    and there is no winner. If the case is True, all tiles need to be reset

    ### Solution ###
    After the winChecker() checks the win condition, the drawChecker checks if the game is set draw.
    Therefore a for loop loops from range(0, 9 (index for tiles dictionary)) and raises the setTileCounter
    += 1.
    If a tile is blank (state = None), setTileCounter wont rise.
    If setTileCounter reaches 9 (all tiles are filled and not blank) and the winner is still None,
    all tiles are reset and the game will continue, until there is a winner.
    Before this happens, the game waits for few seconds, so the game doesnt accidentally take
    two mouse inputs
    ###   End    ###

Problem 5.1: Done
    The game seems to static and needs to be more dynamic. Therefore, every blank tile which collides with
    the mouse, should be displayed in gray as a visual change. Also player with no knowledge would be
    trained.

    ### Solution ###
    The drawTiles() function got another if statement for drawing blank tiles. Therefore, the function
    also gets the mouseX and mouseY variables. If the mouse collides with an blank tile, the tile
    is display in gray. Already taken tiles, don't change their color while mouseover.

    This function is a nice visual gimmick, but also teaches newbies, which tiles they can use.
    ###   End    ###

Problem 6.1:
    Whats about the turn order? The games starts with cross, but nobody knows, especially after a game reset.

    ### Solution ###
    Set the icon of the mouse cursor as x or o, depending of the mousestate (True = cross, False = circle)
    ###   End    ###
"""

import pygame
import pygame.event as GAME_EVENTS
import pygame.time as GAME_TIME
import sys

# initialize pygame
pygame.init()
pygame.font.init()

# set some screen info
windowWidth = 404
windowHeight = 537

window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("TicTacHoe - Preorder Edition")

# load pictures of tile states
blankTile = pygame.image.load("Images/blank.png")
crossTile = pygame.image.load("Images/cross.png")
circleTile = pygame.image.load("Images/circle.png")
winTile = pygame.image.load("Images/win.png")
replayTile = pygame.image.load("Images/replay.png")
greyTile = pygame.image.load("Images/blankMouseOver.png")  # for mouseover visuals

# set information for the wincounters for X and Y
winCounterX = {"image": pygame.image.load("Images/winX.png"),
               "startingX": 5,
               "startingY": 404,
               "wins": 0}

winCounterO = {"image": pygame.image.load("Images/winO.png"),
               "startingX": 204,
               "startingY": 404,
               "wins": 0}

# game info and variables
# set info for tiles
# tileStartingX, tileStartingY,
# tileState (None = blank, True = cross, False = circle)
# win is set, if a row/column/cross win condition is given
tiles = [{"x": 5, "y": 5, "state": None, "win": False},  # Tile 1 from row 1
         {"x": 138, "y": 5, "state": None, "win": False},  # Tile 2 from row 1
         {"x": 271, "y": 5, "state": None, "win": False},  # Tile 3 from row 1

         {"x": 5, "y": 138, "state": None, "win": False},  # Tile 4 from row 2
         {"x": 138, "y": 138, "state": None, "win": False},  # Tile 5 from row 2
         {"x": 271, "y": 138, "state": None, "win": False},  # Tile 6 from row 2

         {"x": 5, "y": 271, "state": None, "win": False},  # Tile 7 from row 3
         {"x": 138, "y": 271, "state": None, "win": False},  # Tile 8 from row 3
         {"x": 271, "y": 271, "state": None, "win": False}, ]  # Tile 9 from row 3

# the tile is an square, meaning all sides are even
tileSize = 128

# this value decides, if a tile is filled with a cross or a circle
# this value only changes, after the current state is set to a tile
# this happens through the function "changeState()"
mouseState = True  # True = cross / False = circle
winner = None

# pre declared variables for mouse position
mouseX = 0
mouseY = 0

# pre declared scores for display
# the old scores are declared as minus, so at the beginning
# scoreRefeshCheck at least draws the new score one until a new change happens
oldScoreX = -1
oldScoreY = -1
newScoreX = 0
newScoreY = 0

global setTileCounter
setTileCounter = 0


def quitGame():
    pygame.quit()
    sys.exit()


def drawTiles():
    global tiles, winCounterX, winCounterO, oldScoreX, oldScoreY, newScoreX, newScoreY, mouseX, mouseY, tileSize

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

        # save the mouse position
        mouseX = pygame.mouse.get_pos()[0]
        mouseY = pygame.mouse.get_pos()[1]

        # if tile got whether cross nor circle state
        if tiles[index]["state"] is None \
                and tiles[index]["state"] is not True \
                and tiles[index]["state"] is not False \
                and not tiles[index]["win"]:
            if tiles[index]["x"] < mouseX < (tiles[index]["x"] + tileSize) \
                    and tiles[index]["y"] < mouseY < (tiles[index]["y"] + tileSize):
                window.blit(greyTile, (tiles[index]["x"], tiles[index]["y"]))
            else:
                window.blit(blankTile, (tiles[index]["x"], tiles[index]["y"]))
                # print("Blank printed")

        # if tile is set to show win
        if tiles[index]["win"] \
                and [tiles[index]["win"] is not None]:
            window.blit(winTile, (tiles[index]["x"], tiles[index]["y"]))

        # draw the win counter tiles
        # but, only redraw them, if the score changed. Or the score layer gets overwritten
        if newScoreX > oldScoreX \
                or newScoreY > oldScoreY:
            window.blit(winCounterX["image"], (winCounterX["startingX"], winCounterX["startingY"]))
            window.blit(winCounterO["image"], (winCounterO["startingX"], winCounterO["startingY"]))

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

    # check for rows
    if tiles[0]["state"] == tiles[1]["state"] == tiles[2]["state"] \
            and tiles[0]["state"] is not None and tiles[1]["state"] is not None and tiles[2]["state"] is not None:
        tiles[0]["win"], tiles[1]["win"], tiles[2]["win"] = True, True, True
        if tiles[0]["state"] and tiles[1]["state"] and tiles[2]["state"]:
            winner = True
        else:
            winner = False
    if tiles[3]["state"] == tiles[4]["state"] == tiles[5]["state"] \
            and tiles[3]["state"] is not None and tiles[4]["state"] is not None and tiles[5]["state"] is not None:
        tiles[3]["win"], tiles[4]["win"], tiles[5]["win"] = True, True, True
        if tiles[3]["state"] and tiles[4]["state"] and tiles[5]["state"]:
            winner = True
        if not tiles[3]["state"] and not tiles[4]["state"] and not tiles[5]["state"]:
            winner = False
    if tiles[6]["state"] == tiles[7]["state"] == tiles[8]["state"] \
            and tiles[6]["state"] is not None and tiles[7]["state"] is not None and tiles[8]["state"] is not None:
        tiles[6]["win"], tiles[7]["win"], tiles[8]["win"] = True, True, True
        if tiles[6]["state"] and tiles[7]["state"] and tiles[8]["state"]:
            winner = True
        if not tiles[6]["state"] and not tiles[7]["state"] and not tiles[8]["state"]:
            winner = False

    # check for columns
    if tiles[0]["state"] == tiles[3]["state"] == tiles[6]["state"] \
            and tiles[0]["state"] is not None and tiles[3]["state"] is not None and tiles[6]["state"] is not None:
        tiles[0]["win"], tiles[3]["win"], tiles[6]["win"] = True, True, True
        if tiles[0]["state"] and tiles[3]["state"] and tiles[6]["state"]:
            winner = True
        if not tiles[0]["state"] and not tiles[3]["state"] and not tiles[6]["state"]:
            winner = False
    if tiles[1]["state"] == tiles[4]["state"] == tiles[7]["state"] \
            and tiles[1]["state"] is not None and tiles[4]["state"] is not None and tiles[7]["state"] is not None:
        tiles[1]["win"], tiles[4]["win"], tiles[7]["win"] = True, True, True
        if tiles[1]["state"] and tiles[4]["state"] and tiles[7]["state"]:
            winner = True
        if not tiles[1]["state"] and not tiles[4]["state"] and not tiles[7]["state"]:
            winner = False
    if tiles[2]["state"] == tiles[5]["state"] == tiles[8]["state"] \
            and tiles[2]["state"] is not None and tiles[5]["state"] is not None and tiles[8]["state"] is not None:
        tiles[2]["win"], tiles[5]["win"], tiles[8]["win"] = True, True, True
        if tiles[2]["state"] and tiles[5]["state"] and tiles[8]["state"]:
            winner = True
        if not tiles[2]["state"] and not tiles[5]["state"] and not tiles[8]["state"]:
            winner = False

    # check for diagonals
    if tiles[0]["state"] == tiles[4]["state"] == tiles[8]["state"] \
            and tiles[0]["state"] is not None and tiles[4]["state"] is not None and tiles[8]["state"] is not None:
        tiles[0]["win"], tiles[4]["win"], tiles[8]["win"] = True, True, True
        if tiles[0]["state"] and tiles[4]["state"] and tiles[8]["state"]:
            winner = True
        if not tiles[0]["state"] and not tiles[4]["state"] and not tiles[8]["state"]:
            winner = False
    if tiles[6]["state"] == tiles[4]["state"] == tiles[2]["state"] \
            and tiles[6]["state"] is not None and tiles[4]["state"] is not None and tiles[2]["state"] is not None:
        tiles[6]["win"], tiles[4]["win"], tiles[2]["win"] = True, True, True
        if tiles[6]["state"] and tiles[4]["state"] and tiles[2]["state"]:
            winner = True
        if not tiles[6]["state"] and not tiles[4]["state"] and not tiles[2]["state"]:
            winner = False


def replayScreen():
    # this screen shows the player the event key to play again
    global tiles
    window.blit(replayTile, (tiles[3]["x"], tiles[3]["y"]))

    pygame.display.update()


def resetTiles():
    # reset every value to its starting value
    global tiles
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
    mouseState = True  # game always starts with cross / True

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

    return setTileCounter


def raiseWin():
    global winner, winCounterX, winCounterO

    if winner:
        winCounterX["wins"] += 1
    elif not winner:
        winCounterO["wins"] += 1


def drawWins():
    global winCounterX, winCounterO

    myfont = pygame.font.SysFont("Arial Black", 75)

    # save the wins of X and O and convert them to strings
    # otherwise .blit() cant display them
    saveWinsX = winCounterX["wins"]
    saveWinsX = str(saveWinsX)

    saveWins0 = winCounterO["wins"]
    saveWins0 = str(saveWins0)

    # set win values and font style to a variable
    winsOfX = myfont.render(saveWinsX, False, (0, 0, 0))
    winsOfO = myfont.render(saveWins0, False, (0, 0, 0))

    # print the created win output for both players
    window.blit(winsOfX, (winCounterX["startingX"] + 75, winCounterX["startingY"] + 35))
    window.blit(winsOfO, (winCounterO["startingX"] + 75, winCounterO["startingY"] + 35))

    pygame.display.update()


def scoreRefreshCheck():
    global oldScoreX, oldScoreY, newScoreX, newScoreY, winCounterX, winCounterO

    newScoreX = winCounterX["wins"]
    newScoreY = winCounterO["wins"]

    if newScoreX > oldScoreX \
            or newScoreY > oldScoreY:
        # drawTiles() needs to be first
        # otherwise the new number will be display over the old one
        drawTiles()
        drawWins()

    # refresh the "new" old values
    oldScoreX = newScoreX
    oldScoreY = newScoreY


# main loop
while winner is None:
    # draws the tiles by their state
    # (0=blank, 1=cross, 2=circle)
    # save the mouse position
    mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]
    drawTiles()
    # check if the score changed and therefore should be displayed again
    scoreRefreshCheck()

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
            # change the state of the chosen tile
            changeState()

    winChecker()
    setTileCounter = drawChecker()
    # if the setTileCounter achieved the reset value, wait
    if setTileCounter == 9:
        GAME_TIME.wait(100)

    if winner or not winner and winner is not None:
        # show winning line and wait bevor asking to play again
        # ask player to play again
        print(winner)
        raiseWin()
        scoreRefreshCheck()
        drawTiles()
        drawWins()
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
