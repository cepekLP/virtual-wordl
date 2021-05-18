import World
from Point import Point
from typing import Any


class Organism:
    def __init__(
        self,
        strength: int,
        initiative: int,
        position: Point,
        world_ref: World.World,
    ) -> None:
        self.strength = strength
        self.initiative = initiative
        self.position = position
        self.world = world_ref
        self.delay: int = 1

    def get_strength(self) -> int:
        return self.strength

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

    def check_type(self, attacker: Any) -> bool:
        return False

    def special_trait(self, attacker: Any) -> bool:
        return False
