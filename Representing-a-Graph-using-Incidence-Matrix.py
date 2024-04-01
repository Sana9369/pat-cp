class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.inc_matrix = [[0] * edges for _ in range(vertices)]
    def add_edge(self, u, v, edge_index,w):
        self.inc_matrix[u][edge_index] = w
        self.inc_matrix[v][edge_index] = w
    def print_matrix(self):
        for row in self.inc_matrix:
            print(row)
# Example usage
if __name__ == "__main__":
    num_vertices = 5
    num_edges = 5
    graph = Graph(num_vertices, num_edges)
    graph.add_edge(0, 1, 0, 9)
    graph.add_edge(1, 2, 1, 8)
    graph.add_edge(2, 3, 2, 6)
    graph.add_edge(3, 0, 3, 4)
    graph.print_matrix()
