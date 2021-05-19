import random

from typing import Union

from Animal import Animal
from Point import Point
from World import World
from Organism import Organism


class Fox(Animal):
    def __init__(self, position: Point, world_ref: World):
        super().__init__(3, 7, position, world_ref)

    def action(self) -> None:
        position_change: Point = Point(0, 0)

        while position_change.x == 0 and position_change.y == 0:
            position_change.x = random.randrange(-1, 2)
            position_change.y = random.randrange(-1, 2)

        next_position = self.position
        next_position.x += position_change.x
        next_position.y += position_change.y

        if next_position.x >= self.world.get_width():
            next_position.x -= 2
        elif next_position.x < 0:
            next_position.x += 2

        if next_position.y >= self.world.get_height():
            next_position.y -= 2
        elif next_position.y < 0:
            next_position.y += 2

        organism: Union[Organism, None] = self.world.check_collision(
            next_position
        )

        if (
            organism is not None
            and organism.get_strength() <= self.strength
            and self.collision(organism) == 1
        ):
            self.position = next_position

        if self.delay > 0:
            self.delay -= 1
