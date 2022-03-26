
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
    for i in range(6):
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
        'A':{'B':4776,'C':5597,'F':2491,'G':4480},
        'B':{'A':4776,'C':8506,'F':4551,'G':6945},
        'C':{'A':5597,'B':8506,'F':5854,'G':6397},
        'D':{'E':2909,'F':5201},
        'E':{'D':2909,'F':6324},
        'F':{'A':2491,'B':4551,'C':5854,'D':5201,'E':6324,'G':6974},
        'G':{'A':4480,'B':6945,'C':6397,'F':6974}
    }

    source = 'A'
    destination = 'G'
    dijsktra(graph,source,destination)