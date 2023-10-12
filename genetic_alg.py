import random

initial_states = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2, 2, 2, 2],
    [3, 3, 3, 3, 3, 3, 3, 3],
    [4, 4, 4, 4, 4, 4, 4, 4],
    [1, 2, 3, 4, 1, 2, 3, 4],
    [4, 3, 2, 1, 4, 3, 2, 1],
    [1, 2, 1, 2, 1, 2, 1, 2],
    [3, 4, 3, 4, 3, 4, 3, 4]
]


def check_constraints(assignment):
    satisfied_constraints = 0

    A, B, C, D, E, F, G, H = assignment

    if A > G:
        satisfied_constraints += 1
    if abs(G - C) == 1:
        satisfied_constraints += 1
    if D != C:
        satisfied_constraints += 1
    if G != F:
        satisfied_constraints += 1
    if abs(E - F) % 2 == 1:
        satisfied_constraints += 1
    if A <= H:
        satisfied_constraints += 1
    if abs(H - C) % 2 == 0:
        satisfied_constraints += 1
    if E != C:
        satisfied_constraints += 1
    if H != F:
        satisfied_constraints += 1
    if abs(F - B) == 1:
        satisfied_constraints += 1
    if H != D:
        satisfied_constraints += 1
    if E < D - 1:
        satisfied_constraints += 1
    if C != F:
        satisfied_constraints += 1
    if G < H:
        satisfied_constraints += 1
    if D >= G:
        satisfied_constraints += 1
    if E != H - 2:
        satisfied_constraints += 1
    if D != F - 1:
        satisfied_constraints += 1

    return satisfied_constraints


# Returns a list of fitness scores based on the assignment (i.e. collection of states) given
def selection(assignment):
    constraint_sum = 0
    unscaled_scores = []

    # generate a sum of constraints so far and add the unscaled values to an array
    for state in assignment:
        constraint_count = check_constraints(state)
        constraint_sum += constraint_count
        unscaled_scores.append(constraint_count)

    # now we have the sum, divide all array elements by the sum
    fitness_scores = list(map(lambda x: x / constraint_sum, unscaled_scores))
    print("Fitness scores: " + str(fitness_scores))

    size = len(assignment)
    # now we have the fitness scores, rearrange the assignment s.t. we can pass it to selection()
    new_assignment = random.choices(assignment, weights=fitness_scores, k=size)

    # print(assignment)
    # print(new_assignment)
    return new_assignment


def crossover_helper(state1, state2, cross_pt):
    print("Parent 1: " + str(state1))
    print("Parent 2: " + str(state2))
    print("Cross Point: " + str(cross_pt))

    state11 = state1[:cross_pt]
    state21 = state2[:cross_pt]
    state12 = state1[cross_pt:]
    state22 = state2[cross_pt:]

    state1 = state11 + state22
    state2 = state21 + state12

    print("Offspring Produced: " + str(state1))
    print("Offspring Produced: " + str(state2))
    print()

    return state1, state2  # returns a tuple


def crossover(assignment):
    new_assignment = []

    # iter1
    cross_pt = random.randint(1, 7)

    state1 = assignment[0]
    state2 = assignment[1]
    crossed_tuple = crossover_helper(state1, state2, cross_pt)

    new_assignment.append(crossed_tuple[0])
    new_assignment.append(crossed_tuple[1])

    # iter2
    cross_pt = random.randint(1, 7)

    state1 = assignment[2]
    state2 = assignment[3]
    crossed_tuple = crossover_helper(state1, state2, cross_pt)

    new_assignment.append(crossed_tuple[0])
    new_assignment.append(crossed_tuple[1])

    # iter3
    cross_pt = random.randint(1, 7)

    state1 = assignment[4]
    state2 = assignment[5]
    crossed_tuple = crossover_helper(state1, state2, cross_pt)

    new_assignment.append(crossed_tuple[0])
    new_assignment.append(crossed_tuple[1])

    # iter 4
    cross_pt = random.randint(1, 7)

    state1 = assignment[6]
    state2 = assignment[7]
    crossed_tuple = crossover_helper(state1, state2, cross_pt)

    new_assignment.append(crossed_tuple[0])
    new_assignment.append(crossed_tuple[1])

    return new_assignment


def mutate(assignment):
    for state in assignment:
        is_mutating = random.random() < 0.3
        if is_mutating:
            index = random.randint(0, len(state) - 1)
            print("Mutated state: " + str(state) + " at index " + str(index))
            state[index] = random.randint(1, 4)

    return assignment


if __name__ == '__main__':
    print("\n=== Generation 1 ===")
    iter1 = mutate(crossover(selection(initial_states)))
    print("\n=== Generation 2 ===")
    iter2 = mutate(crossover(selection(iter1)))
    print("\n=== Generation 3 ===")
    iter3 = mutate(crossover(selection(iter2)))
    print("\n=== Generation 4 ===")
    iter4 = mutate(crossover(selection(iter3)))
    print("\n=== Generation 5 ===")
    iter5 = mutate(crossover(selection(iter4)))
