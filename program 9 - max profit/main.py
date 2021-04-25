import sys


class Graph:

    def __init__(self, mines_arr):
        self.mines_arr = mines_arr
        self.n = len(mines_arr) + 2
        self.graph = [[0 for _ in range(self.n)] for _ in range(self.n)]
        self.p = 0
        self.populate_graph()

    def populate_graph(self):
        for i, mine in enumerate(self.mines_arr, 1):
            if mine < 0:
                self.graph[i][self.n-1] = abs(mine)
            else:
                self.graph[0][i] = mine
                self.p += mine

    def print_graph(self):
        for row in self.graph:
            print(row)

    def add_edge(self, edge_arr):
        s = edge_arr[0]
        for i in range(1, len(edge_arr)):
            d = edge_arr[i]
            self.graph[s][d] = sys.maxsize

    def is_path(self, s, d, parent):
        visited = [False]*self.n
        queue = [s]
        visited[s] = True

        while queue:
            u = queue.pop(0)
            for i, val in enumerate(self.graph[u]):
                if not visited[i] and val > 0:
                    if i == d:
                        visited[i] = True
                        parent[i] = u
                        return True
                    queue.append(i)
                    visited[i] = True
                    parent[i] = u

        return False

    def dfs(self, graph, s, visited):
        visited[s] = True
        for i in range(self.n):
            if graph[s][i] > 0 and not visited[i]:
                self.dfs(graph, i, visited)

    def ford_fulkerson(self):
        source = 0
        sink = self.n-1
        parent = [-1]*self.n
        max_flow = 0
        original_graph = [row[:] for row in self.graph]

        while self.is_path(source, sink, parent):
            path_flow = sys.maxsize
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        visited = len(self.graph) * [False]
        self.dfs(self.graph, source, visited)

        min_cut_cost = 0

        for i in range(self.n):
            for j in range(self.n):
                if original_graph[i][j] > 0 and visited[i] and not visited[j]:
                    min_cut_cost += original_graph[i][j]

        return self.p - min_cut_cost


for line in sys.stdin:
    input = line.rstrip()
    break

n = int(input.split(" ")[0])
m = int(input.split(" ")[1])

for line in sys.stdin:
    input = line.rstrip()
    break

mines_arr = []

for i in range(n):
    mine = int(input.split(" ")[i])
    mines_arr.append(mine)

graph = Graph(mines_arr)

for _ in range(m):
    for line in sys.stdin:
        input = line.rstrip()
        break
    x = len(input.split(" "))
    edges = []
    for i in range(x):
        edge = int(input.split(" ")[i])
        edges.append(edge)
    graph.add_edge(edges)

solution = graph.ford_fulkerson()
sys.stdout.write(str(solution))
