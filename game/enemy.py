import random
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Enemy:
    def __init__(self, speed_factor: float = 1.0):   # ===== MODIFICADO =====
        self.width = 50
        self.height = 50
        self.color = (0, 255, 0)  
        self.x = random.randint(0, SCREEN_WIDTH - self.width)
        self.y = random.randint(50, 200)
        base_speed = 2.0  

        #Velocidad ajustada según dificultad
        self.x_speed = random.choice([-1, 1]) * base_speed * speed_factor  # ===== NUEVO =====
        self.y_step = 35  # ===== nuevo (bajada al rebotar) =====

    def update(self):
        """Mover enemigo"""
        self.x += self.x_speed

        if self.x <= 0:
            self.x = 0
            self.x_speed = abs(self.x_speed)
            self.y += self.y_step    

        elif self.x + self.width >= SCREEN_WIDTH:
            self.x = SCREEN_WIDTH - self.width
            self.x_speed = -abs(self.x_speed)
            self.y += self.y_step     

    def reset_position(self):  
        self.x = random.randint(0, SCREEN_WIDTH - self.width)
        self.y = random.randint(50, 200)

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            self.color,
            (int(self.x), int(self.y), self.width, self.height)
        )
