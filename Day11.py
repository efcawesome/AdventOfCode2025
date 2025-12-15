from collections import defaultdict, deque


with open("input.txt") as f:
    lines = [x.strip("\n") for x in f.readlines()]

def parse_input():
    adj_list = {}
    for line in lines:
        l_s = line.split(": ")
        node = l_s[0]

        adj_list[node] = [x for x in l_s[1].split(" ")]

    return adj_list

def puzzle1():
    adj_list = parse_input()
    res = 0

    q = deque(["you"])
    while q:
        curr = q.popleft()

        for v in adj_list[curr]:
            if v == "out":
                res += 1
            else:
                q.append(v)

    return res


def find_paths(adj_list, curr, fft_seen, dac_seen, cache):
    if (curr, fft_seen, dac_seen) in cache:
        return cache[(curr, fft_seen, dac_seen)]
    if curr == "fft":
        fft_seen = True
    if curr == "dac":
        dac_seen = True

    res = 0
    for v in adj_list[curr]:
        res += find_paths(adj_list, v, fft_seen, dac_seen, cache)
    
    cache[(curr, fft_seen, dac_seen)] = res
    return res


def puzzle2():
    adj_list = parse_input()
    cache = {("out", True, True): 1, ("out", True, False): 0, ("out", False, True): 0, ("out", False, False): 0}
    return find_paths(adj_list, "svr", False, False, cache)

print(puzzle2())
