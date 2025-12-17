from collections import defaultdict

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]


def parse_input():
    diagram = []
    start = None

    for i, line in enumerate(lines):
        curr = []

        for j, c in enumerate(line):
            if c == "S":
                start = (i, j)

            curr.append(c if c == "^" else ".")

        diagram.append(curr)

    return start, diagram


def puzzle1():
    start, diagram = parse_input()

    positions = {start}
    curr_i = 0
    splits = 0

    while curr_i < len(diagram) - 1:
        new_positions = set()

        for i, j in positions:
            if diagram[i + 1][j] == "^":
                splits += 1
                new_positions.add((i + 1, j-1))
                new_positions.add((i + 1, j + 1))
            else:
                new_positions.add((i + 1, j))

        positions = new_positions
        curr_i += 1

    return splits


def puzzle2():
    start, diagram = parse_input()
    cache = defaultdict(tuple)

    return shoot_beam(diagram, start[0], start[1], cache)


def shoot_beam(diagram, i, j, cache):
    if (i, j) in cache:
        return cache[(i, j)]

    if i >= len(diagram) - 1:
        cache[(i, j)] = 1
    elif diagram[i + 1][j] == "^":
        cache[(i, j)] = shoot_beam(diagram, i + 1, j - 1, cache) + shoot_beam(diagram, i + 1, j + 1, cache)
    else:
        cache[(i, j)] = shoot_beam(diagram, i + 1, j, cache)

    return cache[(i, j)]


def solve():
    print(f"Puzzle 1: {puzzle1()}")
    print(f"Puzzle 2: {puzzle2()}")


solve()
