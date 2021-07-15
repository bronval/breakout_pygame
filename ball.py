
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
        self.radius = BALL_RADIUS
        self.center_x = BALL_START_X
        self.center_y = BALL_START_Y
        self.velocity = BALL_SPEED
        self.angle = - math.pi / 2
        self.rectangle = pygame.Rect(self.center_x - self.radius, self.center_y - self.radius, 2 * self.radius, 2 * self.radius)
        self.color = "white"
        self.save_pos = (self.center_x, self.center_y)


    def draw(self, window):
        self.rectangle = pygame.draw.circle(window, self.color, (self.center_x, self.center_y), self.radius)
        # pygame.draw.rect(window, "red", (self.rectangle.x, self.rectangle.y, self.rectangle.width, self.rectangle.height), 2)


    def change_angle(self, new_angle):
        self.angle = new_angle


    def bounce(self, orientation):
        if orientation == "horizontal":
            self.angle *= -1
        elif orientation == "vertical":
            self.angle = math.pi - self.angle
        else:
            print("Not a valid bounce. Either horizontal or vertical")

    def move(self, window):
        self.save_pos = (self.center_x, self.center_y)
        self.center_x = math.cos(self.angle) * self.velocity + self.center_x
        self.center_y = math.sin(self.angle) * self.velocity + self.center_y
        self.rectangle = pygame.draw.circle(window, self.color, (self.center_x, self.center_y), self.radius)

    
    def move_back(self):
        self.center_x, self.center_y = self.save_pos

