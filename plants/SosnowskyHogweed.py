import random

from Plant import Plant, PLANT_DELAY, PLANT_CHANCE_TO_MULTIPLY
from Point import Point
from World import World


class SosnowskyHogweed(Plant):
    def __init__(self, position: Point, world_ref: World):
        super().__init__(11, position, world_ref)

    def action(self):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i != 0 and j != 0:
                    organism = self.world.check_collision(Point(i, j))
                    if organism is not None:
                        self.world.remove_organism(organism)

        if random.random() < PLANT_CHANCE_TO_MULTIPLY and self.delay == 0:
            self.multiply()
            self.delay = PLANT_DELAY
        elif self.delay > 0:
            self.delay = self.delay - 1
