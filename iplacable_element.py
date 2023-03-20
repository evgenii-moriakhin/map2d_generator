from abc import ABC, abstractmethod
from typing import TypeVar


class IPlacableElement(ABC):
    @property
    @abstractmethod
    def width(self):
        pass

    @property
    @abstractmethod
    def height(self):
        pass

    @property
    @abstractmethod
    def x(self):
        pass

    @property
    @abstractmethod
    def y(self):
        pass


TPlacableElement = TypeVar("TPlacableElement", bound=IPlacableElement)
