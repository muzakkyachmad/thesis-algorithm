

import numpy as np
from cached_property import cached_property
import pytest


class Graph(object):
	'''Solve the all-pairs shortest-path (APSP) problem using the Floyd-Warshall algorithm as described
	in Section 25.2 of Cormen et al., Introduction to Algorithms (3rd ed.). The implementation is directly
	from the pseudocode given there; in particular, there is no space optimization, and only the weights
	of the shortest paths are computed; no predecessor pointers are stored to reconstruct the shortest paths.'''

	def __init__(self, edges):
		self.edges = edges 			# List of tuples each containing the head, tail, and weight, respectively, of each edge of the graph

	@cached_property
	def nodes(self): 				# List of the graph's nodes
		_nodes = set()
		for edge in self.edges:
			u, v, weight = edge
			_nodes.add(u)
			_nodes.add(v)
		return list(_nodes)

	@cached_property
	def W(self): 					# Matrix of edge weights
		n = len(self.nodes)
		w = np.full((n, n), np.inf)
		np.fill_diagonal(w, 0)
		for edge in self.edges:
			u, v, weight = edge
			w[u-1, v-1] = weight
		return w

	def floyd_warshall(self):
		'''Compute a matrix of shortest-path weights (if the graph contains no negative cycles)'''
		n = len(self.nodes)
		D = [np.full((n, n), np.inf) for _ in range(n+1)]
		D[0] = self.W
		for k in range(1, n+1):
			for i in range(n):
				for j in range(n):
					D[k][i, j] = min(D[k-1][i, j], D[k-1][i, k-1] + D[k-1][k-1, j])
		if any(np.diag(D[n]) < 0):
			raise ValueError("The graph contains negative cycles.")
		else:
			return D[n].astype(int)


@pytest.fixture
def edges():
	'''Edges from the 5-node graph in Figure 25.1 of Cormen et al., Introduction to Algorithms (3rd ed.)'''
	return [(1, 2, 3),
			(1, 5, -4),
			(1, 3, 8),
			(2, 5, 7),
			(2, 4, 1),
			(3, 2, 4),
			(4, 1, 2),
			(4, 3, -5),
			(5, 4, 6)]

def test_floyd_marshall(edges):
	'''Check that the computed matrix of shortest-path weights is as given in Figure 25.1 of Cormen et al.'''
	graph = Graph(edges)
	D = graph.floyd_warshall()
	assert D.tolist() == [[0,  1, -3,  2, -4],
 						  [3,  0, -4,  1, -1],
 						  [7,  4,  0,  5,  3],
 						  [2, -1, -5,  0, -2],
 						  [8,  5,  1,  6,  0]]

@pytest.fixture
def edges_negative_cycle():
	'''Edges of a graph containing a negative cycle'''
	return [(1, 2, 1),
		    (1, 3, 4),
		    (2, 4, 2),
		    (3, 4, 3),
		    (4, 1, -4)]

def test_negative_cycle(edges_negative_cycle):
	'''Check that the Floyd-Warshall algorithm raises a ValueError if the input graph contains a negative cycle'''
	graph = Graph(edges_negative_cycle)
	with pytest.raises(ValueError):
		graph.floyd_warshall()


if __name__ == "__main__":
	pytest.main([__file__, "-s"])