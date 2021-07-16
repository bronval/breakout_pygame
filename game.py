
#####################################################
#
# breakout game with pygame
# for Python stage in Technofutur TIC (Belgium)

# Authors : Bastien Wiaux and Benoit Ronval
#
#####################################################


import pygame
from constants import *
from player import Player
from ball import Ball
from brick import Brick
import sound
from math import pi


class Game:


    def __init__(self):
        """
        Cree un objet Game pour faire tourner tout le jeu
        """
        self.stop_game = False

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.bkg = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

        self.player = Player()
        self.ball = Ball()

        # cree toutes les brick du jeu
        self.bricks = []
        for row in range(BRICK_ROWS):
            for columns in range(BRICK_COLUMNS):
                self.bricks.append(Brick(columns*(BRICK_WIDTH + BRICK_GAP), BRICK_TOP_VOID+row*(BRICK_HEIGHT+BRICK_GAP)))
                
        # pour afficher du texte sur l'ecran
        pygame.font.init()
        self.font = pygame.font.SysFont(pygame.font.get_default_font(), FONT_SIZE)

        self.victory = False


    def bounce_on_rect(self, rect):
        """
        Fait rebondir la balle sur un rectangle (player ou brick)
        """
        overlap = self.ball.rectangle.clip(rect)

        if overlap.width >= overlap.height:
            self.ball.bounce("horizontal")    # utilise la fonction de Ball pour rebondir
        if overlap.width <= overlap.height:
            self.ball.bounce("vertical")


    def collide_list_of_bricks(self):
        """
        Permet de recuperer les index des brick qui touchent la balle (pour les collisions)
        """
        indices = []
        for i, brick in enumerate(self.bricks):
            if self.ball.rectangle.colliderect(brick.rectangle):    # verifie si la balle touche une brick
                indices.append(i)
                self.bounce_on_rect(brick.rectangle)
                self.ball.move_back()
                sound.brick()
        return indices
    

    def collide_player(self):
        """
        Fait rebondir la balle sur le player
        """
        if self.ball.rectangle.colliderect(self.player.rectangle):
            # fait rebondir la balle avec un angle donne en fonction de la position de la collision entre la balle et le player
            delta = self.ball.center_x - self.player.rectangle.midtop[0]
            angle = - pi / 2 + (delta / (self.player.rectangle.width/2) * pi / 3)
            self.ball.change_angle(angle)
            self.ball.move_back()
            sound.touch()
            

    def collide_screen(self):
        """
        Permet de gérer le rebond de la balle sur les bords de l'ecran
        """
        bounds = self.screen.get_rect()
        if self.ball.rectangle.left <= bounds.left or self.ball.rectangle.right >= bounds.right:  # verifie si on touche le mur de gauche ou de droite
            self.ball.bounce("vertical")
            self.ball.move_back()
        if self.ball.rectangle.top <= bounds.top:    # verifie si on touche le mur du haut
            self.ball.bounce("horizontal")
            self.ball.move_back()
        if self.ball.rectangle.top >= bounds.bottom:    # verifie si on passe en dessous de l'ecran = perdu une vie
            sound.death()
            pygame.time.wait(TIME_BEFORE_RELAUNCH)
            self.player.life -= 1
            if self.player.life <= 0:  # le player n'a plus de vie
                self.stop_game = True
                return
            self.ball = Ball()


    def check_collision(self):
        """
        Verifie l'ensemble des collisions de la balle avec les elements du jeu (brick, mur, player)
        """
        self.collide_screen()    # verifie la collision avec l'ecran
        indices = self.collide_list_of_bricks()    # verifie la collision avec les bricks
        for i, idx in enumerate(indices):
            del(self.bricks[idx-i])    # supprime les bricks qu'on a touchees

        if len(self.bricks) == 0:    # si plus de brick c'est gagne
            self.victory = True
            self.stop_game = True

        self.collide_player()    # verifie la collision avec le player

    
    def draw(self):
        """
        Affiche tous les elements du jeu sur l'ecran (brick, player, balle)
        """
        pygame.draw.rect(self.screen, "black", self.bkg)
        for brick in self.bricks:
            brick.draw(self.screen)
        self.ball.draw(self.screen)
        self.player.draw(self.screen)
        pygame.display.flip()


    def check_quit(self):
        """
        Pour quitter le jeu
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True
        return False


    def run(self):
        """
        Main loop, fait tourner le jeu
        """
        clock = pygame.time.Clock()
        while not self.stop_game:
            self.stop_game = self.check_quit()
            clock.tick(FRAME_RATE)
            self.player.move()
            self.ball.move(self.screen)
            self.check_collision()
            self.draw()
        
        if self.victory:
            # montre l'ecran de victoire
            text = self.font.render("VICTORY", False, "yellow")
            self.screen.blit(text, ((SCREEN_WIDTH-text.get_rect().width)/2,(SCREEN_HEIGHT-text.get_rect().height)/2))
            pygame.display.flip()
            sound.victory()

        else: 
            # montre l'ecran de mort
            text= self.font.render('Game Over', False, (255, 255, 255))
            self.screen.blit(text,((SCREEN_WIDTH-text.get_rect().width)/2,(SCREEN_HEIGHT-text.get_rect().height)/2))
            pygame.display.flip()
            sound.death()

        while not self.check_quit():
            pass