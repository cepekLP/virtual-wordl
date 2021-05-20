import numpy as np
from typing import List, Union

import Organism as Org
from Point import Point
from plants.Plant import Plant


class World:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.organisms: List[Org.Organism] = []  # add correct type annotation
        self.round_number = 0

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height

    def make_round(self) -> None:
        for organism in self.organisms:
            organism.action()

        self.draw_world()

    def draw_world(self) -> np.array:
        organisms_markers = np.zeros((self.width, self.height))

        for organism in self.organisms:
            organisms_markers[organism.get_position().x][
                organism.get_position().y
            ] = organism.draw()

        return organisms_markers

    def check_collision(self, position: Point) -> Union[Org.Organism, None]:
        for organism in self.organisms:
            if organism.position == position:
                return organism

        return None

    def add_organism(self, organism: Org.Organism) -> None:
        if isinstance(organism, Plant):
            self.organisms.append(organism)
        else:
            i = 0
            while (
                i < len(self.organisms)
                and self.organisms[i].get_initiative()
                >= organism.get_initiative()
            ):
                i += 1
            self.organisms.insert(i, organism)

    def remove_organism(self, organism: Org.Organism) -> None:
        try:
            self.organisms.remove(organism)
        except ValueError:
            print("There is no that organism")
