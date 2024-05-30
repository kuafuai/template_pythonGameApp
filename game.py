class DifficultyLevel:
    def __init__(self, level: int):
        self.level = level

    def get_level(self) -> int:
        return self.level

    def set_level(self, level: int) -> None:
        self.level = level

    def increase_level(self) -> None:
        self.level += 1

    def decrease_level(self) -> None:
        self.level -= 1


class GameProps:
    def __init__(self):
        self.props = []
        self.rewards = []

    def get_props(self) -> List[str]:
        return self.props

    def add_prop(self, prop: str) -> None:
        self.props.append(prop)

    def remove_prop(self, prop: str) -> None:
        self.props.remove(prop)

    def get_rewards(self) -> List[str]:
        return self.rewards

    def add_reward(self, reward: str) -> None:
        self.rewards.append(reward)

    def remove_reward(self, reward: str) -> None:
        self.rewards.remove(reward)


class Enemy:
    def __init__(self, name: str, health: int, damage: int):
        self.name = name
        self.health = health
        self.damage = damage

    def get_name(self) -> str:
        return self.name

    def get_health(self) -> int:
        return self.health

    def set_health(self, health: int) -> None:
        self.health = health

    def get_damage(self) -> int:
        return self.damage

    def set_damage(self, damage: int) -> None:
        self.damage = damage
