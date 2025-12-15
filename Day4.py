with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

def parse_input():
    rolls = [[c for c in line] for line in lines]
    return rolls

def get_adjacent_count(rolls, i,j):
    count = 0
    for k in range(i - 1, i + 2):
        for l in range(j - 1, j + 2):
            if k < 0 or l < 0:
                continue
            try:
                if (k != i or l != j) and rolls[k][l] == "@":
                    count += 1
            except:
                continue

    
    return count
            

def puzzle1():
    rolls = parse_input()
    res = 0

    for i, row in enumerate(rolls):
        for j, r in enumerate(row):
            if r == "@" and get_adjacent_count(rolls, i, j) < 4:
                res += 1

    return res


def puzzle2():
    rolls = parse_input()
    old = -1
    res = 0
    to_remove = []

    while old != res:
        old = res

        for i, row in enumerate(rolls):
            for j, r in enumerate(row):
                if r == "@" and get_adjacent_count(rolls, i, j) < 4:
                    to_remove.append((i,j))
                    res += 1

        for i, j in to_remove:
            rolls[i][j] = "."

    return res

print(puzzle2())