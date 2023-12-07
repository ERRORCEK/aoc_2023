""" Day six """


def parse_input(filename: str = "input") -> list:
    with open(filename, encoding="utf-8") as _:
        return _.read().splitlines()


def parse_part_one(lines: str) -> tuple:
    race_times = list(map(int, lines[0].split()[1::]))
    record_distances = list(map(int, lines[1].split()[1::]))
    return race_times, record_distances


def part_two(lines: str) -> tuple:
    race_times = [int("".join(lines[0].split()[1::]))]
    record_distances = [int("".join(lines[1].split()[1::]))]
    return race_times, record_distances


def caluculate_ways(times: list, distances: list):
    ways = [sum(1 for hold in range(time) if hold * (time - hold) > distance)
            for time, distance in zip(times, distances)]
    r = 1
    for w in ways:
        r *= w

    print(r)


if __name__ == '__main__':
    input_lines = parse_input()
    caluculate_ways(*parse_part_one(input_lines))
    caluculate_ways(*part_two(input_lines))
