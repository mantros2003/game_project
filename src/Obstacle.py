import pygame

class Obstacle(pygame.sprite.Sprite):
    OBSTACLE_IMG_SRC = "assets/imgs/wood.png"

    def __init__(self, x: int, y: int, screen: pygame.Surface, img: pygame.Surface = None) -> None:
        super().__init__()

        self._X = x
        self._Y = y
        self.radius = self._X
        self.screen = screen

        if img is None:
            self.image = pygame.image.load(self.OBSTACLE_IMG_SRC)
        else:
            self.image = img
        self.rect = self.image.get_rect()
        self.rect.topleft = (self._X, self._Y)
        #self.render()
    
    def update(self) -> None:
        return