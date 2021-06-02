import random
from typing import TYPE_CHECKING

from Animal import Animal
import animals.CyberSheep as CS
from Plant import Plant, PLANT_DELAY, PLANT_CHANCE_TO_MULTIPLY
from Point import Point

if TYPE_CHECKING:
    from World import World


class SosnowskyHogweed(Plant):
    def __init__(self, position: Point, world_ref: "World"):
        super().__init__(11, position, world_ref)

    def get_name(self) -> str:
        return "Sosnowsky Hogweed"

    def draw(self) -> str:
        return "GUI/images/sosnowskyhogweed.jpg"

    def action(self):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i != 0 and j != 0:
                    organism = self.world.check_collision(
                        Point(self.position.x + i, self.position.y + j)
                    )
                    if (
                        organism is not None
                        and isinstance(organism, Animal)
                        and not isinstance(organism, CS.CyberSheep)
                    ):
                        self.world.remove_organism(organism)

        if random.random() < PLANT_CHANCE_TO_MULTIPLY and self.delay == 0:
            self.multiply()
            self.delay = PLANT_DELAY
        elif self.delay > 0:
            self.delay = self.delay - 1

    def multiply(self) -> None:
        free_position = self.find_free_pos(self.position)
        if free_position is not None:
            self.world.add_organism(
                SosnowskyHogweed(free_position, self.world)
            )
