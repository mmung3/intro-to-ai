# set up variables and domains
my_variables = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
domain = [1, 2, 3, 4]


# set up array `my_constraints` which we will use to check our constraints
# - we use multiple `if` clauses to filter down the constraints
#   so that we do not send in uninitialized variables
# - returns True if all constraints are satisfied considering the context
def check_constraints(context):
    letters = len(context)  # letters = the number of letters (A,B,C...) we have assigned so far
    my_constraints = []

    if letters <= 3:
        # we have at most ABC defined
        return True

    if letters >= 4:
        # we have ABCD defined
        a = context[0][1]  # context is an array of tuples.
        b = context[1][1]  # Here [0][1] will grab the 0th variables' value (value is stored at index 1)
        c = context[2][1]
        d = context[3][1]

        my_constraints.append((d != c, "Error: d != c"))

    if letters >= 5:
        # we have ABCDE defined
        e = context[4][1]

        my_constraints.append((e != c, "Error: e != c"))
        my_constraints.append((e < d - 1, "Error: e < d - 1"))

    if letters >= 6:
        # we have ABCDEF defined
        f = context[5][1]

        my_constraints.append((abs(e - f) % 2 == 1, "Error: abs(e - f) % 2 != 1"))
        my_constraints.append((abs(f - b) == 1, "Error: abs(f - b) != 1"))
        my_constraints.append((c != f, "Error: c != f"))
        my_constraints.append((d != f - 1, "Error: d != f - 1"))

    if letters >= 7:
        # we have ABCDEFG defined
        g = context[6][1]

        my_constraints.append((a > g, "Error: a > g"))
        my_constraints.append((abs(g - c) == 1, "Error: abs(g - c) != 1"))
        my_constraints.append((g != f, "Error: g != f"))
        my_constraints.append((d >= g, "Error: d >= g"))

    if letters == 8:
        # we have ABCDEFGH defined
        h = context[7][1]

        my_constraints.append((a <= h, "Error: a <= h"))
        my_constraints.append((abs(h - c) % 2 == 0, "Error: abs(h - c) % 2 != 0"))
        my_constraints.append((h != f, "Error: h != f"))
        my_constraints.append((h != d, "Error: h != d"))
        my_constraints.append((g < h, "Error: g < h"))
        my_constraints.append((e != h - 2, "Error: e != h - 2"))

    # we have added a bunch of constraints in the form of True/False booleans, so
    # we can `and` them together in order to check for any failing ones
    result = True
    for i in range(0, len(my_constraints)):
        result = result and my_constraints[i][0]
    return result


# our main dfs function
# - variables = the array of variables to assign: ['A', 'B', ... 'H']
# - context = an array which we use to store the problem as it unfolds. Starts as []
# - depth = a depth tracker we use to aid with the printing of the tree. Starts as 0
def dfs(variables, context, depth):

    # check all constraints given the context. If we fail,
    # return an empty array so that nothing is appended
    if not check_constraints(context):
        print("  " * depth + "failed")
        return []

    # check if we have assigned all variables something
    # the `if` clause is equiv to:
    #       if variables == []
    # if successful, return the context so far
    if not variables:
        print("  " * depth + "solution")
        return [context]

    # otherwise, we need to perform a further DFS. We will use the call stack to search
    else:
        var = variables.pop()  # grab the latest from our variables array
        sols = []

        # this `for` loop will:
        # - add a new path to our `context`, as a tuple
        # - add it to a recursive DFS call
        for val in domain:
            new_context = context.copy()
            new_context.append((var, val))
            print("  " * depth + f"{var}={val}", end=" ")
            sols.extend(dfs(variables.copy(), new_context, depth + 1))
        # once done, return the solution
        return sols


if __name__ == '__main__':

    # initial function call
    solutions = dfs(my_variables, [], 0)

    # print all solutions to console
    print("\nSolutions found:\n")
    for sol in solutions:
        print(sol)
