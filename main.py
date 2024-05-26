import game
import game_ui

def main():
    game_obj = game.Game()
    game_ui_obj = game_ui.GameUI(game_obj)
    game_ui_obj.run_game_loop()

if __name__ == "__main__":
    main()
