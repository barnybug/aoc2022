from collections import deque
from .utils import Answer, Point
from functools import cached_property

START = ord("S") - ord("a")
END = ord("E") - ord("a")


def height(c):
    return 0 if c == "S" else 25 if c == "E" else ord(c) - ord("a")


class Grid:
    def __init__(self, grid):
        self.grid = grid

    def __getitem__(self, pos):
        return self.grid[pos.y][pos.x]

    def points(self):
        for y, row in enumerate(self.grid):
            for x, v in enumerate(row):
                yield Point(x, y), v

    @cached_property
    def xrange(self):
        return range(0, len(self.grid[0]))

    @cached_property
    def yrange(self):
        return range(0, len(self.grid))

    def apply(self, fn):
        return Grid(
            [[fn(v) for v in row] for row in self.grid]
        )

    @staticmethod
    def parse(lines):
        return Grid([list(line) for line in lines])


def parse(input: str):
    lines = input.split()
    raw = Grid.parse(lines)
    grid = raw.apply(height)
    start = next(p for p, c in raw.points() if c == "S")
    end = next(p for p, c in raw.points() if c == "E")
    return grid, start, end


def calc(grid: Grid, starts: list[Point], end: Point) -> int:
    visited = {start: 0 for start in starts}
    queue = deque(starts)
    while queue:
        pos = queue.popleft()
        steps = visited[pos]
        height = grid[pos]
        for move in (pos.left, pos.right, pos.up, pos.down):
            if (
                move.x in grid.xrange
                and move.y in grid.yrange
                and grid[move] <= height + 1
                and move not in visited
            ):
                if move == end:
                    return steps + 1
                visited[move] = steps + 1
                queue.append(move)


def solve(input: str):
    grid, start, end = parse(input)
    part1 = calc(grid, [start], end)
    starts = [pos for pos, h in grid.points() if h == 0]
    part2 = calc(grid, starts, end)
    return Answer(part1, part2)
