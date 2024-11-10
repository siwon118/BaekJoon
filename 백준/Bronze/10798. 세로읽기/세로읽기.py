a = []

for _ in range(5):
    s = list(input())
    a.append(s)

max_index = len(a[0])
for index in a:
    if max_index < len(index):
        max_index = len(index)

for i in range(max_index):
    for j in range(len(a)):
        if len(a[j]) > i:
            print(a[j][i], end='')
