from math import prod
import re
from .utils import Answer
from dataclasses import dataclass
from collections import deque

parse = r"""Monkey (\d+):
  Starting items: ([^\n]+)
  Operation: new = ([^\n]+)
  Test: divisible by (\d+)
    If true: throw to monkey (\d+)
    If false: throw to monkey (\d+)"""

def compile_op(s):
    if s == "old * old":
        return lambda o: o*o
    _, op, b = s.split()
    b = int(b)
    if op == '*':
        return lambda o: o*b
    if op == '+':
        return lambda o: o+b
    raise ValueError(f"unsupported op: {s}")

MODS = list(range(2, 24))

class Item:
    mods: list[int]

    def __init__(self, mods: list[int]):
        self.mods = mods

    def __mod__(self, n):
        return self.mods[MODS.index(n)]

    def apply(self, op):
        for i, m in enumerate(MODS):
            self.mods[i] = op(self.mods[i]) % m

def make_item(s):
    return Item([int(s) % m for m in MODS])

@dataclass
class Monkey:
    items: deque[int]
    op: callable
    div: int
    jumps: int
    inspected: int = 0

def parse_monkey(s, part1):
    m = re.match(parse, s)
    if not m:
        raise ValueError(f"failed to parse: {s}")
    _, items, ops, div, jump_true, jump_false = m.groups()
    op = compile_op(ops)
    item = int if part1 else make_item
    items = deque(map(item, items.split(", ")))
    return Monkey(items, op, int(div), [int(jump_false), int(jump_true)])

def calc(input: str, rounds: int, part1: bool):
    global MODS
    monkeys = [parse_monkey(s, part1) for s in input.split("\n\n")]
    MODS = [m.div for m in monkeys]

    for _ in range(rounds):
        for monkey in monkeys:
            monkey.inspected += len(monkey.items)
            for item in monkey.items:
                if part1:
                    item = monkey.op(item)
                    item //= 3
                else:
                    item.apply(monkey.op)
                jump = monkey.jumps[item % monkey.div == 0]
                monkeys[jump].items.append(item)
            monkey.items = deque()

    monkeys.sort(key=lambda m: m.inspected)
    return prod(m.inspected for m in monkeys[-2:])

def solve(input: str):
    part1 = calc(input, 20, True)
    part2 = calc(input, 10000, False)
    return Answer(part1, part2)
