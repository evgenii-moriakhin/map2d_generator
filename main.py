from map_generator import MapGenerator
from vizualizer import visualize_map


def main() -> None:
    map_size = 100
    room_count = 2

    map_generator = MapGenerator(map_size, room_count)
    map_ = map_generator.generate_map()

    visualize_map(map_)


if __name__ == "__main__":
    main()
