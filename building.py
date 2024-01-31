class Building:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def get_name(self) -> str:
        return self.name

    def get_cost(self) -> int:
        return self.cost

    def build(self):
        # Code to build the building
        pass
