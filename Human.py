import random
from copy import copy
from typing import TYPE_CHECKING

from Animal import Animal
from Point import Point

if TYPE_CHECKING:
    from World import World


class Human(Animal):
    def __init__(self, position: Point, world_ref: "World"):
        super().__init__(5, 4, position, world_ref)
        self._position_change: Point
        self._skill_timer: int = 0

    def get_name(self) -> str:
        return "Human"

    def draw(self) -> str:
        return "GUI/images/human.png"

    def action(self) -> None:
        if self._skill_timer > 2 or (
            self._skill_timer > 0 and random.random() < 0.5
        ):
            self._position_change.x *= 2
            self._position_change.y *= 2

        next_position = copy(self._position)
        next_position.x += self._position_change.x
        next_position.y += self._position_change.y

        if next_position.x >= self._world.get_width():
            next_position.x -= 2
        elif next_position.x < 0:
            next_position.x += 2

        if next_position.y >= self._world.get_height():
            next_position.y -= 2
        elif next_position.y < 0:
            next_position.y += 2

        organism = self._world.check_collision(next_position)

        if organism is not None:
            if self._collision(organism) == 1:
                self._position = next_position
        else:
            self._position = next_position

        if self._skill_timer > 0:
            self._skill_timer -= 1
        if self._delay > 0:
            self._delay -= 1

    def set_position_change(self, position_change: Point) -> None:
        self._position_change = position_change

    def activate_skill(self) -> None:
        self._skill_timer = 5
