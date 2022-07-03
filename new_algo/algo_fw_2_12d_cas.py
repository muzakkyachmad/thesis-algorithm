#creator : Achmad Muzakky (Zakky) - MSc Sanitary Engineering IHE Delft 2019

#file name : algo_fw_2 = algorithm floyd-warshall stage 2
#definition : This python file is a file that contains some codes to determine the routes from the SPF results
#input data : An Excel file of the SPF results that contains the shortest path route of each WWTP in matrix
#mechanism : This python file will read the Excel data of each WWTP data in matrix on the sheet and execute it
#output data : The program will release the list of the shortest path route in the run terminal


#######################################################################################################################
#executing the list of the spf results - 12 D - CAS type

# Initializing the distance and
# Next array
def initialise(V):
    global dis, Next

    for i in range(V):
        for j in range(V):
            dis[i][j] = graph5[i][j]

            # No edge between node
            # i and j
            if (graph5[i][j] == INF):
                Next[i][j] = -1
            else:
                Next[i][j] = j


# Function construct the shortest
# path between u and v
def constructPath(u, v):
    global graph5, Next

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
    MAXM, INF = 27**2, 10**7
    dis = [[-1 for i in range(MAXM)] for i in range(MAXM)]
    Next = [[-1 for i in range(MAXM)] for i in range(MAXM)]

#read excel data
    import pandas as pd

    df5 = pd.read_excel('spf_results_12d_cas.xlsx', sheet_name='12d_cas_matrix',index_col=0)
    graph5 = df5.values.tolist() #taking the data and convert it to list of list
    V = len(df5.index)

    # Function to initialise the
    # distance and Next array
    initialise(V)

    # Calling Floyd Warshall Algorithm,
    # this will update the shortest
    # distance as well as Next array
    floydWarshall(V)
    path = []

    for i in range(len(graph5)): #loop the command
        for j in range(len(graph5[0])):
            print(f"Shortest path from {i} to {j}: ", end = "")
            path = constructPath(i, j)
            printPath(path)




