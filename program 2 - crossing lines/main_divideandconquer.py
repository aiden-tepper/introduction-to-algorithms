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


# q = [1, 10, 8, 6]
# p = [6, 2, 5, 1]

# q = [9, 21, 1, 5, 18]
# p = [2, 4, 6, 10, 1]

# intersection occurs when q[i] < p[j] && q[j] > p[i]

def Count3(q1, q2, p1, p2):
    c3 = 0
    n1 = len(q1)
    n2 = len(q2)
    if n1 == 0 or n2 == 0:
        return 0
    for i in range(0, n1):
        for j in range(0, n2):
            if q1[i] > q2[j] and p1[i] < p2[j]:
                c3 += 1
            if q1[i] < q2[j] and p1[i] > p2[j]:
                c3 += 1
    return c3


def CountCrosses(q, p):
    n = len(q)
    if n == 0:
        return 0
    m = int(n / 2)
    c1 = CountCrosses(q[0:m], p[0:m])
    c2 = CountCrosses(q[m + 1:n], p[m + 1:n])

    a1 = q[0:m]
    # a1.sort()

    a2 = q[m:n]
    # a2.sort()

    a3 = p[0:m]
    # a3.sort()

    a4 = p[m:n]
    # a4.sort()

    c3 = Count3(a1, a2, a3, a4)
    return c1 + c2 + c3


result = CountCrosses(q, p)

sys.stdout.write(str(result))
