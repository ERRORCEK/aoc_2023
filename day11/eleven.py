""" Day eleven """


def parse_input(filename: str = "input") -> list[str]:
    with open(filename, encoding="utf-8") as _:
        return _.read().splitlines()

def calculate_length(data: list[str], expand_level: int) -> int:
    expand_cols = []
    expand_rows = []
    galaxies = []

    for r, line in enumerate(data):
        if "#" in line:
            for c, v in enumerate(line):
                if v == "#":
                    galaxies.append((r, c))
        else:
            expand_rows.append(r)

    for c, col in enumerate(zip(*data)):
        if "#" not in col:
            expand_cols.append(c)

    _sum = 0
    for i in range(len(galaxies) - 1):
        for j in range(i + 1, len(galaxies)):
            y1, x1 = galaxies[i]
            y2, x2 = galaxies[j]

            y1, y2 = sorted([y1, y2])
            x1, x2 = sorted([x1, x2])

            w = x2 - x1
            h = y2 - y1

            cols = sum([1 for c in expand_cols if x1 < c < x2])
            rows = sum([1 for r in expand_rows if y1 < r < y2])

            _sum += w + h + (expand_level - 1) * (cols + rows)

    return _sum

def part_one(lines: list[str]):
    expand_level = 2
    print(calculate_length(lines, expand_level))

def part_two(lines: list[str]):
    expand_level = 1000000
    if len(lines) == 10:
        expand_level = 100

    print(calculate_length(lines, expand_level))


if __name__ == '__main__':
    input_lines = parse_input()
    part_one(input_lines)
    part_two(input_lines)
