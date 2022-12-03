from .utils import Answer

def priority(c):
    if 'a' <= c <= 'z':
        return ord(c) - 96
    return ord(c) - 38

def solve(input: str):
    lines = input.split()
    p1, p2 = 0, 0
    for line in lines:
        d = len(line) // 2
        left, right = line[:d], line[d:]
        right = line[d:]
        for common in set(left) & set(right):
            p1 += priority(common)

    for i in range(0, len(lines), 3):
        sets = map(set, lines[i:i+3])
        badge = set.intersection(*sets)
        p2 += priority(badge.pop())

    return Answer(p1, p2)
