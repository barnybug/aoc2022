from aoc2022 import day17

testdata = open("tests/input17.txt").read()

def test_01():
    assert day17.solve(testdata).part1 == 3068

def test_02():
    assert day17.solve(testdata).part2 == 1514285714288
