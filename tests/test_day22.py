from aoc2022 import day22

testdata = open("tests/input22.txt").read()

def test_01():
    assert day22.solve(testdata).part1 == 6032

def test_02():
    assert day22.solve(testdata).part2 == 5031
