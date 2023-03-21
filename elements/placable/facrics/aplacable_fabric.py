from abc import abstractmethod, ABC
from typing import Type, Generic

from elements.placable.abstract.iplacable_element import IPlacableElement
from elements.placable.abstract.shapes.unknown_shape import TUnknownShape


class APlacableFabric(ABC, Generic[TUnknownShape]):
    @abstractmethod
    def create_placable_element(self, element_type: Type[IPlacableElement[TUnknownShape]]) -> IPlacableElement[TUnknownShape]:
        """fabric method"""
        pass
