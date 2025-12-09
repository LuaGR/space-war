import pygame
from constants import SCREEN_WIDTH

class Health_Bar:
    def __init__(self, screen, max_health=3, size=20, spacing=10):
        self.screen = screen
        self.max_health = max_health
        self.current_health = max_health
        self.size = size  
        self.spacing = spacing
        
        self.x_start = SCREEN_WIDTH - 150 
        self.y_start = 20
        self.color = (0, 255, 0) 
        self.empty_color = (50, 50, 50) 

    def lose_health(self):
        self.current_health = max(0, self.current_health - 1)

    def is_alive(self):
        return self.current_health > 0
    
    def reset_health(self):
        self.current_health = self.max_health
    def draw(self):

        for i in range(self.max_health):
            x_pos = self.x_start + i * (self.size * 2 + self.spacing)
            center = (x_pos, self.y_start)
            
            color = self.color if i < self.current_health else self.empty_color
            fill = 0 if i >= self.current_health else 0
            pygame.draw.circle(self.screen, color, (center[0] - self.size // 2, center[1]), self.size // 2, fill)
            pygame.draw.circle(self.screen, color, (center[0] + self.size // 2, center[1]), self.size // 2, fill)
            
            points = [
                (center[0] - self.size, center[1] - self.size // 4),
                (center[0] + self.size, center[1] - self.size // 4),
                (center[0], center[1] + self.size * 1.5)
            ]
            pygame.draw.polygon(self.screen, color, points, fill)

            if i >= self.current_health:
                 pygame.draw.circle(self.screen, self.empty_color, (center[0] - self.size // 2, center[1]), self.size // 2, 1)
                 pygame.draw.circle(self.screen, self.empty_color, (center[0] + self.size // 2, center[1]), self.size // 2, 1)
                 pygame.draw.polygon(self.screen, self.empty_color, points, 1)