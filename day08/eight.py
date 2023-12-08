""" Day eight """

import math

def parse_input(filename: str = "input") -> list[str]:
    with open(filename, encoding="utf-8") as _:
        return _.read().splitlines()

def prepare_data(lines: list) -> tuple[list[str], dict[str, dict[str, str]]]:
    inst = list(lines[0])
    _map = {}
    for line in lines[2:]:
        node, nexts = line.split(" = ")
        _map[node] = dict(zip(['L', 'R'], nexts[1:-1].split(', ')))
    return inst, _map

def part_one(instr: list[str], _map: dict[str, dict[str, str]]):
    curr = "AAA"
    end = "ZZZ"
    instr_idx = 0
    steps = 0

    while curr != end:
        curr = _map[curr][instr[instr_idx]]
        instr_idx = (instr_idx + 1) % len(instr)
        steps += 1

    print(steps)

def part_two(instr: list[str], _map: dict[str, dict[str, str]]):
    curr = [node for node in _map if node.endswith("A")]
    instr_idx = 0
    steps = 0

    least_steps = [0] * len(curr)

    while 0 in least_steps:
        for i, node in enumerate(curr):
            if node.endswith("Z"):
                least_steps[i] = steps
        curr = [_map[node][instr[instr_idx]] for node in curr]
        instr_idx = (instr_idx + 1) % len(instr)
        steps += 1

    print(math.lcm(*least_steps))

if __name__ == "__main__":
    input_lines = parse_input()
    instructions, _map = prepare_data(input_lines)
    part_one(instructions, _map)
    part_two(instructions, _map)
