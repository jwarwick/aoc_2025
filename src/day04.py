from pathlib import Path
from helpers import read_lines 

INPUT_PATH = Path(__file__).with_suffix(".txt")

def parse(lines: list[str]):
    """Turn raw input lines into a useful data structure."""
    rolls = set()
    for row, l in enumerate(lines):
        for col, v in enumerate(l):
            if v == "@":
                rolls.add((col, row))
    return rolls

def reachable(data):
    r = []
    for col, row in data:
        neigh = [(col+x,row+y) for x in [-1,0,1] for y in [-1,0,1] if not(x==0 and y==0)]
        if sum(x in data for x in neigh) < 4:
            r.append((col, row))
    return r


def part1(data) -> int:
    return len(reachable(data))


def part2(data) -> int:
    count = 0
    r_cnt = 1
    while r_cnt > 0:
        r_list = reachable(data)
        r_cnt = len(r_list)
        count += r_cnt
        data.difference_update(r_list)
    return count


def solve(path: Path = INPUT_PATH) -> None:
    """Read input, solve both parts, print results."""
    lines = read_lines(path)
    data = parse(lines)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))


if __name__ == "__main__":
    solve()


EXAMPLE_INPUT = """\
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

def _example_lines() -> list[str]:
    return EXAMPLE_INPUT.splitlines()


def test_example_part1():
    data = parse(_example_lines())
    assert part1(data) == 13


def test_example_part2():
    data = parse(_example_lines())
    assert part2(data) == 43

