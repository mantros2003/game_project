import pygame

class Player(pygame.sprite.Sprite):
    PLAYER_IMG_SRC = "assets/imgs/crazy.png"

    def __init__(self, x: int, y: int, screen: pygame.Surface) -> None:
        super().__init__()
        
        self._X = x
        self._Y = y
        self.screen = screen

        self.img = pygame.image.load(self.PLAYER_IMG_SRC)
    
    def update_x(self, x: int) -> None:
        self._X = x
    
    def update_y(self, y: int) -> None:
        self._Y = y
    
    def render(self) -> None:
        self.screen.blit(self.img, (self._X, self._Y))