graph = {
    '5': ['3', '7', '1', '10'],
    '3': ['2', '4', '23', '45', '100'],
    '7': ['8', '23', '-56', '45', '78'],
    '2': ['1', '-5', '56', '67'],
    '4': ['8', '45', '56', '34', '12'],
    '8': ['12', '78'],
    '1': ['-56'],
    '10': ['12'],
    '23': ['45'],
    '45': ['78'],
    '100': ['34'],
    '-56': ['23'],
    '78': ['100'],
    '-5': ['7', '1'],
    '56': ['1', '-5'],
    '67': ['34'],
    '34': ['67'],
    '12': ['8']
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


def dfs(g, start, visited):
    print(start)
    visited.append(start)
    for n in g[start]:
        if n not in visited:
            dfs(g, n, visited)


#
# obj = Graph(graph=graph)
# obj.calculate_bfs('5')
# obj.dfs.append('5')
# obj.calculate_dfs('5', set())
# print(obj.bfs)
# print(obj.dfs)

print(dfs(graph, '5', []))
