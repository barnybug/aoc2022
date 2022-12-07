from .utils import Answer

class Directory:
    dirs: dict[str, "Directory"]
    files: dict[str, int]

    def __init__(self):
        self.dirs = {}
        self.files = {}

    def walk(self):
        for dir in self.dirs.values():
            yield dir
            yield from dir.walk()

    @property
    def size(self):
        return sum(self.files.values())

    @property
    def total_size(self):
        return self.size + sum(dir.total_size for dir in self.dirs.values())

TOTAL_SPACE = 70000000
MIN_SPACE = 30000000

def solve(input: str):
    root = Directory()
    path = [root]
    for line in input.splitlines():
        name = line.split()[-1]
        if line.startswith("$ cd"):
            if name == "/":
                path = [root]
            elif name == "..":
                path.pop()
            else:
                path.append(path[-1].dirs[name])
        elif line.startswith("$ ls"):
            pass
        elif line.startswith("dir "):
            path[-1].dirs[name] = Directory()
        else:
            size, name = line.split()
            path[-1].files[name] = int(size)

    sizes = [dir.total_size for dir in root.walk()]
    part1 = sum(size for size in sizes if size <= 100000)

    unused = TOTAL_SPACE - root.total_size
    required = MIN_SPACE - unused
    sizes.sort()
    part2 = next(size for size in sizes if size >= required)
    return Answer(part1, part2)
