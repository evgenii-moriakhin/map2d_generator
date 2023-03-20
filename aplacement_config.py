import random
from abc import ABC, abstractmethod
from typing import Generic

from dungeon_elements import Room
from iplacable_element import TPlacableElement


class APlacableConfig(ABC, Generic[TPlacableElement]):
    @abstractmethod
    def create_placable_element(self) -> TPlacableElement:
        """fabric method"""
        pass


class RoomConfig(APlacableConfig[Room]):
    def __init__(self, min_size=5, max_size=10):
        self.min_size = min_size
        self.max_size = max_size

    def create_placable_element(self) -> Room:
        room = Room(self.min_size, self.max_size)
        room.width = random.randint(self.min_size, self.max_size)
        room.height = random.randint(self.min_size, self.max_size)
        return room
