from typing import Any

from cell import Cell
from elements.placable.abstract.iconnectable_element import IConnectableElement
from elements.placable.abstract.iplacable_element import IPlacableElement


class ConnectorPlacementStrategy:
    def place(self, map_: IPlacableElement[Any], element: IConnectableElement) -> None:
        x1, y1 = element.from_cell
        x2, y2 = element.to_cell

        for x in range(min(x1, x2), max(x1, x2)):
            element.add_cell(Cell(x, y1))
        for y in range(min(y1, y2), max(y1, y2)):
            element.add_cell(Cell(x2, y))

        for cell in element.cells:
            map_.add_cell(cell, element.default_tile)
