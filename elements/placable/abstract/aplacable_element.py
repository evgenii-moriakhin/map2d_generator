from abc import ABC
from functools import cached_property

from elements.placable.abstract.iplacable_element import IPlacableElement
from cell import Cell
from elements.placable.abstract.shapes.unknown_shape import TUnknownShape
from elements.tiles.atile import ATile


class APlacableElement(IPlacableElement[TUnknownShape], ABC):
    _cells: dict[Cell, ATile]
    _shape: TUnknownShape

    def __init__(self, shape: TUnknownShape) -> None:
        self._cells = dict()
        self._shape = shape

    @property
    def cells(self) -> dict[Cell, ATile]:
        return self._cells

    def add_cell(self, cell: Cell, tile: ATile | None = None) -> None:
        self._cells[cell] = self.default_tile if not tile else tile

    @property
    def shape(self) -> TUnknownShape:
        return self._shape

    @cached_property
    def center(self) -> Cell:
        return self.shape.define_center(self.cells)
