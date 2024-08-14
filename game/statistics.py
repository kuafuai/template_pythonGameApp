class GameStatistics:
    def __init__(self):
        self.total_games = 0
        self.wins = 0

    def record_score(self, score):
        self.total_games += 1
        if score > 0:
            self.wins += 1

    def display_statistics(self):
        if self.total_games == 0:
            win_rate = 0
        else:
            win_rate = (self.wins / self.total_games) * 100
        
        print(f"Total Games: {self.total_games}")
        print(f"Wins: {self.wins}")
        print(f"Win Rate: {win_rate:.2f}%")
