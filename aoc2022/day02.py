from .utils import Answer

def solve(input: str):
    p1, p2 = 0, 0
    for line in input.split("\n"):
        a = ord(line[0]) - ord('A')
        b = ord(line[2]) - ord('X')
        p1 += ((4 - a) % 3 + b) % 3 * 3 + b+1
        p2 += b * 3 + ((a + 2) % 3 + b) % 3+1

    return Answer(p1, p2)
