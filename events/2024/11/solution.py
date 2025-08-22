import sys
from collections import defaultdict


type Population = dict[str, int]
type Mapping = dict[str, list[str]]


def read_input() -> Mapping:
    mapping = defaultdict(list)

    for line in sys.stdin:
        source, targets = line.strip().split(':')

        for target in targets.split(','):
            mapping[source].append(target)

    return dict(mapping)


def evolve(population: Population, mapping: Mapping) -> Population:
    new_population = defaultdict(int)

    for source, count in population.items():
        if source not in mapping:
            continue

        for target in mapping[source]:
            new_population[target] += count

    return dict(new_population)


def population_size(population: Population, mapping: Mapping, evolutions: int) -> int:
    for _ in range(evolutions):
        population = evolve(population, mapping)

    return sum(population.values())


def main():
    mapping = read_input()

    print(population_size({'A': 1}, mapping, 4))
    print(population_size({'Z': 1}, mapping, 10))

    population_sizes = [
        population_size({key: 1}, mapping, 20) for key in mapping.keys()
    ]
    print(max(population_sizes) - min(population_sizes))


if __name__ == '__main__':
    main()
