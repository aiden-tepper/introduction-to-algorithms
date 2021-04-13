import sys

for line in sys.stdin:
    n = int(line.rstrip())
    break

q = []

for i in range(n):
    for line in sys.stdin:
        element = int(line.rstrip())
        break
    q.append(int(element))

p = []

for i in range(n):
    for line in sys.stdin:
        element = int(line.rstrip())
        break
    p.append(int(element))

def CountCrosses(q, p):
    n = len(q)
    count = 0
    for i in range(0, n):
        for j in range(i, n):
            if q[i] > q[j] and p[i] < p[j]:
                count += 1
            if q[i] < q[j] and p[i] > p[j]:
                count += 1
    return count


result = CountCrosses(q, p)

sys.stdout.write(str(result))
