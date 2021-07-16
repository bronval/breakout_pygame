
#####################################################
#
# breakout game with pygame
# for Python stage in Technofutur TIC (Belgium)

# Authors : Bastien Wiaux and Benoit Ronval
#
#####################################################


from constants import *
import math
import pygame


class Ball:


    def __init__(self):
        """
        Initialise un objet ball avec les constantes du fichier constants.py
        """
        self.radius = BALL_RADIUS
        self.center_x = BALL_START_X
        self.center_y = BALL_START_Y
        self.velocity = BALL_SPEED
        self.angle = - math.pi / 2
        self.rectangle = pygame.Rect(self.center_x - self.radius, self.center_y - self.radius, 2 * self.radius, 2 * self.radius)
        self.color = "white"
        self.save_pos = (self.center_x, self.center_y)


    def draw(self, window):
        """
        Dessine la balle sur la window et update l'attribut rectangle
        """
        # sauvegarde rectangle pour les collisions
        self.rectangle = pygame.draw.circle(window, self.color, (self.center_x, self.center_y), self.radius)

        # pour afficher la hitbox de la balle
        # pygame.draw.rect(window, "red", (self.rectangle.x, self.rectangle.y, self.rectangle.width, self.rectangle.height), 2)


    def change_angle(self, new_angle):
        """
        Met a jour l'attribut angle pour new_angle
        """
        self.angle = new_angle


    def bounce(self, orientation):
        """
        Permet de faire rebondir la balle en changeant l'angle
        """
        if orientation == "horizontal":
            # rebond sur une surface horizontale
            self.angle *= -1
        elif orientation == "vertical":
            # rebond sur une surface verticale
            self.angle = math.pi - self.angle
        else:
            print("Not a valid bounce. Either horizontal or vertical")


    def move(self, window):
        """
        Bouge les positions de la balle et update l'attribut rectangle
        """
        self.save_pos = (self.center_x, self.center_y)    # sauvegarde la position avant de bouger
        self.center_x = math.cos(self.angle) * self.velocity + self.center_x
        self.center_y = math.sin(self.angle) * self.velocity + self.center_y
        self.rectangle = pygame.draw.circle(window, self.color, (self.center_x, self.center_y), self.radius)    # update le rectangle

    
    def move_back(self):
        """
        Permet de mettre la position de la balle a la derniere position connue
        """
        self.center_x, self.center_y = self.save_pos

