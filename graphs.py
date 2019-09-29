class Vertex:
	def __init__(self, id, data):
		self.id = id
		self.data = data
		self.is_visited = False
		self.neighbors = set()
		
	def __str__(self):
		return 'V' + str(self.id)
		
	def get_neighbors(self):
		return self.neighbors
		
	def show_neighbors(self):
		return ', '.join([str(neighbor) for neighbor in self.neighbors])
		
	def set_visited(self, value):
		self.is_visited = value
		

class Edge:
	def __init__(self, vertex_id1, vertex_id2, weight):
		self.vertex_id1 = vertex_id1
		self.vertex_id2 = vertex_id2
		self.weight = weight
		
	def __str__(self):
		return ''.join(['(', str(self.vertex_id1), ', ', str(self.vertex_id2), ')'])
		

class Graph:
	def __init__(self):
		self.vertices = []
		self.edges = []
		
	def __str__(self):
		str_vertices = 'V = {' + ', '.join([str(v) for v in self.vertices]) + '}'
		str_edges = 'E = {' + ','.join([str(e) for e in self.edges]) + '}'
		return str_vertices + '\n' + str_edges
	
	def get_vertex(self, vertex_id):
		for vertex in self.vertices:
			if vertex.id == vertex_id:
				return vertex
		return None
	
	def add_vertex(self, vertex):
		self.vertices.append(vertex)
	
	def add_vertex(self, id, data):
		self.vertices.append(Vertex(id, data))
		
	def add_edge(self, vertex_id1, vertex_id2, weight):
		self.edges.append(Edge(vertex_id1, vertex_id2, weight))
		vertex1 = self.get_vertex(vertex_id1)
		vertex2 = self.get_vertex(vertex_id2)
		vertex1.neighbors.add(vertex2)
	
	
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
	
	vertex1 = G.get_vertex(1)
	print('V1 neighbors:', vertex1.get_neighbors())
	
	print(G)