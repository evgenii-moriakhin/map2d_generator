from abc import abstractmethod
from typing import Any

from cell import Cell
from elements.placable.abstract.iplacable_element import IPlacableElement


class IConnectableElement(IPlacableElement[Any]):
    @property
    @abstractmethod
    def from_cell(self) -> Cell:
        pass

    @property
    @abstractmethod
    def to_cell(self) -> Cell:
        pass
