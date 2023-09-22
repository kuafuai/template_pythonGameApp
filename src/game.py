# Import necessary modules
import pygame
from src.utils import load_image

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = False
        self.score = 0
        self.bird = Bird()
        self.pipes = []
        self.background = load_image("assets/background.png")
        self.ground = Ground()
        self.font = pygame.font.Font(None, 36)
    
    def run(self):
        self.running = True
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            pygame.display.flip()
            self.clock.tick(60)
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bird.jump()
    
    def update(self):
        self.bird.update()
        self.ground.update()
        self.update_pipes()
        self.check_collision()
        self.update_score()
    
    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.bird.render(self.screen)
        self.render_pipes()
        self.ground.render(self.screen)
        self.render_score()
    
    def update_pipes(self):
        for pipe in self.pipes:
            pipe.update()
            if pipe.is_offscreen():
                self.pipes.remove(pipe)
    
    def render_pipes(self):
        for pipe in self.pipes:
            pipe.render(self.screen)
    
    def check_collision(self):
        if self.bird.is_colliding(self.ground):
            self.game_over()
        for pipe in self.pipes:
            if self.bird.is_colliding(pipe):
                self.game_over()
    
    def update_score(self):
        for pipe in self.pipes:
            if not pipe.passed and pipe.x + pipe.width < self.bird.x:
                pipe.passed = True
                self.score += 1
    
    def render_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
    
    def game_over(self):
        self.running = False

class Bird:
    def __init__(self):
        self.x = 100
        self.y = 300
        self.velocity = 0
        self.gravity = 0.5
        self.jump_power = -10
        self.image = load_image("assets/bird.png")
    
    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity
    
    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))
    
    def jump(self):
        self.velocity = self.jump_power

class Pipe:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.width = 100
        self.height = 400
        self.passed = False
        self.image = load_image("assets/pipe.png")
    
    def update(self):
        self.x -= self.speed
    
    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))
    
    def is_offscreen(self):
        return self.x + self.width < 0

class Ground:
    def __init__(self):
        self.x = 0
        self.y = 500
        self.speed = 5
        self.width = 800
        self.height = 100
        self.image = load_image("assets/ground.png")
    
    def update(self):
        self.x -= self.speed
        if self.x <= -self.width:
            self.x = 0
    
    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))

