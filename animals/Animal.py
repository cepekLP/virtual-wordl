from Organism import Organism, Point
from World import World


class Animal(Organism):
    def __init__(
        self,
        strength: int,
        initiative: int,
        position: Point,
        world_ref: World,
    ) -> None:
        super().__init__(strength, initiative, position, world_ref)

    def action(self):
        pass

    def colision(self):
        pass
