
import pygame
import random

class Enemy:
    def __init__(self):
        # Initial position and movement of the enemy
        self.enemy_x = random.randint(0, 733)
        self.enemy_y = random.randint(50, 200)
        self.enemy_width = 50  # Width of the enemy rectangle
        self.enemy_height = 50  # Height of the enemy recta
        self.enemy_x_change = 0.3
        self.enemy_y_change = 50

        # Color for the enemy (using RGB values)
        self.enemy_color = (255, 0, 0)  # Red color

    def draw_enemy(self, screen):
        # Draw the enemy as a red rectangle
        pygame.draw.rect(screen, self.enemy_color, (self.enemy_x, self.enemy_y, self.enemy_width, self.enemy_height))

    def update_enemy(self):
        # Update the enemy position
        self.enemy_x += self.enemy_x_change

        # Check if the enemy hits the screen edges
        if self.enemy_x <= 0:
            self.enemy_x_change = 0.3
            self.enemy_y += self.enemy_y_change
        elif self.enemy_x >= 736:
            self.enemy_x_change = -0.3
            self.enemy_y += self.enemy_y_change

        # Return updated positions
        return self.enemy_x, self.enemy_y 
    