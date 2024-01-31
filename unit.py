import pygame

class Unit:
    def __init__(self, name, hp, attack, move_range):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.move_range = move_range
        self.x = 0
        self.y = 0

    def get_name(self) -> str:
        return self.name

    def get_hp(self) -> int:
        return self.hp

    def get_attack(self) -> int:
        return self.attack

    def get_move_range(self) -> int:
        return self.move_range

    def move(self, x, y):
        self.x = x
        self.y = y

    def attack(self, target):
        target.hp -= self.attack
