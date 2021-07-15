
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

class Game:

    def __init__(self):
        self.stop_game = False

        self.screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
        self.bkg = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_WIDTH)

        self.player = Player()
        self.ball = Ball()
        self.bricks = []
        for row in range(BRICK_ROWS):
            for columns in range(BRICK_COLUMNS):
                self.bricks.append(Brick(columns*(BRICK_WIDTH + BRICK_GAP), BRICK_TOP_VOID+row*(BRICK_HEIGHT+BRICK_GAP)))

    def collide_list_of_bricks(self):
        indices = []
        for i, brick in enumerate(self.bricks):
            if self.ball.rectangle.colliderect(brick.rectangle):
                indices.append(i)
                overlap = self.ball.rectangle.clip(brick.rectangle)
                if overlap.top == brick.rectangle.top or overlap.bottom == brick.rectangle.bottom:
                    self.ball.bounce("Horizontal")
                if overlap.left == brick.rectangle.left or overlap.right == brick.rectangle.right:
                    self.ball.bounce("Vertical")
        return indices
    
    def collide_player(self):
        if self.ball.rectangle.colliderect(self.player.rectangle):
            #TODO bounce
            ...

    def collide_screen(self):
        rep = False
        bounds = self.surface.get_rect()
        if self.ball.rectangle.left < bounds.left or self.ball.rectangle.right > bounds.right:
            self.ball.bounce("Vertical")
            rep = True
        if self.ball.rectangle.top < bounds.top:
            self.ball.bounce("Horizontal")
            rep = True
        if self.ball.rectangle.bottom > bounds.bottom:
            pygame.time.wait(TIME_BEFORE_RELAUNCH)
            self.player.life -= 1
            if self.player.life == 0:
                end_game()
                return
            self.ball = Ball()
            rep = False
        return rep

    def end_game(self):
        pygame.font.init()
        font = pygame.font.SysFont(pygame.font.get_default_font(), FONT_SIZE)
        text= self.font.render(f'Game Over', False, (255, 255, 255))
        self.surface.blit(text,((SCREEN_WIDTH-text.get_rect().width)/2,PLAYER_GAP))
        self.stop_game = True

    def check_collision(self):
        had_collision = False
        had_collision = collide_screen()
        indices = collide_list_of_bricks()
        for i in indices:
            del(self.bricks[i])
            had_collision = True
        had_collision &= collide_player()
        if had_collision:
            self.ball.move_back()

    
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
        return False

    def run(self):
        clock = pygame.time.Clock()
        while not self.stop_game:
            clock.tick(FRAME_RATE)
            self.player.move()
            self.ball.move()
            self.check_collision()
            self.draw()
            self.stop_game = self.check_quit()