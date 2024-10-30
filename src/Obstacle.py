import pygame

class Obstacle:
    def __init__(self, img: str, x: int, y: int, screen: pygame.Surface) -> None:
        self.img_src = img
        self._X = x
        self._Y = y
        self.screen = screen

        self.img = pygame.image.load(img)
        #self.render()
    
    def render(self) -> None:
        self.screen.blit(self.img, (self._X, self._Y))