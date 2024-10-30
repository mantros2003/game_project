import pygame
import Player
import Obstacle
import utils
#import random

# Display constants
DISP_SIZE_X, DISP_SIZE_Y = 800, 600

# Player Constants
PLAYER_IMG_SRC = "assets/imgs/crazy.png"
PLAYER_DEF_X = 370
PLAYER_DEF_Y = 400

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((DISP_SIZE_X, DISP_SIZE_Y))
pygame.display.set_caption("Paadu Game")

# Initialize player
player1 = Player.Player("assets/imgs/crazy.png", 370, 400, screen)
xChange, yChange = 0, 0

# Initialize Obstacle
obstacles = [None] * 3
obstacles[0] = Obstacle.Obstacle("assets/imgs/wood.png", 150, 40, screen)
obstacles[1] = Obstacle.Obstacle("assets/imgs/wood.png", 600, 530, screen)
obstacles[2] = Obstacle.Obstacle("assets/imgs/wood.png", 230, 270, screen)

def player(x, y):
    screen.blit(PLAYER_IMG_SRC, (x, y))

running = True
while running:
    screen.fill((255, 255, 255))

    # Event Checker
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Event of pressing down a key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xChange = -0.3
            if event.key == pygame.K_RIGHT:
                xChange = 0.3
            if event.key == pygame.K_UP:
                yChange = -0.3
            if event.key == pygame.K_DOWN:
                yChange = 0.3
        
        # Event of releasing a key
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                xChange = 0
            if event.key == pygame.K_RIGHT:
                xChange = 0
            if event.key == pygame.K_UP:
                yChange = 0
            if event.key == pygame.K_DOWN:
                yChange = 0
    
    # Update position
    player1.update_x(player1._X + xChange)
    player1.update_y(player1._Y + yChange)

    # Check boundary
    if player1._X < 0:
        player1.update_x(0)
    if player1._X > DISP_SIZE_X - 64:
        player1.update_x(DISP_SIZE_X - 64)
    if player1._Y < 0:
        player1.update_y(0)
    if player1._Y > DISP_SIZE_Y - 64:
        player1.update_y(DISP_SIZE_Y - 64)
    
    # Collision with obstacles
    for obstacle in obstacles:
        collision = utils.detect_collision_edge({'x': obstacle._X, 'y': obstacle._Y, "width": 64, "height": 64}, {'x': player1._X, 'y': player1._Y, "width": 64, "height": 64})
        if not collision is None:
            if collision == "top":
                player1.update_y(obstacle._Y - 64)
            if collision == "bottom":
                player1.update_y(obstacle._Y + 64)
            if collision == "left":
                player1.update_x(obstacle._X - 64)
            if collision == "right":
                player1.update_x(obstacle._X + 64)

    player1.render()
    for obstacle in obstacles:
        obstacle.render()

    pygame.display.update()