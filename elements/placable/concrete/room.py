from typing import Iterable

from cell import Cell
from elements.placable.abstract.aplacable_element import APlacableElement
from elements.placable.abstract.shapes.unknown_shape import TUnknownShape
from elements.tiles.room_tile import RoomTile


class Room(APlacableElement[TUnknownShape]):
    _entrances: list[Cell]

    def __init__(self, shape: TUnknownShape):
        super().__init__(shape)
        self._entrances = []

    def add_entrance(self, entrance_cell: Cell) -> None:
        self._entrances.append(entrance_cell)

    @property
    def entrances(self) -> Iterable[Cell]:
        return self._entrances

    @property
    def default_tile(self) -> RoomTile:
        return RoomTile()
