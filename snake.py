import pygame

class Snake:
    def __init__(self):
        self.position = [(100, 50), (90, 50), (80, 50)]
        self.direction = pygame.K_RIGHT

    def move(self, direction):
        if direction == pygame.K_RIGHT and self.direction != pygame.K_LEFT:
            self.direction = direction
        elif direction == pygame.K_LEFT and self.direction != pygame.K_RIGHT:
            self.direction = direction
        elif direction == pygame.K_UP and self.direction != pygame.K_DOWN:
            self.direction = direction
        elif direction == pygame.K_DOWN and self.direction != pygame.K_UP:
            self.direction = direction

        x, y = self.position[0]
        if self.direction == pygame.K_RIGHT:
            x += 10
        elif self.direction == pygame.K_LEFT:
            x -= 10
        elif self.direction == pygame.K_UP:
            y -= 10
        elif self.direction == pygame.K_DOWN:
            y += 10

        self.position.insert(0, (x, y))
        self.position.pop()

    def eat_food(self, food):
        if self.position[0] == food.position:
            self.position.append((0, 0))

    def check_collision(self):
        x, y = self.position[0]
        if x < 0 or x > 490 or y < 0 or y > 490:
            return True
        for segment in self.position[1:]:
            if segment == (x, y):
                return True
        return False
