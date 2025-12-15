from collections import defaultdict
import heapq


with open("input.txt") as f:
    lines = [x.strip("\n") for x in f.readlines()]

def parse_input():
    return [(int(x.split(",")[0]), int(x.split(",")[1])) for x in lines]
            

def puzzle1():
    coords = parse_input()
    best = 0
    for i, coord in enumerate(coords):
        x, y = coord
        for other in coords[i+1:]:
            ox, oy = other
            area = (abs(ox - x) + 1)*(abs(oy-y) + 1)

            best = max(best, area)

    return best


"""def legal_square (x, y, ox, oy, edges_x, edges_y):
    for j in [y, oy]:
        for e in edges_x:
            if min(x, ox) < e < max(x, ox):
                for r in edges_x[e]:
                    lo, hi = r
                    if lo <= j <= hi:
                        return False
                
    for i in [x, ox]:
        for e in edges_y:
            if min(y, oy) < e < max(y, oy):
                for r in edges_y[e]:
                    lo, hi = r
                    if lo <= i <= hi:
                        return False
    
    return True"""

def legal_square (x, y, ox, oy, edges_x, edges_y):
    in_shape_u = False
    in_shape_d = False

    x, ox = min(x, ox), max(x, ox)
    y, oy = min(y, oy), max(y, oy)
    for i in sorted(edges_x.keys()):
        for lo, hi in edges_x[i]:
            if lo <= y < hi:
                in_shape_u = not in_shape_u
            
            if lo < oy <= hi:
                in_shape_d = not in_shape_d

            if x <= i < ox and (not in_shape_u or not in_shape_d):
                return False
        
    in_shape_u = False
    in_shape_d = False
    for j in sorted(edges_y.keys()):
        for lo, hi in edges_y[j]:
            if lo <= x < hi:
                in_shape_u = not in_shape_u
            
            if lo < ox <= hi:
                in_shape_d = not in_shape_d

            if y <= j < oy and (not in_shape_u or not in_shape_d):
                return False

    return True

def puzzle2():
    coords = parse_input()
    edges_x = defaultdict(list)
    edges_y = defaultdict(list)

    for i, coord in enumerate(coords):
        x, y = coord
        lx, ly = coords[i - 1]

        if x == lx:
            edges_x[x].append((min(y, ly), max(y, ly)))
        else:
            edges_y[y].append((min(x, lx), max(x, lx)))

    best = []

    for i, coord in enumerate(coords):
        x, y = coord
        for other in coords[i+1:]:
            if coord == other:
                continue
        
            ox, oy = other

            heapq.heappush(best, (-(abs(ox - x) + 1)*(abs(oy-y) + 1), (x, y), (ox, oy))) 

    while best:
        a, pos1, pos2 = heapq.heappop(best)
        x1, y1 = pos1
        x2, y2 = pos2

        if legal_square(x1, y1, x2, y2, edges_x, edges_y):
            return -a

print(puzzle2())
