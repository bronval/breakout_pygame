
#####################################################
#
# breakout game with pygame
# for Python stage in Technofutur TIC (Belgium)

# Authors : Bastien Wiaux and Benoit Ronval
#
#####################################################


from constants import *
import pygame


class Brick:


    def __init__(self, x, y):
        """
        initialise un objet Brick avec x et y la position de depart
        """
        self.x = x
        self.y = y
        self.rectangle = pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT)
        self.color = "white"


    def draw(self, window):
        """
        Dessine l'objet brick sur la window
        """
        pygame.draw.rect(window, self.color, self.rectangle)


    def change_color(self, new_color):
        """
        change la couleur de la brick pour new_color
        """
        self.color = new_color


