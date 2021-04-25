import math
import sys


class Arbitrage:
    def __init__(self, n, m):
        self.V = n
        self.E = m
        self.exchanges = {}
        self.adj_table = []
        self.original_table = [[0 for i in range(n)] for i in range(n)]

    def add_edge(self, a, b, weight):
        vertices = [a, b]

        for vertex in vertices:
            if vertex not in self.exchanges:
                length = len(self.exchanges)
                self.exchanges[vertex] = length

        index1 = self.exchanges.get(a)
        index2 = self.exchanges.get(b)
        adjusted_weight = -math.log(weight/100, 10)
        self.adj_table.append([index1, index2, adjusted_weight])
        self.original_table[index1][index2] = weight/100

    def bellman_ford(self):
        D = [sys.maxsize] * self.V
        D[0] = 0
        parent = [-1] * self.V

        for _ in range(self.V-1):
            for i in range(self.E):
                u = self.adj_table[i][0]
                v = self.adj_table[i][1]
                w = self.adj_table[i][2]
                if D[u] + w < D[v]:
                    D[v] = D[u] + w
                    parent[v] = u

        v = 0
        cycle = []
        while True:
            cycle.append(v)
            if v == 0 and len(cycle) > 1:
                break
            u = v
            v = parent[v]

        cycle.reverse()

        arbitrage = self.original_table[cycle[0]][cycle[1]]
        for i in range(1, len(cycle)-1):
            arbitrage *= self.original_table[cycle[i]][cycle[i+1]]

        n = len(cycle) - 1
        return math.ceil((1 - (1/arbitrage)**(1./n))*100)


for line in sys.stdin:
    input = line.rstrip()
    break

n = int(input.split(" ")[0])
m = int(input.split(" ")[1])

g = Arbitrage(n, m)

for _ in range(m):
    for line in sys.stdin:
        input = line.rstrip()
        break
    exchange1 = input.split(" ")[0]
    exchange2 = input.split(" ")[1]
    rate = int(input.split(" ")[2])
    g.add_edge(exchange1, exchange2, rate)

solution = g.bellman_ford()

sys.stdout.write(str(solution))
