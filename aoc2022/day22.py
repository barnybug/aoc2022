from dataclasses import dataclass
import re
from .utils import Answer, Point

DIRS = [Point.R, Point.D, Point.L, Point.U]
DIRNAMES = ["R", "D", "L", "U"]

@dataclass
class Line:
    a: Point
    b: Point

    def __contains__(self, p):
        # lines are only ever horizontal or vertical, so simple bounding box check works
        if min(self.a.x, self.b.x) <= p.x <= max(self.a.x, self.b.x) and min(self.a.y, self.b.y) <= p.y <= max(self.a.y, self.b.y):
            return True
        return False

    @property
    def dir(self):
        return (self.b - self.a).unit

    def __repr__(self):
        return "%s-%s" % (self.a, self.b)

def get_perimeter(p, tiles, size):
    perimeter = [p]
    while len(perimeter) < 14:
        for dir in DIRS:
            np = p + dir * size
            if any(np+d in tiles for d in [Point(0, 0), Point(-1, 0), Point(0, -1), Point(-1, -1)]) and np not in perimeter:
                p = np
                perimeter.append(p)
                break
    return perimeter

def rotate(li, i):
    return li[i:] + li[:i]

def det(a, b):
    return a.x * b.y - a.y * b.x

class circular:
    def __init__(self, li):
        self.li = li

    def __iter__(self):
        return iter(self.li)

    def __getitem__(self, i):
        return self.li[i % len(self.li)]

def solve(input: str):
    board, ins = input.split("\n\n")
    board = board.splitlines()
    instructions = [
        i if i in "LR" else int(i)
        for i in re.findall(r"([0-9]+|R|L)", ins)
    ]
    tiles = {
        (x, y): c
        for y, row in enumerate(board)
        for x, c in enumerate(row)
        if c != " "
    }
    xlimits = [
        (min(i for i, c in enumerate(row) if c != " "), max(i for i, c in enumerate(row) if c != " "))
        for row in board
    ]
    xmin = min(a for a, _ in xlimits)
    xmax = max(b for _, b in xlimits)
    ylimits = [
        (min(y for y, row in enumerate(board) if x < len(row) and row[x] != " "), max(y for y, row in enumerate(board) if x < len(row) and row[x] != " "))
        for x in range(xmin, xmax+1)
    ]
    size = 50 if len(board) > 12 else 4

    def wrap_around(p, d):
        if d == 0:
            return Point(xlimits[p.y][0], p.y), d
        elif d == 2:
            return Point(xlimits[p.y][1], p.y), d
        elif d == 1:
            return Point(p.x, ylimits[p.x][0]), d
        elif d == 3:
            return Point(p.x, ylimits[p.x][1]), d
    start = Point(board[0].index("."), 0)

    perimeter = get_perimeter(start, tiles, size)
    assert len(perimeter) == 14

    perimeter = circular(perimeter) # wraps list around both ways for simpler indexing
    pairs = []
    # find inner inflection points (where cube folds inwards)
    for i, a in enumerate(perimeter):
        b = perimeter[i-1]
        c = perimeter[i+1]
        # cross product of the two vectors is positive (ie clockwise)
        if det(b - a, c - a) > 0: 
            # print(f"inflection point: {a} #{i}")
            pairs.append((Line(a, b), Line(a, c)))
            pairs.append((Line(c, a), Line(b, a)))
            # find further pairings of sides
            # the next two sides going outwards along the perimeter can be paired if one of them is in a straight line
            # to the previous
            j = 1
            while True:
                j += 1
                # two edges are straight if cross product == 0
                # if neither two neighbouring edges are straight, finish pairing
                if (det(perimeter[i-j] - perimeter[i-j+1], perimeter[i-j+1] - perimeter[i-j+2]) != 0 and
                    det(perimeter[i+j] - perimeter[i+j-1], perimeter[i+j-1] - perimeter[i+j-2]) != 0):
                    break
                pairs.append((Line(perimeter[i-j+1], perimeter[i-j]), Line(perimeter[i+j-1], perimeter[i+j])))
                # opposite line direction must be reversed to preserve normal direction pointing into shape
                pairs.append((Line(perimeter[i+j], perimeter[i+j-1]), Line(perimeter[i-j], perimeter[i-j+1])))

    assert len(pairs) == 14

    # 'snap' pairs to the leaving edge
    def adjust(i):
        if i.dir.x == 1:
            return Line(i.a, i.b-i.dir)
        elif i.dir.y == 1:
            return Line(i.a+i.dir.turncw, i.b-i.dir+i.dir.turncw)
        elif i.dir.x == -1:
            return Line(i.a+i.dir+i.dir.turncw, i.b+i.dir.turncw)
        elif i.dir.y == -1:
            return Line(i.a+i.dir, i.b)
    pairs = [
        (adjust(i), adjust(j))
        for i, j in pairs
    ]    
    def wrap_cube(p, d):
        # find pair
        frm, to = next(
            (a, b)
            for a, b in pairs
            if p in a and det(DIRS[d], a.dir) != 0
            # awkward inner corner case - step must be perpendicular to the line
            # (argh, lost an hour to this bug!)
        )
        n = abs(p.x - frm.a.x) + abs(p.y - frm.a.y)
        unit = (to.b - to.a).unit
        np = unit * n + to.a
        nd = DIRS.index(unit.turncw) # perpendicular to entry line
        # print(f"wrapped {p} going {DIRNAMES[d]} to {np} going {DIRNAMES[nd]} {tiles.get(np)} ({frm}--{to})")
        return np, nd

    def run(wrap):
        p = Point(board[0].index("."), 0)
        d = 0
        for instruction in instructions:
            if instruction == "L":
                d = (d - 1) % 4
            elif instruction == "R":
                d = (d + 1) % 4
            else:
                for _ in range(instruction):
                    np = p + DIRS[d]
                    nd = d
                    if np not in tiles: # wrap
                        np, nd = wrap(np, d)
                    if tiles[np] == "#":
                        break
                    p = np
                    d = nd

        return (p.x+1)*4 + (p.y+1)*1000 + d
    
    part1 = run(wrap_around)
    part2 = run(wrap_cube)
    return Answer(part1, part2)
