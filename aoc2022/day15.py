import re
from .utils import Answer, Point

def parse(input: str):
    ret = []
    for line in input.splitlines():
        sx, sy, bx, by = map(int, re.findall(r"-?\d+", line))
        s = Point(sx, sy)
        b = Point(bx, by)
        ret.append((s, b))
    return ret

def exclusion(input: list, row: int):
    bounds = []
    for s, b in input:
        d = s.manhattan(b)
        delta = d - abs(s.y - row)
        if delta < 0:
            continue
        a, b = s.x - delta, s.x + delta + 1
        bounds.extend([(a, True), (b, False)])
    bounds.sort()
    n = 0
    simpler = []
    for x, p in bounds:
        if p:
            if n == 0:
                simpler.append((x, True))
            n += 1
        else:
            n -= 1
            if n == 0:
                simpler.append((x, False))
    return simpler

def part1(input: list, row: int):
    bounds = exclusion(input, row)
    beacons = len({b.x for _, b in input if b.y == row})
    total = sum(b[0]-a[0] for a, b in zip(bounds, bounds[1:]))
    return total - beacons

def part2(input: list, limit: int):
    for y in range(0, limit):
        bounds = exclusion(input, y)
        # find the gap
        for a, b in zip(bounds[1::2], bounds[2::2]):
            if a[0] != b[0]:
                x = a[0]
                return x * 4000000 + y

def solve(input: str):
    readings = parse(input)
    return Answer(part1(readings, 2000000), part2(readings, 4000000))
