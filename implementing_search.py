from collections import deque
# import a double-ended queue from built in python packages

rows = 10
cols = 10
no_path = 10_000  # using 10,000 instead of infinity for the adjacency matrix

adjMat = [[no_path for y in range(rows)] for x in range(cols)]


def init_matrix():
    # filling in special tiles
    # for adjMat[i][j], let i = start and j = end
    adjMat[0][1] = 3  # S -> A
    adjMat[0][2] = 9  # S -> B
    adjMat[0][3] = 4  # S -> C
    adjMat[1][3] = 2  # A -> C
    adjMat[2][3] = 13  # B -> C
    adjMat[3][4] = 5  # C -> D
    adjMat[3][5] = 4  # C -> E
    adjMat[3][6] = 8  # C -> F
    adjMat[4][6] = 5  # D -> F
    adjMat[5][6] = 7  # E -> F
    adjMat[6][7] = 8  # F -> G
    adjMat[6][8] = 7  # F -> H
    adjMat[6][9] = 18  # F -> Z
    adjMat[7][9] = 9  # G -> Z
    adjMat[8][9] = 6  # H -> Z


# dictionary allowing us to convert to letters when printing to console
mat_dict = {
    0: "S",
    1: "A",
    2: "B",
    3: "C",
    4: "D",
    5: "E",
    6: "F",
    7: "G",
    8: "H",
    9: "Z"
}


def is_goal(curr_node):
    print(f"Expanding: {mat_dict[curr_node]}")
    goal = 9
    return curr_node == goal


def stack_push(s, val):
    s.append(val)  # 'append' is equiv to 'push' for stacks in python


def stack_pop(s):
    return s.pop()  # 'pop' for a LIFO stack in python


def queue_push(q, val):
    q.append(val)  # 'append is equiv to 'push' for queues in python


def queue_pop(q):
    return q.popleft()  # 'popleft' for a FIFO queue in python


def search(matrix, start, container, my_push, my_pop):

    size = len(matrix)  # i.e. number of nodes in our array

    frontier = container()
    my_push(frontier, [start])

    # while frontier is not empty
    while len(frontier) != 0:

        # select and remove path from frontier
        curr_path = my_pop(frontier)
        curr_node = curr_path[-1]  # grab last elem on the path

        # if goal, return
        if is_goal(curr_node):
            print("Success: ", end="")

            for i in curr_path:
                print(mat_dict[i], end=" ")
            return curr_path

        # for every neighbour n of n_k, add path to the frontier
        for i in range(size):

            # if we can make it there, add it
            if matrix[curr_node][i] != no_path:
                next_path = curr_path + [i]
                my_push(frontier, next_path)

    # failed to find
    print("Failure")
    return


if __name__ == '__main__':

    init_matrix()

    # # print the contents of the adj matrix
    # for i in range(rows):
    #     for j in range(cols):
    #         print(adjMat[i][j], end="\t")
    #     print()

    """change last param to 'deque' for BFS, and 'list' for DFS"""
    # note that due to the nature of our implementation DFS will
    # perform slightly differently than A1 Q1.
    # that is, it picks the nodes in "reverse alphabetical order" off
    # the stack when breaking ties / pushing onto the frontier
    # ex. if we have to push [ A,B,C ] onto the stack,
    #     DFS will choose to expand C, then B, then A

    print("DFS: ")
    search(adjMat, 0, list, stack_push, stack_pop)

    print("\n\nBFS: ")
    search(adjMat, 0, deque, queue_push, queue_pop)
    print("\n")
