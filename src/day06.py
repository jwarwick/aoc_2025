from pathlib import Path
from helpers import read_lines 
import math

INPUT_PATH = Path(__file__).with_suffix(".txt")

def parse(lines: list[str]):
    """Turn raw input lines into a useful data structure."""
    elts = [l.split() for l in lines]
    elts = list(zip(*elts))
    return elts


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


def part2(data) -> int:
    return 0


def solve(path: Path = INPUT_PATH) -> None:
    """Read input, solve both parts, print results."""
    lines = read_lines(path)
    data = parse(lines)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))


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
    data = parse(_example_lines())
    assert part2(data) == 3263827

