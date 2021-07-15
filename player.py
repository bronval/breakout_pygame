
#####################################################
#
# breakout game with pygame
# for Python stage in Technofutur TIC (Belgium)

# Authors : Bastien Wiaux and Benoit Ronval
#
#####################################################


from constants import *
import pygame


class Player:


    def __init__(self):
        """
        Initialise un objet Player avec les constantes dans constants.py
        """
        self.velocity = PLAYER_SPEED
        self.rectangle = pygame.Rect(PLAYER_START_X, PLAYER_START_Y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.color = "white"
        self.save_pos = PLAYER_START_X

    
    def draw(self, window):
        """
        Dessine le player sur window
        """
        pygame.draw.rect(window, self.color, self.rectangle)

    
    def move(self):
        """
        Gere les inputs claviers et bouge le player
        """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.rectangle.x > 0:
            self.save_pos = self.rectangle.x
            self.rectangle.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and self.rectangle.x + PLAYER_WIDTH < SCREEN_WIDTH:
            self.save_pos = self.rectangle.x
            self.rectangle.x += PLAYER_SPEED

    
    def move_back(self):
        """
        Remets la position du player a celle precedente
        """
        self.rectangle.x = self.save_pos


