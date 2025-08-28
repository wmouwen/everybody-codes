import sys


def throw(peg_board: list[str], toss_slot: int, sequence: str) -> int:
    col, row, s = (toss_slot - 1) * 2, 0, 0

    for row in range(len(peg_board)):
        if peg_board[row][col] != '*':
            continue

        move = sequence[s % len(sequence)]
        s += 1

        col += 1 if move == 'R' else -1
        if not (0 <= col < len(peg_board[0])):
            col -= 2 if move == 'R' else -2

    return (col // 2) + 1


def calc_score(toss_slot: int, final_slot: int) -> int:
    return max(final_slot * 2 - toss_slot, 0)


def minmax(
    outcomes: dict[int, dict[int, int]],
    coin: int = 0,
    used: set[int] = None,
    current: int = 0,
) -> tuple[int, int]:
    if coin == len(outcomes):
        return current, current

    if used is None:
        used = set()

    result = (sys.maxsize, 0)

    for pos, score in outcomes[coin].items():
        if pos in used:
            continue

        outcome = minmax(outcomes, coin + 1, used | {pos}, current + score)
        result = (min(result[0], outcome[0]), max(result[1], outcome[1]))

    return result


def main():
    peg_board = []
    while line := sys.stdin.readline().strip():
        peg_board.append(line)

    toss_slots = (len(peg_board[0]) + 1) // 2
    tokens = [line.strip() for line in sys.stdin.readlines() if line.strip()]

    outcomes = {
        i: {
            toss_slot: calc_score(toss_slot, throw(peg_board, toss_slot, sequence))
            for toss_slot in range(1, toss_slots + 1)
        }
        for i, sequence in enumerate(tokens)
    }
    print(sum(options[(i % toss_slots) + 1] for i, options in outcomes.items()))

    max_scores = [
        max(score for toss_slot, score in options.items())
        for i, options in outcomes.items()
    ]
    print(sum(max_scores))

    result = minmax(outcomes)
    print(f'{result[0]} {result[1]}')


if __name__ == '__main__':
    main()
