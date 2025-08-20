import sys


def words_count(sentence: str, words: list[str]) -> int:
    return sum(sentence.count(word) for word in words)


def symbols_count(sentence: str, words: list[str]) -> int:
    runics = set()

    for i in range(len(sentence)):
        for word in words:
            if sentence[i : i + len(word)] in (word, word[::-1]):
                runics |= set(range(i, i + len(word)))

    return len(runics)


def crossword_count(grid: list[str], words: list[str]) -> int:
    runics = set()
    max_len = max(len(word) for word in words)

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            for dy, dx in (-1, 0), (0, 1), (1, 0), (0, -1):
                word = ''
                cells = set()

                for i in range(max_len):
                    ny = y + i * dy
                    if not 0 <= ny < len(grid):
                        break

                    nx = (x + i * dx) % len(grid[ny])

                    word += grid[ny][nx]
                    cells = cells | {(ny, nx)}

                    if word in words:
                        runics |= cells

    return len(runics)


def main():
    words = sys.stdin.readline().strip()[6:].split(',')
    sys.stdin.readline()

    lines = [line.strip() for line in sys.stdin if line.strip()]

    print(sum(words_count(line, words) for line in lines))
    print(sum(symbols_count(line, words) for line in lines))
    print(crossword_count(lines, words))


if __name__ == '__main__':
    main()
