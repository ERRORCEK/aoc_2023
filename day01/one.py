""" Day one """

import re


def parse_input(filename: str = "input") -> list:
    with open(filename, encoding="utf-8") as _:
        return _.read().splitlines()


def part_one(lines: list):
    result = 0
    for line in lines:
        digits = re.findall(r"\d", line)
        result += int(digits[0] + digits[-1])
    print(result)


d = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def convert(n):
    if n in d:
        return str(d.index(n) + 1)
    return n


def part_two(lines: list):
    result = 0
    for line in lines:
        digits = list(map(convert, re.findall(
            r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', line)))
        result += int(digits[0] + digits[-1])
    print(result)


if __name__ == '__main__':
    input_lines = parse_input()
    part_one(input_lines)
    part_two(input_lines)
