from aoc2022 import day13

testdata = open("tests/test13.txt").read()

def test_01():
    assert day13.solve(testdata)[0] == 13

def test_02():
    assert day13.solve(testdata)[1] == 140
