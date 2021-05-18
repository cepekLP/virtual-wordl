import World
from Point import Point


class Organism:
    def __init__(
        self,
        strength: int,
        initiative: int,
        position: Point,
        world_ref: World.World,
    ) -> None:
        self.strength = strength
        self.initiative = initiative
        self.position = position
        self.world = world_ref

    def multiply(self):
        pass
