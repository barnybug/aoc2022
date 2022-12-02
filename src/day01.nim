import common
import math, strutils, std/algorithm

proc solve*(input: string): Answer =
    let txt = readFile input
    var totals: seq[int]
    for n in txt.split("\n\n"):
        totals.add sum(parseIntList(n))
    totals.sort()

    result.part1 = totals[totals.high]
    result.part2 = sum(totals[^3 .. totals.high])
