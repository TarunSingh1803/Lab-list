from collections import deque

class Graph:
    def __init__(self, num_vertices):
        self.graph = {i: [] for i in range(1, num_vertices + 1)}
        self.visited = {i: False for i in range(1, num_vertices + 1)}

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def bfs(self, start_vertex):
        queue = deque([start_vertex])
        self.visited[start_vertex] = True

        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')
            for neighbor in self.graph[vertex]:
                if not self.visited[neighbor]:
                    queue.append(neighbor)
                    self.visited[neighbor] = True

def main():
    N = int(input("Enter number of vertices: "))
    E = int(input("Enter number of edges: "))

    g = Graph(N)

    for i in range(E):
        s = int(input("Enter source: "))
        d = int(input("Enter destination: "))
        g.add_edge(s, d)

    start_vertex = int(input("Enter Start Vertex for BFS: "))
    print("BFS of graph:")
    g.bfs(start_vertex)

if __name__ == "__main__":
    main()
