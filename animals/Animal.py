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
        position_change_x: int = 0
        position_change_y: int = 0

        while position_change_x == 0 and position_change_y == 0:
            position_change_x = random.randrange(-1, 2)
            position_change_y = random.randrange(-1, 2)

        next_position: Point = self.position
        next_position.x += position_change_x
        next_position.y += position_change_y

        if next_position.x >= self.world.get_width():
            next_position.x -= 2
        elif next_position.x < 0:
            next_position.x -= 2

        if next_position.y >= self.world.get_height():
            next_position.y -= 2
        elif next_position.y < 0:
            next_position.y -= 2

        organism: Union[Organism, None] = self.world.check_collision(
            next_position
        )

        if organism is not None:
            if self.collision(organism) == 1:
                self.position = next_position

    def collision(self, attacked: Organism) -> int:
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
