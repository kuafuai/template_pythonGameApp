import pygame

class GameUI:
    def __init__(self, width, height, title):
        pygame.init()
        self.width = width
        self.height = height
        self.title = title
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)

    def draw_snake(self, snake):
        for segment in snake:
            pygame.draw.rect(self.screen, (0, 255, 0), (segment[0], segment[1], 10, 10))

    def draw_food(self, food):
        pygame.draw.rect(self.screen, (255, 0, 0), (food[0], food[1], 10, 10))

    def draw_game_over(self):
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over", True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.width/2, self.height/2))
        self.screen.blit(text, text_rect)

    def update(self):
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
