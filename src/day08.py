from pathlib import Path
from helpers import read_lines 
import math

INPUT_PATH = Path(__file__).with_suffix(".txt")

def parse(lines: list[str]):
    """Turn raw input lines into a useful data structure."""
    return [tuple(map(int, l.split(","))) for l in lines]

def part1(num_connect, data) -> int:
    distances = []
    for d1 in data:
        for d2 in data:
            if d1 < d2:
                distances.append((math.dist(d1, d2), d1, d2))
    distances.sort()

    circuits = {}
    members = {}
    circuit_num = 0
    for _dist, d1, d2 in distances[:num_connect]:
        if d1 not in circuits and d2 not in circuits:
            circuits[d1] = circuit_num
            circuits[d2] = circuit_num
            members[circuit_num] = {d1, d2}
            circuit_num += 1
        elif d1 not in circuits and d2 in circuits:
            c = circuits[d2]
            circuits[d1] = c
            m = members[c] | {d1}
            members[c] = m
        elif d1 in circuits and d2 not in circuits:
            c = circuits[d1]
            circuits[d2] = c
            m = members[c] | {d2}
            members[c] = m
        else:
            # combine both sets to a new set
            old_d1 = circuits[d1]
            old_d2 = circuits[d2]
            if old_d1 != old_d2:
                m1 = members[old_d1]
                m2 = members[old_d2]
                m = m1 | m2
                members[circuit_num] = m
                del members[old_d1]
                del members[old_d2]
                for e in m:
                    circuits[e] = circuit_num
                circuit_num += 1

    c = members.values()
    c = list(map(len, c))
    c.sort(reverse=True)
    return c[0] * c[1] * c[2]


def part2(data) -> int:
    distances = []
    for d1 in data:
        for d2 in data:
            if d1 < d2:
                distances.append((math.dist(d1, d2), d1, d2))
    distances.sort()

    circuits = {}
    members = {}
    circuit_num = 0
    for _dist, d1, d2 in distances:
        if d1 not in circuits and d2 not in circuits:
            circuits[d1] = circuit_num
            circuits[d2] = circuit_num
            members[circuit_num] = {d1, d2}
            circuit_num += 1
        elif d1 not in circuits and d2 in circuits:
            c = circuits[d2]
            circuits[d1] = c
            m = members[c] | {d1}
            members[c] = m
        elif d1 in circuits and d2 not in circuits:
            c = circuits[d1]
            circuits[d2] = c
            m = members[c] | {d2}
            members[c] = m
        else:
            # combine both sets to a new set
            old_d1 = circuits[d1]
            old_d2 = circuits[d2]
            if old_d1 != old_d2:
                m1 = members[old_d1]
                m2 = members[old_d2]
                m = m1 | m2
                members[circuit_num] = m
                del members[old_d1]
                del members[old_d2]
                for e in m:
                    circuits[e] = circuit_num
                circuit_num += 1
        if len(circuits) == len(data) and len(members) == 1:
            x1, y1, z1 = d1
            x2, y2, z2 = d2
            return x1 * x2

    return 0


def solve(path: Path = INPUT_PATH) -> None:
    """Read input, solve both parts, print results."""
    lines = read_lines(path)
    data = parse(lines)
    print("Part 1:", part1(1000, data))
    print("Part 2:", part2(data))


if __name__ == "__main__":
    solve()


EXAMPLE_INPUT = """\
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""

def _example_lines() -> list[str]:
    return EXAMPLE_INPUT.splitlines()


def test_example_part1():
    data = parse(_example_lines())
    assert part1(10, data) == 40


def test_example_part2():
    data = parse(_example_lines())
    assert part2(data) == 25272

