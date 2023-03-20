from aplacable_element import APlacableElement
from iconnectable_element import IConnectableElement
from iplacable_element import IPlacableElement


class Room(APlacableElement):
    def __init__(self, min_size=5, max_size=10):
        self.min_size = min_size
        self.max_size = max_size


class Corridor(APlacableElement):
    def __init__(self):
        self._cells = []

    @property
    def cells(self):
        return self._cells

    def add_cell(self, x, y):
        self._cells.append((x, y))


class Connector(IConnectableElement):
    def __init__(self, element1: IPlacableElement, element2: IPlacableElement):
        self.element1 = element1
        self.element2 = element2

    @property
    def x1(self):
        return self.element1.x

    @property
    def y1(self):
        return self.element1.y

    @property
    def x2(self):
        return self.element2.x

    @property
    def y2(self):
        return self.element2.y
