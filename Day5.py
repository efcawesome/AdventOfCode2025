import heapq

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]


def parse_input():
    ranges = []
    ingredients = []
    in_range = True

    for line in lines:
        if line == "":
            in_range = False
            continue

        if in_range:
            l_split = line.split("-")
            ranges.append((int(l_split[0]), int(l_split[1])))
        else:
            ingredients.append(int(line))

    return ranges, ingredients


def puzzle1():
    ranges, ingredients = parse_input()

    res = 0
    for ingredient in ingredients:
        for lo, hi in ranges:
            if lo <= ingredient <= hi:
                res += 1
                break

    return res


def puzzle2():
    ranges, _ = parse_input()
    res = 0

    heapq.heapify(ranges)
    while ranges:
        lo, hi = heapq.heappop(ranges)
        while ranges and ranges[0][0] <= hi + 1:
            _, new_hi = heapq.heappop(ranges)
            if new_hi > hi:
                hi = new_hi

        res += hi - lo + 1

    return res


def solve():
    print(f"Puzzle 1: {puzzle1()}")
    print(f"Puzzle 2: {puzzle2()}")


solve()
