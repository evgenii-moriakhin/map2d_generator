from elements.tiles.atile import ATile


class EmptyTile(ATile):
    @property
    def symbol(self) -> str:
        return "#"
