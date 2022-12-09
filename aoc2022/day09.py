from .utils import Answer, Point, DIRS

def sign(x):
    return -1 if x < 0 else 1 if x > 0 else 0

def simulate(input: str, length: int):
    rope = [Point(0, 0)] * length
    visited = set(rope)
    for line in input.splitlines():
        dir, n = line.split()
        for _ in range(int(n)):
            rope[0] += DIRS[dir]
            for i in range(1, length):
                d = rope[i-1] - rope[i]
                if abs(d.x) > 1 or abs(d.y) > 1:
                    rope[i] += Point(sign(d.x), sign(d.y))
            visited.add(rope[-1])
    return len(visited)

def solve(input: str):
    part1 = simulate(input, 2)
    part2 = simulate(input, 10)
    return Answer(part1, part2)
