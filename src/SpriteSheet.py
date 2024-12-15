import pygame

class SpriteSheet():
    def __init__(self, img_src: str, height: int, width: int) -> None:
        self._img = pygame.image.load(img_src)
        self._height = height
        self._width = width
    
    def load(self, height: int, width: int) -> pygame.surface.Surface:
        return pygame.surface.Surface()