# Aiden Tepper

import sys

for line in sys.stdin:
    n = int(line.rstrip())
    break

arr = []

for i in range(n):
    for line in sys.stdin:
        element = int(line.rstrip())
        break
    arr.append(int(element))

sum = 0
temp = 0

for i in range(0, len(arr)):
    temp += arr[i]
    if temp < 0:
        temp = 0
    elif sum < temp:
        sum = temp

sys.stdout.write(str(sum))