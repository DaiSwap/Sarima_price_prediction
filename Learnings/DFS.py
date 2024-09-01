from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, start_vertex, visited=None):
        if visited is None:
            visited = set()
        visited.add(start_vertex)
        print(start_vertex, end=" ")
        for neighbour in self.graph[start_vertex]:
            if neighbour not in visited:
                self.dfs(neighbour, visited)

g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(2, 5)

print("DFS traversal:")
g.dfs(1)

