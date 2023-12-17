""" Day twelve """

from functools import cache

def parse_input(filename: str = "input") -> list[str]:
    with open(filename, encoding="utf-8") as _:
        return _.read().splitlines()

@cache
def get_possible_count(springs, groups, prev_size=0, must_operational=False):
    if springs == "":
        if groups:
            if len(groups) == 1 and groups[0] == prev_size:
                return 1
            return 0
        else:
            if prev_size == 0:
                return 1
            else:
                return 0

    if len(groups) == 0:
        if "#" in springs or prev_size > 0:
            return 0
        return 1

    curr = springs[0]
    rest = springs[1:]

    if curr == "?":
        return get_possible_count("#" + rest, groups, prev_size, must_operational) + \
               get_possible_count("." + rest, groups, prev_size, must_operational)

    if curr == "#":
        if must_operational:
            return 0

        curr_size = prev_size + 1

        if curr_size > groups[0]:
            return 0
        elif curr_size == groups[0]:
            return get_possible_count(rest, groups[1:], 0, True)
        else:
            return get_possible_count(rest, groups, curr_size, False)

    if curr == ".":
        if must_operational:
            return get_possible_count(rest, groups, 0, False)

        if prev_size == 0:
            return get_possible_count(rest, groups, 0, False)
        else:
            if prev_size != groups[0]:
                return 0
            else:
                return get_possible_count(rest, groups[1:], 0, False)

def part_one(lines: list[str]):
    _sum = 0

    for line in lines:
        springs, groups = line.split()
        groups = tuple([*map(int, groups.split(","))])
        _sum += get_possible_count(springs, groups)

    print(_sum)

def part_two(lines: list[str]):
    _sum = 0

    for line in lines:
        springs, groups = line.split()
        
        springs = "?".join([springs] * 5)
        groups = ",".join([groups] * 5)
        groups = tuple([*map(int, groups.split(","))])
        _sum += get_possible_count(springs, groups)

    print(_sum)


if __name__ == '__main__':
    input_lines = parse_input()
    part_one(input_lines)
    part_two(input_lines)
