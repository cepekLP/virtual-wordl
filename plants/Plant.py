from Organism import Organism
from Point import Point
from World import World


class Plant(Organism):
    def __init__(
        self,
        strength: int,
        position: Point,
        world_ref: World,
    ) -> None:
        super().__init__(strength, 0, position, world_ref)

    def action(self):
        pass

    def colision(self):
        pass
