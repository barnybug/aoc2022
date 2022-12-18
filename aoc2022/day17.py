from .utils import Answer

ROCKS = [
    4+8+16+32,
    8+(4+8+16<<8)+(8<<16),
    4+8+16+(16<<8)+(16<<16),
    4+(4<<8)+(4<<16)+(4<<24),
    4+8+(4+8<<8),
] # LSB left - MSB right, bottom to top

def print_chamber(chamber):
    print()
    for c in reversed(chamber):
        line = "{0:7b}".format(c).replace("1", "#").replace("0", " ")
        line = "".join(reversed(line))
        print(f"|{line}|")

def enumerate_rock(rock):
    yield 0, rock & 255
    rock = rock >> 8
    if rock:
        yield 1, rock & 255
        rock = rock >> 8
        if rock:
            yield 2, rock & 255
            rock = rock >> 8
            if rock:
                yield 3, rock & 255

def collision(rock, chamber, height):
    for i, r in enumerate_rock(rock):
        h = height + i
        if h >= len(chamber):
            break # bottom is above chamber
        if chamber[h] & r: # collision
            return True
    return False

def run(input: str, steps: int):
    chamber = [127]
    t = 0
    step = 0
    states = {}
    height_adder = 0
    while step < steps:
        y = len(chamber)+3 # bottom
        rock = ROCKS[step % len(ROCKS)]
        step += 1
        while True:
            gust = input[t]
            if gust == "<" and (rock & 0x01010101 == 0):
                left = rock >> 1
                if not collision(left, chamber, y):
                    rock = left
            elif gust == ">" and (rock & 0x40404040) == 0:
                right = rock << 1
                if not collision(right, chamber, y):
                    rock = right
            t += 1
            if t >= len(input):
                t = 0

            # fall
            if collision(rock, chamber, y - 1):
                # stop where it is
                for i, r in enumerate_rock(rock):
                    h = y + i
                    if h >= len(chamber): # add to top
                        chamber.append(r)
                    else: # merge in
                        chamber[y + i] |= r

                if len(chamber) > 11:
                    top = 0
                    for i in range(11): # must be >= 11 - a horizontal block?
                        top = (top << 8) + chamber[-i]
                    state = (rock, t, top)
                    if state in states:
                        previous_height, previous_step = states[state]
                        remain = steps - step
                        cycle = step - previous_step
                        repeats = remain // cycle
                        step += repeats * cycle
                        height_adder = repeats * (y - previous_height)
                        states = {} # clear for remainder run
                    else:
                        states[state] = (y, step)
                break

            y -= 1
    return len(chamber) - 1 + height_adder

def solve(input: str):
    part1 = run(input, 2022)
    part2 = run(input, 1000000000000)
    return Answer(part1, part2)
