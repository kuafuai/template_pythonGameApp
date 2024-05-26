import pygame
from pygame.locals import *
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()

class Snake:
    def __init__(self):
        self.body = [(200, 50), (190, 50), (180, 50)]
        self.direction = "RIGHT"

class Food:
    def __init__(self):
        self.position = (random.randint(0, 39) * 20, random.randint(0, 29) * 20)

game = Game()
