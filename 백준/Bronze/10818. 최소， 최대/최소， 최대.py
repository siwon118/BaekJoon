n = int(input())
a = ([int(x) for x in input().split()])

min = a[0]
max = a[0]

for i in range(n):
    if min > a[i]:
        min = a[i]

    if max < a[i]:
        max = a[i]

print(min, max)
