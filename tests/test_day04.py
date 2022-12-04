from aoc2022 import day04

testdata = open("tests/test04.txt").read()

def test_01():
    assert day04.solve(testdata)[0] == 2

def test_02():
    assert day04.solve(testdata)[1] == 4
