from abc import ABC, abstractmethod
from typing import TypeVar


class IConnectableElement(ABC):
    @property
    @abstractmethod
    def x1(self):
        pass

    @property
    @abstractmethod
    def y1(self):
        pass

    @property
    @abstractmethod
    def x2(self):
        pass

    @property
    @abstractmethod
    def y2(self):
        pass


TConnectableElement = TypeVar("TConnectableElement", bound=IConnectableElement)
