from cell import Cell
from elements.placable.abstract.aplacable_element import APlacableElement
from elements.placable.abstract.iconnectable_element import IConnectableElement
from elements.placable.abstract.shapes.unknown_shape import UnknownShape
from elements.tiles.corridor_tile import CorridorTile


class Corridor(APlacableElement[UnknownShape], IConnectableElement):
    def __init__(self, shape: UnknownShape, from_cell: Cell, to_cell: Cell) -> None:
        super().__init__(shape)
        self._from_cell = from_cell
        self._to_cell = to_cell

    @property
    def from_cell(self) -> Cell:
        return self._from_cell

    @property
    def to_cell(self) -> Cell:
        return self._to_cell

    @property
    def default_tile(self) -> CorridorTile:
        return CorridorTile()
