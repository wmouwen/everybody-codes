import sys
from functools import cache
from queue import PriorityQueue
from typing import NamedTuple


class Vector(NamedTuple):
    x: int
    y: int

    @cache
    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(x=self.x + other.x, y=self.y + other.y)


DIRECTIONS = {Vector(x=0, y=-1), Vector(x=1, y=0), Vector(x=0, y=1), Vector(x=-1, y=0)}


def floodfill(segments: set[Vector], sources: set[Vector]) -> dict[Vector, int]:
    distances = dict()

    queue = PriorityQueue()
    for source in sources:
        queue.put((0, source))

    while not queue.empty():
        distance, current = queue.get()

        if current in distances:
            continue

        distances[current] = distance

        for delta in DIRECTIONS:
            neighbor = current + delta

            if neighbor in segments:
                queue.put((distance + 1, neighbor))

    return distances


def main():
    grid = [list(line.strip()) for line in sys.stdin]
    segments = {
        Vector(x=x, y=y)
        for y in range(len(grid))
        for x in range(len(grid[y]))
        if grid[y][x] != '#'
    }
    open_edges = {
        v
        for v in segments
        if (v.y in (0, len(grid) - 1) or v.x in (0, len(grid[v.y]) - 1))
    }
    palm_trees = {v for v in segments if grid[v.y][v.x] == 'P'}

    if open_edges:
        flood_time = floodfill(segments, open_edges)
        palm_trees_flood_time = max(flood_time[tree] for tree in palm_trees)
        print(palm_trees_flood_time)
        print(palm_trees_flood_time)
    else:
        print(None)
        print(None)

    distances_sum = {segment: 0 for segment in segments if segment not in palm_trees}

    for palm_tree in palm_trees:
        distances = floodfill(segments, {palm_tree})

        for segment, distance in distances.items():
            if segment in distances_sum:
                distances_sum[segment] += distance

    print(min(distances_sum.values()))


if __name__ == '__main__':
    main()
