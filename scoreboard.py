import pygame

class Scoreboard:
    def __init__(self, x, y, font_size, color):
        self.x = x
        self.y = y
        self.font_size = font_size
        self.color = color
        self.font = pygame.font.Font(None, self.font_size)

    def draw(self, screen, score):
        text = self.font.render(f"Score: {score}", True, self.color)
        screen.blit(text, (self.x, self.y))
