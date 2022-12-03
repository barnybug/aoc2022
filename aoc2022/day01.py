from .utils import Answer

def solve(input: str):
    totals = sorted(
        sum(map(int, block.split()))
        for block in input.split("\n\n")
    )
    return Answer(totals[-1], sum(totals[-3:]))
