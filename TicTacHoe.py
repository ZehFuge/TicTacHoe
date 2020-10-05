"""
Problem 1:
    Tiles are only changed, if the mouse is moving and getting pressed.
    Otherwise it wount change anything

Problem 2:
    Already set tileStates can be overwritten. This shouldn't be

Problem 3:
    There is no win condition checker at the moment. Therefore, there is no end.
"""


import pygame, sys
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

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
cricleTile = pygame.image.load("Images/circle.png")

# game info and variables
# set info for tiles
# tileStartingX, tileStartingY, tileState (0=blank, 1=cross, 2=circle)
tiles =  [{"x" : 5, "y" : 5, "state" : None},    # Tile 1 from 1 row
         {"x" : 138, "y" : 5, "state" : None},  # Tile 2 from 1 row
         {"x" : 271, "y" : 5, "state" : None},  # Tile 3 from 1 row

         {"x": 5, "y": 138, "state": None},     # Tile 4 from 2 row
         {"x": 138, "y": 138, "state": None},   # Tile 5 from 2 row
         {"x": 271, "y": 138, "state": None},   # Tile 6 from 2 row

         {"x": 5, "y": 271, "state": None},     # Tile 7 from 3 row
         {"x": 138, "y": 271, "state": None},   # Tile 8 from 3 row
         {"x": 271, "y": 271, "state": None},]  # Tile 9 from 3 row

# the tile is an square, meaning all sides are even
tileSize = 128

# this value decides, if a tile is filled with a cross or a circle
# this value only changes, after the current state is set to a tile
# this happens through the function "changeState()"
mouseState = True # True = cross / False = circle

def quitGame():
    pygame.quit()
    sys.exit()

def drawTiles():
    global tiles

    for index in range(0, 9):
        # if tile got the cross state
        if tiles[index]["state"] == True:
            window.blit(crossTile, (tiles[index]["x"], tiles[index]["y"]))

        # if tile got the circle state
        elif tiles[index]["state"] == False:
            window.blit(cricleTile, (tiles[index]["x"], tiles[index]["y"]))

        # if tile got wether cross nor circle state
        elif tiles[index]["state"] == None:
            window.blit(blankTile, (tiles[index]["x"], tiles[index]["y"]))

    pygame.display.update()

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

                # collide check for mouse
                # print("The mouse is on tile nr: ", index + 1)
                # print("Its X and Y dates are")
                # print("X: ", tiles[index]["x"], " and Y: ", tiles[index]["y"])

                # change tile to cross if current mouseState is cross
                if mouseState == True:
                    tiles[index]["state"] = mouseState
                    print("Something happend in Cross State")
                    # change the mouseState after a change is done
                    mouseState = False

                # change tile to circle if current mouseState is circle
                elif mouseState == False:
                    tiles[index]["state"] = mouseState
                    print("Something happend in Circle State")
                    # change the mouseState after a change is done
                    mouseState = True

def winChecker():
    pass


# main loop
while True:
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

        # check if left mousebutton got pressed
        # the event of changement happens, if the user let go of the mouse button
        # otherwise it can cause problems, if the user keeps the mouse button pressed
        if pygame.mouse.get_pressed()[0]:
            if pygame.mouse.get_rel()[0]:
                # save the postition of the moment, the mouse get pressed
                mouseX = pygame.mouse.get_pos()[0]
                mouseY = pygame.mouse.get_pos()[1]
                changeState()

    # updates the changement on "window"
    pygame.display.update()

