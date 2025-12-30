from pathlib import Path
from helpers import read_lines 
from functools import cache

INPUT_PATH = Path(__file__).with_suffix(".txt")

def parse(lines: list[str]):
    """Turn raw input lines into a useful data structure."""
    outputs = {}
    for l in lines:
        chunks = l.split(":")
        start = chunks[0]
        end = chunks[1].split()
        outputs[start] = end
    return outputs

global_outputs = {}

def part1(outputs) -> int:
    count = 0
    curr = ["you"]
    while curr:
        next_curr = []
        for c in curr:
            outs = outputs[c]
            if outs == ["out"]:
                count += 1
            else:
                next_curr += outs
        curr = next_curr
    return count


@cache
def count_paths(start, end) -> int:
    if start == end:
        return 1
    else:
        return sum([count_paths(curr, end) for curr in global_outputs.get(start, [])])

def part2(outputs) -> int:
    global global_outputs
    global_outputs = outputs
    s_d = count_paths("svr", "dac")
    d_f = count_paths("dac", "fft")
    f_o = count_paths("fft", "out")
    
    s_f = count_paths("svr", "fft")
    f_d = count_paths("fft", "dac")
    d_o = count_paths("dac", "out")

    return (s_d * d_f * f_o) + (s_f * f_d * d_o)


def solve(path: Path = INPUT_PATH) -> None:
    """Read input, solve both parts, print results."""
    lines = read_lines(path)
    data = parse(lines)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))


if __name__ == "__main__":
    solve()


EXAMPLE_INPUT = """\
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
"""

def _example_lines() -> list[str]:
    return EXAMPLE_INPUT.splitlines()


def test_example_part1():
    data = parse(_example_lines())
    assert part1(data) == 5

EXAMPLE_INPUT2 = """\
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
"""

def test_example_part2():
    data = parse(EXAMPLE_INPUT2.splitlines())
    assert part2(data) == 2

