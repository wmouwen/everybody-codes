import sys


def required_potions(creatures: str, group_size: int) -> int:
    potions = 0

    for i in range(0, len(creatures), group_size):
        group = creatures[i : i + group_size].replace('x', '')

        potions += (
            len(group) * (len(group) - 1)
            + 1 * group.count('B')
            + 3 * group.count('C')
            + 5 * group.count('D')
        )

    return potions


def main():
    creatures = sys.stdin.readline().strip()

    print(required_potions(creatures, 1))
    print(required_potions(creatures, 2))
    print(required_potions(creatures, 3))


if __name__ == '__main__':
    main()
