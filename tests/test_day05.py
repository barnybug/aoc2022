from aoc2022 import day05

testdata = open("tests/test05.txt").read()

def test_01():
    assert day05.solve(testdata)[0] == "CMZ"

def test_02():
    assert day05.solve(testdata)[1] == "MCD"
