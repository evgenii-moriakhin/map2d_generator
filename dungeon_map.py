from typing import Union

from iconnectable_strategy import IConnectableStrategy
from iplacement_strategy import IPlacementStrategy


class DungeonMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]

    def place_element(self, element, strategy: Union[IPlacementStrategy, IConnectableStrategy]):
        strategy.place(self, element)
