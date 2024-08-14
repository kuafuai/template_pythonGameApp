import random
from game.player import Player

class AIPlayer(Player):
    def __init__(self, level):
        super().__init__("AI")
        self.level = level

    def decide_action(self):
        if self.level == 'easy':
            return random.choice(['play_random_card'])
        elif self.level == 'medium':
            return random.choice(['play_strategic_card', 'play_random_card'])
        elif self.level == 'hard':
            return random.choice(['play_advanced_strategic_card', 'play_strategic_card', 'play_random_card'])
