import algorithm, common, os, sequtils, strformat, strutils, tables, times
import day01, day02 #, day03, day04, day05, day06, day06, day06, day07, day08, day09, day10, day11, day12, day13, day14, day15, day16, day17, day18, day19, day20, day21, day22, day23, day23, day24, day25, day25

var SOLUTIONS*: Table[int, proc (input: string): Answer]

SOLUTIONS[1] = day01.solve
SOLUTIONS[2] = day02.solve
# SOLUTIONS[3] = day03.solve
# SOLUTIONS[4] = day04.solve
# SOLUTIONS[5] = day05.solve
# SOLUTIONS[6] = day06.solve
# SOLUTIONS[7] = day07.solve
# SOLUTIONS[8] = day08.solve
# SOLUTIONS[9] = day09.solve
# SOLUTIONS[10] = day10.solve
# SOLUTIONS[11] = day11.solve
# SOLUTIONS[12] = day12.solve
# SOLUTIONS[13] = day13.solve
# SOLUTIONS[14] = day14.solve
# SOLUTIONS[15] = day15.solve
# SOLUTIONS[16] = day16.solve
# SOLUTIONS[17] = day17.solve
# SOLUTIONS[18] = day18.solve
# SOLUTIONS[19] = day19.solve
# SOLUTIONS[20] = day20.solve
# SOLUTIONS[21] = day21.solve
# SOLUTIONS[22] = day22.solve
# SOLUTIONS[23] = day23.solve
# SOLUTIONS[24] = day24.solve
# SOLUTIONS[25] = day25.solve
# SOLUTIONS[25] = day25.solve
# SOLUTIONS[23] = day23.solve
# SOLUTIONS[24] = day24.solve
# SOLUTIONS[25] = day25.solve
# SOLUTIONS[25] = day25.solve

when isMainModule:
  let params = os.commandLineParams()

  let days = if len(params) == 0:
    toSeq(SOLUTIONS.keys).sorted
  else:
    params.map(parseInt).toSeq
  
  var total: float
  for day in days:
    echo fmt"Day {day}:"
    let input = fmt"input{day:02}.txt"
    let start = cpuTime()
    let result = SOLUTIONS[day](input)
    let finish = cpuTime()
    echo result
    let took = (finish-start)*1000
    total += took
    echo fmt" Time: {took:.2f} ms"

  echo "-----------------------------------------------------"
  echo fmt"Total time: {total:.2f} ms"
