from typing import Optional

from iplacable_element import IPlacableElement


class APlacableElement(IPlacableElement):
    _width: Optional[int]
    _height: Optional[int]
    _x: Optional[int]
    _y: Optional[int]

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value
