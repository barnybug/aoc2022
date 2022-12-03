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
