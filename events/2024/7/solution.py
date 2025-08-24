import sys
from enum import StrEnum
from functools import cache
from itertools import permutations
from typing import NamedTuple


type Mapping = dict[str, list[Action]]


class Vector(NamedTuple):
    x: int
    y: int

    @cache
    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(x=self.x + other.x, y=self.y + other.y)


DIRECTIONS = (
    Vector(x=0, y=-1),
    Vector(x=1, y=0),
    Vector(x=0, y=1),
    Vector(x=-1, y=0),
)

EASY_TRACK = """
S-=++=-==++=++=-=+=-=+=+=--=-=++=-==++=-+=-=+=-=+=+=++=-+==++=++=-=-=--
-                                                                     -
=                                                                     =
+                                                                     +
=                                                                     +
+                                                                     =
=                                                                     =
-                                                                     -
--==++++==+=+++-=+=-=+=-+-=+-=+-=+=-=+=--=+++=++=+++==++==--=+=++==+++-
"""
HARD_TRACK = """
S+= +=-== +=++=     =+=+=--=    =-= ++=     +=-  =+=++=-+==+ =++=-=-=--
- + +   + =   =     =      =   == = - -     - =  =         =-=        -
= + + +-- =-= ==-==-= --++ +  == == = +     - =  =    ==++=    =++=-=++
+ + + =     +         =  + + == == ++ =     = =  ==   =   = =++=
= = + + +== +==     =++ == =+=  =  +  +==-=++ =   =++ --= + =
+ ==- = + =   = =+= =   =       ++--          +     =   = = =--= ==++==
=     ==- ==+-- = = = ++= +=--      ==+ ==--= +--+=-= ==- ==   =+=    =
-               = = = =   +  +  ==+ = = +   =        ++    =          -
-               = + + =   +  -  = + = = +   =        +     =          -
--==++++==+=+++-= =-= =-+-=  =+-= =-= =--   +=++=+++==     -=+=++==+++-
"""


class Action(StrEnum):
    INCREASE = '+'
    DECREASE = '-'
    MAINTAIN = '='
    START = 'S'


def read_input() -> Mapping:
    devices = dict()

    for line in sys.stdin:
        source, targets = line.strip().split(':')
        devices[source] = tuple(map(Action, targets.split(',')))

    return devices


def track_sequence(track: str) -> list[Action]:
    grid = [list(line.strip()) for line in track.strip().splitlines()]

    start = next(
        Vector(x=x, y=y)
        for y in range(len(grid))
        for x in range(len(grid[y]))
        if grid[y][x] == Action.START
    )
    sequence = [Action.START]
    previous = {start}
    current = start + Vector(x=1, y=0)

    while grid[current.y][current.x] != Action.START:
        sequence.append(Action(grid[current.y][current.x]))

        for direction in DIRECTIONS:
            neighbor = current + direction
            if neighbor == previous:
                continue
            if not (
                0 <= neighbor.y < len(grid) and 0 <= neighbor.x < len(grid[neighbor.y])
            ):
                continue
            if grid[neighbor.y][neighbor.x] not in Action:
                continue

            previous = current
            current = neighbor

            break

    return sequence


def device_power(device: list[Action], track_length: int) -> int:
    output = 0
    power = 10

    for s in range(track_length):
        match device[s % len(device)]:
            case Action.INCREASE:
                power += 1
            case Action.DECREASE:
                power -= 1

        output += power

    return output


def device_essence(device: list[Action], track: list[Action], loops: int) -> int:
    output = 0
    power = 10

    for s in range(len(track) * (len(device) if loops % len(device) == 0 else loops)):
        match track[(s + 1) % len(track)]:
            case Action.INCREASE:
                power += 1
            case Action.DECREASE:
                power -= 1
            case _:
                match device[s % len(device)]:
                    case Action.INCREASE:
                        power += 1
                    case Action.DECREASE:
                        power -= 1

        output += power

    return output


def main():
    devices = read_input()

    power_levels = {
        label: device_power(device, track_length=10)
        for label, device in devices.items()
    }
    sorted_devices = sorted(
        power_levels.items(),
        key=lambda item: item[1],
        reverse=True,
    )
    print(''.join(label for label, _ in sorted_devices))

    essences = {
        label: device_essence(device, track=track_sequence(EASY_TRACK), loops=10)
        for label, device in devices.items()
    }
    sorted_devices = sorted(
        essences.items(),
        key=lambda item: item[1],
        reverse=True,
    )
    print(''.join(label for label, _ in sorted_devices))

    opponent = device_essence(
        devices['A'],
        track=track_sequence(HARD_TRACK),
        loops=2024,
    )
    actions = [Action.INCREASE] * 5 + [Action.DECREASE] * 3 + [Action.MAINTAIN] * 3
    winning_permutations = 0
    visited = set()
    for permutation in permutations(actions):
        if permutation in visited:
            continue
        visited.add(permutation)

        essence = device_essence(
            list(permutation),
            track=track_sequence(HARD_TRACK),
            loops=2024,
        )

        if essence > opponent:
            winning_permutations += 1

    print(winning_permutations)


if __name__ == '__main__':
    main()
