with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]


def puzzle1():
    curr = 50
    count = 0

    for s in lines:
        direction, amount = -1 if s[0] == "L" else 1, int(s[1:])

        curr = (curr + direction * amount) % 100
        if curr == 0:
            count += 1

    return count


def puzzle2():
    curr = 50
    count = 0

    for s in lines:
        direction, amount = -1 if s[0] == "L" else 1, int(s[1:])

        if direction == -1 and curr - amount <= 0:
            count += (amount - curr) // 100 + int(curr != 0)
        elif direction == 1:
            count += (amount + curr) // 100

        curr = (curr + direction * amount) % 100

    return count


def solve():
    print(f"Puzzle 1: {puzzle1()}")
    print(f"Puzzle 2: {puzzle2()}")


solve()
