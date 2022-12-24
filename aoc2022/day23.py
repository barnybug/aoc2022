from .utils import Answer, Point
from collections import Counter

def solve(input: str):
    gnomes = {
        Point(x, y)
        for y, line in enumerate(input.splitlines())
        for x, c in enumerate(line)
        if c == "#"
    }

    surrounding = [
        Point(-1, -1), Point(0, -1), Point(1, -1),
        Point(-1, 0), Point(1, 0),
        Point(-1, 1), Point(0, 1), Point(1, 1),
    ]
    adjacents = [
        (Point(-1, -1), Point(0, -1), Point(1, -1)),
        (Point(-1, 1), Point(0, 1), Point(1, 1)),
        (Point(-1, -1), Point(-1, 0), Point(-1, 1)),
        (Point(1, -1), Point(1, 0), Point(1, 1)),
    ]

    for round in range(1000000):
        proposed = []
        count = Counter()
        stable = 0
        for gnome in gnomes:
            if gnomes.isdisjoint({gnome + a for a in surrounding}):
                stable += 1
                continue
            for i in range(round, round+4):
                adjacent = adjacents[i % 4]
                points = {gnome + a for a in adjacent}
                if gnomes.isdisjoint(points):
                    b = gnome + adjacent[1]
                    proposed.append((gnome, b))
                    count[b] += 1
                    break

        if stable == len(gnomes):
            break

        for a, b in proposed:
            if count[b] == 1:
                gnomes.remove(a)
                gnomes.add(b)

        if round == 9:
            xr = max(g.x for g in gnomes) + 1 - min(g.x for g in gnomes)
            yr = max(g.y for g in gnomes) + 1 - min(g.y for g in gnomes)
            area = xr * yr
            part1 = area - len(gnomes)

    return Answer(part1, round+1)
