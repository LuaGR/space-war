import sys
import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from game.player import Player
from game.bullet import Bullet
from game.enemy import Enemy
from game.score import Score
from game.healthbar import Health_Bar

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
health_bar = Health_Bar(screen)

try:
    laser_sound = pygame.mixer.Sound("assets/sounds/lazer-gun-432285.wav")
    explosion_sound = pygame.mixer.Sound("assets/sounds/explosion-under-snow-sfx-230505.wav")
except:
    laser_sound = None
    explosion_sound = None

try:
    pygame.mixer.music.load("assets/sounds/game-music-loop-7-145285.wav")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
except:
    pass

clock = pygame.time.Clock()
player = Player(shoot_sound=laser_sound)


game_over = False
start_time_ms = pygame.time.get_ticks()
elapsed_time_sec = 0

font_big = pygame.font.Font(None, 64)
font_med = pygame.font.Font(None, 36)
font_small = pygame.font.Font(None, 24)



running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if game_over:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                game_over = False
                start_time_ms = pygame.time.get_ticks()
                last_spawn_time = pygame.time.get_ticks()
                score.reset_score()
                health_bar.reset_health()
                player.reset_position()
                enemies.clear
                bullets.clear
       
        if not game_over:
            player.handle_movement(event)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                player.shoot()
                bullet = Bullet()

                bullet_x = player.x + player.size // 2 - bullet.image.get_width() // 2
                bullet_y = player.y - bullet.image.get_height()

                bullet.shoot(bullet_x, bullet_y)
                bullets.append(bullet)
        


    # ===== pantalla de game over =====
    if game_over:
        screen.fill((0, 0, 0))

        text_game_over = font_big.render("JUEGO TERMINADO", True, (255, 0, 0))
        text_score = font_med.render(f"Puntaje: {score.score}", True, (255, 255, 255))
        text_time = font_med.render(f"Tiempo: {elapsed_time_sec} s", True, (255, 255, 255))
        text_restart = font_small.render(f"presiona ENTER para reiniciar", True, (200, 200, 200))

        screen.blit(text_game_over, (SCREEN_WIDTH//2 - text_game_over.get_width()//2, SCREEN_HEIGHT//2 - 100))
        screen.blit(text_score, (SCREEN_WIDTH//2 - text_score.get_width()//2, SCREEN_HEIGHT//2 - 20))
        screen.blit(text_time, (SCREEN_WIDTH//2 - text_time.get_width()//2, SCREEN_HEIGHT//2 + 30))
        screen.blit(text_restart, (SCREEN_WIDTH//2 - text_restart.get_width()//2, SCREEN_HEIGHT//2 + 80))

        pygame.display.flip()
        clock.tick(FPS)
        continue
    


    #dificultad dinámica
    current_time = pygame.time.get_ticks()
    puntos = score.score

    max_enemigos = min(10, 4 + puntos // 2)
    current_interval = max(600, ENEMY_SPAWN_INTERVAL - puntos * 120)
    speed_factor = 1.0 + (puntos // 3) * 0.25
   


    if len(enemies) < max_enemigos and current_time - last_spawn_time > current_interval:
        enemies.append(Enemy(speed_factor=speed_factor))  # ===== Modifcado =====
        last_spawn_time = current_time

    for enemy in enemies[:]:
        enemy.update()
        if enemy.y > SCREEN_HEIGHT:
            enemies.remove(enemy)

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

    # ===== mejor colisión bala-enemigo =====
    for bullet in bullets[:]:
        if not bullet.visible:
            continue

        bullet_rect = pygame.Rect(int(bullet.x), int(bullet.y),
                                  bullet.image.get_width(), bullet.image.get_height())

        for enemy in enemies[:]:
            enemy_rect = pygame.Rect(int(enemy.x), int(enemy.y),
                                     enemy.width, enemy.height)

            if bullet_rect.colliderect(enemy_rect):
                bullets.remove(bullet)
                enemies.remove(enemy)
                if explosion_sound:
                    explosion_sound.play()
                score.add()
                break
  


    # ===== colision enemigo-jugador (GAME OVER) =====
    player_rect = pygame.Rect(int(player.x), int(player.y), player.size, player.size)

    for enemy in enemies:
        enemy_rect = pygame.Rect(int(enemy.x), int(enemy.y), enemy.width, enemy.height)

        if enemy_rect.colliderect(player_rect):
            if explosion_sound:
                explosion_sound.play()
                health_bar.lose_health()
                enemies.remove(enemy)
            if not health_bar.is_alive():
                elapsed_time_sec = (pygame.time.get_ticks() - start_time_ms) // 1000
                game_over = True
            else:
                player.reset_position()
            break
  


    player.draw(screen)
    score.draw()
    health_bar.draw()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
