from .utils import Answer

def solve(input: str):
    trees = [[int(c) for c in line] for line in input.split("\n")]
    visible = {}
    ys = range(len(trees))
    xs = range(len(trees[0]))
    def scan(outer):
        for xy in outer:
            height = -1
            for (x, y) in xy:
                if trees[y][x] > height:
                    height = trees[y][x]
                    visible[(x,y)] = 1
                if height == 9:
                    break

    scan(((x, y) for x in xs) for y in ys)
    scan(((x, y) for x in reversed(xs)) for y in ys)
    scan(((x, y) for y in ys) for x in xs)
    scan(((x, y) for y in reversed(ys)) for x in xs)
    part1 = len(visible)

    def unblocked(height, xy):
        for i, (x, y) in enumerate(xy):
            if trees[y][x] >= height:
                return i+1
        return i+1

    def scenic(cx, cy):
        height = trees[cy][cx]
        up = unblocked(height, ((cx, y) for y in range(cy-1, -1,  -1)))
        left = unblocked(height, ((x, cy) for x in range(cx-1, -1, -1)))
        down = unblocked(height, ((cx, y) for y in range(cy+1, len(trees))))
        right = unblocked(height, ((x, cy) for x in range(cx+1, len(trees[0]))))
        return up * left * down * right

    part2 = max(
        scenic(x, y)
        for x in range(1, len(trees[0])-1)
        for y in range(1, len(trees)-1)
    )
    return Answer(part1, part2)
