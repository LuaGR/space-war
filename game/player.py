import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

class Player:
    def __init__(
        self,
        screen_width=SCREEN_WIDTH,
        screen_height=SCREEN_HEIGHT,
        x=400,
        y=300,
        speed=5,
        size_width=80,
        size_height=60,
        shoot_sound=None,
    ):
        self.initial_x = x
        self.initial_y = y
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.x = x
        self.y = y
        self.speed = speed
        
        
        self.size_width = size_width
        self.size_height = size_height
        
        
        self.size = size_width 

        self.shoot_sound = shoot_sound
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False

        
        self.image = None
        try:
            
            original_image = pygame.image.load("assets/image/Paloma_meme_1.png")
            self.image = pygame.transform.scale(original_image, (size_width, size_height))
        except Exception as e:
            print(f"No se pudo cargar la imagen del jugador: {e}")
            self.image = None 

    def handle_movement(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.move_left = True
            elif event.key == pygame.K_d:
                self.move_right = True
            elif event.key == pygame.K_w:
                self.move_up = True
            elif event.key == pygame.K_s:
                self.move_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.move_left = False
            elif event.key == pygame.K_d:
                self.move_right = False
            elif event.key == pygame.K_w:
                self.move_up = False
            elif event.key == pygame.K_s:
                self.move_down = False

    def update(self):
        if self.move_left:
            self.x -= self.speed
        if self.move_right:
            self.x += self.speed
        if self.move_up:
            self.y -= self.speed
        if self.move_down:
            self.y += self.speed

        if self.x < 0:
            self.x = 0
        elif self.x > self.screen_width - self.size_width:
            self.x = self.screen_width - self.size_width

        if self.y < 0:
            self.y = 0
        elif self.y > self.screen_height - self.size_height:
            self.y = self.screen_height - self.size_height

    def draw(self, screen):
        if self.image:
            screen.blit(self.image, (self.x, self.y))
        else:
            pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.size_width, self.size_height))

    def shoot(self):
        if self.shoot_sound:
            self.shoot_sound.play()
            
    def reset_position(self):
        self.x = self.initial_x
        self.y = self.initial_y
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False
