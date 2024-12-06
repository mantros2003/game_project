import pygame
import Player
import Obstacle
import Bullet
import utils
import time
#import random

# Display constants
DISP_SIZE_X, DISP_SIZE_Y = 800, 600

# Player Constants
PLAYER_DEF_X = 370
PLAYER_DEF_Y = 400

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((DISP_SIZE_X, DISP_SIZE_Y))
pygame.display.set_caption("Paadu Game")

# Initialize player
player1 = Player.Player(370, 400, screen)
xChange, yChange = 0, 0

# Initialize Obstacle
obstacles = [None] * 3
obstacles[0] = Obstacle.Obstacle(150, 40, screen)
obstacles[1] = Obstacle.Obstacle(600, 530, screen, obstacles[0].img)
obstacles[2] = Obstacle.Obstacle(230, 270, screen, obstacles[0].img)

# Bullet constants
COOLDOWN_TIME = 0.2
MAX_BULLET = 3
bullet_queue = []
wasd_arr = [False] * 4
last_fire_time = -1

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
            if event.key == pygame.K_w:
                wasd_arr[0] = True
            if event.key == pygame.K_a:
                wasd_arr[1] = True
            if event.key == pygame.K_s:
                wasd_arr[2] = True
            if event.key == pygame.K_d:
                wasd_arr[3] = True
        
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
            if event.key == pygame.K_w:
                wasd_arr[0] = False
            if event.key == pygame.K_a:
                wasd_arr[1] = False
            if event.key == pygame.K_s:
                wasd_arr[2] = False
            if event.key == pygame.K_d:
                wasd_arr[3] = False
    
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
    '''
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
    '''
    
    for obstacle in obstacles:
       if utils.detect_collsiosion_circular(player1._X,  player1._Y,  obstacle._X,  obstacle._Y, 64) :
           correct = utils.collision_correct(player1._X,  player1._Y,  obstacle._X,  obstacle._Y, 64)
           player1._X = correct[0]
           player1._Y = correct[1]

    # Checking Bullet
    if wasd_arr.count(True) in [1, 2] and (wasd_arr[0]^wasd_arr[2] or wasd_arr[1]^wasd_arr[3]):
        dir = utils.attack_direction(wasd_arr[1], wasd_arr[2], wasd_arr[3], wasd_arr[0])
        if len(bullet_queue) in range(MAX_BULLET) and time.time() - last_fire_time > COOLDOWN_TIME:
            bullet_queue.append(Bullet.Bullet(player1._X, player1._Y, screen, "fire", dir))
            last_fire_time = time.time()

    for obstacle in obstacles:
        obstacle.render()
    
    # To remove bullets
    to_remove = [False] * MAX_BULLET
    # Update and render bullets
    for i in range(len(bullet_queue)):
        bullet_queue[i].update_x(bullet_queue[i]._X + 2 * bullet_queue[i].dir[0])
        bullet_queue[i].update_y(bullet_queue[i]._Y - 2 * bullet_queue[i].dir[1])
        if not utils.on_screen(bullet_queue[i]._X, bullet_queue[i]._Y, (DISP_SIZE_X, DISP_SIZE_Y)):
            to_remove[i] = True
        else:
            bullet_queue[i].fire()
    
    # Remove bullets
    for i in range(MAX_BULLET - 1, -1, -1):
        if to_remove[i]:
            bullet_queue.pop(i)
            to_remove[i] = False

    player1.render()

    pygame.display.update()