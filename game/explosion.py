import pygame

class Explosion:
    def __init__(self, x, y):
        self.images = []

        for i in range(1, 6):
            size = i * 15
            img = pygame.Surface((size, size), pygame.SRCALPHA)

            red = 255
            green = max(0, 255 - (i * 50))
            blue = 0

            pygame.draw.circle(img, (red, green, blue), (size // 2, size // 2), size // 2)
            self.images.append(img)

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.counter = 0
        self.speed = 3
        self.finished = False

    def update(self):
        self.counter += 1

        if self.counter >= self.speed:
            self.counter = 0
            self.index += 1

            if self.index < len(self.images):
                self.image = self.images[self.index]
                center_pos = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = center_pos
            else:
                self.finished = True

    def draw(self, screen):
        if not self.finished:
            screen.blit(self.image, self.rect)