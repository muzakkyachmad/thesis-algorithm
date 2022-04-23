
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

#input data of the WWTP - WWTP code is represented in number and started from 0 as WWTP. data = 7 wwtp from python

nodes = [0, 1, 2, 3, 4, 5, 6]
edges = {(0, 1): 1590, (0, 2): 3736, (0, 4): 3281,
         (1, 0): 1590, (1, 2): 1249, (1, 3): 5783, (1, 4): 3795,
         (2, 0): 3736, (2, 1): 1249, (2, 3): 5490, (2, 4): 4282,
         (3, 1): 5783, (3, 2): 5490, (3, 4): 2894, (3, 5): 6395, (3, 6): 9607,
         (4, 0): 3281, (4, 1): 3795, (4, 2): 4282, (4, 3): 2894, (4, 5): 5117, (4, 6): 8676,
         (5, 3): 6395, (5, 4): 5117, (5, 6): 7331,
         (6, 3): 9607, (6, 4): 8676, (6, 5): 7331}

shortest_path_lengths = floyd_warshall(nodes, edges)

print(shortest_path_lengths) #this command will print the length from starting point to every point


