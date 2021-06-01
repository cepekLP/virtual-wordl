from typing import TYPE_CHECKING

from Plant import Plant
from Point import Point

if TYPE_CHECKING:
    from World import World


class DeadlyNightshade(Plant):
    def __init__(self, position: Point, world_ref: "World"):
        super().__init__(99, position, world_ref)

    def get_name(self) -> str:
        return "Deadly Nightshade"

    def draw(self) -> str:
        return "GUI/images/deadlynightshade.png"

    def multiply(self) -> None:
        free_position = self.find_free_pos(self.position)
        if free_position is not None:
            self.world.add_organism(
                DeadlyNightshade(free_position, self.world)
            )
