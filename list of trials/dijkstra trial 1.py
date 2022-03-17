
#cp

def dijkstra(nodes, edges, source_index=0):
    """
    :param list nodes: the set of nodes
    :param dict edges: the set of edges, e.g., {(node, node): distance}
    :param int source_index: the index of the source node
    :return: the shortest distances from the source node
    """

def dijkstra(nodes, edges, source_index=0):
    path_lengths = {v: float('inf') for v in nodes}
    path_lengths[source_index] = 0
    paths = {v: [] for v in nodes}
    paths[source_index] = [source_index]
    adjacent_nodes = {v: {} for v in nodes}
    for (u, v), w_uv in edges.items():
        adjacent_nodes[u][v] = w_uv

    temporary_nodes = [v for v in nodes]
    while len(temporary_nodes) > 0:
        upper_bounds = {v: path_lengths[v] for v in temporary_nodes}
        u = min(upper_bounds, key=upper_bounds.get)
        temporary_nodes.remove(u)
        for v, w_uv in adjacent_nodes[u].items():
            if path_lengths[u] + w_uv < path_lengths[v] and v in temporary_nodes:
                path_lengths[v] = path_lengths[u] + w_uv
                paths[v] = paths[u] + [v]
    return path_lengths, paths

nodes = [1, 2, 3, 4, 5, 6, 7]
edges = {(1, 2): 4776, (1, 3): 5597, (1, 6): 2491, (1, 7): 4480,
         (2, 3): 8506, (2, 6): 4551, (2, 7): 6945,
         (3, 6): 5584, (3,7): 6397,
         (4, 5): 2909, (4,6): 5201,
         (5, 6): 6324,
         (6, 7): 6974}

shortest_path_lengths, shortest_paths = dijkstra(nodes, edges)
print(shortest_path_lengths)
print(shortest_paths)