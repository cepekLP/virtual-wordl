from Animal import Animal
from Point import Point
from World import World


class Wolf(Animal):
    def __init__(self, position: Point, world_ref: World):
        super().__init__(9, 5, position, world_ref)
