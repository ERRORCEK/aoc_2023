""" Day fourteen """

def parse_input(filename: str = "input") -> list[str]:
        with open(filename, encoding="utf-8") as _:
            return _.read().splitlines()


def tilt(_map: list[list[str]]) -> list[list[str]]:
    cols = zip(*_map)
    cols_tilted = []
    for col in cols:
        parts = "".join(col).split("#")
        parts_tilted = [("O" * t.count("O")).ljust(len(t), ".") for t in parts]
        cols_tilted.append("#".join(parts_tilted))
    return [list(x) for x in zip(*cols_tilted)]

def turn(_map: list[list[str]]) -> list[list[str]]:
    return [list(x)[::-1] for x in zip(*_map)]

def count_total_load(_map: list[list[str]]) -> int:
    height = len(_map)
    return sum((height - i) * sum(1 for c in line if c == "O") for i, line in enumerate(_map))

def part_one(lines: list[str]):
    _map = [list(line) for line in lines]
    _map = tilt(_map)
    print(count_total_load(_map))

def part_two(lines: list[str]):
    _map = [list(line) for line in lines]
    cycle = 1000000000
    cache = {}

    for cycle_idx in range(cycle):
        for _ in range(4):
            _map = tilt(_map)
            _map = turn(_map)
        _hash = hash("".join("".join(x) for x in _map))

        if _hash not in cache:
            cache[_hash] = cycle_idx
        else:
            diff = cycle_idx - cache[_hash]
            head = cache[_hash]
            rest = cycle - ((cycle - head) // diff) * diff - head - 1
            break

    for _ in range(rest):
        for _ in range(4):
            _map = tilt(_map)
            _map = turn(_map)

    print(count_total_load(_map))

if __name__ == '__main__':
    input_lines = parse_input()
    part_one(input_lines)
    part_two(input_lines)
