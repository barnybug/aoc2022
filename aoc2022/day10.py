from itertools import islice
from .utils import Answer, grouper

def execute(input: str):
    x = 1
    yield x # before/during 1st cycle
    for line in input.splitlines():
        yield x
        if line.startswith("addx"):
            x += int(line.split()[-1])
            yield x

def solve(input: str):
    xs = list(enumerate(execute(input)))
    part1 = sum((a+1)*b for a, b in islice(xs, 19, None, 40))

    seq = ("#" if abs(i % 40-x) < 2 else "." for i, x in xs[:-1])
    part2 = "\n".join("".join(i) for i in grouper(seq, 40))
    return Answer(part1, part2)
