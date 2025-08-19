import re
import sys


def eni(n: int, e: int, m: int) -> int:
    score = 1
    remainders = []

    for e_i in range(e):
        score = (score * n) % m
        remainders.insert(0, score)

    return int(''.join(map(str, remainders)))


def main():
    highest_result = 0

    for line in sys.stdin:
        a, b, c, x, y, z, m = map(int, re.findall(r'-?\d+', line))

        result = eni(a, x, m) + eni(b, y, m) + eni(c, z, m)
        highest_result = max(highest_result, result)

    print(highest_result)


if __name__ == '__main__':
    main()
