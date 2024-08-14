import pygame

class GameUI:
    def __init__(self, game):
        self.game = game
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Game UI")

    def render(self):
        self.screen.fill((0, 0, 0))  # Clear screen
        # Draw player hands
        # Assuming game has player and opponent attributes with hand cards
        player_hand = self.game.player.hand
        opponent_hand = self.game.opponent.hand
        public_cards = self.game.public_cards

        # Render player hand
        self.draw_hand(player_hand, (50, 500))
        # Render opponent hand (hidden for the user)
        self.draw_hand(opponent_hand, (50, 100), hidden=True)
        # Render public cards
        self.draw_hand(public_cards, (300, 300))

        pygame.display.flip()  # Update the full display Surface to the screen

    def draw_hand(self, cards, position, hidden=False):
        for index, card in enumerate(cards):
            card_pos = (position[0] + index * 30, position[1])
            if hidden:
                pygame.draw.rect(self.screen, (100, 100, 100), (*card_pos, 40, 60))  # Draw a rectangle for hidden card
            else:
                # Assume card has a draw method or surface to draw
                pygame.draw.rect(self.screen, (255, 255, 255), (*card_pos, 40, 60))  # Sample drawing for visible card

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    self.game.start_game()
                elif event.key == pygame.K_p:
                    self.game.pause_game()
                elif event.key == pygame.K_e:
                    self.game.end_game()
