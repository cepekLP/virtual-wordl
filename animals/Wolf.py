from typing import Union

from Animal import Animal
from Point import Point
from World import World


class Wolf(Animal):
    def __init__(self, position: Point, world_ref: World):
        super().__init__(9, 5, position, world_ref)

    def multiply(self) -> None:
        free_position: Union[Point, None] = self.find_free_pos(self.position)

        if free_position is not None:
            self.world.add_organism(Wolf(free_position, self.world))
