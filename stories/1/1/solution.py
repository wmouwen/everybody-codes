import re
import sys


def eni(n: int, e: int, m: int, length: int) -> int:
    remainders = [pow(n, e_i, m) for e_i in range(e, max(0, e - length), -1)]

    return int(''.join(map(str, remainders)))


def main():
    inputs = [tuple(map(int, re.findall(r'-?\d+', line))) for line in sys.stdin]

    print(
        max(
            eni(a, x, m, 10) + eni(b, y, m, 10) + eni(c, z, m, 10)
            for a, b, c, x, y, z, m in inputs
        )
    )

    print(
        max(
            eni(a, x, m, 5) + eni(b, y, m, 5) + eni(c, z, m, 5)
            for a, b, c, x, y, z, m in inputs
        )
    )


if __name__ == '__main__':
    main()
