import sys


class SupplyChain:
    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.adjArr = [[0 for i in range(n)] for j in range(n)]

    def add_edge(self, a, b, weight):
        self.adjArr[a - 1][b - 1] = weight
        self.adjArr[b - 1][a - 1] = weight

    def print_graph(self):
        for row in self.adjArr:
            print(row)

    def find_min_distance(self, key, mst_set):
        min_distance = sys.maxsize

        for node in range(self.n):
            if key[node] < min_distance and mst_set[node] is False:
                min_distance = key[node]
                min_index = node

        return min_index

    def mst(self):
        key = [sys.maxsize] * self.n
        key[0] = 0
        parent = [None] * self.n
        parent[0] = -1
        mst_set = [False] * self.n

        for i in range(self.n):
            a = self.find_min_distance(key, mst_set)
            mst_set[a] = True
            for b in range(self.n):
                if 0 < self.adjArr[a][b] < key[b] and mst_set[b] is False:
                    key[b] = self.adjArr[a][b]
                    parent[b] = a

        return key

    def find_max_distance(self):
        edges = self.mst()
        edges.sort()
        return edges[len(edges)-self.k]


for line in sys.stdin:
    input = line.rstrip()
    break

n = int(input.split(" ")[0])
k = int(input.split(" ")[1])
m = int(input.split(" ")[2])

g = SupplyChain(n, k)

for i in range(m):
    for line in sys.stdin:
        input = line.rstrip()
        break
    u = int(input.split(" ")[0])
    v = int(input.split(" ")[1])
    d = int(input.split(" ")[2])
    g.add_edge(u, v, d)

result = g.find_max_distance()

sys.stdout.write(str(result))
