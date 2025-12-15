with open("input.txt") as f:
    lines = [x.strip("\n") for x in f.readlines()]

def parse_input():
    numbers = []

    for line in lines[:len(lines) - 1]:
        curr = []
        l_split = [x.strip(" ") for x in line.split(" ") if x != ""]

        for c in l_split:
            curr.append(int(c))

        numbers.append(curr)

    operations = [x for x in lines[-1].split(" ") if x != ""]
    return numbers, operations
            

def puzzle1():
    numbers, operations = parse_input()

    res = 0

    for i, operation in enumerate(operations):
        curr = 1 if operation == "*" else 0
        for row in numbers:
            if operation == "*":
                curr *= row[i]
            else:
                curr += row[i]

        res += curr

    return res


def parse_again():
    numbers = []
    operations = []

    for line in lines[:len(lines) - 1]:
        curr = []

        for c in line:
            if c == " ":
                curr.append("")
            else:
                curr.append(c)

        numbers.append(curr)

    for c in lines[-1]:
        if c == " ":
            operations.append("")
        else:
            operations.append(c)
    
    return numbers, operations

def puzzle2():
    numbers, operations = parse_again()
    res = 0

    curr_op = ""
    curr_nums = []
    for i, op in enumerate(operations):
        if op != "":
            curr = 1 if curr_op == "*" else 0
            for n in curr_nums:
                if curr_op == "*":
                    curr *= n
                else:
                    curr += n

            curr_nums.clear()
            res += curr
            curr_op = op

        curr_num = ""
        for row in numbers:
            if row[i] != "":
                curr_num += row[i]

        if curr_num != "":
            curr_nums.append(int(curr_num))

    curr = 1 if curr_op == "*" else 0
    for n in curr_nums:
        if curr_op == "*":
            curr *= n
        else:
            curr += n

    curr_nums.clear()
    res += curr
    
    return res


print(puzzle2())