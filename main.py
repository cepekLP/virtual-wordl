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

        self._organisms_num: int = 1
        self._world_width: int = 2
        self._world_height: int = 2
        self._start_round: bool = False
        self._human: Human
        self._world: World

        self.setWindowTitle("Virtual World")
        self.setFixedSize(screen_width, screen_height)

        self._menu = Menu(screen_width, screen_height)
        self.__check_save_file()

        self._menu.start_button.pressed.connect(self.__start_game)
        self._menu.load_button.pressed.connect(self.__load_game)
        self._menu.world_width.valueChanged.connect(self.__set_world_width)
        self._menu.world_height.valueChanged.connect(self.__set_world_height)
        self._menu.organisms_slider.valueChanged.connect(
            self.__set_organisms_num
        )
        self._menu.organisms_spin.valueChanged.connect(
            self.__set_organisms_num
        )

        self._game = Game(screen_width, screen_height)

        self._end_game = EndGame()
        # self.end_game.new_game_button.pressed.connect(self.new_game)

        self._layout = QStackedLayout()
        self._layout.addWidget(self._menu)
        self._layout.addWidget(self._game)
        self._layout.addWidget(self._end_game)
        widget = QWidget()
        widget.setLayout(self._layout)
        self.setCentralWidget(widget)

    def __check_save_file(self) -> None:
        try:
            f = open("save.p", "rb")
            self._menu.load_button.setEnabled(True)
            f.close()
        except OSError:
            self._menu.load_button.setEnabled(False)

    def __set_world_width(self, v: int) -> None:
        self._world_width = v
        self.__set_max_organisms()

    def __set_world_height(self, v: int) -> None:
        self._world_height = v
        self.__set_max_organisms()

    def __set_max_organisms(self):
        self._menu.organisms_slider.setMaximum(
            self._world_width * self._world_height
        )
        self._menu.organisms_spin.setMaximum(
            self._world_width * self._world_height
        )

    def __set_organisms_num(self, v: int) -> None:
        self._organisms_num = v
        if self._menu.organisms_slider.value() != v:
            self._menu.organisms_slider.setValue(v)
        else:
            self._menu.organisms_spin.setValue(v)

    def __start_game(self) -> None:
        self._game.set_size(self._world_width, self._world_height)
        self._world = World(self._world_width, self._world_height)
        self._human = self._world.generate_organisms(self._organisms_num)
        self._world.draw_world(self._game)
        self._layout.setCurrentIndex(1)

    def __load_game(self) -> None:
        self._world = pi.load(open("save.p", "rb"))
        self._human, validate = self._world.get_human()
        if validate:
            self._game.set_size(
                self._world.get_width(), self._world.get_height()
            )
            self._world.draw_world(self._game)
            self._layout.setCurrentIndex(1)
        else:
            self._layout.setCurrentIndex(2)

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.key() == QtCore.Qt.Key_W:
            self._human.set_position_change(Point(0, -1))
            self._start_round = True
        elif event.key() == QtCore.Qt.Key_S:
            self._human.set_position_change(Point(0, 1))
            self._start_round = True
        elif event.key() == QtCore.Qt.Key_A:
            self._human.set_position_change(Point(-1, 0))
            self._start_round = True
        elif event.key() == QtCore.Qt.Key_D:
            self._human.set_position_change(Point(1, 0))
            self._start_round = True
        elif event.key() == QtCore.Qt.Key_E:
            self._human.activate_skill()
        elif event.key() == QtCore.Qt.Key_Z:
            pi.dump(self._world, open("save.p", "wb"))

        if self._start_round:
            self._world.make_round()
            if self._world.draw_world(self._game):
                self._layout.setCurrentIndex(2)
            self._start_round = False


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()
