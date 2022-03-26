
#using actual data with txa code

import sys
from heapq import heapify, heappush, heappop

def dijsktra(graph,src,dest):
    inf = sys.maxsize
    node_data = {'A':{'cost':inf,'pred':[]},
    'B':{'cost':inf,'pred':[]},
    'C':{'cost':inf,'pred':[]},
    'D':{'cost':inf,'pred':[]},
    'E':{'cost':inf,'pred':[]},
    'F':{'cost':inf,'pred':[]},
    'G':{'cost':inf,'pred':[]},
    }
    node_data[src]['cost'] = 0
    visited = []
    temp = src
    for i in range(3):
        if temp not in visited:  # TODO: Reassign source
            visited.append(temp)
            min_heap = []
            for j in graph[temp]:
                if j not in visited:
                    cost = node_data[temp]['cost'] + graph[temp][j]
                    if cost < node_data[j]['cost']:
                        node_data[j]['cost'] = cost
                        node_data[j]['pred'] = node_data[temp]['pred'] + list(temp)
                    heappush(min_heap, (node_data[j]['cost'], j))
        heapify(min_heap)
        temp = min_heap[0][1]
    print("Shortest Distance: " + str(node_data[dest]['cost']))
    print("Shortest Path: " + str(node_data[dest]['pred'] + list(dest)))


if __name__ == "__main__":
    graph = {
        'A':{'B':4773,'C':5563,'D':7387},
        'B':{'A':4773,'C':8515,'D':8715},
        'C':{'A':5563,'B':8515,'D':11008},
        'D':{'A':7387,'B':8715,'C':11008},
    }

    source = 'D'
    destination = 'D'
    dijsktra(graph,source,destination)