from typing import TYPE_CHECKING

from Animal import Animal
from Point import Point

if TYPE_CHECKING:
    from World import World


class CyberSheep(Animal):
    def __init__(self, position: Point, world_ref: "World"):
        super().__init__(11, 4, position, world_ref)

    def draw(self) -> str:
        return "GUI/images/cybersheep.jpg"
