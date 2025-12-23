from pathlib import Path
from helpers import read_lines 

INPUT_PATH = Path(__file__).with_suffix(".txt")

def parse(lines: list[str]):
    """Turn raw input lines into a useful data structure."""
    # TODO: customize for the puzzle
    return lines


def part1(data) -> int | str:
    # TODO: implement Part 1
    return 0


def part2(data) -> int | str:
    # TODO: implement Part 2
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
467..114..
...*......
..35..633.
......#..#
"""

def _example_lines() -> list[str]:
    return EXAMPLE_INPUT.splitlines()


def test_example_part1():
    data = parse(_example_lines())
    # replace 4361 with the expected answer from the problem statement
    assert part1(data) == 4361


def test_example_part2():
    data = parse(_example_lines())
    # replace 467835 with the expected answer from the problem statement
    assert part2(data) == 467835

