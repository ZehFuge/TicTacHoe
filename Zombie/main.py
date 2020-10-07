import sys
import pygame
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

pygame.init()

windowWidth = 1200
windowHeight = 800
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Sprite, but not to drink!")


def endgame():
    pygame.quit()
    sys.exit()


while True:

    for event in GAME_EVENTS.get():
        if event.type == pygame.QUIT:
            endgame()

    pygame.display.flip()
