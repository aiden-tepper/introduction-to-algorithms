import sys


def find_diff_helper(coins, i, sum_calculated, sum_total):
    if i == 0:
        return abs((sum_total - sum_calculated) - sum_calculated)
    option1 = find_diff_helper(coins, i - 1, sum_calculated + coins[i - 1], sum_total)
    option2 = find_diff_helper(coins, i - 1, sum_calculated, sum_total)
    return min(option1, option2)


def find_diff(coins):
    sum_total = 0

    for i in range(len(coins)):
        sum_total += coins[i]

    return find_diff_helper(coins, len(coins), 0, sum_total)


for line in sys.stdin:
    n = int(line.rstrip())
    break

arr = []

for i in range(n):
    for line in sys.stdin:
        v = int(line.rstrip())
        break
    arr.append(v)

result = "T" if find_diff(arr) == 0 else "F"

sys.stdout.write(result)
