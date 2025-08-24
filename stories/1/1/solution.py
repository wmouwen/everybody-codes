import re
import sys
from functools import cache


@cache
def eni_concat(n: int, e: int, m: int, length: int) -> int:
    remainders = [pow(n, e_i, m) for e_i in range(e, max(0, e - length), -1)]

    return int(''.join(map(str, remainders)))


@cache
def eni_sum(n: int, e: int, m: int) -> int:
    sum_remainders = 0
    remainder = 1
    e_i = 1
    seen = []

    while e_i <= e:
        remainder = (remainder * n) % m

        if remainder in seen:
            loop = seen[seen.index(remainder) :]
            loop_counts = (e - e_i) // len(loop)
            sum_remainders += sum(loop) * loop_counts
            e_i += len(loop) * loop_counts
            seen = []

        seen.append(remainder)

        sum_remainders += remainder
        e_i += 1

    return sum_remainders


def main():
    inputs = [tuple(map(int, re.findall(r'-?\d+', line))) for line in sys.stdin]

    outputs = (
        eni_concat(a, x, m, 10) + eni_concat(b, y, m, 10) + eni_concat(c, z, m, 10)
        for a, b, c, x, y, z, m in inputs
    )
    print(max(outputs))

    outputs = (
        eni_concat(a, x, m, 5) + eni_concat(b, y, m, 5) + eni_concat(c, z, m, 5)
        for a, b, c, x, y, z, m in inputs
    )
    print(max(outputs))

    outputs = (
        eni_sum(a, x, m) + eni_sum(b, y, m) + eni_sum(c, z, m)
        for a, b, c, x, y, z, m in inputs
    )
    print(max(outputs))


if __name__ == '__main__':
    main()
