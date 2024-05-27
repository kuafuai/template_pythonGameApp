import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("My Game")
        self.clock = pygame.time.Clock()
        self.is_running = False

    def run(self):
        self.is_running = True
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False

            self.screen.fill((0, 0, 0))
            pygame.display.flip()
            self.clock.tick(60)

    def quit(self):
        pygame.quit()

def main():
    game = Game()
    game.run()
    game.quit()
