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
        
        try:
            image_original = pygame.image.load("assets/image/Corazon_healt.png").convert_alpha()
            self.heart_image = pygame.transform.scale(image_original, (size * 2, size * 2))
        except Exception:
            self.heart_image = None

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
            
            if self.heart_image:
                x = x_pos - self.size
                y = self.y_start - self.size
                
                if i < self.current_health:
                    self.screen.blit(self.heart_image, (x, y))

            else:
                center = (x_pos, self.y_start)
                color = self.color if i < self.current_health else self.empty_color
                fill = 0
                
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