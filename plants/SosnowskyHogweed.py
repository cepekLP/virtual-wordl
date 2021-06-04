import random
from typing import TYPE_CHECKING

from Organism import Organism
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
                    organism = self._world.check_collision(
                        Point(self._position.x + i, self._position.y + j)
                    )
                    if (
                        organism is not None
                        and isinstance(organism, Animal)
                        and not isinstance(organism, CS.CyberSheep)
                    ):
                        self._world.remove_organism(organism)

        if random.random() < PLANT_CHANCE_TO_MULTIPLY and self._delay == 0:
            self._multiply()
            self._delay = PLANT_DELAY
        elif self._delay > 0:
            self._delay = self._delay - 1

    def special_trait(self, attacker: Organism) -> bool:
        self._world.remove_organism(self)
        self._world.remove_organism(attacker)
        return True

    def _multiply(self) -> None:
        free_position = self._find_free_pos(self._position)
        if free_position is not None:
            self._world.add_organism(
                SosnowskyHogweed(free_position, self._world)
            )
