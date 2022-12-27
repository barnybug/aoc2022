import pytest

from aoc2022 import day25

testdata = open("tests/input25.txt").read()

@pytest.mark.parametrize(("i", "s"), [
    (1, "1"),
    (2, "2"),
    (3, "1="),
    (4, "1-"),
    (5, "10"),
    (6, "11"),
    (7, "12"),
    (8, "2="),
    (9, "2-"),
    (10, "20"),
    (15, "1=0"),
    (20, "1-0"),
    (2022, "1=11-2"),
    (12345, "1-0---0"),
    (314159265, "1121-1110-1=0"),
])
def test_int2snafu(i, s):
    assert day25.int2snafu(i) == s


def test_01():
    assert day25.solve(testdata).part1 == "2=-1=0"

def test_02():
    assert day25.solve(testdata).part2 == None
