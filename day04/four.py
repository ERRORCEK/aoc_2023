""" Day four """


import re


def parse_input(filename: str = "input") -> list:
    with open(filename, encoding="utf-8") as _:
        return _.read().splitlines()


def combined(lines: list):
    result = 0
    s = {}
    for i, line in enumerate(lines):
        left, right = line.split("|")
        winnig_nums = re.findall(r"\d+", left)[1::]
        yours_nums = re.findall(r"\d+", right)
        if i not in s:
            s[i] = 1

        common = set(winnig_nums).intersection(yours_nums)

        # For part one
        if len(common) > 0:
            result += 2 ** (len(common) - 1)

        # For part two
        if len(common) == 0:
            continue

        for n in range(i + 1, i + len(common) + 1):
            s[n] = s.get(n, 1) + s[i]

    print(result)
    print(sum(s.values()))


if __name__ == "__main__":
    input_lines = parse_input()
    combined(input_lines)
