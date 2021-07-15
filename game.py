
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
from math import pi

class Game:


    def __init__(self):
        self.stop_game = False

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.bkg = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

        self.player = Player()
        self.ball = Ball()
        self.bricks = []
        for row in range(BRICK_ROWS):
            for columns in range(BRICK_COLUMNS):
                self.bricks.append(Brick(columns*(BRICK_WIDTH + BRICK_GAP), BRICK_TOP_VOID+row*(BRICK_HEIGHT+BRICK_GAP)))
                
        pygame.font.init()
        self.font = pygame.font.SysFont(pygame.font.get_default_font(), FONT_SIZE)


    def bounce_on_rect(self, rect):
        overlap = self.ball.rectangle.clip(rect)
        if overlap.top == rect.top or overlap.bottom == rect.bottom:
            self.ball.bounce("horizontal")
        if overlap.left == rect.left or overlap.right == rect.right:
            self.ball.bounce("vertical")


    def collide_list_of_bricks(self):
        indices = []
        for i, brick in enumerate(self.bricks):
            if self.ball.rectangle.colliderect(brick.rectangle):
                indices.append(i)
                self.bounce_on_rect(brick.rectangle)
                self.ball.move_back()
        return indices
    

    def collide_player(self):
        if self.ball.rectangle.colliderect(self.player.rectangle):
            delta = self.ball.center_x - self.player.rectangle.midtop[0]
            angle = - pi / 2 + (delta / (self.player.rectangle.width/2) * pi / 3)
            self.ball.change_angle(angle)
            self.ball.move_back()
            

    def collide_screen(self):
        bounds = self.screen.get_rect()
        if self.ball.rectangle.left <= bounds.left or self.ball.rectangle.right >= bounds.right:
            self.ball.bounce("vertical")
            self.ball.move_back()
        if self.ball.rectangle.top <= bounds.top:
            self.ball.bounce("horizontal")
            self.ball.move_back()
        if self.ball.rectangle.bottom >= bounds.bottom:
            pygame.time.wait(TIME_BEFORE_RELAUNCH)
            self.player.life -= 1
            if self.player.life == 0:
                self.end_game()
                return
            self.ball = Ball()


    def end_game(self):
        text= self.font.render('Game Over', False, (255, 255, 255))
        self.screen.blit(text,((SCREEN_WIDTH-text.get_rect().width)/2,PLAYER_GAP))
        self.stop_game = True


    def check_collision(self):
        self.collide_screen()
        indices = self.collide_list_of_bricks()
        for i in indices:
            del(self.bricks[i])
        self.collide_player()

    
    def draw(self):
        pygame.draw.rect(self.screen, "black", self.bkg)
        for brick in self.bricks:
            brick.draw(self.screen)
        self.ball.draw(self.screen)
        self.player.draw(self.screen)
        pygame.display.flip()


    def check_quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True
        return False


    def run(self):
        clock = pygame.time.Clock()
        while not self.stop_game:
            clock.tick(FRAME_RATE)
            self.player.move()
            self.ball.move(self.screen)
            self.check_collision()
            self.draw()
            self.stop_game = self.check_quit()