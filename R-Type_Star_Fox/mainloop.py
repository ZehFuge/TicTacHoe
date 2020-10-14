# import default librarys
import pygame

# import moduls
import window_settings
import player_settings
import game_functions

pygame.init()
pygame.mixer.init()

background_song = "Music/corneria_theme.mp3"
pygame.mixer.music.load(background_song)
pygame.mixer.music.play(1)

player = player_settings.Player()

while True:
    # check for player input
    player.check_player_input()

    # update drawings
    game_functions.draw()
    player.draw_player()

    # update display
    pygame.display.flip()

    # set time
    window_settings.clock.tick(window_settings.FPS)
