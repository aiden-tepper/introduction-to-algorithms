
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

firstIndex = 0

for i in range(len(arr)):
    if arr[i] > 0:
        firstIndex = i
        break

lastIndex = firstIndex

for i in range(len(arr)-1, firstIndex, -1):
    if arr[i] > 0:
        lastIndex = i
        break

sum = 0

for i in range(firstIndex, lastIndex+1):
    sum += arr[i]

if lastIndex == 0:
    sys.stdout.write(str(0))
else:
    sys.stdout.write(str(sum))
