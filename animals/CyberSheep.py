from typing import Union, TYPE_CHECKING
import random
from copy import copy
from math import sqrt

from Organism import Organism
import plants.SosnowskyHogweed as SH
from Animal import Animal
from Point import Point

if TYPE_CHECKING:
    from World import World


class CyberSheep(Animal):
    def __init__(self, position: Point, world_ref: "World"):
        super().__init__(11, 4, position, world_ref)

        self.destination: Union[Point, None] = None

    def get_name(self) -> str:
        return "Cyber Sheep"

    def draw(self) -> str:
        return "GUI/images/cybersheep.jpg"

    def action(self) -> None:
        next_position = copy(self.position)

        if self.destination is None or (
            self.destination.x == self.position.x
            and self.destination.y == self.position.y
        ):
            self.destination = self.find_destination()

        if self.destination is not None:
            x_diff = self.destination.x - self.position.x
            y_diff = self.destination.y - self.position.y
            if x_diff > 0:
                next_position.x += 1
            elif x_diff < 0:
                next_position.x -= 1
            if y_diff > 0:
                next_position.y += 1
            elif y_diff < 0:
                next_position.y -= 1
        else:
            position_change: Point = Point(0, 0)

            while position_change.x == 0 and position_change.y == 0:
                position_change.x = random.randrange(-1, 2)
                position_change.y = random.randrange(-1, 2)

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
        else:
            self.position = next_position

        if self.delay > 0:
            self.delay -= 1

    def multiply(self) -> None:
        free_position = self.find_free_pos(self.position)
        if free_position is not None:
            self.world.add_organism(CyberSheep(free_position, self.world))

    def check_type(self, attacker: Organism) -> bool:
        if isinstance(attacker, CyberSheep):
            return True
        else:
            return False

    def find_destination(self) -> Union[Point, None]:
        def distance(point1: Point, point2: Point) -> float:
            a = point1.x - point2.x
            b = point1.y - point2.y
            return sqrt(a * a + b * b)

        destination: Union[Point, None] = None
        max_dist: float = distance(
            Point(0, 0), Point(self.world.get_width(), self.world.get_height())
        )
        organisms = self.world.get_organism_list()
        for organism in organisms:
            if isinstance(organism, SH.SosnowskyHogweed):
                dist = distance(self.position, organism.get_position())
                if dist < max_dist:
                    max_dist = dist
                    destination = organism.get_position()

        return destination
