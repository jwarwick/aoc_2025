from pathlib import Path
from helpers import read_lines 

INPUT_PATH = Path(__file__).with_suffix(".txt")

def parse(lines: list[str]):
    """Turn raw input lines into a useful data structure."""
    vals = []
    for l in lines:
        r = l.split("-")
        vals.append((int(r[0]), int(r[1])))
    return vals

def is_bad(v: int) -> bool:
    s = str(v)
    l = len(s)
    if l % 2 == 1:
        return False
    mid = l // 2
    if s[:mid] == s[mid:]:
       return True
    else:
       return False


def solve_day(data, f):
    total = 0
    for d in data:
        (start, stop) = d
        for v in range(start, stop+1):
            if f(v):
                total += v
    return total

def is_bad_2(v: int) -> bool:
    s = str(v)
    l = len(s)
    for chunk_len in range(1, (l//2)+1):
        if l % chunk_len != 0:
            continue
        chunks = [s[i:i+chunk_len] for i in range(0, len(s), chunk_len)]
        if len(set(chunks)) == 1:
            return True
    return False


def part1(data) -> int:
    return solve_day(data, is_bad)


def part2(data) -> int:
    return solve_day(data, is_bad_2)


def solve(path: Path = INPUT_PATH) -> None:
    """Read input, solve both parts, print results."""
    lines = path.read_text().strip().split(",")
    data = parse(lines)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))


if __name__ == "__main__":
    solve()


EXAMPLE_INPUT = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

def _example_lines() -> list[str]:
    return EXAMPLE_INPUT.strip().split(",")

def test_is_bad():
    assert is_bad(1010) == True

def test_example_part1():
    data = parse(_example_lines())
    assert part1(data) == 1227775554


def test_example_part2():
    data = parse(_example_lines())
    assert part2(data) == 4174379265

