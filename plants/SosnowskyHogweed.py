from Plant import Plant
from Point import Point
from World import World


class SosnowskyHogweed(Plant):
    def __init__(self, position: Point, world_ref: World):
        super().__init__(11, position, world_ref)
