from .utils import Answer, Point

def trace(a, b):
    if a.y == b.y:
        return (Point(x, a.y) for x in range(min(a.x, b.x), max(a.x, b.x)+1))
    elif a.x == b.x:
        return (Point(a.x, y) for y in range(min(a.y, b.y), max(a.y, b.y)+1))

def parse(input: str):
    grid = {}
    for line in input.splitlines():
        coords = [
            Point(*map(int, coord.split(",")))
            for coord in line.split(" -> ")
        ]
        for start, end in zip(coords, coords[1:]):
            for p in trace(start, end):
                grid[p] = "#"
    return grid
    
def pour(grid, floor):
    bottom = max(y for _, y in grid)
    def flow(start):
        if not floor and start.y >= bottom:
            return False # fall
        for p in (start + Point(0, 1), start + Point(-1, 1), start + Point(1, 1)):
            if p not in grid and p.y != bottom + 2 and not flow(p):
                break # clear below but did not deposit
        else:
            grid[start] = "o" # deposit
            return True
        return False

    flow(Point(500, 0))
    return sum(v == "o" for v in grid.values())

def solve(input: str):
    grid = parse(input)
    part1 = pour(grid, False)
    part2 = pour(grid, True)
    return Answer(part1, part2)
