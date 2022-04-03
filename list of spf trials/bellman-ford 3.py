#tutorial from c.p.

def bellman_ford(nodes, edges, source_index=0):
    path_lengths = {v: float('inf') for v in nodes}
    path_lengths[source_index] = 0

    paths = {v: [] for v in nodes}
    paths[source_index] = [source_index]

    for _ in range(len(nodes) - 1):
        for (u, v), w_uv in edges.items():
            if path_lengths[u] + w_uv < path_lengths[v]:
                path_lengths[v] = path_lengths[u] + w_uv
                paths[v] = paths[u] + [v]

    return path_lengths, paths

#input (positive weights)

nodes = [0, 1, 2, 3, 4, 5]
edges = {(0, 1): 1, (1, 0): 1, (0, 2): 1.5, (2, 0): 1.5,
         (0, 3): 2, (3, 0): 2, (1, 3): 0.5, (3, 1): 0.5,
         (1, 4): 2.5, (4, 1): 2.5, (2, 3): 1.5, (3, 2): 1.5,
         (4, 5): 2, (5, 4): 2,
         (5, 3): -5.5} #if value changed to (-), the algo from dijkstra template is not working
shortest_path_lengths, shortest_paths = bellman_ford(nodes, edges)

print(shortest_path_lengths) #this command will print the length from starting point to every point
print(shortest_paths) #this command will print the list of the shortest route

