import sys

import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from game.player import Player
from game.bullet import Bullet

TITLE = "Space War"
FPS = 60

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()

running = True

player = Player()
bullets = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        player.handle_movement(event)
        # crear una nueva bala al pulsar espacio
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            b = Bullet()
            # calcular posición a partir de Player (usa x, y, size)
            bx = player.x + player.size // 2 - b.image.get_width() // 2
            by = player.y - b.image.get_height()
            b.shoot(bx, by)
            bullets.append(b)

    player.update()

    # pintar fondo y entidades (fuera del bucle de eventos)
    screen.fill((0, 0, 0))

    # actualizar y dibujar balas; eliminar las no visibles
    for b in bullets[:]:
        b.update(SCREEN_HEIGHT)
        if not b.visible:
            bullets.remove(b)
            continue
        b.draw(screen)

    player.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

print("Saliendo del juego...")
pygame.quit()
sys.exit()
