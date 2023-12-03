""" Day three """


def parse_input(filename: str = "input") -> list:
    with open(filename, encoding="utf-8") as _:
        return _.read().splitlines()


def part_one(lines: list):
    s = set()
    lines = [x.strip() for x in lines]

    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char.isdigit() or char == '.':
                continue

            for x in [row - 1, row, row + 1]:
                for y in [col - 1, col, col + 1]:
                    if x < 0 or x >= len(lines) or y < 0 or y >= len(lines[x]) or not lines[x][y].isdigit():
                        continue
                    while y > 0 and lines[x][y-1].isdigit():
                        y -= 1
                    s.add((x, y))

    nums = []
    for x, y in s:
        a = ""
        while y < len(lines[x]) and lines[x][y].isdigit():
            a += lines[x][y]
            y += 1
        nums.append(int(a))

    print(sum(nums))


def part_two(lines: list):
    t = []
    lines = [x.strip() for x in lines]

    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char != '*':
                continue
            s = set()

            for x in [row - 1, row, row + 1]:
                for y in [col - 1, col, col + 1]:
                    if x < 0 or x >= len(lines) or y < 0 or y >= len(lines[x]) or not lines[x][y].isdigit():
                        continue
                    while y > 0 and lines[x][y-1].isdigit():
                        y -= 1
                    s.add((x, y))

            if len(s) != 2:
                continue

            nums = []

            for x, y in s:
                a = ""
                while y < len(lines[x]) and lines[x][y].isdigit():
                    a += lines[x][y]
                    y += 1
                nums.append(int(a))
            t.append(nums[0] * nums[1])

    print(sum(t))


if __name__ == "__main__":
    input_lines = parse_input()
    part_one(input_lines)
    part_two(input_lines)
