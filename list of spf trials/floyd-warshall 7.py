#another code from daniel based on geeksforgeeks

# Python3 program to find the shortest
# path between any two nodes using
# Floyd Warshall Algorithm.

# Initializing the distance and
# Next array
def initialise(V):
    global dis, Next

    for i in range(V):
        for j in range(V):
            dis[i][j] = graph[i][j]

            # No edge between node
            # i and j
            if (graph[i][j] == INF):
                Next[i][j] = -1
            else:
                Next[i][j] = j


# Function construct the shortest
# path between u and v
def constructPath(u, v):
    global graph, Next

    # If there's no path between
    # node u and v, simply return
    # an empty array
    if (Next[u][v] == -1):
        return {}

    # Storing the path in a vector
    path = [u]
    while (u != v):
        u = Next[u][v]
        path.append(u)

    return path


# Standard Floyd Warshall Algorithm
# with little modification Now if we find
# that dis[i][j] > dis[i][k] + dis[k][j]
# then we modify next[i][j] = next[i][k]
def floydWarshall(V):
    global dist, Next
    for k in range(V):
        for i in range(V):
            for j in range(V):

                # We cannot travel through
                # edge that doesn't exist
                if (dis[i][k] == INF or dis[k][j] == INF):
                    continue
                if (dis[i][j] > dis[i][k] + dis[k][j]):
                    dis[i][j] = dis[i][k] + dis[k][j]
                    Next[i][j] = Next[i][k]


# Print the shortest path
def printPath(path):
    n = len(path)
    for i in range(n - 1):
        print(path[i], end=" -> ")
    print(path[n - 1])


