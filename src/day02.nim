import common

proc solve*(input: string): Answer =
  for line in lines input:
    let a = int(line[0]) - int('A')
    let b = int(line[2]) - int('X')
    let p1 = ((4 - a) mod 3 + b) mod 3 * 3 + b+1
    result.part1 += p1
    let p2 = b * 3 + ((a + 2) mod 3 + b) mod 3+1
    result.part2 += p2