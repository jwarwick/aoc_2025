from pathlib import Path
from helpers import read_lines 
import math
from collections import defaultdict

INPUT_PATH = Path(__file__).with_suffix(".txt")

def parse(lines: list[str]):
    """Turn raw input lines into a useful data structure."""
    elts = [l.split() for l in lines]
    elts = list(zip(*elts))
    return elts

def parse2(lines: list[str]):
    ops = lines[-1].split()
    idx_list = [idx for idx, ch in enumerate(lines[-1]) if not ch.isspace()][1:]
    idx_list.insert(0, 0)
    idx_list.append(len(lines[-1])+2)
    pairs = list(zip(idx_list, idx_list[1:]))
    values = defaultdict(list)
    for idx, pos in enumerate(pairs):
        start, stop = pos
        for l in lines[:-1]:
            s = l[start:stop-1]
            values[idx].append(s)
    data = []
    for k in values.keys():
        l = values[k]
        new_l = list(zip(*l))
        new_l = list(map(lambda x: int("".join(x)), new_l))
        new_l.append(ops[k])
        data.append(new_l)
    return data

def part1(data) -> int:
    result = 0
    for d in data:
        op = d[-1]
        args = list(map(int, d[:-1]))
        if op == "*":
            result += math.prod(args)
        else:
            result += sum(args)
    return result


def solve(path: Path = INPUT_PATH) -> None:
    """Read input, solve both parts, print results."""
    lines = read_lines(path)
    data = parse(lines)
    print("Part 1:", part1(data))
    data2 = parse2(lines)
    print("Part 2:", part1(data2))


if __name__ == "__main__":
    solve()


EXAMPLE_INPUT = """\
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   + 
"""

def _example_lines() -> list[str]:
    return EXAMPLE_INPUT.splitlines()


def test_example_part1():
    data = parse(_example_lines())
    assert part1(data) == 4277556


def test_example_part2():
    data = parse2(_example_lines())
    assert part1(data) == 3263827

