import common
import sets
import sequtils

proc priority(c: char): int =
  if 'a' <= c and c <= 'z':
    return ord(c)-96
  else:
    return ord(c)-38

proc solve*(input: string): Answer =
  let lines = toSeq(lines input)
  for line in lines:
    let d = line.len div 2
    let (left, right) = (line[0 .. d-1], line[d .. line.high])
    let common = left.toHashSet * right.toHashSet
    for c in common:
      result.part1 += c.priority

  for i in countup(0, lines.high, 3):
    let a = lines[i].toHashSet
    let b = lines[i+1].toHashSet
    let c = lines[i+2].toHashSet
    var badge = a * b * c
    result.part2 += badge.pop.priority
