my_variables = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
domain = [1, 2, 3, 4]


def check_constraints(context):
    letters = len(context)
    my_constraints = []

    if letters <= 3:
        return True

    if letters >= 4:
        a = context[0][1]
        b = context[1][1]
        c = context[2][1]
        d = context[3][1]

        my_constraints.append((d != c, "Error: d != c"))

    if letters >= 5:
        e = context[4][1]

        my_constraints.append((e != c, "Error: e != c"))
        my_constraints.append((e < d - 1, "Error: e < d - 1"))

    if letters >= 6:
        f = context[5][1]

        my_constraints.append((abs(e - f) % 2 == 1, "Error: abs(e - f) % 2 != 1"))
        my_constraints.append((abs(f - b) == 1, "Error: abs(f - b) != 1"))
        my_constraints.append((c != f, "Error: c != f"))
        my_constraints.append((d != f - 1, "Error: d != f - 1"))

    if letters >= 7:
        g = context[6][1]

        my_constraints.append((a > g, "Error: a > g"))
        my_constraints.append((abs(g - c) == 1, "Error: abs(g - c) != 1"))
        my_constraints.append((g != f, "Error: g != f"))
        my_constraints.append((d >= g, "Error: d >= g"))

    if letters == 8:
        h = context[7][1]

        my_constraints.append((a <= h, "Error: a <= h"))
        my_constraints.append((abs(h - c) % 2 == 0, "Error: abs(h - c) % 2 != 0"))
        my_constraints.append((h != f, "Error: h != f"))
        my_constraints.append((h != d, "Error: h != d"))
        my_constraints.append((g < h, "Error: g < h"))
        my_constraints.append((e != h - 2, "Error: e != h - 2"))

    result = True
    for i in range(0, len(my_constraints)):
        result = result and my_constraints[i][0]
    return result


def dfs(variables, context, depth=0):
    if not check_constraints(context):
        print("  " * depth + "failed")
        return []
    if not variables:
        print("  " * depth + "solution")
        return [context]
    else:
        var = variables.pop()
        sols = []
        for val in domain:
            new_context = context.copy()
            new_context.append((var, val))
            print("  " * depth + f"{var}={val}", end=" ")
            sols.extend(dfs(variables.copy(), new_context, depth + 1))
        return sols


if __name__ == '__main__':

    solutions = dfs(my_variables, [])

    print("\nSolutions found:\n")
    for sol in solutions:
        print(sol)
