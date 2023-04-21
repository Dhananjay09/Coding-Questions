graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}


class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.bfs = []
        self.dfs = []

    def calculate_bfs(self, head):
        queue = []
        visited = set()
        queue.append(head)
        visited.add(head)
        self.bfs.append(head)
        while queue:
            first_node = queue.pop(0)
            for neighbour in self.graph[first_node]:
                if neighbour not in visited:
                    self.bfs.append(neighbour)
                    visited.add(neighbour)
                    queue.append(neighbour)

    def calculate_dfs(self, head, visited):
        visited.add(head)
        for item in self.graph[head]:
            if item not in visited:
                self.dfs.append(item)
                self.calculate_dfs(item, visited=visited)


obj = Graph(graph=graph)
obj.calculate_bfs('5')
obj.dfs.append('5')
obj.calculate_dfs('5', set())
print(obj.bfs)
print(obj.dfs)
