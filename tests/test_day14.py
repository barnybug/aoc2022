from aoc2022 import day14

testdata = open("tests/test14.txt").read()

def test_01():
    assert day14.solve(testdata).part1 == 24

def test_02():
    assert day14.solve(testdata).part2 == 93
