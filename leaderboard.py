class Leaderboard:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = []

    def load(self):
        try:
            with open(self.file_path, 'r') as file:
                self.data = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            print(f"File {self.file_path} not found.")

    def save(self):
        with open(self.file_path, 'w') as file:
            for line in self.data:
                file.write(line + '\n')

    def add_score(self, score):
        self.data.append(score)

    def get_ranking(self):
        return self.data
