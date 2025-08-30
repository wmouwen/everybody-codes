import sys
from functools import cache
from typing import NamedTuple, Counter


GRID_SIZE = 8
EDGE_THICKNESS = 2


class Vector(NamedTuple):
    x: int
    y: int

    @cache
    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(x=self.x + other.x, y=self.y + other.y)


def read_input() -> list[dict[Vector, str]]:
    lines = [line.strip() for line in sys.stdin]

    return [
        {
            Vector(x=x, y=y): cell
            for y, row in enumerate(lines[by : by + GRID_SIZE + 1])
            for x, cell in enumerate(row[bx : bx + GRID_SIZE + 1])
        }
        for by in range(0, len(lines), GRID_SIZE + 1)
        for bx in range(0, len(lines[by]), GRID_SIZE + 1)
    ]


def extract_runic(grid: dict[Vector, str]) -> str:
    runic = ''

    for y in range(EDGE_THICKNESS, GRID_SIZE - EDGE_THICKNESS):
        for x in range(EDGE_THICKNESS, GRID_SIZE - EDGE_THICKNESS):
            symbols = Counter(
                value
                for cell, value in grid.items()
                if (cell.y == y or cell.x == x) and value != '.'
            )
            runic += symbols.most_common(1)[0][0]

    return runic


def main():
    grids = read_input()

    runic_words = [extract_runic(grid) for grid in grids]
    print(runic_words[0])

    print(
        sum(
            (key + 1) * (ord(value) - ord('A') + 1)
            for runic in runic_words
            for key, value in enumerate(runic)
        )
    )


if __name__ == '__main__':
    main()
