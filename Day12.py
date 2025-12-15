with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]


def parse_input():
    counts = []
    sizes = []
    amounts = []

    for i in range(0, 30, 5):
        original = []
        for line in lines[i + 1: i + 4]:
            original.append([1 if c == "#" else 0 for c in line])

        counts.append(sum([sum(x) for x in original]))

    for line in lines[30:]:
        l_split = line.split(": ")
        size = tuple([int(x) for x in l_split[0].split("x")])
        amount = [int(x) for x in l_split[1].split(" ")]
        sizes.append(size)
        amounts.append(amount)

    return counts, sizes, amounts


def puzzle1():
    counts, sizes, amounts_l = parse_input()
    res = 0
    for size, amounts in zip(sizes, amounts_l):
        x, y = size
        total = 0
        for i, n in enumerate(amounts):
            total += n * counts[i]

        if total > x * y:
            continue
        else:
            res += 1

    return res


def puzzle2():
    pass


def solve():
    print(f"Puzzle 1: {puzzle1()}")
    print(f"Puzzle 2: {puzzle2()}")


solve()