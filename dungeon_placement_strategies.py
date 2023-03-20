import random

from dungeon_elements import Connector, Corridor, Room
from iconnectable_strategy import IConnectableStrategy
from iplacement_strategy import IPlacementStrategy


class RoomPlacementStrategy(IPlacementStrategy[Room]):
    def place(self, dungeon_map, element: Room):
        width, height = element.width, element.height
        element.x = random.randint(0, dungeon_map.width - width - 1)
        element.y = random.randint(0, dungeon_map.height - height - 1)

        for i in range(element.y, element.y + height):
            for j in range(element.x, element.x + width):
                if 0 <= i < dungeon_map.height and 0 <= j < dungeon_map.width:
                    dungeon_map.grid[i][j] = 1


class CorridorPlacementStrategy(IPlacementStrategy[Corridor]):
    def place(self, dungeon_map, element: Corridor):
        if 0 <= element.y < dungeon_map.height and 0 <= element.x < dungeon_map.width:
            dungeon_map.grid[element.y][element.x] = 1
            element.add_cell(element.x, element.y)


class ConnectorPlacementStrategy(IConnectableStrategy[Connector]):
    def place(self, dungeon_map, element: Connector):
        x1, y1 = element.x1, element.y1
        x2, y2 = element.x2, element.y2

        corridor = Corridor()

        # Horizontal corridor
        for x in range(min(x1, x2), max(x1, x2) + 1):
            corridor.x = x
            corridor.y = y1
            dungeon_map.place_element(corridor, CorridorPlacementStrategy())

        # Vertical corridor
        for y in range(min(y1, y2), max(y1, y2) + 1):
            corridor.x = x2
            corridor.y = y
            dungeon_map.place_element(corridor, CorridorPlacementStrategy())
