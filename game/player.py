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
        size=50,
        shoot_sound=None,
        health_bar= None,
    ):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.x = x
        self.y = y
        self.speed = speed
        self.size = size
        self.shoot_sound = shoot_sound
        self.health_bar = health_bar
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False

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
        elif self.x > self.screen_width - self.size:
            self.x = self.screen_width - self.size

        if self.y < 0:
            self.y = 0
        elif self.y > self.screen_height - self.size:
            self.y = self.screen_height - self.size

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.size, self.size))

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
