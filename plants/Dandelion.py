import random

from Plant import Plant, PLANT_DELAY, PLANT_CHANCE_TO_MULTIPLY
from Point import Point
from World import World


class Dandelion(Plant):
    def __init__(self, position: Point, world_ref: World):
        super().__init__(0, position, world_ref)

    def action(self) -> None:
        for i in range(3):
            if random.random() < PLANT_CHANCE_TO_MULTIPLY and self.delay == 0:
                self.multiply()
                self.delay = PLANT_DELAY
            elif self.delay > 0:
                self.delay = self.delay - 1
