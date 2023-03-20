from abc import ABC, abstractmethod
from typing import Generic

from iconnectable_element import TConnectableElement


class IConnectableStrategy(ABC, Generic[TConnectableElement]):
    @abstractmethod
    def place(self, dungeon_map, element: TConnectableElement):
        pass
