from pathlib import Path
from helpers import read_lines 
import z3

INPUT_PATH = Path(__file__).with_suffix(".txt")

def parse_one(line):
    chunks = line.split()
    target = chunks[0]
    target_set = set()
    for idx, c in enumerate(target[1:-1]):
        if c == "#":
            target_set.add(idx)
    options = chunks[1:-1]
    options_list = []
    for c in options:
        vals = c[1:-1].split(",")
        vals = set(map(int, vals))
        options_list.append(vals)
    joltage = chunks[-1]
    joltage = list(map(int, joltage[1:-1].split(",")))
    return (target_set, options_list, joltage)

def parse(lines: list[str]):
    """Turn raw input lines into a useful data structure."""
    return [parse_one(l) for l in lines]

def part1_one(d):
    target, options, _joltage = d
    curr = [set()]
    seen = {frozenset(set())}
    steps = 0
    while True:
        steps += 1
        new_curr = []
        for c in curr:
            for o in options:
                n = c ^ o
                if n == target:
                    return steps
                if n not in seen:
                    seen.add(frozenset(n))
                    new_curr.append(n)
        curr = new_curr

    return steps


def part2_one(data):
    _lights, button_data, joltage_data = data
    num_buttons = len(joltage_data)

    buttons = []
    for b in button_data:
        button = [0] * len(joltage_data)
        for idx in list(b):
            button[idx] = 1
        buttons.append(button)

    button_presses = [z3.Int(f"b_{i}") for i in range(len(button_data))]
    opt = z3.Optimize()
    for x in button_presses:
        opt.add(x >= 0)

    num_joltage = len(joltage_data)
    num_buttons = len(buttons)
    for j in range(num_joltage):
        opt.add(z3.Sum(buttons[b][j] * button_presses[b] for b in range(num_buttons)) == joltage_data[j])

    obj = z3.Sum(button_presses)
    opt.minimize(obj)

    if opt.check() != z3.sat:
        print(f"FAILED TO SATISFY")
        return 0

    model = opt.model()
    total_presses =  sum([model.evaluate(x).as_long() for x in button_presses])
    return total_presses


def part1(data) -> int:
    total = 0
    for d in data:
        total += part1_one(d)
    return total


def part2(data) -> int:
    total = 0
    for d in data:
        total += part2_one(d)
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
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""

def _example_lines() -> list[str]:
    return EXAMPLE_INPUT.splitlines()


def test_example_part1():
    data = parse(_example_lines())
    assert part1(data) == 7


def test_example_part2():
    data = parse(_example_lines())
    assert part2(data) == 33

