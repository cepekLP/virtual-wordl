import random
from typing import Any, Union, TYPE_CHECKING

from Point import Point

if TYPE_CHECKING:
    from World import World


class Organism:
    def __init__(
        self,
        strength: int,
        initiative: int,
        position: Point,
        world_ref: "World",
    ) -> None:
        self.strength: int = strength
        self.initiative: int = initiative
        self.position: Point = position
        self.world: "World" = world_ref
        self.delay: int = 1

    def get_strength(self) -> int:
        return self.strength

    def get_initiative(self) -> int:
        return self.initiative

    def get_position(self) -> Point:
        return self.position

    def draw(self) -> str:
        return ""

    def action(self) -> None:
        pass

    def collision(self, attacked: Any) -> int:
        return -1

    def multiply(self) -> None:
        pass

    def deflect(self, attacker: Any) -> bool:
        return False

    # fix type annotation from Any
    #
    #   NodeT = TypeVar(`NodeT`, bound=`Node`)
    #
    #    class Node(Object):
    #       def add_sub(self, sub: NodeT):
    #            ...
    #
    #       def get_subs(self) -> Sequence[NodeT]:
    #            ...

    def run_away(self) -> bool:
        return False

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

    def check_type(self, attacker: Any) -> bool:
        return False

    def special_trait(self, attacker: Any) -> bool:
        return False
