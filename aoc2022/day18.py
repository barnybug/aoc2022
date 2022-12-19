from .utils import Answer
from typing import NamedTuple

class Cube(NamedTuple):
    x: int
    y: int
    z: int

    def neighbours(self):
        for x, y, z in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, 1), (0, 0, -1)]:
            yield Cube(self.x+x, self.y+y, self.z+z)

def solve(input: str):
    cubes = set()
    for line in input.splitlines():
        cube = Cube(*map(int, line.split(",")))
        cubes.add(cube)

    part1 = sum(
        neighbour not in cubes
        for cube in cubes
        for neighbour in cube.neighbours()
    )

    steam = set()
    xs = range(min(c.x-1 for c in cubes), max(c.x+2 for c in cubes))
    ys = range(min(c.y-1 for c in cubes), max(c.y+2 for c in cubes))
    zs = range(min(c.z-1 for c in cubes), max(c.z+2 for c in cubes))
    fill = [Cube(xs.start, ys.start, zs.start)]
    while fill:
        c = fill.pop()
        steam.add(c)
        for neighbour in c.neighbours():
            if neighbour.x in xs and neighbour.y in ys and neighbour.z in zs:
                if neighbour not in steam and neighbour not in cubes:
                    fill.append(neighbour)

    part2 = sum(
        neighbour in steam
        for cube in cubes
        for neighbour in cube.neighbours()
    )

    return Answer(part1, part2)
