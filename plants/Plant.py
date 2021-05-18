import random

from Organism import Organism
from Point import Point
from World import World

PLANT_CHANCE_TO_MULTIPLY = 0.15
PLANT_DELAY = 2


class Plant(Organism):
    def __init__(
        self,
        strength: int,
        position: Point,
        world_ref: World,
    ) -> None:
        super().__init__(strength, 0, position, world_ref)

    def action(self) -> None:
        if random.random() < PLANT_CHANCE_TO_MULTIPLY and self.delay == 0:
            self.multiply()
            self.delay = PLANT_DELAY
        elif self.delay > 0:
            self.delay = self.delay - 1
