import re
from math import prod

from .utils import Answer
from collections import deque
from dataclasses import dataclass
from typing import NamedTuple, Optional

NAMES = ["ore", "clay", "obsidian", "geode"]


def words(resources):
    return " and ".join(f"{r} {NAMES[i]}" for i, r in enumerate(resources) if r)


def evaluate(blueprint, minutes):
    robots = Four(1, 0, 0, 0)
    resources = Four(0, 0, 0, 0)
    geodes = build(blueprint, robots, resources, minutes)
    return geodes


class Four(NamedTuple):
    ore: int
    clay: int
    obsidian: int
    geode: int

    def __add__(self, b):
        return Four(
            self.ore + b.ore,
            self.clay + b.clay,
            self.obsidian + b.obsidian,
            self.geode + b.geode,
        )

    def __sub__(self, b):
        return Four(
            self.ore - b.ore,
            self.clay - b.clay,
            self.obsidian - b.obsidian,
            self.geode - b.geode,
        )


@dataclass
class Blueprint:
    number: int
    costs: list[Four]


ROBOTS = [Four(1, 0, 0, 0), Four(0, 1, 0, 0), Four(0, 0, 1, 0), Four(0, 0, 0, 1)]


class State(NamedTuple):
    robots: Four
    resources: Four
    minute: int
    last: Optional[int]

    def wait(self):
        return State(self.robots, self.resources + self.robots, self.minute - 1, None)

    def build(self, n, cost):
        return State(
            self.robots + ROBOTS[n],
            self.resources + self.robots - cost,
            self.minute - 1,
            n,
        )


def build(blueprint, robots, resources, minutes):
    # You don't need more robots than the maximum resource you can use in a turn.
    robot_limits = Four(*[max(cost[i] for cost in blueprint.costs) for i in range(4)])
    state = State(robots, resources, minutes, None)
    states = deque([state])
    best = 0
    while states:
        robots, resources, time, last = state = states.pop()

        if time == 0:
            best = max(best, resources.geode)
            continue

        # Theoretical upper limit for geodes produced in remaining time
        upper_limit = resources.geode + (time * (2 * robots.geode + time - 1)) // 2
        if upper_limit <= best:
            continue

        time -= 1
        wait = False

        for i, (cost, robot, resource, limit) in enumerate(
            zip(blueprint.costs, robots, resources, robot_limits)
        ):
            # Check if there are sufficient robots of this type for the remainder
            if i != 3 and robot * time + resource > limit * time:
                continue

            # Don't create one if could have created one last time
            if (last is None or last == i) and all(
                rs - ro >= c for rs, ro, c in zip(resources, robots, cost)
            ):
                continue

            # If not enough resources presently, but would waiting for other robots help
            if any(r < c for r, c in zip(resources, cost)):
                wait = wait or all(r > 0 for c, r in zip(cost, robots) if c > 0)
                continue

            # Otherwise build one
            states.append(state.build(i, cost))

        if wait:
            # Wait for more resources
            states.append(state.wait())

    return best


def parse(input: str):
    for line in input.splitlines():
        m = re.match(r"Blueprint (\d+):", line)
        if m is None:
            continue
        number = int(m.group(1))
        costs = []
        for m in re.finditer(r"Each (\w+) robot costs ([^\.]+).", line):
            cost = [0] * 4
            for n, resource in re.findall(r"(\d+) (\w+)", m.group(2)):
                cost[NAMES.index(resource)] = int(n)
            costs.append(Four(*cost))

        yield Blueprint(number, costs)


def solve(input: str):
    blueprints = list(parse(input))

    part1 = sum(blueprint.number * evaluate(blueprint, 24) for blueprint in blueprints)
    part2 = prod(evaluate(blueprint, 32) for blueprint in blueprints[:3])
    return Answer(part1, part2)
