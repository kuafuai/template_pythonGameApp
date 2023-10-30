# Import necessary modules
import pygame
import random

# Implement all specific logic of the game
class Game:
    def __init__(self):
        pygame.init()
        self.window_width = 800
        self.window_height = 600
        self.background_color = (255, 255, 255)
        self.ball_color = (0, 0, 255)
        self.obstacle_color = (255, 0, 0)
        self.ball_radius = 10
        self.ball_x = self.window_width // 2
        self.ball_y = self.window_height // 2
        self.ball_speed = 5
        self.obstacle_width = 100
        self.obstacle_height = 20
        self.obstacle_x = random.randint(0, self.window_width - self.obstacle_width)
        self.obstacle_y = -self.obstacle_height
        self.obstacle_speed = 3
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.game_over = False

        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Game")

    def run(self):
        while not self.game_over:
            self.handle_events()
            self.update()
            self.draw()

    def draw(self):
        self.window.fill(self.background_color)
        pygame.draw.circle(self.window, self.ball_color, (self.ball_x, self.ball_y), self.ball_radius)
        pygame.draw.rect(self.window, self.obstacle_color, (self.obstacle_x, self.obstacle_y, self.obstacle_width, self.obstacle_height))
        score_text = self.font.render("Score: " + str(self.score), True, (0, 0, 0))
        self.window.blit(score_text, (10, 10))
        pygame.display.flip()

    def update(self):
        self.move_ball()
        self.move_obstacle()
        self.check_collision()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.move_ball("left")
                elif event.key == pygame.K_RIGHT:
                    self.move_ball("right")

    def move_ball(self, direction=None):
        if direction == "left":
            self.ball_x -= self.ball_speed
        elif direction == "right":
            self.ball_x += self.ball_speed

    def move_obstacle(self):
        self.obstacle_y += self.obstacle_speed
        if self.obstacle_y > self.window_height:
            self.generate_obstacle()

    def generate_obstacle(self):
        self.obstacle_x = random.randint(0, self.window_width - self.obstacle_width)
        self.obstacle_y = -self.obstacle_height
        self.score += 1

    def check_collision(self):
        if self.ball_x + self.ball_radius > self.obstacle_x and self.ball_x - self.ball_radius < self.obstacle_x + self.obstacle_width and self.ball_y + self.ball_radius > self.obstacle_y and self.ball_y - self.ball_radius < self.obstacle_y + self.obstacle_height:
            self.game_over = True

    def game_over(self):
        self.window.fill(self.background_color)
        game_over_text = self.font.render("Game Over", True, (0, 0, 0))
        self.window.blit(game_over_text, (self.window_width // 2 - game_over_text.get_width() // 2, self.window_height // 2 - game_over_text.get_height() // 2))
        score_text = self.font.render("Score: " + str(self.score), True, (0, 0, 0))
        self.window.blit(score_text, (self.window_width // 2 - score_text.get_width() // 2, self.window_height // 2 + score_text.get_height() // 2))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.__init__()
                        self.run()
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        return
