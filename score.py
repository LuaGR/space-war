import pygame

class Score:
    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.WHITE = (255, 255, 255)
        self.font = pygame.font.Font(None, 20)
        self.sonido_score = pygame.mixer.Sound("sounds/sounds_score.mp3")
        self.text = self.font.render(f"Score: {self.score}", True, self.WHITE)
        
    def Add(self):
        self.score += 1
        self.sonido_score.play()
        self.Write()
        
    def Write(self):
        self.text = self.font.render(f"Score: {self.score}", True, self.WHITE)

    def Draw(self):
        self.screen.blit(self.text, (20, 20))
