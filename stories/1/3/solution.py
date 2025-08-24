import re
import sys
from math import lcm
from typing import NamedTuple


class Snail(NamedTuple):
    x: int
    y: int

    @property
    def disc(self) -> int:
        return self.x + self.y - 1

    @property
    def offset(self) -> int:
        return self.x % self.disc

    def move(self, steps: int) -> 'Snail':
        offset = (self.offset + steps - 1) % self.disc

        return Snail(x=offset + 1, y=self.disc - offset)


def read_input() -> list[Snail]:
    snails = []

    for line in sys.stdin:
        x, y = map(int, re.findall(r'-?\d+', line))
        snails.append(Snail(x=x, y=y))

    return snails


def time_to_golden_line(snails: list[Snail]) -> int | None:
    offset = (snails[0].disc - snails[0].offset) % snails[0].disc
    multiplier = snails[0].disc

    for snail in snails[1:]:
        while (snail.offset + offset) % snail.disc != 0:
            if snail.disc % multiplier == 0:
                return None

            offset += multiplier

        multiplier = lcm(multiplier, snail.disc)

    return offset


def main():
    snails = read_input()

    evolved = (snail.move(100) for snail in snails)
    print(sum(snail.x + 100 * snail.y for snail in evolved))

    offset = time_to_golden_line(snails)
    print(offset)
    print(offset)


if __name__ == '__main__':
    main()
