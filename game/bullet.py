import pygame
class Bullet:
    def __init__(self, image: pygame.Surface | None = None, speed: int = 10):
        
        self.visible = False
        self.x = 0
        self.y = 0
        self.speed = speed

        if image is not None:
            self.image = image
        else:
            self.image = pygame.Surface((6, 16))
            self.image.fill((128, 0, 128)) 

    def shoot(self, x: float, y: float) -> None:
        self.visible = True
        self.x = x
        self.y = y
    def update(self, screen_height: int) -> None:
        if not self.visible:
            return
        self.y -= self.speed
        if self.y + self.image.get_height() < 0:
            self.visible = False
    def draw(self, screen: pygame.Surface) -> None:
        if self.visible:
            screen.blit(self.image, (self.x, self.y))
