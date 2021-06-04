import random
from typing import Any, Union, TYPE_CHECKING
from copy import copy

from Point import Point

if TYPE_CHECKING:
    from World import World


class Organism:
    def __init__(
        self,
        strength: int,
        initiative: int,
        position: Point,
        world_ref: "World",
    ) -> None:
        self._strength: int = strength
        self._initiative: int = initiative
        self._position: Point = position
        self._world: "World" = world_ref
        self._delay: int = 1

    def get_strength(self) -> int:
        return self._strength

    def get_initiative(self) -> int:
        return self._initiative

    def get_position(self) -> Point:
        return self._position

    def get_name(self) -> str:
        return ""

    def get_delay(self) -> int:
        return self._delay

    def draw(self) -> str:
        return ""

    def action(self) -> None:
        pass

    def special_trait(self, attacker: "Organism") -> bool:
        return False

    def increase_strength(self) -> None:
        self._strength += 3

    def _multiply(self) -> None:
        pass

    def _deflect(self, attacker: Any) -> bool:
        return False

    def _run_away(self) -> bool:
        return False

    def _find_free_pos(self, position: Point) -> Union[Point, None]:
        positions = []
        for i in range(-1, 2):
            for j in range(-1, 2):
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
            self._world.check_collision(next_position) is None
            and 0 <= next_position.x < self._world.get_width()
            and 0 <= next_position.y < self._world.get_height()
        ):
            return next_position
        else:
            return None
