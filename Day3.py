with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]


def parse_input():
    banks = [[int(c) for c in line] for line in lines]
    return banks


def puzzle1():
    banks = parse_input()
    res = 0

    for bank in banks:
        best_first = 0
        best = 0

        for i, battery in enumerate(bank):
            if battery < best_first:
                continue

            best_first = battery

            for second in bank[i+1:]:
                if battery * 10 + second > best:
                    best = battery * 10 + second

        res += best

    return res


def puzzle2():
    banks = parse_input()
    res = 0

    for bank in banks:
        res += find_best_joltage(bank, 0)

    return res


def find_best_joltage(bank, n):
    l = 0 if n == 0 else len(str(n))

    if l == 11:
        return n* 10 + max(bank)
        
    best = 0
    best_i = 0
    for i, b in enumerate(bank[:len(bank) - (12-l) + 1]):
        if b > best:
            best = b
            best_i = i

    return find_best_joltage(bank[best_i+1:], n*10 + best)


print(puzzle2())