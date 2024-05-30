import pygame
from pygame.locals import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.is_running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.is_running = False

    def update(self):
        pass

    def draw(self):
        pass

    def run(self):
        while self.is_running:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)

class MathModelGame(Game):
    def __init__(self):
        super().__init__()

    def create_shape(self, shape_type):
        if shape_type == "rectangle":
            shape = Rectangle()
        elif shape_type == "circle":
            shape = Circle()
        elif shape_type == "triangle":
            shape = Triangle()
        else:
            raise ValueError("Invalid shape type")
        self.draw_shape(shape)

    def handle_input(self, input):
        shape_type = input.lower()
        self.create_shape(shape_type)

    def handle_mouse_drag(self, event):
        pass

    def handle_mouse_scroll(self, event):
        pass

    def draw_shape(self, shape):
        shape.draw()

class Shape:
    def __init__(self):
        pass

    def draw(self):
        pass

class Rectangle(Shape):
    def __init__(self):
        super().__init__()

    def draw(self):
        pygame.draw.rect(self.screen, (255, 0, 0), (100, 100, 200, 100))

class Circle(Shape):
    def __init__(self):
        super().__init__()

    def draw(self):
        pygame.draw.circle(self.screen, (0, 255, 0), (400, 300), 50)

class Triangle(Shape):
    def __init__(self):
        super().__init__()

    def draw(self):
        pygame.draw.polygon(self.screen, (0, 0, 255), [(600, 100), (700, 200), (500, 200)])

if __name__ == "__main__":
    game = MathModelGame()
    game.run()
