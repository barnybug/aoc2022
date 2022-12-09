from aoc2022 import day09

testdata = open("tests/test09.txt").read()
testdata2 = open("tests/test09-2.txt").read()

def test_01():
    assert day09.solve(testdata)[0] == 13

def test_02():
    assert day09.solve(testdata)[1] == 1
    assert day09.solve(testdata2)[1] == 36
