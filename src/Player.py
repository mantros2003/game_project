import pygame

class Player:
    def __init__(self, img: str, x: int, y: int, screen: pygame.Surface) -> None:
        self.img_src = img
        self._X = x
        self._Y = y
        self.screen = screen

        self.img = pygame.image.load(img)
    
    def update_x(self, x: int) -> None:
        self._X = x
    
    def update_y(self, y: int) -> None:
        self._Y = y
    
    def render(self) -> None:
        self.screen.blit(self.img, (self._X, self._Y))