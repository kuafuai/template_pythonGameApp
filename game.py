import pygame
import random

class AimTrainer:
    def __init__(self, width, height, target_num, target_speed, target_size, target_color, player_color):
        pygame.init()
        self.width = width
        self.height = height
        self.target_num = target_num
        self.target_speed = target_speed
        self.target_size = target_size
        self.target_color = target_color
        self.player_color = player_color
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.targets = []
        self.player = None
        self.scoreboard = None
        self.clock = pygame.time.Clock()
        self.score = 0
        self.health = 3
        self.game_over = False

        for _ in range(self.target_num):
            x = random.randint(0, self.width - self.target_size)
            y = random.randint(0, self.height - self.target_size)
            target = Target(x, y, self.target_size, self.target_color, self.target_speed)
            self.targets.append(target)

        self.player = Player(self.width // 2, self.height // 2, 20, self.player_color)
        self.scoreboard = Scoreboard(10, 10, 20, (255, 255, 255))

    def run(self):
        while not self.game_over:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.check_collision()

    def update(self):
        for target in self.targets:
            target.move()
        self.player.move(*pygame.mouse.get_pos())

    def draw(self):
        self.screen.fill((0, 0, 0))
        for target in self.targets:
            target.draw()
        self.player.draw()
        self.scoreboard.draw()
        pygame.display.flip()

    def check_collision(self):
        for target in self.targets:
            if target.rect.colliderect(self.player.rect):
                self.increase_score()
                self.targets.remove(target)
                break
        else:
            self.decrease_health()

    def increase_score(self):
        self.score += 1
        self.scoreboard.update_score(self.score)

    def decrease_health(self):
        self.health -= 1
        self.scoreboard.update_health(self.health)
        if self.health == 0:
            self.game_over()

    def reset(self):
        self.targets = []
        for _ in range(self.target_num):
            x = random.randint(0, self.width - self.target_size)
            y = random.randint(0, self.height - self.target_size)
            target = Target(x, y, self.target_size, self.target_color, self.target_speed)
            self.targets.append(target)
        self.score = 0
        self.health = 3
        self.scoreboard.update_score(self.score)
        self.scoreboard.update_health(self.health)

    def game_over(self):
        self.game_over = True


class Target:
    def __init__(self, x, y, size, color, speed):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.speed = speed
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def move(self):
        self.x += self.speed
        if self.x > 800:
            self.x = 0
            self.y = random.randint(0, 600)
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def draw(self):
        pygame.draw.rect(pygame.display.get_surface(), self.color, self.rect)


class Player:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def move(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def draw(self):
        pygame.draw.rect(pygame.display.get_surface(), self.color, self.rect)


class Scoreboard:
    def __init__(self, x, y, font_size, font_color):
        self.x = x
        self.y = y
        self.font_size = font_size
        self.font_color = font_color
        self.font = pygame.font.Font(None, self.font_size)
        self.score_text = self.font.render("Score: 0", True, self.font_color)
        self.health_text = self.font.render("Health: 3", True, self.font_color)

    def update_score(self, score):
        self.score_text = self.font.render(f"Score: {score}", True, self.font_color)

    def update_health(self, health):
        self.health_text = self.font.render(f"Health: {health}", True, self.font_color)

    def draw(self):
        pygame.display.get_surface().blit(self.score_text, (self.x, self.y))
        pygame.display.get_surface().blit(self.health_text, (self.x, self.y + self.font_size + 5))
