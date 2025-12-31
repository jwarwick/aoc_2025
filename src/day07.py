from pathlib import Path
from helpers import read_lines 
from collections import defaultdict

INPUT_PATH = Path(__file__).with_suffix(".txt")

def parse(lines: list[str]):
    """Turn raw input lines into a useful data structure."""
    splitters = {}
    start = (0,0)
    manifold_end = len(lines)
    for r, line in enumerate(lines):
        for c, val in enumerate(line):
            if val == "S":
                start = (c, r)
            elif val == "^":
                splitters[(c, r)] = "^"

    return (start, splitters, manifold_end)


def part1(data) -> int:
    start, splitters, manifold_end = data
    split_cnt = 0
    tachyons = set([start])
    for row in range(manifold_end):
        new_tachyons = set()
        for x, y in tachyons:
            new_pos = (x, y+1)
            if new_pos in splitters:
                split_cnt += 1
                new_tachyons.update([(x-1, y+1), (x+1, y+1)])
            else:
                new_tachyons.add(new_pos)
        tachyons = new_tachyons
    return split_cnt


def part2(data) -> int:
    start, splitters, manifold_end = data
    x, _y = start
    tachyons = {x: 1}
    for y in range(manifold_end):
        new_tachyons = defaultdict(int)
        for x in tachyons.keys():
            cnt = tachyons[x]
            new_pos = (x, y+1)
            if new_pos in splitters:
                new_tachyons[x-1] += cnt
                new_tachyons[x+1] += cnt
            else:
                new_tachyons[x] += cnt
        tachyons = new_tachyons
    total = sum(tachyons.values())
    return total


def solve(path: Path = INPUT_PATH) -> None:
    """Read input, solve both parts, print results."""
    lines = read_lines(path)
    data = parse(lines)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))


if __name__ == "__main__":
    solve()


EXAMPLE_INPUT = """\
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""

def _example_lines() -> list[str]:
    return EXAMPLE_INPUT.splitlines()


def test_example_part1():
    data = parse(_example_lines())
    assert part1(data) == 21


def test_example_part2():
    data = parse(_example_lines())
    assert part2(data) == 40

