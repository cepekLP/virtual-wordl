from typing import List, Any


class World:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.organisms: List[Any]  # add correct type annotation
        self.round_number = 0

    def make_round(self):
        pass

    def draw_world(self):
        pass
