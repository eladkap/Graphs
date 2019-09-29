from stack import *
from queue import *
from graphs import *


'''
Input: Graph and start vertex
Output: For each vertex v in the graph calculates the distance from the start vertex
means: for each v in G calculates d(v)
'''


def bfs(graph, start):
	pass
			


if __name__ == '__main__':
	G = Graph()
	
	for vertex_id in range(1, 9):
		G.add_vertex(vertex_id, chr(ord('a') + vertex_id))
		#G.add_vertex(Vertex(vertex_id, chr(ord('a') + vertex_id)))	
	
	
	G.add_edge(1, 2, 2)
	G.add_edge(1, 3, 2)
	G.add_edge(1, 4, 1)
	G.add_edge(2, 3, 5)
	G.add_edge(2, 4, 4)
	G.add_edge(2, 5, 6)
	G.add_edge(3, 1, 5)
	G.add_edge(3, 4, 5)
	G.add_edge(4, 5, 4)
	G.add_edge(5, 4, 4)
	G.add_edge(5, 5, 9)
	G.add_edge(5, 6, 8)
	G.add_edge(6, 6, 5)
	G.add_edge(6, 7, 3)
	G.add_edge(6, 8, 1)
	G.add_edge(7, 8, 4)
	G.add_edge(8, 2, 3)
	
	
	s = G.get_vertex(1)
	bfs(G, s)