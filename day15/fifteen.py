""" Day fifteen """

from functools import reduce


def parse_input(filename: str = "input") -> list[str]:
    with open(filename, encoding="utf-8") as _:
        return _.read().splitlines()


def calc_hash(item):
    return reduce(lambda acc, c: (acc + ord(c)) * 17 % 256, item, 0)


def part_one(lines: list[str]):
    data = lines[0].split(",")
    print(sum(calc_hash(item) for item in data))


def part_two(lines: list[str]):
    data = lines[0].split(",")
    boxes = [{} for _ in range(256)]

    for line in data:
        if "=" in line:
            label, value = line.split("=")
            box_id = calc_hash(label)
            boxes[box_id][label] = int(value)
        else:
            label = line[:-1]
            box_id = calc_hash(label)
            if label in boxes[box_id]:
                del boxes[box_id][label]

    power = 0
    for boxid1, box in enumerate(boxes, 1):
        for slot_id, lens in enumerate(box.items(), 1):
            power += boxid1 * slot_id * lens[1]

    print(power)


if __name__ == '__main__':
    input_lines = parse_input()
    part_one(input_lines)
    part_two(input_lines)
