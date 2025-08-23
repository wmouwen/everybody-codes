import sys
from collections import defaultdict
from queue import Queue

type Mapping = dict[str, list[str]]
type Path = tuple[str]


def read_input() -> Mapping:
    mapping = dict()

    for line in sys.stdin:
        source, targets = line.strip().split(':')
        mapping[source] = targets.split(',')

    return dict(mapping)


def get_paths(mapping: Mapping, start: str, end: str) -> set[Path]:
    paths = set()

    queue: Queue[tuple[str, list[str]]] = Queue()
    queue.put((start, []))

    while not queue.empty():
        current, path = queue.get()

        if current == end:
            paths.add((*path, current))
            continue

        if current in path:
            continue

        for neighbor in mapping.get(current, []):
            queue.put((neighbor, path + [current]))

    return paths


def group_by_length(paths: set[Path]) -> dict[int, list[Path]]:
    grouped = defaultdict(list)

    for path in paths:
        grouped[len(path)].append(path)

    return dict(grouped)


def main():
    mapping = read_input()
    paths = get_paths(mapping, 'RR', '@')

    unique_lengths = [
        path
        for group in group_by_length(paths).values()
        if len(group) == 1
        for path in group
    ]

    print(''.join(unique_lengths[0]))
    print(''.join([p[0] for p in unique_lengths[0]]))
    print(''.join([p[0] for p in unique_lengths[0]]))


if __name__ == '__main__':
    main()
