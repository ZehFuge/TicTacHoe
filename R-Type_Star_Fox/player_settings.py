# import default librarys
import pygame

# import modules
import mainloop
import window_settings
import game_functions

pygame.init()

class Player:
    def __init__(self):
        # player sprite information
        self.player_sprite_sheet = pygame.image.load("Images/arwing_sprites_32x32_hostr.png")
        self.player_position = [window_settings.windowWidth / 2, window_settings.windowHeigth - 32]
        # self.player_state[0] = go left, [1] = stay mid, [2] = go right
        self.player_states = ({"startingX" : 0, "startingY" : 0, "size" : 32},
                             {"startingX" : 32, "startingY" : 0, "size" : 32},
                             {"startingX" : 64, "startingY" : 0, "size" : 32})

        # player attributes
        self.player_movespeed = 10

    # methode for movement
    def check_player_input(self):
        for event in pygame.event.get():
            # if window gets closed
            if event.type == pygame.QUIT:
                game_functions.end_game()

            # check for key down inputs
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_functions.end_game()

                if event.key == pygame.K_w:
                    pass
                if event.key == pygame.K_s:
                    pass
                if event.key == pygame.K_a:
                    pass
                if event.key == pygame.K_d:
                    pass
