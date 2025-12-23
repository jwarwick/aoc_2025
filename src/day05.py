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
    print(f"Ranges: {ranges}")
    blocks = [(ranges[0].start, ranges[0].stop-1)]
    for r in ranges[1:]:
        idx_to_mod = -1
        new_start = -1
        new_stop = -1
        r_start = r.start
        r_stop = r.stop-1
        print(f"Blocks: {blocks}")
        for idx, (start, stop) in enumerate(blocks):
            print(f"Considering block {idx}: {start}, {stop}")
            if r_start >= start and r_stop <= stop:
                print(f"Contained, dropping")
                break
            elif r_start <= stop:
                print(f"Extending: {start}, {r_stop}")
                idx_to_mod = idx
                new_start = start
                new_stop = r_stop
            else:
                idx_to_mod = len(blocks)
                print(f"Appending: {idx_to_mod}: {r_start}, {r_stop}")
                new_start = r_start
                new_stop = r_stop
        if idx_to_mod > -1:
            if idx_to_mod >= len(blocks):
                blocks.append((0,0))
            blocks[idx_to_mod] = (new_start, new_stop)
            print(f"updated blocks: {blocks}")

    print(f"Blocks: {blocks}")
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

