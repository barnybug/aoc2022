from aoc2022 import day07

testdata = open("tests/test07.txt").read()

def test_01():
    assert day07.solve(testdata)[0] == 95437

def test_02():
    assert day07.solve(testdata)[1] == 24933642
