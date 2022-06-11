#this algorithm is to find the shortest path of for 7sd - mbr

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

#input data of the WWTP - WWTP code is represented in number and started from 0 as WWTP. data = 4 wwtp

nodes = [0, 1, 2]
edges = {(0, 1): 1590, (0, 2): 3736,
         (1, 0): 1590, (1, 2): 1249,
         (2, 0): 3736, (2, 1): 1249,
         }

shortest_path_lengths = floyd_warshall(nodes, edges)

print(shortest_path_lengths) #this command will print the length from starting point to every point

#print("Shortest Distance: " + str(node_data[dest]['cost']))
#print("Shortest Path: " + str(node_data[dest]['pred'] + list(dest)))