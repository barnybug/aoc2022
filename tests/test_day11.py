from aoc2022 import day11

testdata = open("tests/input11.txt").read()

def test_both_parts():
    answer = day11.solve(testdata)
    assert answer.part1 == 10605
    assert answer.part2 == 2713310158
