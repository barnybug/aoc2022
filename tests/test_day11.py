from aoc2022 import day11

testdata = open("tests/test11.txt").read()

def test_01():
    assert day11.solve(testdata)[0] == 10605

def test_02():
    assert day11.solve(testdata)[1] == 2713310158
