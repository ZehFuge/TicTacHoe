import pygame

pygame.init()

# set window information
windowWidth = 1200
windowHeigth = 1000
window = pygame.display.set_mode((windowWidth, windowHeigth))
pygame.display.set_caption("Star Fox Tournament")
pygame.display.toggle_fullscreen()
background = pygame.image.load("Images/background_frame_1200x1000.png")

# set time information
clock = pygame.time.Clock()
FPS = 60

# pre defined colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CONV_PINK = (255, 174, 201)
