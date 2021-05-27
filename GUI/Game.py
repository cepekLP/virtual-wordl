from typing import List

from PyQt5 import uic
from PyQt5.QtWidgets import (
    QWidget,
    QGridLayout,
    QPushButton,
)


class Game(QWidget):
    def __init__(self, width: int = 1024, height: int = 600) -> None:
        super().__init__()
        self.world_tiles: List[List[QPushButton]] = []

        self.setFixedSize(width, height)
        uic.loadUi("GUI/game.ui", self)
        self.layout = QGridLayout()
        self.game_area.setLayout(self.layout)

    def set_size(self, world_width: int, world_height: int) -> None:
        tile_size = min(550 // world_width, 550 // world_height)
        for i in range(world_height):
            h_list = []
            for j in range(world_width):
                button = QPushButton()
                button.setFixedSize(tile_size, tile_size)
                h_list.append(button)

                # button.setStyleSheet(
                #    "border-image: url(GUI/images/turtle.png) \
                #    0 0 0 0 stretch stretch"
                # )
                self.layout.addWidget(button, j, i)
            self.world_tiles.append(h_list)

        # self.world_tiles[1][1].label.setPixmap(QPixmap("GUI/images/turtle.png"))
