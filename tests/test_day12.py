from aoc2022 import day12

testdata = open("tests/test12.txt").read()


def test_01():
    assert day12.solve(testdata)[0] == 31


def test_02():
    assert day12.solve(testdata)[1] == 29