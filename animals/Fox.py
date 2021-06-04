import random
from typing import TYPE_CHECKING
from copy import copy

from Animal import Animal
from Organism import Organism
from Point import Point

if TYPE_CHECKING:
    from World import World


class Fox(Animal):
    def __init__(self, position: Point, world_ref: "World"):
        super().__init__(3, 7, position, world_ref)

    def get_name(self) -> str:
        return "Fox"

    def draw(self) -> str:
        return "GUI/images/fox.png"

    def action(self) -> None:
        position_change: Point = Point(0, 0)

        while position_change.x == 0 and position_change.y == 0:
            position_change.x = random.randrange(-1, 2)
            position_change.y = random.randrange(-1, 2)

        next_position = copy(self._position)
        next_position.x += position_change.x
        next_position.y += position_change.y

        if next_position.x >= self._world.get_width():
            next_position.x -= 2
        elif next_position.x < 0:
            next_position.x += 2

        if next_position.y >= self._world.get_height():
            next_position.y -= 2
        elif next_position.y < 0:
            next_position.y += 2

        organism = self._world.check_collision(next_position)

        if (
            organism is not None
            and organism.get_strength() <= self._strength
            and self._collision(organism) == 1
        ):
            self._position = next_position

        if self._delay > 0:
            self._delay -= 1

    def _multiply(self):
        free_position = self._find_free_pos(self._position)
        if free_position is not None:
            self._world.add_organism(Fox(free_position, self._world))

    def _check_type(self, attacker: Organism) -> bool:
        if isinstance(attacker, Fox):
            return True
        else:
            return False
