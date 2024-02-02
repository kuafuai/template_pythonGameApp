import pygame

class DouyinGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Douyin Game")

    def main(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((255, 255, 255))
            pygame.display.flip()

        pygame.quit()

def main():
    game = DouyinGame()
    game.main()
