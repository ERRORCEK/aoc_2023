""" Day nine """


def parse_input(filename: str = "input") -> list[str]:
    with open(filename, encoding="utf-8") as _:
        return _.read().splitlines()

def solve(lines: list[str]):
    result_p1 = 0
    result_p2 = 0

    for line in lines:
        history = [*map(int, line.split())]
        diff = [b - a for a, b in zip(history, history[1:])]

        seqs = [history, diff]
        check = sum(1 for i in diff if i)

        while check:
            next_diff = [b - a for a, b in zip(diff, diff[1:])]
            seqs.append(next_diff)
            diff = next_diff
            check = sum(1 for i in diff if i)

        next_value_p1 = 0
        next_value_p2 = 0
        for seq in seqs[::-1]:
            next_value_p1 += seq[-1]
            next_value_p2 = seq[0] - next_value_p2

        result_p1 += next_value_p1
        result_p2 += next_value_p2

    print(result_p1)
    print(result_p2)

if __name__ == '__main__':
    input_lines = parse_input()
    solve(input_lines)
