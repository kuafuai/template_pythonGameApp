import game.ai

class Player:
    def __init__(self, name):
        self.name = name
        self.hand_cards = []  # 初始玩家手牌为空

    def call_landlord(self):
        # 玩家叫地主的逻辑
        print(f"{self.name} is calling landlord.")

    def play_card(self, cards):
        # 玩家出牌的逻辑
        print(f"{self.name} is playing cards: {cards}")
        # 这里可以添加逻辑来更新手牌
