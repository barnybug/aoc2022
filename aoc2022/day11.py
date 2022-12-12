import enum
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
    _, op, b = s.split()
    if b == "old":
        op = "**"
    else:
        b = int(b)
    return op, b

@dataclass
class Monkey:
    items: deque[int]
    op: callable
    div: int
    jumps: int
    inspected: int = 0

def parse_monkey(s):
    m = re.match(parse, s)
    if not m:
        raise ValueError(f"failed to parse: {s}")
    _, items, ops, div, jump_true, jump_false = m.groups()
    op = compile_op(ops)
    items = deque(map(int, items.split(", ")))
    return Monkey(items, op, int(div), [int(jump_false), int(jump_true)])

def calc(input: str, rounds: int, part1: bool):
    monkeys = [parse_monkey(s) for s in input.split("\n\n")]
    lcm = prod(m.div for m in monkeys)

    for _ in range(rounds):
        for monkey in monkeys:
            monkey.inspected += len(monkey.items)
            for item in monkey.items:
                op, n = monkey.op
                match op:
                    case "+":
                        item = item + n
                    case "*":
                        item = item * n
                    case _:
                        item = item * item % lcm
                if part1:
                    item //= 3
                jump = monkey.jumps[item % monkey.div == 0]
                monkeys[jump].items.append(item)
            monkey.items = deque()

    monkeys.sort(key=lambda m: m.inspected)
    return prod(m.inspected for m in monkeys[-2:])

def solve(input: str):
    part1 = calc(input, 20, True)
    part2 = calc(input, 10000, False)
    return Answer(part1, part2)
