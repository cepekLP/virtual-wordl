from typing import TYPE_CHECKING

from Organism import Organism
from Animal import Animal
from Point import Point

if TYPE_CHECKING:
    from World import World


class Wolf(Animal):
    def __init__(self, position: Point, world_ref: "World"):
        super().__init__(9, 5, position, world_ref)

    def get_name(self) -> str:
        return "Wolf"

    def draw(self) -> str:
        return "GUI/images/wolf.png"

    def _multiply(self) -> None:
        free_position = self._find_free_pos(self._position)
        if free_position is not None:
            self._world.add_organism(Wolf(free_position, self._world))

    def _check_type(self, attacker: Organism) -> bool:
        if isinstance(attacker, Wolf):
            return True
        else:
            return False
