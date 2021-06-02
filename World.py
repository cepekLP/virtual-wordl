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

random.seed(10)


class World:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.organisms: List[Org.Organism] = []  # add correct type annotation
        self.round_number = 1
        self.log: str = "Round number: 0"

    # self.game = game

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height

    def get_human(self) -> Tuple[Human, bool]:
        for organism in self.organisms:
            if isinstance(organism, Human):
                return organism, True

        return Human(Point(0, 0), self), False

    def make_round(self) -> None:
        for organism in self.organisms:
            organism.action()

        self.round_number += 1

    def draw_world(self, game: Game) -> bool:
        self.add_log("Organism number: " + str(len(self.organisms)))
        for i in range(self.height):
            for j in range(self.width):
                game.world_tiles[j][i].setStyleSheet("")
        print(self.round_number)

        endgame: bool = True
        for organism in self.organisms:
            if isinstance(organism, Human):
                endgame = False
            game.world_tiles[organism.get_position().x][
                organism.get_position().y
            ].setStyleSheet(
                "border-image: url("
                + organism.draw()
                + ") 0 0 0 0 stretch stretch"
            )
            print(
                organism.get_name()
                + " "
                + str(organism.get_position().x)
                + " "
                + str(organism.get_position().y)
            )

        game.log.setText(self.log)
        self.log = "Round number: " + str(self.round_number) + "\n\n"

        return endgame

    def check_collision(self, position: Point) -> Union[Org.Organism, None]:
        for organism in self.organisms:
            if (
                organism.get_position().x == position.x
                and organism.get_position().y == position.y
            ):
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
            self.organisms.remove(organism)
        except ValueError:
            print("There is no that organism")

    def generate_organisms(
        self,
        organisms_number: int,
        antelope_chance: int = 50,
        cyber_sheep_chance: int = 10,
        dandelion_chance: int = 25,
        deadly_nightshade_chance: int = 5,
        fox_chance: int = 25,
        grass_chance: int = 100,
        guarana_chance: int = 50,
        sheep_chance: int = 75,
        sosnowsky_hogweed_chance: int = 5,
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
        pos.x = random.randrange(self.width)
        pos.y = random.randrange(self.height)
        human = Human(pos, self)
        self.add_organism(human)

        for i in range(organisms_number - 1):
            rand = random.randrange(wolf_chance)
            position = Point(0, 0)
            while True:
                position.x = random.randrange(self.width)
                position.y = random.randrange(self.height)

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
        self.log = self.log + log + " \n"
