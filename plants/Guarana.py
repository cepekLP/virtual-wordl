from typing import TYPE_CHECKING

from Organism import Organism
from Plant import Plant
from Point import Point

if TYPE_CHECKING:
    from World import World


class Guarana(Plant):
    def __init__(self, position: Point, world_ref: "World"):
        super().__init__(0, position, world_ref)

    def get_name(self) -> str:
        return "Guarana"

    def draw(self) -> str:
        return "GUI/images/guarana.jpeg"

    def special_trait(self, attacker: Organism) -> bool:
        attacker.increase_strength()
        return False

    def _multiply(self) -> None:
        free_position = self._find_free_pos(self._position)
        if free_position is not None:
            self._world.add_organism(Guarana(free_position, self._world))
