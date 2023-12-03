""" Day two """


def parse_input(filename: str = "input") -> list:
    with open(filename, encoding="utf-8") as _:
        return _.read().splitlines()


def part_one_and_two(lines: list):
    total_one = 0
    total_two = 0
    impossible = []
    for idx, line in enumerate(lines):
        _, rule = line.strip().split(":")
        right = rule.split(";")
        min_dict = {
            "red": 0,
            "green": 0,
            "blue": 0
        }

        total_one += idx + 1

        for i in right:
            color_dict = {
                "red": 0,
                "green": 0,
                "blue": 0
            }

            for j in i.split(","):
                count, color = j.strip().split(" ")
                color_dict[color] = int(count)

            if any(val > limit for val, limit in zip(color_dict.values(), [12, 13, 14])):
                impossible.append(idx + 1)

            for color, _ in color_dict.items():
                min_dict[color] = max(min_dict[color], color_dict[color])

        total_two += min_dict["red"] * min_dict["green"] * min_dict["blue"]

    print(total_one - sum(set(impossible)))
    print(total_two)


if __name__ == "__main__":
    input_lines = parse_input()
    part_one_and_two(input_lines)
