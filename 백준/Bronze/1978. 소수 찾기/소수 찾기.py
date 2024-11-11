import math

n = int(input())

a = list(map(int, input().split()))

count = 0

for v in a:
    for i in range(2, int(math.sqrt(v))+1):
        if v % i == 0:
            count -= 1
            break
    count += 1
    if v == 1:
        count -= 1


print(count)
