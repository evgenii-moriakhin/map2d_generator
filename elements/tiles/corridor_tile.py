from elements.tiles.atile import ATile


class CorridorTile(ATile):
    @property
    def symbol(self) -> str:
        return "-"
