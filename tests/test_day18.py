from aoc2022 import day18

testdata = open("tests/input18.txt").read()

def test_01():
    assert day18.solve(testdata).part1 == 64

def test_02():
    assert day18.solve(testdata).part2 == 58
