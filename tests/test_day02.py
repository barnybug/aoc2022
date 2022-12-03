from aoc2022 import day02

testdata = open("tests/test02.txt").read()

def test_01():
    assert day02.solve(testdata)[0] == 15

def test_02():
    assert day02.solve(testdata)[1] == 12
