from abc import ABC, abstractmethod
from typing import Generic, Any

from cell import Cell
from elements.placable.abstract.shapes.unknown_shape import TUnknownShape
from elements.tiles.atile import ATile


class IPlacableElement(ABC, Generic[TUnknownShape]):
    @abstractmethod
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        pass

    @property
    @abstractmethod
    def cells(self) -> dict[Cell, ATile]:
        pass

    @abstractmethod
    def add_cell(self, cell: Cell, tile: ATile | None = None) -> None:
        pass

    @property
    @abstractmethod
    def center(self) -> Cell:
        pass

    @property
    @abstractmethod
    def default_tile(self) -> ATile:
        pass

    @property
    @abstractmethod
    def shape(self) -> TUnknownShape:
        pass
