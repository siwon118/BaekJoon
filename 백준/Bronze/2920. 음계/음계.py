a = list(map(int, input().split()))

result = ''
for i in range(len(a)-1):
    if a[i+1] - a[i] == 1:
        result = 'ascending'
    elif a[i] - a[i+1] == 1:
        result = 'descending'
    else:
        result = 'mixed'
        break

print(result)
