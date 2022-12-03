from aoc2022 import day03

testdata = open("tests/test03.txt").read()

def test_01():
    assert day03.solve(testdata)[0] == 157

def test_02():
    assert day03.solve(testdata)[1] == 70
