import random
from typing import List, Union, Tuple

import Organism as Org
from GUI.Game import Game
from Human import Human
from Plant import Plant
from Point import Point
from animals.Antelope import Antelope
from animals.CyberSheep import CyberSheep
from animals.Fox import Fox
from animals.Sheep import Sheep
from animals.Turtle import Turtle
from animals.Wolf import Wolf
from plants.Dandelion import Dandelion
from plants.DeadlyNightshade import DeadlyNightshade
from plants.Grass import Grass
from plants.Guarana import Guarana
from plants.SosnowskyHogweed import SosnowskyHogweed


class World:
    def __init__(self, width: int, height: int) -> None:
        self._width = width
        self._height = height
        self._organisms: List[Org.Organism] = []  # add correct type annotation
        self._round_number = 1
        self._log: str = "Round number: 0 \n\n"
        self._end_game: bool = False

    # self.game = game

    def get_width(self) -> int:
        return self._width

    def get_height(self) -> int:
        return self._height

    def get_human(self) -> Tuple[Human, bool]:
        for organism in self._organisms:
            if isinstance(organism, Human):
                return organism, True

        return Human(Point(0, 0), self), False

    def get_organism_list(self) -> List[Org.Organism]:
        return self._organisms

    def make_round(self) -> None:
        for organism in self._organisms:
            organism.action()

        self._round_number += 1

    def draw_world(self, game: Game) -> bool:
        self.add_log("Organism number: " + str(len(self._organisms)))
        for i in range(self._height):
            for j in range(self._width):
                game.world_tiles[j][i].setStyleSheet("background-color: white")

        for organism in self._organisms:
            game.world_tiles[organism.get_position().x][
                organism.get_position().y
            ].setStyleSheet(
                "border-image: url("
                + organism.draw()
                + ") 0 0 0 0 stretch stretch"
            )

        game.log.setText(self._log)
        self._log = "Round number: " + str(self._round_number) + "\n\n"

        return self._end_game

    def check_collision(self, position: Point) -> Union[Org.Organism, None]:
        for organism in self._organisms:
            if (
                organism.get_position().x == position.x
                and organism.get_position().y == position.y
            ):
                return organism

        return None

    def add_organism(self, organism: Org.Organism) -> None:
        if isinstance(organism, Plant):
            self._organisms.append(organism)
        else:
            i = 0
            while (
                i < len(self._organisms)
                and self._organisms[i].get_initiative()
                >= organism.get_initiative()
            ):
                i += 1
            self._organisms.insert(i, organism)
        self.add_log(
            "Added "
            + organism.get_name()
            + " in ["
            + str(organism.get_position().x)
            + ","
            + str(organism.get_position().y)
            + "]"
        )

    def remove_organism(self, organism: Org.Organism) -> None:
        try:
            self._organisms.remove(organism)
            if isinstance(organism, Human):
                self._end_game = True
        except ValueError:
            print("There is no that organism")

    def generate_organisms(
        self,
        organisms_number: int,
        antelope_chance: int = 50,
        cyber_sheep_chance: int = 10,
        dandelion_chance: int = 25,
        deadly_nightshade_chance: int = 10,
        fox_chance: int = 25,
        grass_chance: int = 100,
        guarana_chance: int = 50,
        sheep_chance: int = 75,
        sosnowsky_hogweed_chance: int = 10,
        turtle_chance: int = 50,
        wolf_chance: int = 10,
    ) -> Human:
        cyber_sheep_chance += antelope_chance
        dandelion_chance += cyber_sheep_chance
        deadly_nightshade_chance += dandelion_chance
        fox_chance += deadly_nightshade_chance
        grass_chance += fox_chance
        guarana_chance += grass_chance
        sheep_chance += guarana_chance
        sosnowsky_hogweed_chance += sheep_chance
        turtle_chance += sosnowsky_hogweed_chance
        wolf_chance += turtle_chance

        pos = Point(0, 0)
        pos.x = random.randrange(self._width)
        pos.y = random.randrange(self._height)
        human = Human(pos, self)
        self.add_organism(human)

        for i in range(organisms_number - 1):
            rand = random.randrange(wolf_chance)
            position = Point(0, 0)
            while True:
                position.x = random.randrange(self._width)
                position.y = random.randrange(self._height)

                if self.check_collision(position) is None:
                    break

            if rand < antelope_chance:
                self.add_organism(Antelope(position, self))
            elif rand < cyber_sheep_chance:
                self.add_organism(CyberSheep(position, self))
            elif rand < dandelion_chance:
                self.add_organism(Dandelion(position, self))
            elif rand < deadly_nightshade_chance:
                self.add_organism(DeadlyNightshade(position, self))
            elif rand < fox_chance:
                self.add_organism(Fox(position, self))
            elif rand < grass_chance:
                self.add_organism(Grass(position, self))
            elif rand < guarana_chance:
                self.add_organism(Guarana(position, self))
            elif rand < sheep_chance:
                self.add_organism(Sheep(position, self))
            elif rand < sosnowsky_hogweed_chance:
                self.add_organism(SosnowskyHogweed(position, self))
            elif rand < turtle_chance:
                self.add_organism(Turtle(position, self))
            elif rand < wolf_chance:
                self.add_organism(Wolf(position, self))

        # self.draw_world()
        return human

    def add_log(self, log: str) -> None:
        self._log = self._log + log + " \n"
