from pathlib import Path
from helpers import read_lines 

INPUT_PATH = Path(__file__).with_suffix(".txt")

def parse(lines: list[str]):
    """Turn raw input lines into a useful data structure."""
    cmds = []
    for l in lines:
        direction = l[0]
        num = int(l[1:])
        cmds.append((direction, num))
    return cmds


def part1(data) -> int:
    curr = 50
    cnt = 0
    for (direction, num) in data:
        delta = num if direction == "R" else (-1 * num)
        curr = (curr + delta) % 100
        if curr == 0:
            cnt += 1
    return cnt


def part2(data) -> int:
    curr = 50
    cnt = 0
    for (direction, num) in data:
        mult = 1 if direction == "R" else -1
        values = []
        for v in range(1, num+1):
            values.append((curr + (mult * v)) % 100)
        cnt += values.count(0)
        curr = values[-1]
    return cnt


def solve(path: Path = INPUT_PATH) -> None:
    """Read input, solve both parts, print results."""
    lines = read_lines(path)
    data = parse(lines)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))


if __name__ == "__main__":
    solve()


EXAMPLE_INPUT = """\
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

def _example_lines() -> list[str]:
    return EXAMPLE_INPUT.splitlines()


def test_example_part1():
    data = parse(_example_lines())
    assert part1(data) == 3


def test_example_part2():
    data = parse(_example_lines())
    assert part2(data) == 6

