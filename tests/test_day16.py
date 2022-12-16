from aoc2022 import day16

testdata = open("tests/test16.txt").read()

def test_01():
    assert day16.solve(testdata).part1 == 1651

def test_02():
    assert day16.solve(testdata).part2 == 1707
