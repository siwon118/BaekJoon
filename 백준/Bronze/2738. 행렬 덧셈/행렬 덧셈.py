n, m = map(int, input().split())
a = []
b = []

for i in range(n):
    user_input = input()
    a.append([int(x) for x in user_input.split()])

for i in range(n):
    user_input = input()
    b.append([int(x) for x in user_input.split()])

for i in range(n):
    for j in range(m):
        print((a[i][j] + b[i][j]), end=' ')
    print()
