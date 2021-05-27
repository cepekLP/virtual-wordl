from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class Menu(QWidget):
    def __init__(self, width: int = 1024, height: int = 600):
        super().__init__()

        self.setFixedSize(width, height)
        uic.loadUi("GUI/menu.ui", self)
