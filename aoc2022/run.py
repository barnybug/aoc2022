import argparse
import importlib
from pathlib import Path

from .utils import input_data

def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("day", nargs="*", type=int)
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
        
    for day in days:
        name = f"aoc2022.day{day:02d}"
        mod = importlib.import_module(name)
        input = input_data(day)
        print(f"Day {day}:")
        print(mod.solve(input))
