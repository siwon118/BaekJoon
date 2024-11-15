n, m = map(int, input().split())

a = []
for i in range(m):
    a.append(list(map(int, input().split())))

result = []

for i in range(n):
    result.append(0)

for i in range(m):
    for j in range(a[i][0]-1, a[i][1], 1):
            result[j] = a[i][2]


print(*result, sep=' ')
