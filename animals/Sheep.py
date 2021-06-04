from typing import TYPE_CHECKING

from Organism import Organism
from Animal import Animal
from Point import Point

if TYPE_CHECKING:
    from World import World


class Sheep(Animal):
    def __init__(self, position: Point, world_ref: "World"):
        super().__init__(4, 4, position, world_ref)

    def get_name(self) -> str:
        return "Sheep"

    def draw(self) -> str:
        return "GUI/images/sheep.png"

    def _multiply(self) -> None:
        free_position = self._find_free_pos(self._position)
        if free_position is not None:
            self._world.add_organism(Sheep(free_position, self._world))

    def _check_type(self, attacker: Organism) -> bool:
        if isinstance(attacker, Sheep):
            return True
        else:
            return False
