from abc import ABC, abstractmethod
from typing import Generic

from iconnectable_element import TConnectableElement
from iplacable_element import TPlacableElement


class IPlacementStrategy(ABC, Generic[TPlacableElement]):
    @abstractmethod
    def place(self, dungeon_map, element: TConnectableElement):
        pass
