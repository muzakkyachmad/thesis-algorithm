
#tutorial from c.p

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

#input data

nodes = [0, 1, 2, 3, 4, 5]
edges = {(0, 1): 1, (1, 0): 1, (0, 2): 1.5, (2, 0): 1.5, (0, 3): 2, (1, 3): 0.5, (3, 1): 0.5,
         (1, 4): 2.5, (2, 3): 1.5, (4, 5): 2, (5, 3): -4.5}
shortest_path_lengths = floyd_warshall(nodes, edges)

print(shortest_path_lengths) #this command will print the length from starting point to every point

