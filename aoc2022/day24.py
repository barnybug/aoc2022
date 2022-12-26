import itertools
from dataclasses import dataclass
from .utils import Answer, Point
from collections import deque

DIRS = {
    '>': Point.R,
    '<': Point.L,
    '^': Point.U,
    'v': Point.D,
}

@dataclass
class Board:
    blizzards: list
    width: int
    height: int
    start: Point
    end: Point

def parse(input: str):
    lines = input.splitlines()
    blizzards = [
        (Point(x, y), DIRS[c])
        for y, line in enumerate(lines[1:-1])
        for x, c in enumerate(line[1:-1])
        if c != "."
    ]
    width = len(lines[0])-2
    height = len(lines)-2
    start = Point(lines[0].index(".")-1, -1)
    end = Point(lines[-1].index(".")-1, len(lines)-2)
    return Board(blizzards, width, height, start, end)

def run(board, tstart: int, start: Point, end: Point):
    def mod(p):
        return Point(p.x % board.width, p.y % board.height)
    possible = {start}
    for t in itertools.count(tstart):
        additions = {
            move
            for p in possible
            for move in (p.down, p.up, p.left, p.right)
            if (0 <= move.x < board.width and 0 <= move.y < board.height) or move == start or move == end
        }
        blocked = {
            mod(bp + (d * t))
            for bp, d in board.blizzards
        }
        possible = (possible | additions) - blocked
        if end in possible:
            return t

def solve(input: str):
    board = parse(input)
    part1 = run(board, 0, board.start, board.end)
    snacks = run(board, part1, board.end, board.start)
    part2 = run(board, snacks, board.start, board.end)
    return Answer(part1, part2)
