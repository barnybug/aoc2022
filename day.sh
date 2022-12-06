#!/bin/bash

day=$(date +%02d)
testinput="tests/test$day.txt"
input="aoc2022/inputs/input$day.txt" 
daycode="aoc2022/day$day.py"
testcode="tests/test_day$day.py"

touch $testinput $input
if [ ! -f "$testcode" ]; then
    cat <<EOF > $testcode
from aoc2022 import day$day

testdata = open("tests/test$day.txt").read()

def test_01():
    assert day$day.solve(testdata)[0] == None

def test_02():
    assert day$day.solve(testdata)[1] == None
EOF
fi
if [ ! -f "$daycode" ]; then
    cat <<EOF > $daycode
from .utils import Answer

def solve(input: str):
    return Answer(0, 0)
EOF
fi

code $input $testinput $testcode $daycode