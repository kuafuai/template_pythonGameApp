import random

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.generate()

    def generate(self):
        self.position = (random.randint(0, 19) * 20, random.randint(0, 19) * 20)
