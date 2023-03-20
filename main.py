from dungeon_generator import DungeonGenerator
from vizualizer import visualize_dungeon


def main():
    dungeon_width = 50
    dungeon_height = 50
    room_count = 10

    dungeon_generator = DungeonGenerator(dungeon_width, dungeon_height, room_count)
    dungeon_map = dungeon_generator.generate_dungeon()

    visualize_dungeon(dungeon_map)


if __name__ == "__main__":
    main()
