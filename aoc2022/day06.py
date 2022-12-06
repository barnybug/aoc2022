from .utils import Answer

def find(s: str, n: int) -> int:
    for i in range(len(s)):
        if len(set(s[i:i+n])) == n:
            return i+n

def solve(input: str):
    return Answer(find(input, 4), find(input, 14))
