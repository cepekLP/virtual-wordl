import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedLayout, QWidget

from GUI.Menu import Menu
from GUI.Game import Game

from Point import Point

from World import World
from Human import Human


class MainWindow(QMainWindow):
    def __init__(
        self, screen_width: int = 1024, screen_height: int = 600
    ) -> None:
        super().__init__()

        self.organisms_num: int = 1
        self.world_width: int = 1
        self.world_height: int = 1
        self.human: Human
        self.world: World

        self.setWindowTitle("Virtual World")
        self.setFixedSize(screen_width, screen_height)

        self.menu = Menu(screen_width, screen_height)

        self.menu.start_button.pressed.connect(self.start_game)
        self.menu.world_width.valueChanged.connect(self.set_world_width)
        self.menu.world_height.valueChanged.connect(self.set_world_height)
        self.menu.organisms_slider.valueChanged.connect(self.set_organisms_num)
        self.menu.organisms_spin.valueChanged.connect(self.set_organisms_num)

        self.game = Game(screen_width, screen_height)

        self.layout = QStackedLayout()
        self.layout.addWidget(self.menu)
        self.layout.addWidget(self.game)
        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

    def set_world_width(self, v: int) -> None:
        self.world_width = v
        self.set_max_organisms()

    def set_world_height(self, v: int) -> None:
        self.world_height = v
        self.set_max_organisms()

    def set_max_organisms(self):
        self.menu.organisms_slider.setMaximum(
            self.world_width * self.world_height
        )
        self.menu.organisms_spin.setMaximum(
            self.world_width * self.world_height
        )

    def set_organisms_num(self, v: int) -> None:
        self.organisms_num = v
        if self.menu.organisms_slider.value() != v:
            self.menu.organisms_slider.setValue(v)
        else:
            self.menu.organisms_spin.setValue(v)

    def start_game(self):
        self.game.set_size(self.world_width, self.world_height)
        self.world = World(self.world_width, self.world_height, self.game)
        self.human = self.world.generate_organisms(self.organisms_num)
        self.layout.setCurrentIndex(1)

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.key() == QtCore.Qt.Key_W:
            self.human.set_position_change(Point(0, -1))
        elif event.key() == QtCore.Qt.Key_S:
            self.human.set_position_change(Point(0, 1))
        elif event.key() == QtCore.Qt.Key_A:
            self.human.set_position_change(Point(-1, 0))
        elif event.key() == QtCore.Qt.Key_D:
            self.human.set_position_change(Point(1, 0))
        self.world.make_round()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()
