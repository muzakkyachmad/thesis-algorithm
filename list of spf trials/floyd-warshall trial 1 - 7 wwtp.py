
def floyd_warshall(nodes, edges): #definition of the floyd-warshall algorith
    """this function is defining the floyd-warshall algorithm definition and its component
    param: distance (d), starting wwtp(u), ending wwtp(v), and alternative route(k)"""

    d = {(u,v): float('inf') if u != v else 0 for u in nodes for v in nodes} #d is the distance of the start wwtp to the destination
    for (u,v), w_uv in edges.items():
        d[(u,v)] = w_uv #w_uv is the length of the distance in meter

    for k in nodes: #k represents the intermediate destination if there is another point to go in the shortest route
        for u in nodes:
            for v in nodes:
                d[(u,v)] = min(d[u,v], d[u,k] + d[k,v])


    if any(d[(u,u)] < 0 for u in nodes): #this line is the indicator if there is any mistakes in the input
        print("Graph has a negative-weight cycle")

    return d #to call or run the shortest path algorithm to figure out the lengths

#input data of the WWTP - WWTP code is represented in number and started from 0 as WWTP | data = 7 wwtp from python
nodes = [0, 1, 2, 3, 4, 5, 6] #node represents the WWTP
edges = {(0, 1): 1590, (0, 2): 3736, (0, 4): 3281,
         (1, 0): 1590, (1, 2): 1249, (1, 3): 5783, (1, 4): 3795,
         (2, 0): 3736, (2, 1): 1249, (2, 3): 5490, (2, 4): 4282,
         (3, 1): 5783, (3, 2): 5490, (3, 4): 2894, (3, 5): 6395, (3, 6): 9607,
         (4, 0): 3281, (4, 1): 3795, (4, 2): 4282, (4, 3): 2894, (4, 5): 5117, (4, 6): 8676,
         (5, 3): 6395, (5, 4): 5117, (5, 6): 7331,
         (6, 3): 9607, (6, 4): 8676, (6, 5): 7331} #edges represents the distance of the starting WWTP to the destination - based on the QGIS and graph

shortest_path_lengths = floyd_warshall(nodes, edges) #to execute the floyd-warshall algorithm

print(shortest_path_lengths) #this command will print the length from starting point to every point


