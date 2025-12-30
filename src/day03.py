from pathlib import Path
from helpers import read_lines 

INPUT_PATH = Path(__file__).with_suffix(".txt")

def parse(lines: list[str]):
    """Turn raw input lines into a useful data structure."""
    return list(map(list, lines))


def compute_joltage(l) -> int:
    curr_max = 0
    for idx, v1 in enumerate(l[:-1]):
        for v2 in l[idx+1:]:
            curr = int("".join([v1, v2]))
            if curr > curr_max:
                curr_max = curr
    return curr_max


def compute_joltage_part2(l) -> int:
    result = ""
    start_idx = 0
    digits_left = 12
    while digits_left > 0:
        stop_idx = (len(l) - digits_left) + 1
        s = l[start_idx:stop_idx]
        m = max(s)
        idx = s.index(m)
        start_idx += idx + 1
        digits_left -= 1
        result += m
    return int(result)


def part1(data) -> int:
    total = 0
    for d in data:
        total += compute_joltage(d)
    return total


def part2(data) -> int | str:
    total = 0
    for d in data:
        total += compute_joltage_part2(d)
    return total
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
987654321111111
811111111111119
234234234234278
818181911112111
"""

def _example_lines() -> list[str]:
    return EXAMPLE_INPUT.splitlines()


def test_example_part1():
    data = parse(_example_lines())
    assert part1(data) == 357


def test_example_part2():
    data = parse(_example_lines())
    assert part2(data) == 3121910778619

