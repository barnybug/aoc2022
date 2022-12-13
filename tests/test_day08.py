from aoc2022 import day08

testdata = open("tests/test08.txt").read()

def test_01():
    assert day08.solve(testdata).part1 == 21

def test_02():
    assert day08.solve(testdata).part2 == 8
