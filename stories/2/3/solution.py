import re
import sys
from typing import NamedTuple


class Dice(NamedTuple):
    id: int
    faces: tuple[int, ...]
    seed: int


def read_input() -> tuple[list[Dice], list[list[int]]]:
    dices, race_tracks = [], []

    for line in sys.stdin:
        match = re.match(r'(\d+): faces=\[(.+)] seed=(\d+)', line.strip())
        if not match:
            break

        dice = Dice(
            id=int(match.group(1)),
            faces=tuple(map(int, match.group(2).split(','))),
            seed=int(match.group(3)),
        )
        dices.append(dice)

    for line in sys.stdin:
        if line.strip():
            race_tracks.append(list(map(int, line.strip())))

    return dices, race_tracks


def main():
    dices, race_tracks = read_input()

    pulses = [dice.seed for dice in dices]
    rotation = [0 for _ in dices]

    roll_number, points = 0, 0
    while points < 10000:
        roll_number += 1

        for i, dice in enumerate(dices):
            spin = roll_number * pulses[i]

            rotation[i] += spin
            rotation[i] %= len(dice.faces)

            pulses[i] += spin
            pulses[i] %= dice.seed
            pulses[i] = pulses[i] + 1 + roll_number + dice.seed

            points += dice.faces[rotation[i] % len(dice.faces)]

    print(roll_number)

    race_track = race_tracks[0]
    pulses = [dice.seed for dice in dices]
    rotation = [0 for _ in dices]
    track_position = [0 for _ in dices]
    finishing_order = []

    roll_number = 0
    while race_track and len(finishing_order) < len(dices):
        roll_number += 1

        for i, dice in enumerate(dices):
            spin = roll_number * pulses[i]

            rotation[i] += spin
            rotation[i] %= len(dice.faces)

            pulses[i] += spin
            pulses[i] %= dice.seed
            pulses[i] = pulses[i] + 1 + roll_number + dice.seed

            rolled_value = dice.faces[rotation[i] % len(dice.faces)]

            if (
                track_position[i] < len(race_track)
                and rolled_value == race_track[track_position[i]]
            ):
                track_position[i] += 1
                if track_position[i] == len(race_track):
                    finishing_order.append(dice.id)

    print(','.join(map(str, finishing_order)))

    # TODO Grid Traversal


if __name__ == '__main__':
    main()
