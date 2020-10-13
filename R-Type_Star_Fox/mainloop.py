# import default librarys
import pygame

# import moduls
import window_settings
import player_settings
import game_functions

pygame.init()

player = player_settings.Player()

while True:
    # check for player input
    player.check_player_input()

    # update drawings
    game_functions.draw()

    # update display
    pygame.display.flip()
