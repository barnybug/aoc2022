import itertools
import re
import numpy as np
from .utils import Answer

def solve(input: str):
    rows = []
    all_valves = []
    for line in input.splitlines():
        m = re.match(r"Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.+)", line)
        valve, rate, valves = m.groups()
        valves = valves.split(", ")
        all_valves.append(valve)
        rows.append((valve, int(rate), valves))

    lookup = {valve: i for i, valve in enumerate(all_valves)}
    size = len(all_valves)
    shape = (size, size)

    # make adjacency matrix of neighbours
    adj = np.zeros(shape)
    for valve, rate, valves in rows:
        for v in valves:
            adj[lookup[valve], lookup[v]] = 1
            adj[lookup[v], lookup[valve]] = 1

    # calculate distance matrix
    dist = np.where(adj, 1, np.inf)
    m = adj
    for i in range(2, size):
        m = np.matmul(m, adj)
        dist = np.minimum(dist, np.where(m, i, np.inf))

    with_valves = [lookup[valve] for valve, i, _ in rows if i > 0]
    dist = dist.astype(int)
    # print(dist[with_valves][:,with_valves])


    # iterate permutations with remaining cutoff
    best_score = 0
    def walk(start, remaining, time_left, score):
        nonlocal best_score
        shortest = min(dist[start, r] for r in remaining) + 1
        max_remaining = sum(
            (time_left - shortest - i*2) * rows[r][1]
            for i, r in enumerate(sorted(remaining, reverse=True))
        )
        if score + max_remaining < best_score:
            return
        for r in remaining:
            t = time_left - dist[start, r] - 1
            if t < 0:
                # finish
                continue
            s = score + t * rows[r][1]
            if s > best_score:
                best_score = s
            if t > 0 and len(remaining) > 1:
                walk(r, [i for i in remaining if i != r], t, s)

    aa = lookup["AA"]
    walk(aa, with_valves, 30, 0)
    part1 = best_score

    best_score = 0
    def walk2(start, remaining, time_left, score):
        nonlocal best_score
        s0 = min(dist[start[0], r] for r in remaining) + 1
        s1 = min(dist[start[1], r] for r in remaining) + 1
        tl = max(time_left[0] - s0, time_left[1] - s1)
        max_remaining = sum(
            (tl - i//2) * rows[r][1]
            for i, r in enumerate(sorted(remaining, reverse=True))
        )
        if score + max_remaining < best_score:
            return
        for r in remaining:
            # quickest to get there
            t1 = time_left[0] - dist[start[0], r] - 1
            t2 = time_left[1] - dist[start[1], r] - 1
            t = max(t1, t2)
            if t < 0:
                continue
            i = 0 if t1 > t2 else 1
            s = score + t * rows[r][1]
            if s > best_score:
                best_score = s
            start2 = (r, start[1]) if i == 0 else (start[0], r)
            tt = (t1, time_left[1]) if i == 0 else (time_left[0], t2)
            if (tt[0] > 0 or tt[1] > 0) and len(remaining) > 1:
                walk2(start2, [i for i in remaining if i != r], tt, s)

    walk2((aa, aa), with_valves, (26, 26), 0)
    part2 = best_score
    return Answer(part1, part2)
