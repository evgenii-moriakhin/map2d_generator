from typing import Any

from cell import Cell
from elements.placable.abstract.iplacable_element import IPlacableElement
from elements.placable.abstract.shapes.square_shape import SquareShape
from strategies.placable.abstract.iplacement_strategy import IPlacementStrategy


class SquarePlacementStrategy(IPlacementStrategy[Any, SquareShape]):
    def place(self, map_: IPlacableElement[Any], element: IPlacableElement[SquareShape]) -> None:
        # Get the size of the square element
        square_size = element.shape.size

        # Calculate the position to place the square element
        center_offset = (square_size - 1) // 2
        top_left_x = map_.center.x - center_offset
        top_left_y = map_.center.y - center_offset

        # Add cells to the element
        for i in range(square_size):
            for j in range(square_size):
                element_cell_x = top_left_x + i
                element_cell_y = top_left_y + j

                cell_to_add = Cell(element_cell_x, element_cell_y)

                # Check if the cell exists within the map's cells
                if cell_to_add in map_.cells:
                    element.add_cell(cell_to_add)

        # Add square element's cells to the map element
        for cell in element.cells:
            map_.add_cell(cell, element.default_tile)
