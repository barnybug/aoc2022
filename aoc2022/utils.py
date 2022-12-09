from pathlib import Path
from typing import NamedTuple

input_dir = Path(__file__).parent / "inputs"

class Answer(NamedTuple):
    part1: int
    part2: int

    def __str__(self):
        return "part1: %s\npart2: %s" % (self.part1, self.part2)

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

DIRS = {
    'L': Point(-1, 0),
    'U': Point(0, 1),
    'D': Point(0, -1),
    'R': Point(1, 0),
}
