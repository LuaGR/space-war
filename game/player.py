import pygame
import sys
import pygame

class Player:
    def __init__(self):
        self.mover_izquierda = False
        self.mover_derecha = False
        self.mover_arriba = False
        self.mover_abajo = False
        self.x = 400
        self.y = 300
        self.velocidad = 5
    # Detectar movimiento mediante la tecla
    def Move(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.mover_izquierda = True
            elif event.key == pygame.K_d:
                self.mover_derecha = True
            elif event.key == pygame.K_w:
                self.mover_arriba = True
            elif event.key == pygame.K_s:
                self.mover_abajo = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.mover_izquierda = False
            elif event.key == pygame.K_d:
                self.mover_derecha = False
            elif event.key == pygame.K_w:
                self.mover_arriba = False
            elif event.key == pygame.K_s:
                self.mover_abajo = False
    # Movimiento dependiendo la tecla pulsada
    def update(self):
        if self.mover_izquierda:
            self.x -= self.velocidad
        if self.mover_derecha:
            self.x += self.velocidad
        if self.mover_arriba:
            self.y -= self.velocidad
        if self.mover_abajo:
            self.y += self.velocidad

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, 50, 50))
