from collections import defaultdict
import operator
import re
from typing import NamedTuple

from .utils import Answer

ops = {
    "+": (operator.add, operator.sub, operator.sub),
    "-": (operator.sub, operator.add, lambda var, a: a - var),
    "*": (operator.mul, operator.ifloordiv, operator.ifloordiv),
    "/": (operator.ifloordiv, operator.mul, lambda var, a: a // var),
}

class Equation(NamedTuple):
    var: str
    a: str
    b: str
    op: callable

    def calc(self, vars):
        if self.a in vars and self.b in vars:
            return self.var, self.op[0](vars[self.a], vars[self.b])
        elif self.a not in vars:
            return self.a, self.op[1](vars[self.var], vars[self.b])
        elif self.b not in vars:
            return self.b, self.op[2](vars[self.var], vars[self.a])

def resolve(vars: dict, eqs: dict[str, Equation]):
    vars = dict(vars)
    res = defaultdict(list)
    for eq in eqs.values():
        res[eq.var].append(eq)
        res[eq.a].append(eq)
        res[eq.b].append(eq)

    resolved = defaultdict(int)
    pending = list(vars.keys())
    while pending:
        var = pending.pop()
        if var not in res:
            continue
        for eq in res[var]:
            resolved[eq] += 1
            if resolved[eq] == 2:
                var, n = eq.calc(vars)
                vars[var] = n
                pending.append(var)

    return vars

def parse(input: str):
    vars = {}
    eqs = {}
    for line in input.splitlines():
        if m := re.match(r"(\w+): (\w+) ([-+*/]) (\w+)", line):
            var, a, op, b = m.groups()
            eq = Equation(var, a, b, ops[op])
            eqs[var] = eq
        else:
            var, i = line.split(": ")
            vars[var] = int(i)
    return vars, eqs

def solve(input: str):
    vars, eqs = parse(input)
    part1_vars = resolve(vars, eqs)
    part1 = part1_vars["root"]

    # part2: drop humn assignment
    del vars["humn"]
    # rewrite root to a == b, ie root = a - b AND root = 0
    root = eqs.pop("root")
    eqs["root"] = Equation("root", root.a, root.b, ops["-"])
    vars["root"] = 0
    part2_vars = resolve(vars, eqs)
    part2 = part2_vars["humn"]

    return Answer(part1, part2)
