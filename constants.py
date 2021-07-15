
#####################################################
#
# breakout game with pygame
# for Python stage in Technofutur TIC (Belgium)

# Authors : Bastien Wiaux and Benoit Ronval
#
#####################################################


# Constants for screen

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 480
FRAME_RATE = 60
FONT_SIZE = 30


# constants for player

PLAYER_WIDTH = 150
PLAYER_HEIGHT = 10
PLAYER_SPEED = 10
PLAYER_GAP = 5
PLAYER_START_X = SCREEN_WIDTH // 2 - PLAYER_WIDTH // 2 
PLAYER_START_Y = SCREEN_HEIGHT - PLAYER_GAP - PLAYER_HEIGHT
PLAYER_LIFE = 3


# constants for ball

BALL_RADIUS = 10
BALL_START_X = SCREEN_WIDTH // 2
BALL_START_Y = PLAYER_START_Y - 20
BALL_SPEED = 2
TIME_BEFORE_RELAUNCH = 2000 #[ms]


# constants for bricks

BRICK_WIDTH = 75
BRICK_HEIGHT = 30
BRICK_ROWS = 3
BRICK_COLUMNS = 8
BRICK_GAP = 5
BRICK_TOP_VOID = 50

