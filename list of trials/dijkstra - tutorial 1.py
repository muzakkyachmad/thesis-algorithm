#tutorial dijkstra from cp

def dijkstra(nodes, edges, source_index=0):
    """

    :param list nodes: the set of nodes
    :param dict edges: the set of edges, e.g., {(node, node): distance}
    :param int source_index: the index of the source node
    :return: the shortest distances from the source node
    """

def dijkstra(nodes, edges, source_index=0):

    path_lengths = {v: float('inf') for v in nodes} #v times | v = number of nodes
    path_lengths[source_index] = 0

    paths = {v: [] for v in nodes}
    paths[source_index] = [source_index]

    adjacent_nodes = {v: {} for v in nodes} #to provide the dict as an input
    for (u, v), w_uv in edges.items():
        adjacent_nodes[u][v] = w_uv

    temporary_nodes = [v for v in nodes]
    while len(temporary_nodes) > 0: #v times to reduce the loop
        upper_bounds = {v: path_lengths[v] for v in temporary_nodes}
        u = min(upper_bounds, key=upper_bounds.get)
        temporary_nodes.remove(u)

        for v, w_uv in adjacent_nodes[u].items():
            if path_lengths[u] + w_uv < path_lengths[v] and v in temporary_nodes:
                path_lengths[v] = path_lengths[u] + w_uv
                paths[v] = paths[u] + [v]
    return path_lengths, paths

nodes = [0, 1, 2, 3, 4, 5]
edges = {(0, 1): 1, (1, 0): 1, (0, 2): 1.5, (2, 0): 1.5,
         (0, 3): 2, (3, 0): 2, (1, 3): 0.5, (3, 1): 0.5,
         (1, 4): 2.5, (4, 1): 2.5, (2, 3): 1.5, (3, 2): 1.5,
         (4, 5): 2, (5, 4): 2,
         (5, 3): 1} #if (5, 3) value changed to -4.5, the algo from dijkstra template isnt working
shortest_path_lengths, shortest_paths = dijkstra(nodes, edges)
print(shortest_path_lengths)
print(shortest_paths)