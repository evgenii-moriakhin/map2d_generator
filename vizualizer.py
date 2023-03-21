import tkinter as tk
from cell import Cell
from elements.placable.concrete.map2d import Map2D

# Configuration for character-color mapping
CHARACTER_COLOR_MAPPING = {
    '#': 'gray',
    ' ': 'white',
    '-': 'tan',
}


class DungeonVisualizer(tk.Tk):
    def __init__(self, map_: Map2D, max_screen_width=800, max_screen_height=800):
        super().__init__()

        self.map = map_
        self.cell_size = min(max_screen_width // self.map.shape.size, max_screen_height // self.map.shape.size)
        self.canvas = tk.Canvas(self, width=self.map.shape.size * self.cell_size, height=self.map.shape.size * self.cell_size)
        self.canvas.pack()

        self.title("Dungeon Visualizer")
        self._draw_map()

    def _draw_map(self):
        for x in range(self.map.shape.size):
            for y in range(self.map.shape.size):
                cell = Cell(x, y)
                symbol = self.map.cells[cell].symbol
                color = CHARACTER_COLOR_MAPPING.get(symbol, 'red')  # Default to red for unknown symbols

                self._draw_cell(x, y, color)

    def _draw_cell(self, x, y, color):
        x1, y1 = x * self.cell_size, y * self.cell_size
        x2, y2 = x1 + self.cell_size, y1 + self.cell_size

        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='')


def visualize_map(map_: Map2D) -> None:
    app = DungeonVisualizer(map_)
    app.mainloop()
