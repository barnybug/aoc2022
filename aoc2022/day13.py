from itertools import zip_longest
from functools import cmp_to_key
from .utils import Answer

def compare(a: list, b: list) -> int:
    if isinstance(a, int):
        a = [a]
    if isinstance(b, int):
        b = [b]

    for left, right in zip_longest(a, b):
        if left is None:
            return -1
        if right is None:
            return 1
        if isinstance(left, int) and isinstance(right, int):
            if left < right:
                return -1
            elif left > right:
                return 1
        else:
            # one or both lists - recurse
            if c := compare(left, right):
                return c
    return 0

def solve(input: str):
    pairs = input.split("\n\n")
    part1 = 0

    part1 = sum(
        i+1
        for i, pair in enumerate(pairs)
        for left, right in [map(eval, pair.split())]
        if compare(left, right) == -1
    )

    packets = list(map(eval, (packet for packet in input.split() if packet)))
    packets.append([[2]])
    packets.append([[6]])

    packets.sort(key=cmp_to_key(compare))
    a = packets.index([[2]])
    b = packets.index([[6]])
    part2 = (a+1)*(b+1)

    return Answer(part1, part2)
