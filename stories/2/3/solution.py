import re
import sys
from copy import copy


class Dice:
    def __init__(self, id: str, faces: tuple[int, ...], seed: int):
        self.id: str = id
        self._faces: tuple[int, ...] = faces
        self._seed: int = seed
        self._pulse: int = seed
        self._roll_number: int = 0
        self._rotation: int = 0

    def roll(self) -> int:
        self._roll_number += 1
        spin = self._roll_number * self._pulse

        self._rotation += spin
        self._rotation %= len(self._faces)

        self._pulse += spin
        self._pulse %= self._seed
        self._pulse = self._pulse + 1 + self._roll_number + self._seed

        return self._faces[self._rotation]


def read_input() -> tuple[list[Dice], list[list[int]]]:
    dices, grid = [], []

    for line in sys.stdin:
        match = re.match(r'(\w+): faces=\[(.+)] seed=(\d+)', line.strip())
        if not match:
            break

        dice = Dice(
            id=match.group(1),
            faces=tuple(map(int, match.group(2).split(','))),
            seed=int(match.group(3)),
        )
        dices.append(dice)

    for line in sys.stdin:
        if line.strip():
            grid.append(list(map(int, line.strip())))

    return dices, grid


def rolls_to_points(dices: list[Dice], target: int) -> int:
    roll_number, points = 0, 0

    while points < target:
        roll_number += 1
        points += sum(dice.roll() for dice in dices)

    return roll_number


def race_track_finish(dices: list[Dice], race_track: list[int]) -> list[Dice]:
    track_position = [0 for _ in dices]
    finishing_order = []

    roll_number = 0
    while race_track and len(finishing_order) < len(dices):
        roll_number += 1

        for i, dice in enumerate(dices):
            roll = dice.roll()

            if (
                track_position[i] < len(race_track)
                and roll == race_track[track_position[i]]
            ):
                track_position[i] += 1
                if track_position[i] == len(race_track):
                    finishing_order.append(dice)

    return finishing_order


def grid_visits(dice: Dice, grid: list[list[int]]) -> set[tuple[int, int]]:
    roll = dice.roll()
    cells = {
        (x, y)
        for y in range(len(grid))
        for x in range(len(grid[y]))
        if grid[y][x] == roll
    }

    visited = [
        [(x, y) in cells for x, cell in enumerate(row)] for y, row in enumerate(grid)
    ]

    while cells:
        roll = dice.roll()
        new_cells = set()

        for x, y in cells:
            for nx, ny in ((x, y), (x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)):
                if not (0 <= ny < len(grid) and 0 <= nx < len(grid[ny])):
                    continue

                if grid[ny][nx] == roll:
                    new_cells.add((nx, ny))
                    visited[ny][nx] = True

        cells = new_cells

    return set(
        (x, y) for y in range(len(grid)) for x in range(len(grid[y])) if visited[y][x]
    )


def main():
    dices, grid = read_input()

    print(rolls_to_points([copy(dice) for dice in dices], 10000))

    if grid:
        finishing_order = race_track_finish([copy(dice) for dice in dices], grid[0])
        print(','.join(dice.id for dice in finishing_order))

        reachable_fields = set()
        for dice in dices:
            reachable_fields.update(grid_visits(copy(dice), grid))
        print(len(reachable_fields))

    else:
        print(None)
        print(None)


if __name__ == '__main__':
    main()
