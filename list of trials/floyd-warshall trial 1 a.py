#algorithm concept or framework A using floyd warshall based on c.p

def floyd_warshall(nodes, edges):
    """

    :param list nodes: the set of nods
    :param dict edges: the set of edges e.g., {(nodes, nodes): distance}
    :return: the shortest path lengths between all pairs of nodes
    """

    d = {(u,v): float('inf') if u != v else 0 for u in nodes for v in nodes}
    for (u,v), w_uv in edges.items():
        d[(u,v)] = w_uv

    for k in nodes:
        for u in nodes:
            for v in nodes:
                d[(u,v)] = min(d[u,v], d[u,k] + d[k,v])


    if any(d[(u,u)] < 0 for u in nodes):
        print("Graph has a negative-weight cycle")

    return d #shortest path lengths

#input data of the WWTP - WWTP code is represented in number and started from 0 as WWTP A

nodes = [0, 1, 2, 3, 4, 5, 6]
edges = {(0, 1): 4776, (0, 2): 5597, (0, 5): 2491, (0, 6): 4480,
         (1, 0): 4776, (1, 2): 8506, (1, 5): 4551, (1, 6): 6945,
         (2, 0): 5597, (2, 1): 8506, (2, 5): 5854, (2, 6): 6397,
         (3, 4): 2909, (3, 5): 5201,
         (4, 3): 2909, (4, 5): 6324,
         (5, 0): 2491, (5, 1): 4551, (5, 2): 5854, (5, 3): 5201, (5, 4): 6324, (5, 6): 6974,
         (6, 0): 4480, (6, 1): 6945, (6, 2): 6397, (6, 5): 6974}

shortest_path_lengths = floyd_warshall(nodes, edges)

print(shortest_path_lengths) #this command will print the length from starting point to every point

for(int(i=1), i<v ++j):
    {
        for(int j=0;j<v: ++j):
            cout<<i<<" to "<<j<<" distance is"
    }