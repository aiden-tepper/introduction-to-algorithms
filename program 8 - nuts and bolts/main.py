import sys


class Graph:

    def __init__(self, nuts_arr, l, r):
        self.nuts_arr = nuts_arr
        self.nuts = l
        self.bolts = r
        self.n = l + r + 2
        self.graph = [[0 for _ in range(self.n)] for _ in range(self.n)]
        self.populate_graph()

    def populate_graph(self):
        for i in range(self.nuts):
            self.graph[0][i+1] = 1
            for j in range(self.bolts):
                if self.nuts_arr[i][j] == 1:
                    self.graph[i+1][j+1+self.nuts] = 1

        for i in range(self.bolts):
            self.graph[i+1+self.nuts][self.n-1] = 1

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

    def ford_fulkerson(self):
        source = 0
        sink = self.n-1
        parent = [-1]*self.n
        max_flow = 0

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

        return max_flow


for line in sys.stdin:
    input = line.rstrip()
    break

l = int(input.split(" ")[0])
r = int(input.split(" ")[1])

nuts_arr = []

for _ in range(l):
    for line in sys.stdin:
        input = line.rstrip()
        break
    nut = []
    for i in range(r):
        nut.append(int(input.split(" ")[i]))
    nuts_arr.append(nut)

graph = Graph(nuts_arr, l, r)
solution = graph.ford_fulkerson()
sys.stdout.write(str(solution))
