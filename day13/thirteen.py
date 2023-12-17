""" Day thirteen """


def parse_input(filename: str = "input") -> list[str]:
    with open(filename, encoding="utf-8") as _:
        return _.read().splitlines()

def part_one(data: list[str]):
    maps = ("\n".join(data)).split("\n\n")
    print(sum(find_mirror(_map) for _map in maps))

def part_two(data: list[str]):
    maps = ("\n".join(data)).split("\n\n")
    print(sum(find_mirror(_map, diff=1) for _map in maps))

def find_mirror(_map: str, diff=0) -> int:
    _map_h = _map.split("\n")
    _map_v = ["".join(c) for c in zip(*_map_h)]

    for pattern, weight in ((_map_h, 100), (_map_v, 1)):
        for i in range(1, len(pattern)):
            a, b = pattern[:i], pattern[i:]
            a = "".join(a[::-1])
            b = "".join(b)
            if sum(x != y for x, y in zip(a, b)) == diff:
                return i * weight

    return -1

if __name__ == '__main__':
    input_lines = parse_input()
    part_one(input_lines)
    part_two(input_lines)