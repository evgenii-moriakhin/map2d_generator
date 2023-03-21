import dataclasses
from typing import Iterator


@dataclasses.dataclass
class Cell:
    x: int
    y: int

    def __iter__(self) -> Iterator[int]:
        return iter((self.x, self.y))

    def __hash__(self) -> int:
        return hash((self.x, self.y))
