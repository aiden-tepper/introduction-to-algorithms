import sys


class Graph:
    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.adjArr = [[] for _ in range(n)]

    def add_edge(self, a, b):
        self.adjArr[a - 1].append(b - 1)
        self.adjArr[b - 1].append(a - 1)

    def solution(self):
        colors = [-1] * self.n
        colors[0] = 0
        available = [False] * self.n
        cr_max = 0

        for i in range(1, len(colors)):

            for vertex in self.adjArr[i]:
                if colors[vertex] != -1:
                    available[colors[vertex]] = True

            cr = 0
            while cr < self.n:
                if not available[cr]:
                    break
                cr += 1

            colors[i] = cr

            if cr > cr_max:
                cr_max = cr

            for j in self.adjArr[i]:
                if colors[j] != -1:
                    available[colors[j]] = False

        return cr_max < self.k


for line in sys.stdin:
    input = line.rstrip()
    break

n = int(input.split(" ")[0])
m = int(input.split(" ")[1])
k = int(input.split(" ")[2])

g = Graph(n, k)

for _ in range(m):
    for line in sys.stdin:
        input = line.rstrip()
        break
    a = int(input.split(" ")[0])
    b = int(input.split(" ")[1])
    g.add_edge(a, b)

solution = g.solution()
sys.stdout.write(str(solution))
