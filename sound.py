
#####################################################
#
# breakout game with pygame
# for Python stage in Technofutur TIC (Belgium)

# Authors : Bastien Wiaux and Benoit Ronval
#
#####################################################


import pygame


pygame.init()
death_sound = pygame.mixer.Sound("death_sound.mp3")
touch_ball = pygame.mixer.Sound("player_sound.mp3")
brick_sound = pygame.mixer.Sound("brick_sound.mp3")
victory_sound = pygame.mixer.Sound("victory.mp3")

pygame.mixer.Sound.set_volume(death_sound, 0.7)
pygame.mixer.Sound.set_volume(touch_ball, 0.7)
pygame.mixer.Sound.set_volume(brick_sound, 0.7)
pygame.mixer.Sound.set_volume(victory_sound, 0.7)


def touch():
    pygame.mixer.Sound.play(touch_ball)

def death():
    pygame.mixer.Sound.play(death_sound)

def brick():
    pygame.mixer.Sound.play(brick_sound)

def victory():
    pygame.mixer.Sound.play(victory_sound)

