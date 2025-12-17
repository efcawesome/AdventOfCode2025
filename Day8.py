import heapq
from functools import cache

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]


def get_coords(line):
    l_split = line.split(",")
    return int(l_split[0]), int(l_split[1]), int(l_split[2])


def get_sqr_distance(x, y, z, ox, oy, oz):
    return (x - ox) ** 2 + (y - oy) ** 2 + (z - oz) ** 2


@cache
def parse_input():
    boxes = [[] for i in range(len(lines))]
    for i, line in enumerate(lines):
        x, y, z = get_coords(line)

        for j, other in enumerate(lines[i+1:]):
            ox, oy, oz = get_coords(other)
            d = get_sqr_distance(x, y, z, ox, oy, oz)

            boxes[i].append((j + i + 1, d))

    return boxes


def puzzle1(connections):
    boxes = parse_input()
    edges = []
    graphs = {}
    in_set = {}

    for i, v in enumerate(boxes):
        graphs[i] = {i}
        in_set[i] = i
        for e in v:
            heapq.heappush(edges, (e[1], i, e[0]))

    # kruskals
    while connections > 0:
        e, u, v = heapq.heappop(edges)
        u_set = in_set[u]
        v_set = in_set[v]

        if u_set != v_set:
            for node in graphs[v_set]:
                in_set[node] = u_set
            new_set = graphs[u_set].union(graphs[v_set])
            graphs[u_set] = new_set
            del graphs[v_set]

        connections -= 1

    biggest = sorted(graphs.values(), key=len, reverse=True)
    return len(biggest[0]) * len(biggest[1]) * len(biggest[2])


def puzzle2():
    boxes = parse_input()
    edges = []
    graphs = {}
    in_set = {}

    for i, v in enumerate(boxes):
        graphs[i] = {i}
        in_set[i] = i
        for e in v:
            heapq.heappush(edges, (e[1], i, e[0]))

    last_x1, last_x2 = 0, 0
    while edges and len(graphs) > 1:
        e, u, v = heapq.heappop(edges)
        u_set = in_set[u]
        v_set = in_set[v]

        if u_set != v_set:
            for node in graphs[v_set]:
                in_set[node] = u_set
            new_set = graphs[u_set].union(graphs[v_set])
            graphs[u_set] = new_set
            del graphs[v_set]

        last_x1, last_x2 = int(lines[u].split(",")[0]), int(lines[v].split(",")[0])

    return last_x1 * last_x2


def solve():
    print(f"Puzzle 1: {puzzle1(1000)}")
    print(f"Puzzle 2: {puzzle2()}")


solve()
