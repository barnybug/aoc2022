from aoc2022 import day20

testdata = open("tests/input20.txt").read()

def test_01():
    assert day20.solve(testdata).part1 == 3

def test_02():
    assert day20.solve(testdata).part2 == 1623178306
