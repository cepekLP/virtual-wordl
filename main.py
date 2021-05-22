from PyQt5.QtWidgets import QApplication, QMainWindow

from GUI.Menu import Ui_Menu
from World import World


class MainWindow(QMainWindow):
    def __init__(
        self, screen_width: int = 1024, screen_height: int = 600
    ) -> None:
        super().__init__(self)

        self.setFixedSize(screen_width, screen_height)

        self.menu = Ui_Menu()
        self.menu.setupUi(self)

        self.organisms_num: int = 0
        self.world_width: int = 0
        self.world_height: int = 0

        self.menu.start_button.pressed.connect(self.start_game)
        self.menu.world_width.valueChanged(self.set_world_width)
        self.menu.world_height.valueChanged(self.set_world_height)
        self.menu.organisms_slider.valueChanged(self.set_organisms_num)
        self.menu.organisms_spin.valueChanged(self.set_organisms_num)

    def set_world_width(self, v: int) -> None:
        self.world_width = v
        self.set_max_organisms()

    def set_world_height(self, v: int) -> None:
        self.world_height = v
        self.set_max_organisms()

    def set_max_organisms(self):
        if self.world_width * self.world_height > 0:
            self.menu.organisms_slider.setMaximum(
                self.world_width * self.world_height
            )
            self.menu.organisms_spin.setMaximum(
                self.world_width * self.world_height
            )
        else:
            self.menu.organisms_slider.setMaximum(1)
            self.menu.organisms_spin.setMaximum(1)

    def set_organisms_num(self, v: int) -> None:
        self.organisms_num = v
        if self.menu.organisms_slider != v:
            self.menu.organisms_slider.setValue(v)
        else:
            self.menu.organisms_spin.setValue(v)

    def start_game(self):
        self.word = World(self.world_width, self.world_height)
        # self.word.generate_organisms()


if __name__ == "main":
    app = QApplication

    window = MainWindow()
    window.show()

    app.exec_()
