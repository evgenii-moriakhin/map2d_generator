from abc import ABC
from typing import Iterable, TypeVar

from shapely.geometry import Point, Polygon, MultiPolygon


class UnknownShape(ABC):
    _geometry: MultiPolygon

    def __init__(self, points: Iterable[Point]):
        self._geometry = self._points_to_geometry(points)

    @staticmethod
    def _points_to_geometry(points: Iterable[Point]) -> MultiPolygon:
        geometry = Polygon([(point.x, point.y) for point in points]).convex_hull

        if geometry.geom_type == 'Polygon':
            return MultiPolygon([geometry])
        elif geometry.geom_type == 'MultiPolygon':
            return geometry
        else:
            raise ValueError("Unexpected geometry type")

    def center(self) -> Point:
        return self._geometry.centroid

    @property
    def area(self) -> float:
        return self._geometry.area

    def intersects(self, other: 'UnknownShape') -> bool:
        return self._geometry.intersects(other._geometry)

    def contains(self, other: 'UnknownShape') -> bool:
        return self._geometry.contains(other._geometry)

    def distance(self, other: 'UnknownShape') -> float:
        return self._geometry.distance(other._geometry)

    def bounding_box(self) -> Iterable[Point]:
        bounds = self._geometry.bounds
        top_left = Point(bounds[0], bounds[1])
        bottom_right = Point(bounds[2], bounds[3])
        return top_left, bottom_right


TUnknownShape = TypeVar("TUnknownShape", bound=UnknownShape)
