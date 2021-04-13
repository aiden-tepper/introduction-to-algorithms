import sys

class AdjNode:
    def __init__(self, city):
        self.city = city
        self.next = None


class TourMap:
    def __init__(self, N):
        self.N = N
        self.graph = [None] * self.N
        self.weeks = -1

    def add_road(self, a, b):
        city = AdjNode(b)
        city.next = self.graph[a]
        self.graph[a] = city

        city = AdjNode(a)
        city.next = self.graph[b]
        self.graph[b] = city

    def print_graph(self):
        for i in range(self.N):
            print(i)
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.city), end="")
                temp = temp.next
            print(" \n")

    def exists(self, s, d):
        current = self.graph[s]
        while current:
            if current.city == d:
                return True
            current = current.next
        return False

    def find_weeks_helper(self, u, d, visited, path):
        visited[u] = True
        path.append(u)

        if u == d:
            # print(path)
            if self.weeks == -1 or len(path) < self.weeks:
                self.weeks = len(path) - 1
                # print(self.weeks)
            # if len(path) == 6:
                # s = path[0]
                # if not self.tourMap.exists(s, d):
                #     self.tourMap.add_road(s, d)
        else:
            current = self.graph[u]
            while current:
                if visited[current.city] == False:
                    self.find_weeks_helper(current.city, d, visited, path)
                current = current.next

        path.pop()
        visited[u] = False

    def find_weeks(self, s, d):
        visited = [False] * self.N
        path = []
        self.find_weeks_helper(s, d, visited, path)
        return self.weeks


class Graph:
    def __init__(self, N):
        self.N = N
        self.graph = [None] * self.N
        self.tourMap = TourMap(N)

    def add_road(self, a, b):
        city = AdjNode(b)
        city.next = self.graph[a]
        self.graph[a] = city

        city = AdjNode(a)
        city.next = self.graph[b]
        self.graph[b] = city

    def print_graph(self):
        for i in range(self.N):
            print(i)
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.city), end="")
                temp = temp.next
            print(" \n")

    def find_paths_helper(self, u, d, visited, path):
        visited[u] = True
        path.append(u)

        if u == d:
            if len(path) == 6:
                s = path[0]
                if not self.tourMap.exists(s, d):
                    self.tourMap.add_road(s, d)
        else:
            current = self.graph[u]
            while current:
                if visited[current.city] == False:
                    self.find_paths_helper(current.city, d, visited, path)
                current = current.next

        path.pop()
        visited[u] = False

    def find_paths(self, s, d):
        visited = [False] * self.N
        path = []
        self.find_paths_helper(s, d, visited, path)

    def find_all_paths(self):
        for city1 in range(self.N):
            for city2 in range(city1, self.N):
                self.find_paths(city1, city2)

    def solution(self):
        self.find_all_paths()
        # self.tourMap.print_graph()
        solution = self.tourMap.find_weeks(1, self.N - 1)
        return solution


# g = Graph(8)
# g.add_road(1, 2)
# g.add_road(2, 3)
# g.add_road(2, 5)
# g.add_road(3, 4)
# g.add_road(3, 6)
# g.add_road(4, 5)
# g.add_road(5, 6)
# g.add_road(6, 7)

# g = Graph(7)
# g.add_road(1, 2)
# g.add_road(1, 3)
# g.add_road(1, 4)
# g.add_road(2, 3)
# g.add_road(2, 5)
# g.add_road(3, 5)
# g.add_road(4, 5)
# g.add_road(5, 6)
#
# solution = g.solution()
# print(solution)


for line in sys.stdin:
    input = line.rstrip()
    break

N = int(input.split(" ")[0])
M = int(input.split(" ")[1])

tourMap = Graph(N + 1)

for i in range(M):
    for line in sys.stdin:
        input = line.rstrip()
        break
    a = int(input.split(" ")[0])
    b = int(input.split(" ")[1])
    tourMap.add_road(a, b)

result = tourMap.solution()

sys.stdout.write(str(result))