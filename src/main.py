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
PLAYER_SPEED_X = 4
PLAYER_SPEED_Y = 4

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((DISP_SIZE_X, DISP_SIZE_Y))
pygame.display.set_caption("Paadu Game")
clock = pygame.time.Clock()
FPS = 60

# Initialize player
player1 = Player.Player(370, 400, screen)
xChange, yChange = 0, 0

# Initialize Obstacle
OBSTACLE_COUNT = 3
obstacles = pygame.sprite.Group()
obstacles.add(Obstacle.Obstacle(150, 40, screen))
obstacles.add(Obstacle.Obstacle(600, 530, screen, obstacles.sprites()[0].image))
obstacles.add(Obstacle.Obstacle(230, 270, screen, obstacles.sprites()[0].image))

# Bullet constants
COOLDOWN_TIME = 0.2
MAX_BULLET = 3
bullets = pygame.sprite.Group()
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
            if event.key == pygame.K_w:
                wasd_arr[0] = False
            if event.key == pygame.K_a:
                wasd_arr[1] = False
            if event.key == pygame.K_s:
                wasd_arr[2] = False
            if event.key == pygame.K_d:
                wasd_arr[3] = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player1.update_x(player1._X - PLAYER_SPEED_X)
    if keys[pygame.K_RIGHT]:
        player1.update_x(player1._X + PLAYER_SPEED_X)
    if keys[pygame.K_UP]:
        player1.update_y(player1._Y - PLAYER_SPEED_Y)
    if keys[pygame.K_DOWN]:
        player1.update_y(player1._Y + PLAYER_SPEED_Y)

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
    
    # Corrects the collsion by pushing out the object
    for obstacle in obstacles.sprites():
       if utils.detect_collsiosion_circular(player1._X,  player1._Y,  obstacle._X,  obstacle._Y, 64) :
           correct = utils.collision_correct(player1._X,  player1._Y,  obstacle._X,  obstacle._Y, 64)
           player1._X = correct[0]
           player1._Y = correct[1]

    # Checking Bullet
    if wasd_arr.count(True) in [1, 2] and (wasd_arr[0]^wasd_arr[2] or wasd_arr[1]^wasd_arr[3]):
        dir = utils.attack_direction(wasd_arr[1], wasd_arr[2], wasd_arr[3], wasd_arr[0])
        if len(bullets.sprites()) in range(MAX_BULLET) and time.time() - last_fire_time > COOLDOWN_TIME:
            bullets.add(Bullet.Bullet(player1._X, player1._Y, screen, dir))
            last_fire_time = time.time()

    # Update and render bullets
    for i in range(len(bullets.sprites())):
        bullets.sprites()[i].update_x(bullets.sprites()[i]._X + 20 * bullets.sprites()[i].dir[0])
        bullets.sprites()[i].update_y(bullets.sprites()[i]._Y - 20 * bullets.sprites()[i].dir[1])

    for obstacle in obstacles.sprites():
        pygame.sprite.groupcollide(obstacles, bullets, False, True, pygame.sprite.collide_rect)

    obstacles.draw(screen)

    bullets.update()
    bullets.draw(screen)

    player1.render()

    pygame.display.update()

    clock.tick(FPS)