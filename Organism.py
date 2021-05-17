from World import World


class Point:
    x: int
    y: int


class Organism:
    def __init__(
        self, strength: int, initiative: int, position: Point, world_ref: World
    ) -> None:
        self.strength = strength
        self.initiative = initiative
        self.position = position
        self.world = world_ref

    def multiply(self):
        pass
