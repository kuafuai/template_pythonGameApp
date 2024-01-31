class Player:
    def __init__(self, name):
        self.name = name
        self.gold = 0
        self.units = []
        self.buildings = []

    def get_name(self) -> str:
        return self.name

    def get_gold(self) -> int:
        return self.gold

    def add_gold(self, amount):
        self.gold += amount

    def subtract_gold(self, amount):
        self.gold -= amount

    def get_units(self):
        return self.units

    def add_unit(self, unit):
        self.units.append(unit)

    def remove_unit(self, unit):
        self.units.remove(unit)

    def get_buildings(self):
        return self.buildings

    def add_building(self, building):
        self.buildings.append(building)

    def remove_building(self, building):
        self.buildings.remove(building)
