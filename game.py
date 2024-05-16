import pygame
from pygame.locals import *
from player import Player
from map import Map
from obstacle import Obstacle
from enemy import Enemy
from item import Item

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.map = Map()
        self.obstacle = Obstacle()
        self.enemy = Enemy()
        self.item = Item()
        self.game_over = False

    def start(self):
        while not self.game_over:
            self.update()
            self.draw()
            self.handle_input()
            self.check_collision()
            pygame.display.flip()
            self.clock.tick(60)

    def update(self):
        self.player.update()
        self.enemy.update()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.map.draw(self.screen)
        self.obstacle.draw(self.screen)
        self.player.draw(self.screen)
        self.enemy.draw(self.screen)
        self.item.draw(self.screen)

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.game_over = True
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    self.player.jump()

    def check_collision(self):
        if pygame.sprite.collide_rect(self.player, self.obstacle):
            self.game_over = True
        if pygame.sprite.collide_rect(self.player, self.enemy):
            self.game_over = True
        if pygame.sprite.collide_rect(self.player, self.item):
            self.item.collect()
    
    def game_over(self):
        pass

    def restart(self):
        pass
