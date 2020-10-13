import pygame

pygame.init()

# set window information
windowWidth = 800
windowHeigth = 600
window = pygame.display.set_mode((windowWidth, windowHeigth))

# set time information
clock = pygame.time.Clock()
FPS = 45

# pre defined colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
