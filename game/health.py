import pygame

class HealthManager:
    
    def __init__(self, vidas_iniciales=3, tiempo_inmunidad=2000):
        self.vidas = vidas_iniciales
        self.max_vidas = vidas_iniciales
        self.es_invencible = False
        self.tiempo_ultimo_golpe = 0
        self.duracion_inmunidad = tiempo_inmunidad  
        self.font = pygame.font.Font(None, 40)

    def recibir_daño(self):

        tiempo_actual = pygame.time.get_ticks()

        if self.es_invencible:
            if tiempo_actual - self.tiempo_ultimo_golpe > self.duracion_inmunidad:
                self.es_invencible = False  
            else:
                return False  
        self.vidas -= 1
        self.es_invencible = True
        self.tiempo_ultimo_golpe = tiempo_actual
        print(f"Se recibio el daño, las vidas que quedan son: {self.vidas}")
        return True

    def procesar_colisiones(self, player, enemies_list):

        player_rect = pygame.Rect(player.x, player.y, player.size, player.size)

        colision_detectada = False
        for enemy in enemies_list:

            enemy_rect = pygame.Rect(enemy.x, enemy.y, enemy.width, enemy.height)

            if player_rect.colliderect(enemy_rect):
                self.recibir_daño()
                colision_detectada = True
        
        return colision_detectada

    def dibujar_ui(self, screen):

        corazones = "♥ " * self.vidas
        
        if self.es_invencible:
            if (pygame.time.get_ticks() // 200) % 2 == 0:
                color = (255, 100, 100) 
            else:
                color = (255, 255, 255) 
        else:
            color = (255, 0, 0) 

        img_texto = self.font.render(f"Salud: {corazones}", True, color)
        screen.blit(img_texto, (10, 10))

    def esta_vivo(self):
        return self.vidas > 0