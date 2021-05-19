from typing import Union

from Animal import Animal
from Point import Point
from World import World


class Sheep(Animal):
    def __init__(self, position: Point, world_ref: World):
        super().__init__(4, 4, position, world_ref)

    def multiply(self) -> None:
        free_position: Union[Point, None] = self.find_free_pos(self.position)

        if free_position is not None:
            self.world.add_organism(Sheep(free_position, self.world))
