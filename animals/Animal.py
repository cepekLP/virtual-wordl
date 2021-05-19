import random

from typing import Union

from Organism import Organism
from Point import Point
from World import World

ANIMAL_MULTIPLY_DELAY = 5


class Animal(Organism):
    def __init__(
        self,
        strength: int,
        initiative: int,
        position: Point,
        world_ref: World,
    ) -> None:
        super().__init__(strength, initiative, position, world_ref)

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

        if organism is not None:
            if self.collision(organism) == 1:
                self.position = next_position

        if self.delay > 0:
            self.delay -= 1

    def collision(self, attacked: Organism) -> int:
        """
        Returns:
            1 for attacker win
            0 for attacker lose
        """

        # info: str = ""
        if self.check_type(attacked):
            self.multiply()
        else:
            if attacked.get_strength() <= self.get_strength():
                if attacked.deflect(self):
                    # info = "O"
                    return 0
                elif attacked.run_away():
                    # info = "U"
                    return 1
                else:
                    if attacked.special_trait(self) is False:
                        pass
                    self.world.remove_organism(attacked)
                    # info = "R"
                    return 1
            else:
                if self.run_away() is False:
                    self.world.remove_organism(self)
                return 0

        return -1

    def find_free_pos(self, position: Point) -> Union[Point, None]:
        positions = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                positions.append(Point(i, j))

        while True:
            temp = random.randrange(len(positions))
            position_change = positions[temp]
            positions.pop(temp)
            next_position = position
            next_position.x += position_change.x
            next_position.y += position_change.y
            if (
                next_position.x >= 0
                and next_position.x < self.world.get_width()
                and next_position.y >= 0
                and next_position.y < self.world.get_height()
                and self.world.check_collision(next_position) is None
            ):
                break

        if self.world.check_collision(next_position) is not None:
            return next_position
        else:
            return None
