from .utils import Answer

class Number:
    def __init__(self, s):
        self.value = int(s)

    def __repr__(self):
        return str(self.value)

def mix(numbers: list[Number], times: int):
    size = len(numbers)
    mixed = numbers[:]
    for _ in range(times):
        for number in numbers:
            current = mixed.index(number)
            new = current + number.value
            if new >= size or new < 0:
                new = new % (size - 1)
            mixed.insert(new, mixed.pop(current))

    zero_index = next(i for i, n in enumerate(mixed) if n.value == 0)
    return sum(
        mixed[(zero_index + i) % size].value
        for i in (1000, 2000, 3000)
    )

KEY = 811589153

def solve(input: str):
    numbers = list(map(Number, input.split()))
    part1 = mix(numbers, 1)
    part2 = mix([Number(n.value * KEY) for n in numbers], 10)
    return Answer(part1, part2)
