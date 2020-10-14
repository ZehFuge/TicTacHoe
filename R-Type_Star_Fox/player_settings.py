# import default librarys
import pygame

# import modules
import window_settings
import game_functions

pygame.init()

class Player:
    def __init__(self):
        # player sprite information
        self.player_sprite_sheet = pygame.image.load("Images/arwing_sprites_128x128_hostr_big.png").convert()
        self.player_sprite_sheet.set_colorkey(window_settings.CONV_PINK)
        self.player_position = [window_settings.windowWidth / 2, window_settings.windowHeigth - 128]
        self.player_frame_size = 128
        # self.player_state[0] = go left, [1] = IDLE, [2] = go right
        self.player_states = ({"startingX" : 0, "startingY" : 0, "size" : 128},
                             {"startingX" : 128, "startingY" : 0, "size" : 128},
                             {"startingX" : 256, "startingY" : 0, "size" : 128})
        self.player_displayed_state = "MIDDLE"

        # player attributes
        self.player_movespeed = 20

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

        pressed_button = pygame.key.get_pressed()
        if pressed_button[pygame.K_w]:
            if self.player_position[1] - self.player_movespeed > 0:
                self.player_displayed_state = "MIDDLE"
                self.player_position[1] -= self.player_movespeed
        if pressed_button[pygame.K_s]:
            if self.player_position[1] + self.player_movespeed + self.player_frame_size < window_settings.windowHeigth:
                self.player_displayed_state = "MIDDLE"
                self.player_position[1] += self.player_movespeed
        if pressed_button[pygame.K_a]:
            if self.player_position[0] - self.player_movespeed > 0:
                self.player_displayed_state = "LEFT"
                self.player_position[0] -= self.player_movespeed
        if pressed_button[pygame.K_d]:
            if self.player_position[0] + self.player_movespeed + self.player_frame_size < window_settings.windowWidth:
                self.player_displayed_state = "RIGHT"
                self.player_position[0] += self.player_movespeed

        # back to IDLE if A or S are not being pressed
        elif not pressed_button[pygame.K_s] \
            and not pressed_button[pygame.K_a]:
            self.player_displayed_state = "MIDDLE"


    # draw player sprite depending of his displayed state
    def draw_player(self):
        if self.player_displayed_state == "MIDDLE":
            window_settings.window.blit(self.player_sprite_sheet,
                                        (self.player_position[0],
                                         self.player_position[1]),

                                        (self.player_states[1]["startingX"],
                                         self.player_states[1]["startingY"],
                                         self.player_states[1]["size"],
                                         self.player_states[1]["size"]))

        if self.player_displayed_state == "LEFT":
            window_settings.window.blit(self.player_sprite_sheet,
                                        (self.player_position[0],
                                         self.player_position[1]),

                                        (self.player_states[0]["startingX"],
                                         self.player_states[0]["startingY"],
                                         self.player_states[0]["size"],
                                         self.player_states[0]["size"]))

        if self.player_displayed_state == "RIGHT":
            window_settings.window.blit(self.player_sprite_sheet,
                                        (self.player_position[0],
                                         self.player_position[1]),

                                        (self.player_states[2]["startingX"],
                                         self.player_states[2]["startingY"],
                                         self.player_states[2]["size"],
                                         self.player_states[2]["size"]))

    # this methode is used to shoot
