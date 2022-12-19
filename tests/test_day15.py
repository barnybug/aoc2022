from aoc2022 import day15

testdata = open("tests/input15.txt").read()

def test_01():
    readings = day15.parse(testdata)
    assert day15.part1(readings, 10) == 26
    assert day15.part1(readings, 9) == 25
    assert day15.part1(readings, 11) == 29

def test_02():
    readings = day15.parse(testdata)
    assert day15.part2(readings, 20) == 56000011
