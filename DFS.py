class Graph:
    def __init__(self, num_vertices):
        self.graph = {i: [] for i in range(1, num_vertices + 1)}
        self.visited = {i: False for i in range(1, num_vertices + 1)}

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def dfs(self, vertex):
        print(vertex, end=' ')
        self.visited[vertex] = True
        for neighbor in self.graph[vertex]:
            if not self.visited[neighbor]:
                self.dfs(neighbor)

def main():
    N = int(input("Enter number of vertices: "))
    E = int(input("Enter number of edges: "))
    g = Graph(N)

    for _ in range(E):
        s = int(input("Enter source: "))
        d = int(input("Enter destination: "))
        g.add_edge(s, d)

    start_vertex = int(input("Enter Start Vertex for DFS: "))
    print("DFS of graph:")
    g.dfs(start_vertex)

if __name__ == "__main__":
    main()