# Driver code
if __name__ == '__main__':
    MAXM, INF = 100, 10 ** 7
    dis = [[-1 for i in range(MAXM)] for i in range(MAXM)]
    Next = [[-1 for i in range(MAXM)] for i in range(MAXM)]

    V = 7
    graph = [[0, 1590, 3736, INF, 3281, INF, INF],
             [1590, 0, 1249, 5783, 3795, INF, INF],
             [3736, 1249, 0, 5490, 4282, INF, INF],
             [INF, 5783, 5490, 0, 2894, 6395, 9607],
             [3281, 3795, 4282, 2894, 0, 5117, 8676],
             [INF, INF, INF, 6395, 5117, 0, 7331],
             [INF, INF, INF, 9607, 8676, 7331, 0]]

    # Function to initialise the
    # distance and Next array
    initialise(V)

    # Calling Floyd Warshall Algorithm,
    # this will update the shortest
    # distance as well as Next array
    floydWarshall(V)
    path = []

    # Path from node 0 to 1
    print("Shortest path from 0 to 1: ", end="")
    path = constructPath(0, 1)
    printPath(path)

    # Path from node 0 to 2
    print("Shortest path from 0 to 2: ", end="")
    path = constructPath(0, 2)
    printPath(path)

    # Path from node 0 to 3
    print("Shortest path from 0 to 3: ", end="")
    path = constructPath(0, 3)
    printPath(path)

    # Path from node 0 to 4
    print("Shortest path from 0 to 4: ", end="")
    path = constructPath(0, 4)
    printPath(path)

    # Path from node 0 to 5
    print("Shortest path from 0 to 5: ", end="")
    path = constructPath(0, 5)
    printPath(path)

    # Path from node 0 to 6
    print("Shortest path from 0 to 6: ", end="")
    path = constructPath(0, 6)
    printPath(path)

    # Path from node 1 to 2
    print("Shortest path from 1 to 2: ", end="")
    path = constructPath(1, 2)
    printPath(path)

    # Path from node 1 to 3
    print("Shortest path from 1 to 3: ", end="")
    path = constructPath(1, 3)
    printPath(path)

    # Path from node 1 to 4
    print("Shortest path from 1 to 4: ", end="")
    path = constructPath(1, 4)
    printPath(path)

    # Path from node 1 to 5
    print("Shortest path from 1 to 5: ", end="")
    path = constructPath(1, 5)
    printPath(path)

    # Path from node 1 to 6
    print("Shortest path from 1 to 6: ", end="")
    path = constructPath(1, 6)
    printPath(path)

    # Path from node 2 to 0
    print("Shortest path from 2 to 0: ", end="")
    path = constructPath(2, 0)
    printPath(path)

    # Path from node 2 to 1
    print("Shortest path from 2 to 1: ", end="")
    path = constructPath(2, 1)
    printPath(path)

    # Path from node 2 to 3
    print("Shortest path from 2 to 3: ", end="")
    path = constructPath(2, 3)
    printPath(path)

    # Path from node 2 to 4
    print("Shortest path from 2 to 4: ", end="")
    path = constructPath(2, 4)
    printPath(path)

    # Path from node 2 to 5
    print("Shortest path from 2 to 5: ", end="")
    path = constructPath(2, 5)
    printPath(path)

    # Path from node 2 to 6
    print("Shortest path from 2 to 6: ", end="")
    path = constructPath(2, 0)
    printPath(path)

    # Path from node 3 to 0
    print("Shortest path from 3 to 0: ", end="")
    path = constructPath(3, 0)
    printPath(path)

    # Path from node 3 to 1
    print("Shortest path from 3 to 1: ", end="")
    path = constructPath(3, 1)
    printPath(path)

    # Path from node 3 to 2
    print("Shortest path from 3 to 2: ", end="")
    path = constructPath(3, 2)
    printPath(path)

    # Path from node 3 to 4
    print("Shortest path from 3 to 4: ", end="")
    path = constructPath(3, 4)
    printPath(path)

    # Path from node 3 to 5
    print("Shortest path from 3 to 5: ", end="")
    path = constructPath(3, 5)
    printPath(path)

    # Path from node 3 to 6
    print("Shortest path from 3 to 6: ", end="")
    path = constructPath(3, 6)
    printPath(path)

    # Path from node 4 to 0
    print("Shortest path from 4 to 0: ", end="")
    path = constructPath(4, 0)
    printPath(path)

    # Path from node 4 to 1
    print("Shortest path from 4 to 1: ", end="")
    path = constructPath(4, 1)
    printPath(path)

    # Path from node 4 to 2
    print("Shortest path from 4 to 2: ", end="")
    path = constructPath(4, 2)
    printPath(path)

    # Path from node 4 to 3
    print("Shortest path from 4 to 3: ", end="")
    path = constructPath(4, 3)
    printPath(path)

    # Path from node 4 to 5
    print("Shortest path from 4 to 5: ", end="")
    path = constructPath(4, 5)
    printPath(path)

    # Path from node 4 to 6
    print("Shortest path from 4 to 6: ", end="")
    path = constructPath(4, 6)
    printPath(path)

    # Path from node 5 to 0
    print("Shortest path from 5 to 0: ", end="")
    path = constructPath(5, 0)
    printPath(path)

    # Path from node 5 to 1
    print("Shortest path from 5 to 1: ", end="")
    path = constructPath(5, 1)
    printPath(path)

    # Path from node 5 to 2
    print("Shortest path from 5 to 2: ", end="")
    path = constructPath(5, 2)
    printPath(path)

    # Path from node 5 to 3
    print("Shortest path from 5 to 3: ", end="")
    path = constructPath(5, 3)
    printPath(path)

    # Path from node 5 to 4
    print("Shortest path from 5 to 4: ", end="")
    path = constructPath(5, 4)
    printPath(path)

    # Path from node 5 to 6
    print("Shortest path from 5 to 6: ", end="")
    path = constructPath(5, 6)
    printPath(path)

    # Path from node 6 to 0
    print("Shortest path from 6 to 0: ", end="")
    path = constructPath(6, 0)
    printPath(path)

    # Path from node 6 to 1
    print("Shortest path from 6 to 1: ", end="")
    path = constructPath(6, 1)
    printPath(path)

    # Path from node 6 to 2
    print("Shortest path from 6 to 2: ", end="")
    path = constructPath(6, 2)
    printPath(path)

    # Path from node 6 to 3
    print("Shortest path from 6 to 3: ", end="")
    path = constructPath(6, 3)
    printPath(path)

    # Path from node 6 to 4
    print("Shortest path from 6 to 4: ", end="")
    path = constructPath(6, 4)
    printPath(path)

    # Path from node 6 to 5
    print("Shortest path from 6 to 5: ", end="")
    path = constructPath(6, 5)
    printPath(path)




