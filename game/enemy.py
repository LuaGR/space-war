# En game/enemy.py (o donde esté definida la clase Enemy)
import random
import pygame
from constants import SCREEN_WIDTH

class Enemy:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH - 50)  # Posición aleatoria en el ancho de la pantalla
        self.y = random.randint(50, 200)  # Posición aleatoria en el eje Y
        self.width = 50
        self.height = 50
        self.color = (111, 0, 111)  # Color rojo
        self.speed = 0.5  # Velocidad de movimiento

    def update(self):
        """Actualizar la posición del enemigo"""
        self.x += self.speed  # Mover al enemigo a la derecha
        
        if self.x > SCREEN_WIDTH:
            self.x = 0  # Si el enemigo se sale por la derecha, aparece de nuevo en la izquierda

    def draw(self, screen):
        """Dibujar al enemigo en la pantalla"""
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    