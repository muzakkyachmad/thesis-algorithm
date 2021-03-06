# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 14:02:42 2022

@author: DM16303
"""
import pandas as pd

#df = pd.read_excel('test.xlsx', sheet_name='7matrix',index_col=0)

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
    print (path[n - 1])
 
    
# #read excel data
# df = pd.read_excel('test.xlsx', sheet_name='matrix',index_col=0)
# graph = df.values.tolist()
# V = len(df.index)

# Driver code
if __name__ == '__main__':
    MAXM,INF = 27**2,10**7 #the masx value for the infinite
    dis = [[-1 for i in range(MAXM)] for i in range(MAXM)]
    Next = [[-1 for i in range(MAXM)] for i in range(MAXM)]
 
    # V = 4
    # graph = [ [ 0, 3, INF, 7 ],
    #         [ 8, 0, 2, INF ],
    #         [ 5, INF, 0, 1 ],
    #         [ 2, INF, INF, 0 ] ]
    
    
    #read excel data
    df = pd.read_excel('SPF_Results.xlsx', sheet_name='Shortest_path_Matrix',index_col=0)
    graph = df.values.tolist() #taking the data and convert it to list of list
    V = len(df.index)


    # Function to initialise the
    # distance and Next array
    initialise(V)
 
    # Calling Floyd Warshall Algorithm,
    # this will update the shortest
    # distance as well as Next array
    floydWarshall(V)
    path = []
 

    
    for i in range(len(graph)): #loop the command
        for j in range(len(graph[0])):
            print(f"Shortest path from {i} to {j}: ", end = "")
            path = constructPath(i, j)
            printPath(path)
           
        
    # This code is contributed by mohit kumar 29