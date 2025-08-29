import sys


def calc_depths(
    grid: list[list[str]], directions: list[tuple[int, int]]
) -> list[list[int]]:
    depths = [[None if cell == '#' else 0 for cell in row] for row in grid]

    depth = 0
    triggered = True
    while triggered:
        depth += 1
        triggered = False

        for y in range(len(depths)):
            for x in range(len(depths[y])):
                if depths[y][x] is not None:
                    continue

                neighbors = [
                    depths[y + dy][x + dx]
                    for dx, dy in directions
                    if 0 <= y + dy < len(depths) and 0 <= x + dx < len(depths[y + dy])
                ]

                if any(
                    neighbor is not None and neighbor != depth for neighbor in neighbors
                ) and all(
                    neighbor is None or neighbor <= depth for neighbor in neighbors
                ):
                    triggered = True
                    depths[y][x] = depth

    return depths


def main():
    grid = [list(line.strip()) for line in sys.stdin]

    neighbors = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    depths = calc_depths(grid, neighbors)
    print(sum(cell for row in depths for cell in row))
    print(sum(cell for row in depths for cell in row))

    grid = [
        ['.'] * (len(grid[0]) + 2),
        *(['.'] + row + ['.'] for row in grid),
        ['.'] * (len(grid[-1]) + 2),
    ]
    neighbors = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
    depths = calc_depths(grid, neighbors)
    print(sum(cell for row in depths for cell in row))


if __name__ == '__main__':
    main()
