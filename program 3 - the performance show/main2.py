import sys

for line in sys.stdin:
    input = line.rstrip()
    break

N = int(input.split(" ")[0])
M = int(input.split(" ")[1])

adjacencyArr = [[0 for i in range(N)] for j in range(N)]

for i in range(M):
    for line in sys.stdin:
        input = line.rstrip()
        break
    a = int(input.split(" ")[0])
    b = int(input.split(" ")[1])
    adjacencyArr[a-1][b-1] = 1
    adjacencyArr[b-1][a-1] = 1

for row in adjacencyArr:
    print(row)


def findPath(city1, city2):
    if visitedArr[city1] == True:
        return
    visitedArr[city1] = True
    currentPath.append(city1)



pathArr = [[0 for i in range(N)] for j in range(N)]

for city1 in range(N):
    for city2 in range(city1, N):
        visitedArr = [False for i in range(N)]
        currentPath = []
        allPaths = []
        findPath(city1, city2)
        # if findPath(city1, city2) == True:
        #     pathArr[city1][city2] = 1
        #     pathArr[city2][city1] = 1
