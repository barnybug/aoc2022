import argparse
import importlib
from pathlib import Path

from .utils import input_data

class MarkdownOutput:
    def header(self):
        print("# Solutions")
        print()

    def day(self, day, answer):
        print(f"## Day {day}")
        print()
        print(f"- Part 1: {answer.part1}")
        print(f"- Part 2: {answer.part2}")
        print()

class TextOutput:
    def header(self):
        print("Solutions")

    def day(self, day, answer):
        print(f"Day {day}:")
        print(answer)
        print()

# run: echo '### Hello world! :rocket:' >> $GITHUB_STEP_SUMMARY

def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("day", nargs="*", type=int)
    parser.add_argument("--markdown", action="store_true", help="Format output in markdown")
    args = parser.parse_args()

    if args.day:
        days = args.day
    else:
        paths = Path(__file__).parent.glob("day*.py")
        days = [
            int(path.stem[3:])
            for path in paths
        ]
        days.sort()

    output = MarkdownOutput() if args.markdown else TextOutput()
    output.header()

    for day in days:
        name = f"aoc2022.day{day:02d}"
        mod = importlib.import_module(name)
        input = input_data(day)
        answer = mod.solve(input)
        output.day(day, answer)
