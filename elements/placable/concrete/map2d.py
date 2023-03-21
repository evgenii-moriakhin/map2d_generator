from elements.placable.abstract.aplacable_element import APlacableElement
from elements.placable.abstract.shapes.square_shape import SquareShape
from elements.tiles.empty_tile import EmptyTile


class Map2D(APlacableElement[SquareShape]):
    @property
    def default_tile(self) -> EmptyTile:
        return EmptyTile()
