class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {v: [] for v in range(vertices)}

    def add_edge(self, u, v, w):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
    def print_list(self):
        for vertex, neighbors in self.adj_list.items():
            print(vertex, "->", neighbors)
# Example usage
if __name__ == "__main__":
    num_vertices = 5
    graph = Graph(num_vertices)
    graph.add_edge(0, 1, 3)
    graph.add_edge(1, 2, 5)
    graph.add_edge(3, 4, 6)
    graph.add_edge(2, 3, 10)
    graph.add_edge(0, 4, 7)
    graph.add_edge(4, 1, 11)
    graph.add_edge(1, 3, 2)
    graph.print_list()