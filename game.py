import pygame
import random

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.score = 0
        self.health = 100
        self.game_over = False

    def start(self):
        while not self.game_over:
            self.update()
            self.draw()
            self.clock.tick(60)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.create_target()
            self.check_collision()
            self.update_score()
            self.update_health()

        if self.health <= 0:
            self.game_over = True

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.show_score()
        self.show_health()
        if self.game_over:
            self.show_game_over()
        pygame.display.flip()

    def create_target(self):
        x = random.randint(0, 800)
        y = random.randint(0, 600)
        pygame.draw.circle(self.screen, (255, 0, 0), (x, y), 10)

    def check_collision(self):
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if pygame.Rect(mouse_pos[0], mouse_pos[1], 1, 1).colliderect(pygame.Rect(x, y, 10, 10)):
                        self.score += 1

    def update_score(self):
        self.score += 1

    def update_health(self):
        self.health -= 10

    def show_score(self):
        score_text = self.font.render("Score: " + str(self.score), True, (0, 0, 0))
        self.screen.blit(score_text, (10, 10))

    def show_health(self):
        health_text = self.font.render("Health: " + str(self.health), True, (0, 0, 0))
        self.screen.blit(health_text, (10, 50))

    def show_game_over(self):
        game_over_text = self.font.render("Game Over", True, (0, 0, 0))
        self.screen.blit(game_over_text, (400, 300))

game = Game()
game.start()
