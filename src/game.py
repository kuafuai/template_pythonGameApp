import pygame
import random

class Game:
    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Flappy Bird")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.background = pygame.image.load("background.png").convert()
        self.bird = pygame.image.load("bird.png").convert_alpha()
        self.pipe_top = pygame.image.load("pipe_top.png").convert_alpha()
        self.pipe_bottom = pygame.image.load("pipe_bottom.png").convert_alpha()
        self.bird_rect = self.bird.get_rect()
        self.bird_rect.center = (100, self.screen_height // 2)
        self.gravity = 0.5
        self.jump_force = -10
        self.bird_movement = 0
        self.pipes = []
        self.pipe_gap = 200
        self.pipe_frequency = 1500
        self.score = 0
        self.game_over = False

    def run(self):
        while not self.game_over:
            self.clock.tick(30)
            self.handle_events()
            self.update_bird()
            self.update_pipes()
            self.check_collisions()
            self.update_score()
            self.render()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bird_movement = self.jump_force

    def update_bird(self):
        self.bird_movement += self.gravity
        self.bird_rect.centery += self.bird_movement

    def update_pipes(self):
        if self.pipes:
            for pipe in self.pipes:
                pipe.centerx -= 5
            self.pipes = [pipe for pipe in self.pipes if pipe.right > 0]
        else:
            self.create_pipe()

    def create_pipe(self):
        pipe_height = random.randint(100, 400)
        pipe_top_rect = self.pipe_top.get_rect(midbottom=(self.screen_width, pipe_height - self.pipe_gap // 2))
        pipe_bottom_rect = self.pipe_bottom.get_rect(midtop=(self.screen_width, pipe_height + self.pipe_gap // 2))
        self.pipes.append(pipe_top_rect)
        self.pipes.append(pipe_bottom_rect)

    def check_collisions(self):
        if self.bird_rect.top <= 0 or self.bird_rect.bottom >= self.screen_height:
            self.game_over = True
        for pipe in self.pipes:
            if self.bird_rect.colliderect(pipe):
                self.game_over = True

    def update_score(self):
        for pipe in self.pipes:
            if pipe.right < self.bird_rect.left and not pipe.top:
                self.score += 1

    def render(self):
        self.screen.blit(self.background, (0, 0))
        for pipe in self.pipes:
            if pipe.top:
                self.screen.blit(self.pipe_top, pipe)
            else:
                self.screen.blit(self.pipe_bottom, pipe)
        self.screen.blit(self.bird, self.bird_rect)
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        pygame.display.flip()

game = Game()
game.run()