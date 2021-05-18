from typing import List, Union
import Organism as Org
from Point import Point


class World:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.organisms: List[Org.Organism]  # add correct type annotation
        self.round_number = 0

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height

    def make_round(self) -> None:
        for organism in self.organisms:
            organism.action()

    def draw_world(self):
        pass

    def check_collision(self, position: Point) -> Union[Org.Organism, None]:
        for organism in self.organisms:
            if organism.position == position:
                return organism

        return None

    def remove_organism(self, organism: Org.Organism) -> None:
        pass
