import pickle as pi
import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedLayout, QWidget

from GUI.Game import Game
from GUI.Menu import Menu
from GUI.EndGame import EndGame
from Human import Human
from Point import Point
from World import World


class MainWindow(QMainWindow):
    def __init__(
        self, screen_width: int = 1024, screen_height: int = 600
    ) -> None:
        super().__init__()

        self.organisms_num: int = 1
        self.world_width: int = 2
        self.world_height: int = 2
        self.start_round: bool = False
        self.human: Human
        self.world: World

        self.setWindowTitle("Virtual World")
        self.setFixedSize(screen_width, screen_height)

        self.menu = Menu(screen_width, screen_height)
        self.check_save_file()

        self.menu.start_button.pressed.connect(self.start_game)
        self.menu.load_button.pressed.connect(self.load_game)
        self.menu.world_width.valueChanged.connect(self.set_world_width)
        self.menu.world_height.valueChanged.connect(self.set_world_height)
        self.menu.organisms_slider.valueChanged.connect(self.set_organisms_num)
        self.menu.organisms_spin.valueChanged.connect(self.set_organisms_num)

        self.game = Game(screen_width, screen_height)

        self.end_game = EndGame()
        # self.end_game.new_game_button.pressed.connect(self.new_game)

        self.layout = QStackedLayout()
        self.layout.addWidget(self.menu)
        self.layout.addWidget(self.game)
        self.layout.addWidget(self.end_game)
        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

    def check_save_file(self) -> None:
        try:
            f = open("save.p", "rb")
            self.menu.load_button.setEnabled(True)
            f.close()
        except OSError:
            self.menu.load_button.setEnabled(False)

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

    def start_game(self) -> None:
        self.game.set_size(self.world_width, self.world_height)
        self.world = World(self.world_width, self.world_height)
        self.human = self.world.generate_organisms(self.organisms_num)
        self.world.draw_world(self.game)
        self.layout.setCurrentIndex(1)

    def load_game(self) -> None:
        self.world = pi.load(open("save.p", "rb"))
        self.human, validate = self.world.get_human()
        if validate:
            self.game.set_size(self.world.get_width(), self.world.get_height())
            self.world.draw_world(self.game)
            self.layout.setCurrentIndex(1)
        else:
            self.layout.setCurrentIndex(2)

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.key() == QtCore.Qt.Key_W:
            self.human.set_position_change(Point(0, -1))
            self.start_round = True
        elif event.key() == QtCore.Qt.Key_S:
            self.human.set_position_change(Point(0, 1))
            self.start_round = True
        elif event.key() == QtCore.Qt.Key_A:
            self.human.set_position_change(Point(-1, 0))
            self.start_round = True
        elif event.key() == QtCore.Qt.Key_D:
            self.human.set_position_change(Point(1, 0))
            self.start_round = True
        elif event.key() == QtCore.Qt.Key_E:
            self.human.activate_skill()
        elif event.key() == QtCore.Qt.Key_Z:
            pi.dump(self.world, open("save.p", "wb"))

        if self.start_round:
            self.world.make_round()
            if self.world.draw_world(self.game):
                self.layout.setCurrentIndex(2)
            self.start_round = False


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()
