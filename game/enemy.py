
import random
import pygame
from constants import SCREEN_WIDTH

class Enemy:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH - 50)  
        self.y = random.randint(50, 200)  
        self.width = 50
        self.height = 50
        self.color = (111, 0, 111)  
        self.speed = 0.5  

    def update(self):
        """Actualizar la posición del enemigo"""
        self.x += self.speed  
        
        if self.x > SCREEN_WIDTH:
            self.x = 0  

    def draw(self, screen):
        """Dibujar al enemigo en la pantalla"""
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    