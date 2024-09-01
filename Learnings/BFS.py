from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, starting_vertex):
        visited = set()
        queue = []
        queue.append(starting_vertex)
        visited.add(starting_vertex)
        while queue:
            vertex = queue.pop(0)
            print(vertex, end=" ")
            for neighbour in self.graph[vertex]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)

g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 5)
g.add_edge(2, 5)
g.add_edge(2, 3)
g.add_edge(5, 3)
g.add_edge(5, 4)
g.add_edge(3, 4)

print("BFS traversal:")
g.bfs(4)
