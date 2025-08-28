import sys
from collections import deque

SEQUENCE = 'RGB'


def fluffbolts_line(balloons: str) -> int:
    bolts = 1

    for balloon_index in range(len(balloons)):
        if balloons[balloon_index] == SEQUENCE[(bolts - 1) % len(SEQUENCE)]:
            continue

        if balloon_index < len(balloons) - 1:
            bolts += 1

    return bolts


def fluffbolts_circle(balloons: str, repeat: int) -> int:
    left = deque(balloons * (repeat // 2))
    right = deque(balloons * (repeat // 2))
    bolts = 0

    while left:
        bolts += 1
        balloon = left.popleft()

        if (
            balloon == SEQUENCE[(bolts - 1) % len(SEQUENCE)]
            and (len(left) + len(right)) % 2 == 1
        ):
            right.popleft()

        elif len(right) > len(left):
            left.append(right.popleft())

    return bolts


def main():
    balloons = sys.stdin.readline().strip()

    print(fluffbolts_line(balloons))
    print(fluffbolts_circle(balloons, 100))
    print(fluffbolts_circle(balloons, 100000))


if __name__ == '__main__':
    main()
