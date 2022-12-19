from aoc2022 import day05

testdata = open("tests/input05.txt").read()

def test_01():
    assert day05.solve(testdata).part1 == "CMZ"

def test_02():
    assert day05.solve(testdata).part2 == "MCD"
