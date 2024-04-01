#Object oriented approach  
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]
    def add_edge(self, u, v, w):
        self.adj_matrix[u][v] = w
        self.adj_matrix[v][u] = w 
    def print_matrix(self):
        for row in self.adj_matrix:
            print(row)
if __name__ == "__main__":
    num_vertices = 5
    graph = Graph(num_vertices)
    graph.add_edge(0, 1, 5)
    graph.add_edge(0, 2, 6)
    graph.add_edge(1, 3, 7)
    graph.add_edge(2, 4, 8)
    graph.print_matrix()
