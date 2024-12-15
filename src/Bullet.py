import pygame
from utils import on_screen

DISP_SIZE_X, DISP_SIZE_Y = 800, 600

class Bullet(pygame.sprite.Sprite):
    IMGS = ["assets/imgs/bullets/bullet_east.png" ,
            "assets/imgs/bullets/bullet_northeast.png" ,
            "assets/imgs/bullets/bullet_north.png" ,
            "assets/imgs/bullets/bullet_northwest.png" ,
            "assets/imgs/bullets/bullet_west.png" ,
            "assets/imgs/bullets/bullet_southwest.png" ,
            "assets/imgs/bullets/bullet_south.png" ,
            "assets/imgs/bullets/bullet_southeast.png"]

    def __init__(self, x: int, y: int, screen: pygame.Surface, dir: tuple, img: pygame.Surface = None) -> None:
        super().__init__()

        self._X = x
        self._Y = y
        self.screen = screen
        self.dir = dir

        if img is None:
            self.image = pygame.image.load(self.IMGS[self.get_bullet_img(dir)])
        else:
            self.image = img
        self.rect = self.image.get_rect()
        self.rect.topleft = (self._X, self._Y)

    def update_x(self, x: int) -> None:
        self._X = x
        self.rect.topleft = (self._X, self._Y)
    
    def update_y(self, y: int) -> None:
        self._Y = y
        self.rect.topleft = (self._X, self._Y)

    def update_dir(self,dir) -> None:
        self.dir = dir

    def update(self) -> None:
        if not on_screen(self._X, self._Y, (DISP_SIZE_X, DISP_SIZE_Y)):
            self.kill()
        
    def get_bullet_img(self, dir):
        x = dir[0]
        y = dir[1]
        if x == 1 and y == 0:
            return 0
        if x == 1 and y == 1:
            return 1
        if x == 0 and y == 1:
            return 2
        if x == -1 and y == 1:
            return 3
        if x == -1 and y == 0:
            return 4
        if x == -1 and y == -1:
            return 5
        if x == 0 and y == -1:
            return 6
        if x == 1 and y == -1:
            return 7