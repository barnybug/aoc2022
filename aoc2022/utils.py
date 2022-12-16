import itertools
from pathlib import Path
from typing import NamedTuple

input_dir = Path(__file__).parent / "inputs"


class Answer(NamedTuple):
    part1: int
    part2: int

    def __str__(self):
        def spacer(s):
            s = str(s)
            return ("\n" if "\n" in s else " ") + s

        return "part1:%s\npart2:%s" % (spacer(self.part1), spacer(self.part2))


def input_data(day):
    file = input_dir / f"input{day:02d}.txt"
    return file.read_text()


class Point(NamedTuple):
    x: int
    y: int

    def __add__(self, b):
        return Point(self.x + b.x, self.y + b.y)

    def __sub__(self, b):
        return Point(self.x - b.x, self.y - b.y)

    def __str__(self):
        return "(%d,%d)" % (self.x, self.y)

    def manhattan(self, p):
        return abs(self.x-p.x) + abs(self.y-p.y)

    @property
    def left(self):
        return Point(self.x - 1, self.y)

    @property
    def right(self):
        return Point(self.x + 1, self.y)

    @property
    def up(self):
        return Point(self.x, self.y - 1)

    @property
    def down(self):
        return Point(self.x, self.y + 1)

Point.L = Point(-1, 0)
Point.U = Point(0, 1)
Point.D = Point(0, -1)
Point.R = Point(1, 0)

DIRS = {
    "L": Point(-1, 0),
    "U": Point(0, 1),
    "D": Point(0, -1),
    "R": Point(1, 0),
}


def grouper(iterable, n, *, incomplete="fill", fillvalue=None):
    "Collect data into non-overlapping fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, fillvalue='x') --> ABC DEF Gxx
    # grouper('ABCDEFG', 3, incomplete='strict') --> ABC DEF ValueError
    # grouper('ABCDEFG', 3, incomplete='ignore') --> ABC DEF
    args = [iter(iterable)] * n
    if incomplete == "fill":
        return itertools.zip_longest(*args, fillvalue=fillvalue)
    if incomplete == "strict":
        return zip(*args, strict=True)
    if incomplete == "ignore":
        return zip(*args)
    else:
        raise ValueError("Expected fill, strict, or ignore")
