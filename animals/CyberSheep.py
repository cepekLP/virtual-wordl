from Animal import Animal
from Point import Point
from World import World


class Fox(Animal):
    def __init__(self, position: Point, world_ref: World):
        super().__init__(11, 4, position, world_ref)
