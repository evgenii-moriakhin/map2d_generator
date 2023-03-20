from aplacement_config import RoomConfig
from dungeon_elements import Connector
from dungeon_map import DungeonMap
from dungeon_placement_strategies import ConnectorPlacementStrategy, RoomPlacementStrategy


class DungeonGenerator:
    def __init__(self, width, height, room_count=5):
        self.width = width
        self.height = height
        self.room_count = room_count

    def generate_dungeon(self):
        dungeon_map = DungeonMap(self.width, self.height)

        room_config = RoomConfig()
        room_placement_strategy = RoomPlacementStrategy()
        connector_placement_strategy = ConnectorPlacementStrategy()

        rooms = [room_config.create_placable_element() for _ in range(self.room_count)]

        for room in rooms:
            dungeon_map.place_element(room, room_placement_strategy)

        for i in range(1, len(rooms)):
            connector = Connector(rooms[i - 1], rooms[i])
            dungeon_map.place_element(connector, connector_placement_strategy)

        return dungeon_map
