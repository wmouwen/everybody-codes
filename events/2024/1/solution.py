import sys


def main():
    potions = sys.stdin.readline().strip()

    print(potions.count('B') + 3 * potions.count('C'))


if __name__ == '__main__':
    main()
