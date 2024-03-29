import random
from typing import TYPE_CHECKING

from Plant import Plant, PLANT_DELAY, PLANT_CHANCE_TO_MULTIPLY
from Point import Point

if TYPE_CHECKING:
    from World import World


class Dandelion(Plant):
    def __init__(self, position: Point, world_ref: "World"):
        super().__init__(0, position, world_ref)

    def get_name(self) -> str:
        return "Dandelion"

    def draw(self) -> str:
        return "GUI/images/dandelion.jpeg"

    def action(self) -> None:
        for i in range(3):
            if random.random() < PLANT_CHANCE_TO_MULTIPLY and self._delay == 0:
                self._multiply()
                self._delay = PLANT_DELAY
            elif self._delay > 0:
                self._delay = self._delay - 1

    def _multiply(self) -> None:
        free_position = self._find_free_pos(self._position)
        if free_position is not None:
            self._world.add_organism(Dandelion(free_position, self._world))
