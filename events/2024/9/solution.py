import sys
from math import ceil, floor


def calc_min_beetles(stamps, target) -> list[int]:
    dp = [float('inf')] * (target + 1)
    dp[0] = 0

    for i in range(1, target + 1):
        for stamp in stamps:
            if stamp <= i:
                dp[i] = min(dp[i], dp[i - stamp] + 1)

    return dp


def main():
    balls = [int(line.strip()) for line in sys.stdin]

    stamps = [1, 3, 5, 10]
    beetles = calc_min_beetles(stamps, max(balls))
    print(sum(beetles[ball] for ball in balls))

    stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30]
    beetles = calc_min_beetles(stamps, max(balls))
    print(sum(beetles[ball] for ball in balls))

    stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101]
    max_difference = 100
    beetles = calc_min_beetles(stamps, max(balls) + ceil(max_difference / 2))
    print(
        sum(
            min(
                beetles[ceil(ball / 2) - d] + beetles[floor(ball / 2) + d]
                for d in range(ceil(max_difference / 2) + 1)
            )
            for ball in balls
        )
    )


if __name__ == '__main__':
    main()
