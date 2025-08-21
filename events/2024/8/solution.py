import sys
from math import ceil, sqrt


def missing_blocks_for_pyramid(blocks: int) -> int:
    level = ceil(sqrt(blocks))

    required_blocks = level**2

    width = 2 * level - 1
    return width * (required_blocks - blocks)


def missing_blocks_for_tower(priests: int, acolytes: int, blocks: int) -> int:
    level = 0
    required_blocks = 0

    while required_blocks < blocks:
        level += 1
        thickness = pow(priests, level - 1, acolytes)
        width = 2 * level - 1

        required_blocks += thickness * width

    width = 2 * level - 1
    return width * (required_blocks - blocks)


def missing_blocks_for_shrine(priests: int, acolytes: int, blocks: int) -> int:
    # TODO
    return 0


def main():
    seed = int(sys.stdin.readline())

    print(missing_blocks_for_pyramid(seed))
    print(missing_blocks_for_tower(seed, 1111, 20240000))
    print(missing_blocks_for_shrine(seed, 10, 202400000))


if __name__ == '__main__':
    main()
