from pathlib import Path
from helpers import read_lines 

INPUT_PATH = Path(__file__).with_suffix(".txt")

piece_sizes = {0: 7,
               1: 7,
               2: 5,
               3: 7,
               4: 7,
               5: 6}

def parse(lines: list[str]):
    """Turn raw input lines into a useful data structure."""
    results = []
    spaces = lines[30:]
    for s in spaces:
        chunks = s.split(":")
        sizes = tuple(map(int, chunks[0].split("x")))
        counts = list(map(int, chunks[1].split()))
        results.append((sizes, counts))
    return results


def part1(data) -> int:
    count = 0
    for size, counts in data:
        w, h = size
        area_total = w * h
        piece_total = sum(map(lambda v: v[1] * piece_sizes[v[0]], enumerate(counts)))
        if piece_total <= area_total:
            count += 1
    return count


def solve(path: Path = INPUT_PATH) -> None:
    """Read input, solve both parts, print results."""
    lines = read_lines(path)
    data = parse(lines)
    print("Part 1:", part1(data))


if __name__ == "__main__":
    solve()


EXAMPLE_INPUT = """\
0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2
"""

def _example_lines() -> list[str]:
    return EXAMPLE_INPUT.splitlines()


def test_example_part1():
    data = parse(_example_lines())
    assert part1(data) == 2
