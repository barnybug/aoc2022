from aoc2022 import day02

testdata = open("tests/input02.txt").read()

def test_01():
    assert day02.solve(testdata).part1 == 15

def test_02():
    assert day02.solve(testdata).part2 == 12
