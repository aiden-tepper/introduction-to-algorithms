a = [1, 2, 5, 4, 7, 8, 9, 3, 5, 3, 5]


def Count3(a, b):
    c3 = 0
    n = len(a)
    if n == 0 or len(b) == 0:
        return 0
    for i in range(0, n):
        j = 0
        while j < n and b[j] < a[i]:
            j += 1
        c3 += j
    return c3


def CountInv(a):
    n = len(a)
    if n == 0:
        return 0
    m = int(n / 2)
    c1 = CountInv(a[0:m])
    c2 = CountInv(a[m+1:n])

    a1 = a[0:m]
    a1.sort()

    a2 = a[m+1:n]
    a2.sort()

    c3 = Count3(a1, a2)
    return c1 + c2 + c3


inversions = CountInv(a)
print(inversions)
