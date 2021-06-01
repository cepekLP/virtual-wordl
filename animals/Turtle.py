import random
from typing import TYPE_CHECKING

from Animal import Animal
from Point import Point

if TYPE_CHECKING:
    from World import World


class Turtle(Animal):
    def __init__(self, position: Point, world_ref: "World"):
        super().__init__(2, 1, position, world_ref)

    def draw(self) -> str:
        return "GUI/images/turtle.png"

    def action(self):
        if random.random() < 0.25:
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

            organism = self.world.check_collision(next_position)

            if organism is not None:
                if self.collision(organism) == 1:
                    self.position = next_position

        if self.delay > 0:
            self.delay -= 1

    def multiply(self) -> None:
        free_position = self.find_free_pos(self.position)

        if free_position is not None:
            self.world.add_organism(Turtle(free_position, self.world))
