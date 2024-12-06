import pygame

class Bullet:
    def __init__(self, x: int, y: int, screen: pygame.Surface ,state ,dir) -> None:
       
        self._X = x
        self._Y = y
        self.screen = screen
        self.state = state      
        self.dir = dir
    def update_x(self, x: int) -> None:
        self._X = x
    
    def update_y(self, y: int) -> None:
        self._Y = y
    def update_dir(self,dir) -> None:
        self._Dir = dir
    
   #  def render(self) -> None:
   #      self.screen.blit(self.img, (self._X, self._Y))
    def fire(self , img , x ,y)-> None:
        self.state = "fire"
        self._X = x 
        self._Y = y 
        self.screen.blit( img,(x,y))
        