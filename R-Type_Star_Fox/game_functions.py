import pygame
import sys
import window_settings

pygame.init()

def end_game():
    pygame.quit()
    sys.exit()

def draw():
    # draw background
    window_settings.window.blit(window_settings.background, (0, 0))
