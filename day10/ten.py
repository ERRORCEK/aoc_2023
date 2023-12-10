""" Day ten """


import re


def parse_input(filename: str = "input") -> list[str]:
    with open(filename, encoding="utf-8") as _:
        return _.read().splitlines()


def parse_map(lines: list[str]) -> tuple[list, set]:
    start = None
    _map = []

    for h, line in enumerate(lines):
        _map.append(list(line))
        if 'S' in line:
            start = (h, line.index('S'))

    adjacent_dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    symbol_connections = {
        "|": (1, 0, 1, 0),
        "-": (0, 1, 0, 1),
        "L": (1, 1, 0, 0),
        "J": (1, 0, 0, 1),
        "7": (0, 0, 1, 1),
        "F": (0, 1, 1, 0),
    }

    adj_conn_types = {
        (-1, 0): "F|7",
        (0, 1): "7-J",
        (1, 0): "L|J",
        (0, -1): "F-L",
    }

    adjs = [0, 0, 0, 0]

    for i, adj in enumerate(adjacent_dirs):
        pos = tuple(a + b for a, b in zip(start, adj))
        if _map[pos[0]][pos[1]] in adj_conn_types[adj]:
            adjs[i] = 1

    _map[start[0]][start[1]] = {
        v: k for k, v in symbol_connections.items()}[tuple(adjs)]

    queue = [start]
    visited = set()

    while queue:
        pos = queue.pop(0)
        if pos in visited:
            continue
        visited.add(pos)
        if _map[pos[0]][pos[1]] in " .":
            continue

        sym = _map[pos[0]][pos[1]]
        _dirs = [adjacent_dirs[i]
                 for i, v in enumerate(symbol_connections[sym]) if v == 1]
        for dy, dx in _dirs:
            queue.append((pos[0] + dy, pos[1] + dx))
    print(type(_map))
    return _map, visited


def part_one(lines: list[str]):
    _, _loop_nodes = parse_map(lines)
    print(len(_loop_nodes) / 2)


def part_two(lines: list[str]):
    _map, _loop_nodes = parse_map(lines)
    row_counts = []

    for h, items in enumerate(_map):
        line = [v if (h, w) in _loop_nodes else "."
                for w, v in enumerate(items)]
        line = "".join(line)

        line = re.sub(r"L-*7", "|", line)
        line = re.sub(r"L-*J", "||", line)
        line = re.sub(r"F-*7", "||", line)
        line = re.sub(r"F-*J", "|", line)

        cross = 0
        inside = 0

        for c in line:
            if c == "." and cross % 2:
                inside += 1
            elif c in "F7LJ|":
                cross += 1
        row_counts.append(inside)
    print(sum(row_counts))


if __name__ == '__main__':
    input_lines = parse_input()
    part_one(input_lines)
    part_two(input_lines)
