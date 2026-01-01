from pathlib import Path
from helpers import read_lines 
from shapely import Polygon
from shapely.geometry import box

INPUT_PATH = Path(__file__).with_suffix(".txt")

def parse(lines: list[str]):
    """Turn raw input lines into a useful data structure."""
    points = []
    for l in lines:
        vals = l.split(",")
        points.append((int(vals[0]), int(vals[1])))
    return points

def area(p1, p2):
    p1x, p1y = p1
    p2x, p2y = p2
    w = abs(p2x-p1x)+1
    h = abs(p2y-p1y)+1
    return w*h

def part1(data) -> int:
    best = 0
    for p1 in data:
        for p2 in data:
            if p1 < p2:
                a = area(p1, p2)
                if a > best:
                    best = a
    return best


def part2(data) -> int:
    big = Polygon(data)
    best_area = 0
    for p1 in data:
        for p2 in data:
            p1x, p1y = p1
            p2x, p2y = p2
            rect = box(min(p1x, p2x),
                    min(p1y, p2y),
                    max(p1x, p2x),
                    max(p1y, p2y))
            a = area(p1, p2)
            if big.covers(rect) and a > best_area:
                best_area = a
    return best_area


def solve(path: Path = INPUT_PATH) -> None:
    """Read input, solve both parts, print results."""
    lines = read_lines(path)
    data = parse(lines)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))


if __name__ == "__main__":
    solve()


EXAMPLE_INPUT = """\
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""

def _example_lines() -> list[str]:
    return EXAMPLE_INPUT.splitlines()


def test_example_part1():
    data = parse(_example_lines())
    assert part1(data) == 50


def test_example_part2():
    data = parse(_example_lines())
    assert part2(data) == 24

