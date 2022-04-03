#trial using code from c.p. and actual data

def bellman_ford(nodes, edges, source_index=0):
    path_lengths = {v: float('inf') for v in nodes}
    path_lengths[source_index] = 1

    paths = {v: [] for v in nodes}
    paths[source_index] = [source_index]

    for _ in range(len(nodes) - 1):
        for (u, v), w_uv in edges.items():
            if path_lengths[u] + w_uv < path_lengths[v]:
                path_lengths[v] = path_lengths[u] + w_uv
                paths[v] = paths[u] + [v]

    return path_lengths, paths

#input (positive weights)

nodes = [1, 2, 3, 4, 5, 6, 7]
edges = {(1, 2): 4776, (1, 3): 5597, (1, 6): 2491, (1, 7): 4480,
         (2, 3): 8506, (2, 6): 4551, (2, 7): 6945,
         (3, 6): 5584, (3,7): 6397,
         (4, 5): 2909, (4,6): 5201,
         (5, 6): 6324,
         (6, 7): 6974}
shortest_path_lengths, shortest_paths = bellman_ford(nodes, edges)

print(shortest_path_lengths) #this command will print the length from starting point to every point
print(shortest_paths) #this command will print the list of the shortest route

