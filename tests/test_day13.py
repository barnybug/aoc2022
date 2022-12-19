from aoc2022 import day13

testdata = open("tests/input13.txt").read()

def test_01():
    assert day13.solve(testdata).part1 == 13

def test_02():
    assert day13.solve(testdata).part2 == 140
