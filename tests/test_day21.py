from aoc2022 import day21

testdata = open("tests/input21.txt").read()

def test_01():
    assert day21.solve(testdata).part1 == 152

def test_02():
    assert day21.solve(testdata).part2 == 301
