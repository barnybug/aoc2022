import re
from .utils import Answer

def solve(input: str):
    full, partial = 0, 0
    for line in input.split():
        a, b, c, d = map(int, re.split(r"\D", line))
        if (a <= c and b >= d) or (c <= a and d >= b): # fully contained
            full += 1
        elif (a <= c and b >= c) or (a <= d and b >= d): # partial overlap
            partial += 1
    return Answer(full, full + partial)
