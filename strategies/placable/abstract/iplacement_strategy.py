from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from elements.placable.abstract.iplacable_element import IPlacableElement
from elements.placable.abstract.shapes.unknown_shape import UnknownShape

TUnknownShape1 = TypeVar("TUnknownShape1", bound=UnknownShape)
TUnknownShape2 = TypeVar("TUnknownShape2", bound=UnknownShape)


class IPlacementStrategy(ABC, Generic[TUnknownShape1, TUnknownShape2]):
    @abstractmethod
    def place(self, _map: IPlacableElement[TUnknownShape1], element: IPlacableElement[TUnknownShape2]) -> None:
        pass
