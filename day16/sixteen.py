""" Day sixteen """


def parse_input(filename: str = "input") -> list[str]:
    with open(filename, encoding="utf-8") as _:
        return _.read().splitlines()


def calc(data, start, init_dir):
    q = [(start, init_dir)]
    visited = set()
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    h = len(data)
    w = len(data[0])

    while q:
        pos, d = q.pop(0)

        if (pos, d) in visited:
            continue
        visited.add((pos, d))

        _next_d = []
        curr = data[pos[0]][pos[1]]

        if curr == ".":
            _next_d.append(d)
        elif curr == "\\":
            _next_d.append(d + (-1) ** d)
        elif curr == "/":
            _next_d.append(3 - d)
        elif curr == "-":
            if d % 2:
                _next_d.append((d + 1) % 4)
                _next_d.append((d + 3) % 4)
            else:
                _next_d.append(d)
        elif curr == "|":
            if d % 2:
                _next_d.append(d)
            else:
                _next_d.append((d + 1) % 4)
                _next_d.append((d + 3) % 4)

        for _d in _next_d:
            y, x = (pos[0] + dirs[_d][0], pos[1] + dirs[_d][1])
            if 0 <= y < h and 0 <= x < w and ((y, x), _d) not in visited:
                q.append(((y, x), _d))

    return len(set(pos for pos, _ in visited))


def part_one(lines: list[str]):
    start = (0, 0)
    d = 0
    print(calc(lines, start, d))


def part_two(lines: list[str]):
    h = len(lines)
    w = len(lines[0])
    results = []

    for y in range(h):
        for x in range(w):
            if y not in [0, h - 1] and x not in [0, w - 1]:
                continue

            init_dir = []

            if y == 0:
                init_dir.append(1)
            elif y == h - 1:
                init_dir.append(3)

            if x == 0:
                init_dir.append(0)
            elif x == w - 1:
                init_dir.append(2)

            for d in init_dir:
                results.append(calc(lines, (y, x), d))

    print(max(results))


if __name__ == '__main__':
    input_lines = parse_input()
    part_one(input_lines)
    part_two(input_lines)
