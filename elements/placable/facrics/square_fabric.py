import random
from typing import Type

from elements.placable.abstract.iplacable_element import IPlacableElement
from elements.placable.abstract.shapes.square_shape import SquareShape
from elements.placable.facrics.aplacable_fabric import APlacableFabric


class SquareFabric(APlacableFabric[SquareShape]):
    def __init__(self, min_size: int = 5, max_size: int = 10) -> None:
        self.min_size = min_size
        self.max_size = max_size

    def create_placable_element(self, element_type: Type[IPlacableElement[SquareShape]]) -> IPlacableElement[SquareShape]:
        size = random.randint(self.min_size, self.max_size)
        square_shape = SquareShape(size)
        element = element_type(square_shape)
        return element
