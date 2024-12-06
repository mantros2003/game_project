import pygame

class Bullet:
    IMGS = ["assets/imgs/bullets/bullet_east.png" ,
            "assets/imgs/bullets/bullet_northeast.png" ,
            "assets/imgs/bullets/bullet_north.png" ,
            "assets/imgs/bullets/bullet_northwest.png" ,
            "assets/imgs/bullets/bullet_west.png" ,
            "assets/imgs/bullets/bullet_southwest.png" ,
            "assets/imgs/bullets/bullet_south.png" ,
            "assets/imgs/bullets/bullet_southeast.png"]

    def __init__(self, x: int, y: int, screen: pygame.Surface, state: str, dir: tuple, img: pygame.Surface = None) -> None:
        self._X = x
        self._Y = y
        self.screen = screen
        self.state = state
        self.dir = dir

        if img is None:
            self.img = pygame.image.load(self.IMGS[self.get_bullet_img(dir)])
        else:
            self.img = img
        #self.img = pygame.image.load(self.IMGS[self.get_bullet_img(dir)])

    def update_x(self, x: int) -> None:
        self._X = x
    
    def update_y(self, y: int) -> None:
        self._Y = y

    def update_dir(self,dir) -> None:
        self.dir = dir

    def fire(self) -> None:
        self.state = "fire"
        self.screen.blit(self.img, (self._X, self._Y))
    
    def get_bullet_img(self, dir):
        x = dir[0]
        y = dir[1]
        if( x == 1 and y == 0 ):
            return 0
        if( x == 1 and y == 1 ):
            return 1
        if( x == 0 and y == 1 ):
            return 2
        if( x == -1 and y == 1 ):
            return 3
        if( x == -1 and y == 0 ):
            return 4
        if( x == -1 and y == -1 ):
            return 5
        if( x == 0 and y == -1 ):
            return 6
        if( x == 1 and y == -1 ):
            return 7