from abc import ABC, abstractmethod


class ATile(ABC):
    @property
    @abstractmethod
    def symbol(self) -> str:
        pass
