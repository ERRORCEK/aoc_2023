""" Day seventeen """

from heapq import heappop, heappush


def parse_input(filename: str = "input") -> list[str]:
    with open(filename, encoding="utf-8") as _:
        return _.read().splitlines()


def find_path(lines: list[str], minimum_step_before_turn=1, maximum_consecutive_steps=3):
    h = len(lines)
    w = len(lines[0])
    start = (0, 0)
    end = (h - 1, w - 1)

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    visited = {}                # {(pos, d): loss}
    q = [(0, start, -1, 0)]     # (loss, pos, dir, dir_continuous)

    while q:
        loss, pos, d, _ = heappop(q)
        if pos == end:
            return loss

        allowed_dirs = [_d for _d in range(4) if _d != d and (_d + 2) % 4 != d]

        for _d in allowed_dirs:
            _next_loss = loss
            for d_cont in range(1, maximum_consecutive_steps + 1):
                _next_pos = tuple(a + b * d_cont for a,
                                  b in zip(pos, dirs[_d]))
                if 0 <= _next_pos[0] < h and 0 <= _next_pos[1] < w:
                    _next_loss += int(lines[_next_pos[0]][_next_pos[1]])
                    if _next_loss < visited.get((_next_pos, _d), float("inf")):
                        visited[(_next_pos, _d)] = _next_loss
                        if d_cont >= minimum_step_before_turn:
                            heappush(q, (_next_loss, _next_pos, _d, d_cont))


def part_one(lines: list[str]):
    print(find_path(lines, 1, 3))


def part_two(lines: list[str]):
    print(find_path(lines, 4, 10))


if __name__ == "__main__":
    lines = parse_input()
    part_one(lines)
    part_two(lines)
