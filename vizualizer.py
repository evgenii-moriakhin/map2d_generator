def visualize_dungeon(dungeon_map):
    symbols = {
        0: "#",
        1: " ",
    }

    for row in dungeon_map.grid:
        print("".join(symbols[cell] for cell in row))
