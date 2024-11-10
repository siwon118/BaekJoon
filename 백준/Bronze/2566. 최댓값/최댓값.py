a = []

for _ in range(9):
    a.append(list(map(int, input().split())))

maximum = a[0][0]
x, y = 0, 0
for i in range(len(a)):
    for j in range(len(a[i])):
        if maximum < a[i][j]:
            maximum = a[i][j]
            x = i
            y = j

print(maximum)
print(x+1, y+1)
