from Plant import Plant
from Point import Point
from World import World


class Guarana(Plant):
    def __init__(self, position: Point, world_ref: World):
        super().__init__(0, position, world_ref)
