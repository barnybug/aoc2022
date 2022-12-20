from aoc2022 import day19

testdata = open("tests/input19.txt").read()


def test_01():
    assert day19.solve(testdata).part1 == 33


def test_02():
    blueprints = list(day19.parse(testdata))
    assert day19.evaluate(blueprints[0], 32) == 56
    assert day19.evaluate(blueprints[1], 32) == 62
