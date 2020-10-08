import sys
import pygame
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

pygame.init()

# set game information
windowWidth = 1200
windowHeight = 800
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Sprite, but not to drink!")
FPS = 30
clock = pygame.time.Clock()

# declare a variable, which contains every sprite
# this is needed to handle every sprite at once
all_sprites = pygame.sprite.Group()

# pre declared colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# this class represents the player
# it derives from the "Sprite" class in Pygame
class Player(pygame.sprite.Sprite):
    # sprite for the player

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect =  self.image.get_rect()
        self.rect.center = (windowWidth / 2, windowHeight / 2)

    def update(self):
        self.rect.x += 5


def endgame():
    pygame.quit()
    sys.exit()


player = Player()
all_sprites.add(player)

while True:

    # keep loop running at the right speed
    clock.tick(FPS)

    # process inputs (events)
    for event in GAME_EVENTS.get():
        if event.type == pygame.QUIT:
            endgame()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                endgame()

    # update
    all_sprites.update()

    # draw / render
    window.fill(BLACK)
    all_sprites.draw(window)

    # after drawing everything, flip the display
    # pygame.display.flip() -> changes everything on the screen
    # pygame.display.update() -> just updates a single element
    pygame.display.flip()
