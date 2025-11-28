import pygame

class Score:
    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.WHITE = (255, 255, 255)
        self.font = pygame.font.Font(None, 20)
        self.sound_score = pygame.mixer.Sound("assets/sounds/sound-of-collision.wav")
        self.text = self.font.render(f"Score: {self.score}", True, self.WHITE)
        
    def add(self):
        self.score += 1
        self.sound_score.play()
        self.write()
        
    def write(self):
        self.text = self.font.render(f"Score: {self.score}", True, self.WHITE)

    def draw(self):
        self.screen.blit(self.text, (20, 20))
