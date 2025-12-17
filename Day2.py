with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]


def parse_input():
    lines_split = lines[0].split(",")
    ranges = []
    for line in lines_split:
        r = line.split("-")
        ranges.append((int(r[0]), int(r[1])))

    return ranges


def is_invalid(id):
    s = str(id)

    if len(s) % 2 != 0:
        return False

    return s[0:len(s) // 2] == s[len(s) // 2:]


def is_extra_invalid(id):
    s = str(id)

    for i in range(1, len(s)):
        if len(s) % i != 0:
            continue

        pattern = s[0:i]
        has_pattern = True

        for j in range(0, len(s), i):
            if s[j:j+i] != pattern:
                has_pattern = False
                break

        if has_pattern:
            return True

    return False


def puzzle1():
    ranges = parse_input()
    res = 0

    for r in ranges:
        for n in range(r[0], r[1] + 1):
            if is_invalid(n):
                res += n

    return res


def puzzle2():
    ranges = parse_input()
    res = 0

    for r in ranges:
        for n in range(r[0], r[1] + 1):
            if is_extra_invalid(n):

                res += n

    return res


def solve():
    print(f"Puzzle 1: {puzzle1()}")
    print(f"Puzzle 2: {puzzle2()}")


solve()
