from collections import deque
import re

from .utils import Answer

def parse(input: str, order: bool):
    initial, moves = input.split("\n\n")
    lines = initial.split("\n")
    stacks = []
    for n in re.finditer(r"\d", lines[-1]):
        stack = [line[n.start()] for line in lines[:-1]]
        stack = [s for s in stack if s != " "]
        stacks.append(deque(reversed(stack)))

    for move in moves.split("\n"):
        count, frm, to = map(int, re.findall(r"\d+", move))
        moving = [stacks[frm-1].pop() for _ in range(count)]
        if order:
            moving.reverse()
        stacks[to-1].extend(moving)

    return "".join(stack[-1] for stack in stacks)

def solve(input: str):
    part1 = parse(input, False)
    part2 = parse(input, True)
    return Answer(part1, part2)
