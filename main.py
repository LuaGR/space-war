import sys
import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from game.player import Player
from game.bullet import Bullet
from game.enemy import Enemy 
from game.score import Score

TITLE = "Space War"
FPS = 60
ENEMY_SPAWN_INTERVAL = 2000

pygame.init()
pygame.mixer.init()

enemies = []
bullets = []
last_spawn_time = pygame.time.get_ticks()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)
score = Score(screen)
try:
    laser_sound = pygame.mixer.Sound("assets/sounds/lazer-gun-432285.wav")
    explosion_sound = pygame.mixer.Sound("assets/sounds/explosion-under-snow-sfx-230505.wav")
except FileNotFoundError as e:
    print(f"Warning: Sound file not found: {e}")
    laser_sound = None
    explosion_sound = None

try:
    pygame.mixer.music.load("assets/sounds/game-music-loop-7-145285.wav")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
except FileNotFoundError as e:
    print(f"Warning: Music file not found: {e}")

clock = pygame.time.Clock()

player = Player(shoot_sound=laser_sound)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        player.handle_movement(event)
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            player.shoot()
            bullet = Bullet()
            
            bullet_x = player.x + player.size // 2 - bullet.image.get_width() // 2
            bullet_y = player.y - bullet.image.get_height()
            
            bullet.shoot(bullet_x, bullet_y)
            bullets.append(bullet)

    current_time = pygame.time.get_ticks()
    
    if current_time - last_spawn_time > ENEMY_SPAWN_INTERVAL:
        new_enemy = Enemy()
        enemies.append(new_enemy)
        last_spawn_time = current_time

    for enemy in enemies:
        enemy.update()

    player.update()

    screen.fill((0, 0, 0))

    for enemy in enemies:
        enemy.draw(screen)

    for bullet in bullets[:]:
        bullet.update(SCREEN_HEIGHT)
        if not bullet.visible:
            bullets.remove(bullet)
            continue
        bullet.draw(screen)

    player.draw(screen)
    score.Draw()
    pygame.display.flip()

    clock.tick(FPS)

print("Saliendo del juego...")
pygame.quit()
sys.exit()
