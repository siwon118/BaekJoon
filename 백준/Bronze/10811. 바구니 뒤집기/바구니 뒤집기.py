n, m = map(int, input().split())

a = []
for i in range(n):
    a.append(i+1)

for i in range(m):
    x, y = map(int, input().split())
    x -= 1
    a[x:y] = a[x:y][::-1]

print(*a)
