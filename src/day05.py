from pathlib import Path
from helpers import read_lines 

INPUT_PATH = Path(__file__).with_suffix(".txt")

def parse(lines: list[str]):
    """Turn raw input lines into a useful data structure."""
    blank = lines.index("")
    ranges = []
    for l in lines[:blank]:
        vals = l.split("-")
        ranges.append(range(int(vals[0]), int(vals[1])+1))
    vals = []
    for l in lines[blank+1:]:
        vals.append(int(l))
    return (ranges, vals)


def part1(data) -> int:
    ranges, vals = data
    count = 0
    for v in vals:
        for r in ranges:
            if v in r:
                count += 1
                break
    return count


def part2(data) -> int:
    ranges, _vals = data
    ranges = sorted(ranges, key=lambda v: v.start)
    blocks = [(ranges[0].start, ranges[0].stop-1)]
    for r in ranges[1:]:
        last_start, last_stop = blocks[-1]
        r_start = r.start
        r_stop = r.stop-1
        if r_stop <= last_stop:
            continue
        elif r_start > last_stop:
            blocks.append((r_start, r_stop))
        else:
            blocks[-1] = (last_start, r_stop)
    return sum(map(lambda x: (x[1]-x[0])+1, blocks))


def solve(path: Path = INPUT_PATH) -> None:
    """Read input, solve both parts, print results."""
    lines = read_lines(path)
    data = parse(lines)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))


if __name__ == "__main__":
    solve()


EXAMPLE_INPUT = """\
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

def _example_lines() -> list[str]:
    return EXAMPLE_INPUT.splitlines()


def test_example_part1():
    data = parse(_example_lines())
    assert part1(data) == 3


def test_example_part2():
    data = parse(_example_lines())
    assert part2(data) == 14

