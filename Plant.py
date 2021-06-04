import random
from typing import TYPE_CHECKING

from Organism import Organism
from Point import Point

if TYPE_CHECKING:
    from World import World

PLANT_CHANCE_TO_MULTIPLY = 0.15
PLANT_DELAY = 2


class Plant(Organism):
    def __init__(
        self, strength: int, position: Point, world_ref: "World"
    ) -> None:
        super().__init__(strength, 0, position, world_ref)

    def action(self) -> None:
        if random.random() < PLANT_CHANCE_TO_MULTIPLY and self._delay == 0:
            self._multiply()
            self._delay = PLANT_DELAY
        elif self._delay > 0:
            self._delay = self._delay - 1
