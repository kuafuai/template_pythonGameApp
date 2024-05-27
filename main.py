import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("My Game")
        self.clock = pygame.time.Clock()
        self.is_running = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def update(self):
        pass

    def render(self):
        self.screen.fill((0, 0, 0))
        pygame.display.flip()

    def run(self):
        self.is_running = True
        while self.is_running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)

    def quit(self):
        pygame.quit()

def main():
    game = Game()
    game.run()
    game.quit()