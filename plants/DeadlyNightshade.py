from Plant import Plant
from Point import Point
from World import World


class DeadlyNightshade(Plant):
    def __init__(self, position: Point, world_ref: World):
        super().__init__(99, position, world_ref)
