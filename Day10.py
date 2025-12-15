import numpy as np
import optlang

with open("input.txt") as f:
    lines = [x.strip("\n") for x in f.readlines()]

def parse_input():
    machine_goals = []
    buttons = []
    joltages = []

    for line in lines:
        l_split = line.split(" ")
        machine_goal = 0
        m_split = l_split[0].strip("[]") 
        for x in m_split:
            machine_goal <<= 1
            if x == "#":
                machine_goal += 1
        
        machine_goals.append(machine_goal)

        curr_buttons = []
        for b in l_split[1:-1]:
            res = 0
            for x in b.strip("()").split(","):
                res += (1 << (len(m_split) - int(x) - 1))
            curr_buttons.append(res)
        buttons.append(curr_buttons)

    return machine_goals, buttons, joltages

def find_sol(m, buttons, curr, i):
    if curr == m:
        return 0
    
    if i >= len(buttons):
        return 1000000000
    
    on_res = 1 + find_sol(m, buttons, curr ^ buttons[i], i + 1)
    off_res = find_sol(m, buttons, curr, i + 1)

    return min(on_res, off_res)


def puzzle1():
    machine_goals, buttons, joltages = parse_input()
    
    res = 0
    for i, m in enumerate(machine_goals):
        res += find_sol(m, buttons[i], 0, 0)
        print("done")

    return res


def parse_p2():
    buttons = []

    for line in lines:
        l_split = line.split(" ")[1:]

        curr_joltages = []
        total = 0
        for x in l_split[-1].strip("\{\}").split(","):
            total += int(x)
            curr_joltages.append(int(x))

        curr_buttons = []
        for b in l_split[:-1]:
            res = [0] * len(curr_joltages)
            for x in b.strip("()").split(","):
                res[int(x)] = 1

            curr_buttons.append(np.array(res))

        curr_buttons.append(curr_joltages)
        buttons.append(np.column_stack(curr_buttons))

    return buttons


def puzzle2():
    buttons = parse_p2()
    res = 0

    for button in buttons:
        n, m = len(button[0]) - 1, len(button)
        variables = [optlang.Variable(f'x_{i+1}', lb=0, type="integer") for i in range(n)]

        constraints = []
        for i in range(m):
            coefficients = button[i, :-1]
            constant_term = button[i, -1]

            expr = sum(coefficients[j] * variables[j] for j in range(n))
            constraint = optlang.Constraint(expr, lb=constant_term, ub=constant_term)
            constraints.append(constraint)
        
        objective_expr = sum(variables)
        objective = optlang.Objective(objective_expr, direction="min")

        model = optlang.Model(variables = variables, constraints = constraints, objective=objective)
        model.optimize()

        res += model.objective.value

    return res

print(puzzle2())
