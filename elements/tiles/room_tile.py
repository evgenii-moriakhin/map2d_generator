from elements.tiles.atile import ATile


class RoomTile(ATile):
    @property
    def symbol(self) -> str:
        return " "
