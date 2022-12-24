from aoc2022 import day23

testdata = open("tests/input23.txt").read()

def test_01():
    assert day23.solve(testdata).part1 == 110

def test_02():
    assert day23.solve(testdata).part2 == 20
