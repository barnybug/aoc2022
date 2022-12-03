from aoc2022 import day01

testdata = open("tests/test01.txt").read()

def test_01():
    assert day01.solve(testdata)[0] == 24000

def test_02():
    assert day01.solve(testdata)[1] == 45000
