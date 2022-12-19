from aoc2022 import day06

testdata = open("tests/input06.txt").read()

def test_01():
    assert day06.find("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 4) == 7
    assert day06.find("bvwbjplbgvbhsrlpgdmjqwftvncz", 4) == 5
    assert day06.find("nppdvjthqldpwncqszvftbrmjlhg", 4) == 6
    assert day06.find("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4) == 10
    assert day06.find("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4) == 11

def test_02():
    assert day06.find("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14) == 19
    assert day06.find("bvwbjplbgvbhsrlpgdmjqwftvncz", 14) == 23
    assert day06.find("nppdvjthqldpwncqszvftbrmjlhg", 14) == 23
    assert day06.find("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14) == 29
    assert day06.find("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14) == 26
