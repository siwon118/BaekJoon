rows, cols = 100, 100
array = [[0] * cols for _ in range(rows)]
count = 0

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    for j in range(10):
        for k in range(10):
            array[(y+j)*-1][x+k-1] += 1


for row in array:
    for i in row:
        if i >= 1:
            count += 1

print(count)
