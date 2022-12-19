from aoc2022 import day01

testdata = open("tests/input01.txt").read()

def test_01():
    assert day01.solve(testdata).part1 == 24000

def test_02():
    assert day01.solve(testdata).part2 == 45000
