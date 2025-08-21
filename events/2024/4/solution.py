import statistics
import sys


def main():
    nails = list(int(line.strip()) for line in sys.stdin)

    hammer_strikes = sum(nail - min(nails) for nail in nails)
    print(hammer_strikes)
    print(hammer_strikes)

    median = int(statistics.median(nails))
    print(sum(abs(nail - median) for nail in nails))


if __name__ == '__main__':
    main()
