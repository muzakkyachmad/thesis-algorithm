#this algorithm is to find the shortest path of for 7sd - cas

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

#input data = wwtp cas - sd3, sd4, sd5, sd6

nodes = [3, 4, 5, 6]
edges = {(3, 4): 2894, (3, 5): 6395, (3, 6): 9607,
         (4, 3): 2894, (4, 5): 5117, (4, 6): 8676,
         (5, 3): 6395, (5, 4): 5117, (5, 6): 7331,
         (6, 3): 9607, (6, 4): 8676, (6, 5): 7331,
         }

shortest_path_lengths = floyd_warshall(nodes, edges)

print(shortest_path_lengths) #this command will print the length from starting point to every point

#print("Shortest Distance: " + str(node_data[dest]['cost']))
#print("Shortest Path: " + str(node_data[dest]['pred'] + list(dest)))