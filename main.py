import pygame
from game import Game

def main():
    # Set up the game window
    pygame.init()
    window_width = 800
    window_height = 600
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Snake Game")

    # Create an instance of the Game class
    game = Game(window_width, window_height)

    # Game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                game.handle_events(event.key)

        # Update game state
        game.update()

        # Draw game objects
        game.draw(window)

        # Update the display
        pygame.display.update()

    # Quit the game
    pygame.quit()

if __name__ == "__main__":
    main()