from .utils import Answer

values = ["=", "-", "0", "1", "2"]

def snafu2int(s: str):
    return sum(
        (values.index(c) - 2) * (5 ** i)
        for i, c in enumerate(reversed(s))
    )

def int2snafu(i: int) -> str:
    ret = ''
    while i:
        m = i % 5
        i //= 5
        if m > 2: # carry
            m -= 5
            i += 1
        ret = values[m+2] + ret
    return ret

def solve(input: str):
    total = sum(map(snafu2int, input.split()))
    part1 = int2snafu(total)
    return Answer(part1, 0)
