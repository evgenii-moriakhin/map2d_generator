from cell import Cell
from elements.placable.abstract.shapes.square_shape import SquareShape
from elements.placable.abstract.shapes.unknown_shape import UnknownShape
from elements.placable.concrete.corridor import Corridor
from elements.placable.concrete.map2d import Map2D
from elements.placable.concrete.room import Room

from elements.placable.facrics.square_fabric import SquareFabric
from strategies.placable.concrete.connector_strategy import ConnectorPlacementStrategy

from strategies.placable.concrete.square_strategy import SquarePlacementStrategy


class MapGenerator:
    def __init__(self, size: int, room_count: int=5) -> None:
        self.size = size
        self.room_count = room_count

    def generate_map(self) -> Map2D:
        _map = Map2D(SquareShape(self.size))
        for i in range(self.size):
            for j in range(self.size):
                _map.add_cell(Cell(i, j))

        square_placement_strategy = SquarePlacementStrategy()
        # square_placement_strategy.place(_map, _map)

        square_fabric = SquareFabric()

        rooms = [square_fabric.create_placable_element(Room) for _ in range(self.room_count)]

        for room in rooms:
            square_placement_strategy.place(_map, room)

        corridor_placement_strategy = ConnectorPlacementStrategy()
        corridor = Corridor(UnknownShape(1), rooms[0].center, rooms[1].center)
        corridor_placement_strategy.place(_map, corridor)

        return _map
