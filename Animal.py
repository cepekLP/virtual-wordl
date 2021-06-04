import random
from copy import copy
from typing import TYPE_CHECKING

from Organism import Organism
from Point import Point

if TYPE_CHECKING:
    from World import World

ANIMAL_MULTIPLY_DELAY = 5


class Animal(Organism):
    def __init__(
        self,
        strength: int,
        initiative: int,
        position: Point,
        world_ref: "World",
    ) -> None:
        super().__init__(strength, initiative, position, world_ref)

    def action(self) -> None:
        position_change: Point = Point(0, 0)

        while position_change.x == 0 and position_change.y == 0:
            position_change.x = random.randrange(-1, 2)
            position_change.y = random.randrange(-1, 2)

        next_position = copy(self._position)
        next_position.x += position_change.x
        next_position.y += position_change.y

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

        if self._delay > 0:
            self._delay -= 1

    def _collision(self, attacked: Organism) -> int:
        """
        Returns:
            1 for attacker win
            0 for attacker lose
            -1 for error
        """

        if self._check_type(attacked):
            if self._delay == 0 and attacked.get_delay() == 0:
                self._multiply()
                self._delay = ANIMAL_MULTIPLY_DELAY
            return 0
        else:
            if attacked.get_strength() <= self.get_strength():
                if attacked._deflect(self):
                    self._world.add_log(
                        self._log(attacked, "deflect attack from", self)
                    )
                    return 0
                elif attacked._run_away():
                    self._world.add_log(
                        self._log(attacked, "run away from", self)
                    )
                    return 1
                else:

                    if isinstance(attacked, Animal):
                        self._world.add_log(self._log(self, "kill", attacked))
                    else:
                        self._world.add_log(self._log(self, "eat", attacked))
                    if not attacked.special_trait(self):
                        self._world.remove_organism(attacked)
                    return 1
            else:
                if isinstance(attacked, Animal):
                    if self._run_away() is False:
                        self._world.add_log(
                            self._log(self, "attacked and lose with", attacked)
                        )
                        self._world.remove_organism(self)
                    else:
                        self._world.add_log(
                            self._log(
                                self, "attacked and run away from", attacked
                            )
                        )
                    return 0
                else:
                    self._world.remove_organism(attacked)
                    self._world.remove_organism(self)
                    return 0

    def _check_type(self, attacker: Organism) -> bool:
        return False

    @staticmethod
    def _log(organism: Organism, text: str, organism2: Organism) -> str:
        info = (
            organism.get_name()
            + " ["
            + str(organism.get_position().x)
            + ","
            + str(organism.get_position().y)
            + "] "
            + text
            + " "
            + organism2.get_name()
            + " ["
            + str(organism2.get_position().x)
            + ","
            + str(organism2.get_position().y)
            + "]"
        )
        return info
