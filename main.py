# game.py

class Game:
    def __init__(self):
        # Initialize game variables
        pass

    def initialize(self):
        # Initialize game state
        pass

    def update(self):
        # Update game state
        pass

    def draw(self):
        # Draw game objects on the screen
        pass

    def handle_events(self):
        # Handle user input events
        pass

    def game_over(self):
        # Handle game over condition
        pass

# game_ui.py

class GameUI:
    def __init__(self, game):
        self.game = game

    def run_game_loop(self):
        self.game.initialize()

        while True:
            self.game.handle_events()
            self.game.update()
            self.game.draw()

            if self.game.game_over():
                break
