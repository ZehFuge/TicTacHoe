import pygame
import sys
import mainloop
import window_settings

pygame.init()

def end_game():
    pygame.quit()
    sys.exit()

def draw():
    window_settings.window.blit(mainloop.player.player_sprite_sheet, (mainloop.player.player_position[0],
                                                                      mainloop.player.player_position[1]))
