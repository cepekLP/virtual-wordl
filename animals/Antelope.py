import random
from typing import Union, TYPE_CHECKING
from copy import copy

from Organism import Organism
from Animal import Animal
from Point import Point

if TYPE_CHECKING:
    from World import World


class Antelope(Animal):
    def __init__(self, position: Point, world_ref: "World"):
        super().__init__(4, 4, position, world_ref)

    def get_name(self) -> str:
        return "Antelope"

    def draw(self) -> str:
        return "GUI/images/antelope.png"

    def action(self) -> None:
        position_change_x = 0
        position_change_y = 0

        while position_change_x == 0 and position_change_y == 0:
            position_change_x = random.randrange(-2, 3)
            position_change_y = random.randrange(-2, 3)

        next_position = copy(self._position)
        next_position.x += position_change_x
        next_position.y += position_change_y

        if next_position.x >= self._world.get_width():
            next_position.x -= 3
        elif next_position.x < 0:
            next_position.x += 3

        if next_position.y >= self._world.get_height():
            next_position.y -= 3
        elif next_position.y < 0:
            next_position.y += 3

        organism = self._world.check_collision(next_position)

        if organism is not None:
            if self._collision(organism) == 1:
                self._position = next_position

        if self._delay > 0:
            self._delay -= 1

    def _multiply(self):
        free_position = self._find_free_pos(self._position)
        if free_position is not None:
            self._world.add_organism(Antelope(free_position, self._world))

    def _run_away(self):
        if random.random() < 0.5:
            next_position = self._find_free_pos(self._position)
            if next_position is not None:
                self.position = next_position
                return True
            else:
                return False
        else:
            return False

    def _find_free_pos(self, position: Point) -> Union[Point, None]:
        positions = []
        for i in range(-2, 3):
            for j in range(-2, 3):
                positions.append(Point(i, j))

        while True:
            temp = random.randrange(len(positions))
            position_change = positions[temp]
            positions.pop(temp)
            next_position = copy(position)
            next_position.x += position_change.x
            next_position.y += position_change.y
            if (
                0 <= next_position.x < self._world.get_width()
                and 0 <= next_position.y < self._world.get_height()
                and self._world.check_collision(next_position) is None
            ) or len(positions) == 0:
                break

        if (
            0 <= next_position.x < self._world.get_width()
            and 0 <= next_position.y < self._world.get_height()
            and self._world.check_collision(next_position) is None
        ):
            return next_position
        else:
            return None

    def _check_type(self, attacker: Organism) -> bool:
        if isinstance(attacker, Antelope):
            return True
        else:
            return False
