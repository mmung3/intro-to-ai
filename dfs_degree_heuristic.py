"""
Note that this file only contains a partial function implementation!
To test this, replace the original `check_constraints()` in `dfs_constraints.py`
"""

def check_constraints(context):
    letters = len(context)  # letters = the number of letters (A,B,C...) we have assigned so far
    my_constraints = []

    if letters <= 1:
        # we have nothing worth using
        return True

    if letters >= 2:
        # we have H, F
        h = context[0][1]
        f = context[1][1]

        my_constraints.append((h != f, "Error: h != f"))

    if letters >= 3:
        # we have H, F, G
        g = context[2][1]

        my_constraints.append((g < h, "Error: g < h"))
        my_constraints.append((g != f, "Error: g != f"))

    if letters >= 4:
        # we have H, F, G, D
        d = context[3][1]

        my_constraints.append((h != d, "Error: h != d"))
        my_constraints.append((d != f - 1, "Error: d != f - 1"))
        my_constraints.append((d >= g, "Error: d >= g"))

    if letters >= 5:
        # we have H, F, G, D, C
        c = context[4][1]

        my_constraints.append((abs(g - c) == 1, "Error: abs(g - c) != 1"))
        my_constraints.append((abs(h - c) % 2 == 0, "Error: abs(h - c) % 2 != 0"))
        my_constraints.append((c != f, "Error: c != f"))
        my_constraints.append((d != c, "Error: d != c"))

    if letters >= 6:
        # we have H, F, G, D, C, E
        e = context[5][1]

        my_constraints.append((e != c, "Error: e != c"))
        my_constraints.append((e < d - 1, "Error: e < d - 1"))
        my_constraints.append((abs(e - f) % 2 == 1, "Error: abs(e - f) % 2 != 1"))
        my_constraints.append((e != h - 2, "Error: e != h - 2"))

    if letters >= 7:
        # we have H, F, G, D, C, E, A
        a = context[6][1]

        my_constraints.append((a > g, "Error: a > g"))
        my_constraints.append((a <= h, "Error: a <= h"))

    if letters >= 8:
        # we have H, F< G, D, C, E, A, B
        b = context[7][1]

        my_constraints.append((abs(f - b) == 1, "Error: abs(f - b) != 1"))

    # we have added a bunch of constraints in the form of True/False booleans, so
    # we can `and` them together in order to check for any failing ones
    result = True
    for i in range(0, len(my_constraints)):
        result = result and my_constraints[i][0]
    return result
