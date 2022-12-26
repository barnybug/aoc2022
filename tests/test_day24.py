from aoc2022 import day24

testdata = open("tests/input24.txt").read()

def test_01():
    assert day24.solve(testdata).part1 == 18

def test_02():
    assert day24.solve(testdata).part2 == 54
