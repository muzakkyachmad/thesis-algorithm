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
    'G':{'cost':inf,'pred':[]}
    }
    node_data[src]['cost'] = 0
    visited = []
    temp = src
    for j in range(6):
        if temp not in visited: # TODO: Reassign source
            visited.append(temp)
            min_heap = []
            for m in graph[temp]:
                if m not in visited:
                    cost = node_data[temp]['cost'] + graph[temp][m]
                    if cost < node_data[m]['cost']:
                        node_data[m]['cost'] = cost
                        node_data[m]['pred'] = node_data[temp]['pred'] + list(temp)
                    heappush(min_heap,(node_data[m]['cost'],m))
        heapify(min_heap)
        temp = min_heap[0][6]
    print("Shortest Distance: " + str(node_data[dest]['cost']))
    print("Shortest Path: " + str(node_data[dest]['pred'] + list(dest)))


if __name__ == "__main__":
    graph = {
        'A':{'B':2903,'C':3073,'F':1866,'G':2198},
        'B':{'A':2903,'C':5894,'F':2171,'G':5079},
        'C':{'A':3073,'B':5894,'F':4162,'G':1604},
        'D':{'E':2247,'F':3196},
        'E':{'E':2247,'F':3815},
        'F':{'A':1866,'B':2171,'C':4162,'D':3196,'E':3815,'G':3851},
        'G':{'A':2198,'B':5079,'C':1604,'G':3851}
    }

    source = 'A'
    destination = 'D'
    dijsktra(graph,source,destination)

